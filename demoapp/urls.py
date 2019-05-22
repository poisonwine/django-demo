from django.urls import path

from .views import DemoView

urlpatterns = [
    path('messages', DemoView.as_view()),
]
