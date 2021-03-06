from django.urls import path
from .views import (
    ReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
)
from . import views

app_name = 'questionnaire'

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('report/', ReportListView.as_view(), name='report-list'),
    path('report/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('report/<int:pk>/update', ReportUpdateView.as_view(), name='report-update'),
    path('report/new/', ReportCreateView.as_view(),
         name='report-create'),
    path('about/', views.about, name='blog-about'),
]
