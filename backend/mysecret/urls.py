from django.urls import path

from .views import (CheckAvailableView, CreateSecretView, PrivateView,
                    RetriveSecretView)

urlpatterns = [
    path(r'secrets', CreateSecretView.as_view()),
    path(r'secrets/<str:pk>', RetriveSecretView.as_view()),
    path(r'check/<str:pk>', CheckAvailableView.as_view()),
    path(r'private/<str:pk>', PrivateView.as_view()),
]
