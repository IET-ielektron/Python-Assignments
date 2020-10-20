from django.urls import path

from . import views

urlpatterns = [
    # /hr/
    path('employees/', views.snippet_list)
]