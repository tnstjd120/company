from django.urls import path
from app_main import views

urlpatterns = [
    path('',views.View_Controls.as_view(),name="index"),
    path('test/',views.View_Controls_Test.as_view(),name="test")
]
