from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.hello_world),
    path('admin/', admin.site.urls),
]
