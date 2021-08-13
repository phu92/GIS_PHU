from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from projectapp.views import ProjectCreateView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),


]