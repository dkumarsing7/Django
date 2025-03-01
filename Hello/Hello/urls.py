from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Ice creams Admin"
admin.site.site_title = "Ice creams Admin Portal"
admin.site.index_title = "Welcome to Ice creams Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
]
