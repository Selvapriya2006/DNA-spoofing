from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send/', views.send_message, name="send_message"),
    path('receive/<int:user_id>/', views.receive_message, name="receive_message"),
]

