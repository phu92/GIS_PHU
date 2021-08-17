from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from projectapp.views import ProjectCreateView, ProjectDetailView, ProjectListView

app_name = 'projectapp'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),
    path('list/', ProjectListView.as_view(), name='list'),

]