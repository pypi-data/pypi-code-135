from django.contrib.auth import get_user_model

from rest_framework import generics, viewsets, response
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.serializers import AccountSerializer, CreateAccountSerializer


Account = get_user_model()


class CreateAccountView(generics.CreateAPIView):
    queryset = Account.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CreateAccountSerializer


class WhoamiViewSet(viewsets.ViewSet):

    """
    View to return the current user.
    * Requires token authentication.
    """
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = Account.objects.get(id=self.request.user.id)
        serializer = AccountSerializer(queryset)
        return response.Response(serializer.data)