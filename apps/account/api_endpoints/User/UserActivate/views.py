from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from rest_framework import status
from apps.account.models import User, UserAccount


class UserActivateApiView(APIView):

    def get(self, request):
        return Response(data={"phone_number": _("Phone"), "token": _("JWT Token")})
    
    def post(self, request):
        phone_number = request.data.get('phone_number', None)
        token = request.data.get("token", None)

        if phone_number and token:
            user_exist = User.objects.filter(phone_number = phone_number).exists()
        
            if user_exist:
                user = User.objects.get(phone_number = phone_number)
                account_exists = UserAccount.objects.filter(user = user).exists()
                if not account_exists:
                    user.is_active = True
                    user.token = token
                    user.save()
                    account = UserAccount.objects.create(user = user, username = user.username, phone_number = user.phone_number)
                    user_account_link = "http://127.0.0.1:8000" + reverse("account:user-account-retrive", kwargs={"pk":account.pk})

                    return Response(data={"detail": _(f"Successfully activated user account, Your account link -> {user_account_link}")}, status=status.HTTP_202_ACCEPTED)
                return Response(data={"detail": "Your Account already exist!"})
            return Response(data={"detail": _(f"User not found!")}, status=status.HTTP_404_NOT_FOUND)
        return Response(data={"detail":_("<Phone number> or <token> not found !")}, status=status.HTTP_404_NOT_FOUND)