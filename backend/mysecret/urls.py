from django.urls import path

from .views import CreateSecretView, RetriveSecretView

urlpatterns = [
    path(r'secret', CreateSecretView.as_view()),
    path(r'secret/<str:pk>', RetriveSecretView.as_view()),
]
