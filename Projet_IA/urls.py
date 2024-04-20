
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name='home'),
    path("good_news/", views.good_view, name='good' ),
    path("bad_news/", views.bad_view, name='bad' ),
    path("verify_news/", views.verify_view, name='verify' ),
    path("contact_news/", views.contact_view, name='contact' ),
]
