from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, DebtSerializer
from rest_framework import viewsets
from .models import Debt

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response({'users': usernames })


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # return empty list... users can be display only with endpoint /users
    # Instead I would add: Admin Access or Specific User who wants to see his ballance
    # permission_classes = [Admin]
    # authentication_classes = (TokenAuthentication,)
    # def get_queryset(self):
    #     queryset = []
    #     return queryset

# ViewSets define the view behavior.
class DebtViewSet(viewsets.ModelViewSet):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
    
    def get_queryset(self):
        queryset = []
        return queryset

    # def create(self, request, *args, **kwargs):
    #     pass    