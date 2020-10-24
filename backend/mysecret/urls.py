from django.urls import path  # , include

from .views import RetriveSecretView, CreateSecretView  # , TestView

urlpatterns = [
    path(r'secrets', CreateSecretView.as_view()),
    path(r'secrets/<str:pk>', RetriveSecretView.as_view()),
]
