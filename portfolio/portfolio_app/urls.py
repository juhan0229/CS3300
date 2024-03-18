from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('project/create/', views.create_project, name='create_project'),  
    path('project/<int:project_id>/', views.view_project, name='view_project'),
    path('project/<int:project_id>/update/', views.update_project, name='update_project'),
    path('project/<int:project_id>/delete/', views.delete_project, name='delete_project'),
    path('portfolio/create/', views.create_portfolio, name='create_portfolio'),
    path('portfolio/<int:portfolio_id>/delete/', views.delete_portfolio, name='delete_portfolio'),
]