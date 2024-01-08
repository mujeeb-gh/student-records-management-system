from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_student, name='add_student'),
    path('read/<path:matric_number>/', views.read_student, name='read_student'),
    path('download/<path:matric_number>/', views.download_report, name='download_report'),
    path('delete/<path:matric_number>/', views.delete_student, name='delete_student'),
    path('edit/<path:matric_number>/', views.edit_student, name='edit_student'),
    path('homepage/', views.homepage, name='homepage'),
    # path('download_report/<path:matric_number>/', views.generate_pdf, name='download_report')
    # Add more URL patterns for CRUD operations if needed
]
