
from django.contrib import admin
from django.urls import path
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page-list/', views.page_list, name = "page-list"),
    path('page-detail/<int:page_id>', views.page_detail, name = "page-detail"),
]
