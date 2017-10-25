from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'course$', views.course),
    url(r'course/create$', views.create),
    url(r'course/remove(?P<course_number>\d+)$', views.remove),
    url(r'course/destroy(?P<course_number>\d+)$', views.destroy),
]