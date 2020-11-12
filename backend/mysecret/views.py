from rest_framework import generics

from .models import Secret
from .serializers import CheckAvailableSerializer, SecretSerializer

# Create your views here.


class CreateSecretView(generics.CreateAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer


class CheckAvailableView(generics.RetrieveAPIView):
    queryset = Secret.objects.all()
    serializer_class = CheckAvailableSerializer
    # TODO если сущетвует пароль то поле с паролем
    # заменить на True, а не отправлять сам пароль
    # если щуствует if тогда флаг Available тоже true иначе false


class RetriveSecretView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Secret.objects.all()
    serializer_class = SecretSerializer


# class TestView(views.APIView):
#     def get(self, request):
#         secrets = Secret.objects.all()

#         # the many param informs the serializer
#         # that it will be serializing more than a single article.
#         serializer = CreateSecretSerializer(secrets, many=True)
#         return Response({"secrets": serializer.data})

#     def post(self, request):
#         secret = request.data.get('secret')
#         # Create an article from the above data
#         serializer = CreateSecretSerializer(data=secret)
#         if serializer.is_valid(raise_exception=True):
#             # secret_saved =
#             serializer.save()
#         return Response({
#             "success": "Secret created successfully",
#             "data": serializer.data  # .get('uuid'),
#         })
