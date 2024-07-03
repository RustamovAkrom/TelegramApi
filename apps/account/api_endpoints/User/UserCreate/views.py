from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from apps.account.models import User


class UserCreateApiView(APIView):
    def get(self, request):
        return Response(data={"username":_("Username"), "phone_number": _("Phone number"), "password": _("Password")})
    
    def post(self, request):
        activated_account_link = "http://127.0.0.1:8000" + reverse("account:user-activate")
        username = request.data.get("username", None)
        phone_number = request.data.get('phone_number', None)
        password = request.data.get("password", None)

        try:
            if phone_number and username and password:
                user_phone_exist = User.objects.filter(phone_number = phone_number).exists()
                user_username_exist = User.objects.filter(username = username).exists()

                if user_phone_exist:
                    return Response(data={"detail":_("User phone number already exist!")})

                if user_username_exist:
                    return Response(data={"detail":_("User username already exist!")})
                
                user = User.objects.create(username = username, phone_number = phone_number)
                user.set_password(password)
                user.save()

                return Response(data={"detail": _(f"{user.username} successfully created. Activate account link -> {activated_account_link}")}, status=status.HTTP_201_CREATED)
            return Response(data={"detail": _("<phone_number> or <username> not found")}, status=status.HTTP_404_NOT_FOUND)
        except:
            return Response(data={"detail":_("Internal Server Error")}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
__all__ = ("UserCreateApiView", )