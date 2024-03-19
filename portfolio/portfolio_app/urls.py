from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.logout, name='logout'), 
    path('', views.login, name='login'), 
    path('students/', views.student_list, name='student_list'),
    path('student/<int:student_id>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('project/create/<int:portfolio_id>/', views.create_project, name='create_project'),
    path('project/<int:project_id>/', views.view_project, name='view_project'),
    path('project/update/<int:pk>/', views.update_project, name='update_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('project/<int:project_id>/delete/confirmation/', views.delete_project_confirmation, name='delete_project_confirmation'),
    path('portfolio/<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('portfolio/update/<int:pk>/', views.update_portfolio, name='update_portfolio'), 
]