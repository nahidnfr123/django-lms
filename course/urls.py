from django.urls import path
from . import views
from .views import course

urlpatterns = [
    path("", views.index, name='courses'),
    path("<slug:slug>", course.as_view(), name='course_details'),
]



