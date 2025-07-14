from django.urls import path
from . import views # Uncomment this line
from .views import import_students_view # Keep the explicit import
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
#from .views import add_daily_memorization_task
#from .views import Daily_Memorization_Task_select_student, Daily_Memorization_Task_add
from .views import Daily_Memorization_Task_select_student, Daily_Memorization_Task_add
from .views import save_memorization_task
from .views import weekly_lecture_list, weekly_lecture_detail, add_weekly_lecture
from .views import chat_view
from .views import chat_with_admin_view
from .views import latest_lecture_view
from .views import manage_msars
from .views import manage_msars

from .views import student_register, student_home_view


urlpatterns = [
    path('manage/weekly_lectures/<int:lecture_id>/delete/', views.delete_weekly_lecture_view, name='delete_weekly_lecture'), # Changed base path to /manage/
    path('register_student/', views.student_register, name='register_student'),
    path('register_teacher/', views.teacher_register, name='register_teacher'),
    path('student_login_view/', views.teacher_register, name='student_login_view'),
    path('teacher_registration_success/', views.teacher_registration_success, name='teacher_registration_success'),
    path('employee_login_view/', views.teacher_register, name='employee_login_view'),
    path('add_teacher/', views.add_teacher_view, name='add_teacher'),
   
   
   path('login/', views.custom_login_view, name='login'),  # تأكد من استخدام 'user_login' بدلاً من 'login_view'
   
   
   path('', views.index, name='index'),
   
   
   
    path('superuser_dashboard/', views.superuser_dashboard, name='superuser_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/weekly_lectures/edit/<int:lecture_id>/', views.edit_weekly_lecture_view, name='edit_weekly_lecture'),
    path('manage_weekly_lectures/', views.manage_weekly_lectures_view, name='manage_weekly_lectures'),
    path('manage_links/', views.manage_links_view, name='manage_links'),
    path('manage_report/', views.manage_report_view, name='manage_report'),
   path('student_report/', views.student_report_view, name='student_report'),
   path('student_report/export/excel/', views.export_student_report_excel, name='export_student_report_excel'),
   path('teacher_report/', views.teacher_report_view, name='teacher_report'),
   path('teacher_report/export/excel/', views.export_teacher_report_excel, name='export_teacher_report_excel'),
   path('memorization_report/', views.memorization_report_view, name='memorization_report'), # Added memorization report URL
   path('halaqa_report/', views.halaqa_report_view, name='halaqa_report'),
   path('halaqa_report/export/excel/<int:halaqa_id>/', views.export_halaqa_report_excel, name='export_halaqa_report_excel'),
    path('student_report_single/', views.student_report_single_view, name='student_report_single'),
   path('halaqa/<int:id>/', views.halaqa_detail, name='halaqa_detail'),
   path('halaqa/<int:halaqa_id>/memorization_history/', views.memorization_history_view, name='memorization_history'),
 
    
    
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
  
    
    path('about/', views.about, name='about'),
    path('almaqraa/', views.almaqraa, name='almaqraa'),
    path('teluse/', views.teluse, name='teluse'),
   
   
    path('student/<int:student_id>/', views.student_detail_view, name='student_detail'),
   
   
   
   path('Daily_Memorization_Task/add/<int:student_id>/', views.Daily_Memorization_Task_add, name='add_memorization_task'),
    path('halaqa/<int:pk>/', views.halaqa_detail, name='halaqa_detail'),
    path('save-memorization-task/', views.save_memorization_task, name='save_memorization_task'),
    path('add-memorization-task/<int:student_id>/', views.Daily_Memorization_Task_add, name='add_memorization_task'),
    path('get-surahs/<str:category>/', views.get_surahs_by_category, name='get_surahs_by_category'),
    path('get_surahs/', views.get_surahs_by_category, name='get_surahs'), # Added to handle /get_surahs?category=X requests
    path('get_ayahs/', views.get_ayahs_by_surah, name='get_ayahs'), # Added URL pattern for get_ayahs
    path('success/<int:student_id>/', views.success_page, name='success_page'),
    path('Daily_Memorization_Task/select_student/<int:halaqa_id>/', views.Daily_Memorization_Task_select_student, name='Daily_Memorization_Task_select_student'),
    path('Daily_Review_Task/select_student/<int:halaqa_id>/', views.Daily_Review_Task_select_student, name='Daily_Review_Task_select_student'),
   
   
   
    path('get_surahs_by_category/<str:category>/', views.get_surahs_by_category, name='get_surahs_by_category'),
 
 
 
 
   path('add_review_task/<int:student_id>/', views.Daily_Review_Task_add, name='add_review_task'),
 
 
    path('daily-review-task/add/<int:student_id>/', views.Daily_Review_Task_add, name='Daily_Review_Task_add'),
   
 
    
    
    
   
    path('success_review/<int:student_id>/', views.success_review, name='success_review'),
   
   
   path('daily-talqeen-task/add/<int:student_id>/', views.Daily_Talqeen_Task_add, name='Daily_Talqeen_Task_add'),
    path('save-daily-talqeen-task/', views.save_daily_talqeen_task, name='save_daily_talqeen_task'),
   
   
    path('daily-talqeen-task/select-student/<int:halaqa_id>/', views.Daily_Talqeen_Task_select_student, name='Daily_Talqeen_Task_select_student'),
 
    path('success-talqeen/<int:student_id>/', views.success_talqeen, name='success_talqeen'),
   
   path('student/<int:student_id>/weekly-plan/', views.weekly_plan_view, name='weekly_plan'),
   
    path('save-daily-review-task/', views.save_daily_review_task, name='save_daily_review_task'),
 
   path('export_student_report_single_excel/', views.export_student_report_excel, name='export_student_report_excel'), # Existing URL for all students report
   path('student_report_single/export/excel/<int:student_id>/<str:from_date>/<str:to_date>/', views.export_student_report_single_excel_view, name='export_student_report_single_excel'), # New URL for single student report
     path('halaqa/<int:halaqa_id>/select-student/', views.weekly_plan_select_student, name='weekly_plan_select_student'),
    
 
    
   path('student/<int:student_id>/home/', views.student_home_view, name='student_home'),
 
  path('teacher/<str:username>/home/', views.teacher_home, name='teacher_home'),  # استخدام اسم المستخدم
 
 
   path('latest-lecture/', latest_lecture_view, name='latest_lecture'),
 
  path('chat_with_admin/<str:username>/', chat_with_admin_view, name='chat_with_admin'),
 
     path('lectures/', weekly_lecture_list, name='lecture_list'),
     path('lectures/<int:lecture_id>/', weekly_lecture_detail, name='lecture_detail'),
     path('lectures/add/', add_weekly_lecture, name='add_lecture'),
     path('weekly_lectures/edit/<int:lecture_id>/', views.edit_weekly_lecture_view, name='edit_weekly_lecture'),
     path('manage_weekly_lectures/add/', views.add_weekly_lecture_view, name='add_weekly_lecture'),
   path('notify_user/', views.notify_user, name='notify_user'),
   
    path('registration_success/', student_register, name='registration_success'),  # إضافة نمط URL لصفحة النجاح
    # أنماط URLs أخرى
    path('chat/<str:username>/', views.chat_view, name='chat'),
  
     
        
   path('manage_sections/', views.manage_sections, name='manage_sections'),
   path('manage_msars/', views.manage_msars, name='manage_msars'),
   path('manage_halaqat/', views.manage_halaqat, name='manage_halaqat'),
   path('manage_typereads/', views.manage_typereads, name='manage_typeread'),
   path('add_department/', views.add_department, name='add_department'),
   path('edit_department/<int:department_id>/', views.edit_department, name='edit_department'),
   path('delete_department/<int:department_id>/', views.delete_department, name='delete_department'),
   path('add_msar/', views.add_msar_view, name='add_msar'),
   path('edit_msar/<int:msar_id>/', views.edit_msar_view, name='edit_msar'),
   path('delete_msar/<int:msar_id>/', views.delete_msar_view, name='delete_msar'),
   path('add_halaqa/', views.add_halaqa_view, name='add_halaqa'),
   path('edit_halaqa/<int:halaqa_id>/', views.edit_halaqa_view, name='edit_halaqa'),
   path('add_typeread/', views.add_typeread_view, name='add_typeread'),
   path('edit_typeread/<int:typeread_id>/', views.edit_typeread_view, name='edit_typeread'),
   path('delete_typeread/<int:typeread_id>/', views.delete_typeread_view, name='delete_typeread'),
   path('delete_halaqa/<int:halaqa_id>/', views.delete_halaqa_view, name='delete_halaqa'),
   path('student_distribution/', views.student_distribution_view, name='student_distribution'), # Added student distribution URL
   path('assign_halaqa/', views.assign_halaqa_to_student, name='assign_halaqa_to_student'), # New URL for assigning halaqa
   path('statistics_dashboard/', views.statistics_dashboard_view, name='statistics_dashboard'), # New URL for statistics dashboard
   path('manage_students/', views.manage_students, name='manage_students'),
   path('add_student/', views.add_student_view, name='add_student'), # URL for adding a new student
   path('edit_student/<int:student_id>/', views.edit_student_view, name='edit_student'), # URL for editing a student
   path('delete_student/<int:student_id>/', views.delete_student_view, name='delete_student'), # URL for deleting a student
   path('maqraapp_admin/export_students_excel/', views.export_students_excel_view, name='export_students_excel'),
  path('manage_teachers/', views.manage_teachers_view, name='manage_teachers'),
  path('edit_teacher/<int:teacher_id>/', views.edit_teacher_view, name='edit_teacher'), # URL for editing a teacher
  path('delete_teacher/<int:teacher_id>/', views.delete_teacher_view, name='delete_teacher'), # URL for deleting a teacher
  path('export_teachers/', views.export_teacher_report_excel, name='export_teachers_excel'), # URL for exporting teachers to Excel
  path('import_students/', import_students_view, name='import_students'), # URL for importing students from Excel
path('generate_student_template/', views.generate_student_excel_template_view, name='generate_student_template'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
