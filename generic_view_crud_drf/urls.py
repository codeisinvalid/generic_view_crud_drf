from django.contrib import admin
from django.urls import path
from api.views import RUDStudentAPI, LCStudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-api/', LCStudentAPI.as_view()),
    path('student-api/<int:pk>', RUDStudentAPI.as_view()),
]
