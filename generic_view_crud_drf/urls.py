
from django.contrib import admin
from django.urls import path
from api.views import StudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student-api/', StudentAPI.as_view()),
    path('student-api/,int:pk>', StudentAPI.as_view()),
]
