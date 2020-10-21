from django.urls import path  # , include

from .views import SecretViewSet, CreateSecretView  # , TestView

urlpatterns = [
    path(r'secrets', CreateSecretView.as_view()),
    path(r'secrets/<str:pk>', SecretViewSet.as_view({'get': 'retrieve'})),
]
