from django.urls import path
from.import views
urlpatterns = [
    path('',views.index,name="index.html"),
    path('profile',views.profile,name="profile"),
    path('skill',views.Skill,name="skill"),
    path('project',views.Project,name="project"),
]
