"""TrackingSystem URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import include, url
    2. Add a URL to urlpatterns:  url('blog/', include('blog.urls'))
"""
from django.contrib import admin

from KumoGT import views
from KumoGT.registration import sign_up, manage_users, all_users, manage_my_account,\
    change_my_pwd, change_users_pwd, delete_user, activate_user, deactivate_user
from django.contrib.auth import views as auth_views
from KumoGT.registration.forms import AdminChangePasswordForm

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

stu_search_options = r'(?:uin=(?P<uin>[0-9]+)/)?'\
                     r'(?:first_name=(?P<first_name>[a-zA-Z]+)/)?'\
                     r'(?:last_name=(?P<last_name>[a-zA-Z]+)/)?'\
                     r'(?:gender=(?P<gender>[a-zA-Z_]+)/)?'\
                     r'(?:ethnicity=(?P<ethnicity>[a-zA-Z_]+)/)?'\
                     r'(?:us_residency=(?P<us_residency>[a-zA-Z]+)/)?'\
                     r'(?:texas_residency=(?P<texas_residency>[a-zA-Z]+)/)?'\
                     r'(?:citizenship=(?P<citizenship>[a-zA-Z]+)/)?'\
                     r'(?:status=(?P<status>[a-zA-Z]+)/)?'\
                     r'(?:start_year=(?P<start_year>[0-9-]+)/)?'\
                     r'(?:start_sem=(?P<start_sem>[a-zA-Z]+)/)?'\
                     r'(?:cur_degree=(?P<cur_degree>[a-zA-Z_]+)/)?'\
                     r'(?:cur_degree__major=(?P<cur_degree__major>[a-zA-Z]+)/)?'\
                     r'(?:advisor=(?P<advisor>[a-zA-Z ]+)/)?'\
                     r'(?:upe=(?P<upe>[yesno]+)/)?'\
                     r'(?:ace=(?P<ace>[yesno]+)/)?'\
                     r'(?:iga=(?P<iga>[yesno]+)/)?$'

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # Admin and users authentication
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    url(r'^account/$', manage_my_account, name='account'),
    url(r'^account/change_pwd/$', change_my_pwd, name='change_my_pwd'),
    url(r'^account/reset_pwd/$', auth_views.PasswordResetView.\
        as_view(template_name='reset_pwd.html', success_url='done/', subject_template_name='reset_pwd_subject.txt',\
                email_template_name='reset_pwd_email.html'), name='reset_pwd'),
    url(r'^account/reset_pwd/done/$',\
        auth_views.PasswordResetDoneView.as_view(template_name='reset_pwd_done.html'), name='reset_pwd_done'),
    url(r'^account/reset/(?P<uidb64>.+)/(?P<token>.+)/$', auth_views.PasswordResetConfirmView.\
        as_view(template_name='reset_pwd_confirm.html', success_url='/account/reset/done/',\
                form_class=AdminChangePasswordForm), name='reset_pwd_confirm'),
    url(r'^account/reset/done/$', auth_views.PasswordResetCompleteView.\
        as_view(template_name='reset_pwd_complete.html'), name='reset_pwd_complete'),
    url(r'^manage_users/$', manage_users, name='manage_users'),
    url(r'^manage_users/sign_up/$', sign_up, name='sign_up'),
    url(r'^manage_users/user_list/$', all_users, name='user_list'),
    url(r'^manage_users/user_list/change_pwd/(?P<id>\d+)/$',
        change_users_pwd, name='change_users_pwd'),
    url(r'^manage_users/user_list/delete_user/(?P<id>\d+)/$', delete_user, name='delete_user'),
    url(r'^manage_users/user_list/activate/(?P<id>\d+)/$', activate_user, name='activate_user'),
    url(r'^manage_users/user_list/deactivate/(?P<id>\d+)/$', deactivate_user, name='deactivate_user'),
    url(r'^admin/', admin.site.urls, name='admin'),

    url(r'^download_stu_info/' + stu_search_options,\
        views.download_stu_info, name = 'download_stu_info'),
    url(r'^get_tmp_file/(?:type=(?P<content_type>.+)/)(?:path=(?P<file_path>.+))$',\
        views.get_tmp_file, name='get_tmp_file'),

    url(r'^students/' + stu_search_options, views.students, name='students'),
    url(r'^students/show_stu/(?P<id>\d+)/$', views.show_stu, name='show_stu'),
    url(r'^students/basic_info/(?P<id>\d+)/$', views.basic_info, name='basic_info'),
    url(r'^students/degree_info/(?P<id>\d+)/$', views.degree_info, name='degree_info'),
    url(r'^students/degree_info_more/(?P<id>\d+)/$', views.degree_info_more, name='degree_info_more'),
    url(r'^students/degree_note/(?P<id>\d+)/$', views.degree_note, name='degree_note'),
    #path('students/', views.students, name = 'students'),
    url(r'^students/edit/(?P<id>\d+)/$', views.edit_stu, name='edit_stu'),
    url(r'^students/delete/(?P<id>\d+)/$', views.delete_stu, name='delete_stu'),
    url(r'^students/add/$', views.create_stu, name='create_stu'),
    url(r'^students/parse/$', views.parse_stu, name='parse_stu'),

    url(r'^students/degree_info/(?P<id>\d+)/$', views.degree_info, name = 'degree_info'), 
    url(r'^student/(?:(?P<stu_id>\d+)/)degrees/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.degrees, name='degrees'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)quals/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.quals, name='quals'),
    url(r'^student/(?:(?P<stu_id>\d+)/)session_note/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.session_note, name='session_note'),

    url(r'^upload/$', views.upload, name='upload'),
    url(r'^form_upload/$', views.form_upload, name='form_upload'),

    url(r'^students/advising_note/(?P<id>\d+)/$', views.advising_note, name='advising_note'),
    #url(r'^students/advising_note/$', views.advising_note, name='advising_note'),
    # degree docs
    url(r'^degree/(?:(?P<deg_id>\d+)/)degree_plan/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.degree_plan, name='degree_plan'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)preliminary_exam/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.preliminary_exam, name='preliminary_exam'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)qualifying_exam/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.qualifying_exam, name='qualifying_exam'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)qualifying_exam_new/(?:(?P<option>[a-z_]+)/)?$',\
        views.qualifying_exam_new, name='qualifying_exam_new'),
    # url(r'^students/qualifying_exam_new/(?P<id>\d+)/$', views.qualifying_exam_new, name='qualifying_exam_new'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)annual_review/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.annual_review, name='annual_review'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)thesis_dissertation_proposal/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.thesis_dissertation_proposal, name='thesis_dissertation_proposal'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)final_exam/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.final_exam, name='final_exam'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)thesis_dissertation/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.thesis_dissertation, name='thesis_dissertation'),
    url(r'^degree/(?:(?P<deg_id>\d+)/)other_doc/(?:(?P<option>[a-z_]+)/)?(?:(?P<id>\d+)/)?$',\
        views.other_doc, name='other_doc'),

    url(r"^(?P<file_path>.+)$", views.serve_protected_document, name='decrypt_and_serve'),

]
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
