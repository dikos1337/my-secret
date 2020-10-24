from django.urls import path

from .views import CreateSecretView, RetriveSecretView

urlpatterns = [
    path(r'secrets', CreateSecretView.as_view()),
    path(r'secrets/<str:pk>', RetriveSecretView.as_view()),
]
