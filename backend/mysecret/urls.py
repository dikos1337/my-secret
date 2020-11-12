from django.urls import path

from .views import CheckAvailableView, CreateSecretView, RetriveSecretView

urlpatterns = [
    path(r'secret', CreateSecretView.as_view()),
    path(r'secret/<str:pk>', RetriveSecretView.as_view()),
    path(r'check/<str:pk>', CheckAvailableView.as_view()),
]
