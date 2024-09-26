from django.urls import path
from . import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'),
    path('issue/<int:pk>/', views.issue_detail, name='issue_detail'),
    path('issue/<int:pk>/vote/<int:vote_value>/', views.vote, name='vote'),
    path('issue/<int:pk>/results/', views.issue_results, name='issue_results'),
]
