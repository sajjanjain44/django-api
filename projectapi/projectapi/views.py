import binascii
import os
from pprint import pprint

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import uuid
from rest_framework.response import Response

from api.models import BryUser, Ttdphw016100
from api.serializers import BryUserSerializer, FirstCompanyrSerializer


# @csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
      valData =   ValidationError({"username": "please insert correct data", "password": 'please input pass'})
    return Response({'error': 'Please provide both username and password'},
                    status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


def checkAuthSz(r) -> object:
    return "sadfasdf"


@api_view(['POST'])
@permission_classes((AllowAny,))
def testing(request):
    # print(checkAuthSz(request))
    bryUser = BryUser.objects.filter(t_usr="10706", t_mbno="9582700980")
    bryUserObj = BryUser(bryUser)
    bryUserFirst = bryUser.values_list('t_ispass', flat=True)
    # if bryUserFirst == "2":
    print(bryUserObj.t_usr)
    if bryUser.exists():
        print("exists")
        # print(bryUser)
        data = binascii.hexlify(os.urandom(10)).decode()
        print(data)
        # bryUser.t_autk = data
        bryUser.update(t_autk=data)

    else:
        print("not exists")
    # pprint(bryUser[:1])
    # token, _ = Token.objects.get_or_create(user=bryUser)
    # print(token.key);

    bryUserSer = BryUserSerializer(bryUser, many=True)
    firstCom = Ttdphw016100.objects.all()
    firstComSer = FirstCompanyrSerializer(firstCom, many=True)
    return Response({"user": bryUserSer.data, "companyDetails": firstComSer.data})


