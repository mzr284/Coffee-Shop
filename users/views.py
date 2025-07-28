import random
from rest_framework import status
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, UserPofile
from .serializer import UserSerializer



class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serial = UserSerializer(users, many=True, context={"request": request})
        return Response(serial.data)


class UserDetail(APIView):

    def get(self, request, username):
        user = User.objects.get(username=username)
        serial = UserSerializer(user, context={"request": request})
        return Response(serial.data)


class UserGetCode(APIView):

    def post(self, request):
        phone_number = request.data.get("phone_number")
        code = random.randint(100000, 999999)
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(phone_number=phone_number).exists():
            return Response({"error": "This phone number already registered"}, status=status.HTTP_409_CONFLICT)

        cache.set(str(phone_number), code, 1 * 60)
        return Response({"code": code}, status=status.HTTP_200_OK)

logs = {}

class UserRegister(APIView):

     def post(self, request):
         phone_number = request.data.get("phone_number")
         code = request.data.get("code")
         cashed_code = cache.get(str(phone_number))

         if str(phone_number) in logs:
             if logs[str(phone_number)] == 3:
                 return Response(status=status.HTTP_401_UNAUTHORIZED)

         if cashed_code != code or cashed_code is None:
             if str(phone_number) in logs:
                 logs[str(phone_number)] += 1
             else:
                 logs[str(phone_number)] = 1
             return Response(status=status.HTTP_409_CONFLICT)

         user = User.objects.create_user(phone_number=phone_number)
         user_profile = UserPofile.objects.create(user=user)
         return Response({"message": "This phone number registered successfully"}, status=status.HTTP_201_CREATED)
