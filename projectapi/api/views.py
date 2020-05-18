import uuid
from datetime import datetime, date
from datetime import timedelta
from random import randint
from django.http import HttpResponse
from django.db import connection as conn

import pytz
import sys
from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.utils import timezone
from sendotp import sendotp

from api.serializers import BryUserSerializer, Ttdphw016200Serializer
import hashlib
from api.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)

from rest_framework import viewsets
from django.apps import apps


class UserView(viewsets.ModelViewSet):
    queryset = BryUser.objects.all()
    serializer_class = BryUserSerializer


def my_response(error=False, code=200, status=1, message="Success", payload=[], extra_data={}):
    return {
        "Error": error,
        "Code": code,
        "Status": 200,
        "Message": message,
        "Payload": payload,
        "Extra": extra_data
    }


def initial_validation(request, my_list=[]):
    pass


def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def zone_division_auth(user_id, order_no):
    # userZone = BryUser.objects.filter(t_usr=user_id).values('t_zone')[0]['t_zone']
    # userDivision = BryUser.objects.filter(t_usr=user_id).values('t_diva')[0]['t_diva']
    order_zone = order_no[2]
    order_division = order_no[3]
    # user_company = find_user_company(user_id=user_id)
    # user_division = find_user_division(user_id=user_id)
    # # return HttpResponse(user_company)
    #
    # user_div_for_search = []
    # user_div_for_search_full_name_list = []
    #
    # for items in user_division:
    #     user_div_for_search.append(items['t_div'])
    # # print(user_zones_for_search)
    # # print(user_div_for_search)
    # user_div_for_search_full_name = Ttdphw020100.objects.filter(t_ncmp=user_company,
    #                                                             t_ornoch__in=user_div_for_search).values()
    # for items in user_div_for_search_full_name:
    #     user_div_for_search_full_name_list.append(items['t_div'])
    # # print(user_company)
    # # table_name_for_search = apps.get_model('api', 'Ttdphw016' + user_company)

    find_auth = Ttdphw019100.objects.filter(t_user=user_id, t_zone=order_zone, t_div=order_division)
    if find_auth.exists():
        return True
    else:
        return False


def find_user_zone(user_id):
    a = Ttdphw019100.objects.filter(t_user=user_id).values('t_zone')
    return (a)
    return Ttdphw019100.objects.filter(t_user=user_id).values('t_zone')[0]['t_zone']


def find_user_division(user_id):
    a = Ttdphw019100.objects.filter(t_user=user_id).values('t_div')
    return (a)
    return Ttdphw019100.objects.filter(t_user=user_id).values('t_div')[0]['t_div']


def get_company_milestones(company_name=None):
    if company_name is not None:
        return Ttdphw023100.objects.filter(t_ncmp=company_name).values('t_mlcd')
    else:
        return None


def find_user_company(user_id=None, device_id=None):
    company = None
    if user_id is not None:
        bryuser_obj = BryUser.objects.filter(t_usr=user_id)
        if bryuser_obj.exists():
            company = (bryuser_obj.values("t_comp")[0]['t_comp'])

    elif device_id is not None:
        bryuser_obj = BryUser.objects.filter(t_deviceid=device_id)
        if bryuser_obj.exists():
            company = (bryuser_obj.values("t_comp")[0]['t_comp'])

    if company == 1:
        return "100"
    elif company == 2:
        return "200"
    elif company == 3:
        return "300"


def find_user_device_id_exists(device_id=None):
    usr_id = None
    if device_id is not None:
        bryuser_obj = BryUser.objects.filter(t_deviceid=device_id)
        if bryuser_obj.exists():
            usr_id = (bryuser_obj.values("t_usr")[0]['t_usr'])
    return usr_id


def compare_user_zone_and_orderno(user_id=None, order_no=None):
    order_zone = order_no[2]
    compare_user_zone_and_orderno()
    pass


@api_view(['POST'])
def first_time_login(request):
    user_id = request.data.get("user_id")
    user_mobile = request.data.get("user_mobile")
    device_id = request.data.get("device_id")

    if user_id is None or user_mobile is None or user_id == "" or user_mobile == "" or device_id is None or device_id == "":
        return Response(my_response(True, HTTP_200_OK, 1, "Please Fill all fields user_id , user_mobile"))

    bryuser_obj = BryUser.objects.filter(t_usr=user_id)
    bryuser_obj_mobile = BryUser.objects.filter(t_usr=user_id, t_mbno=user_mobile)

    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "Invalid User Id"))
    elif not bryuser_obj_mobile:
        return Response(my_response(True, HTTP_200_OK, 1, "Invalid User Mobile"))
    else:
        bryuser_obj_active = BryUser.objects.filter(t_usr=user_id, t_mbno=user_mobile, t_isatuc=1)
        if not bryuser_obj_active:
            return Response(my_response(True, HTTP_200_OK, 1, "User not Active"))
        else:
            bryuser_obj_for_device_id = BryUser.objects.filter(t_deviceid=device_id)
            bryuser_obj_for_device_id.update(t_deviceid="")
            send_otp(bryuser_obj, user_id, user_mobile)
            bryuser_obj.update(t_deviceid=device_id)

            bryUserSer = BryUserSerializer(bryuser_obj, many=True)
            # data = serializers.serialize('json', bryuser_obj)
            # print(type(bryUserSer.data))
            return Response(my_response(False, HTTP_200_OK, 1, "Main Data", bryUserSer.data))


@api_view(['POST'])
def resend_otp(request):
    user_id = request.data.get("user_id")
    user_mobile = request.data.get("user_mobile")
    if user_id is None or user_mobile is None or user_id == "" or user_mobile == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields user_id,user_mobile"))

    # bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id)
    bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_mbno=user_mobile)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "Please enter valid user_id"))
    else:
        send_otp(bryuser_obj, user_id, user_mobile)
        bryUserSer = BryUserSerializer(bryuser_obj, many=True)
        return Response(
            my_response(False, HTTP_200_OK, 1, "Resend sucessfully!", {"OTP": bryuser_obj.values('t_otp')[0]['t_otp']}))


@api_view(['POST'])
def verify_otp(request):
    user_id = request.data.get("user_id")
    device_id = request.data.get("device_id")
    otp = request.data.get("otp")

    if user_id is None or device_id is None or otp is None or user_id == "" or device_id == "" or otp == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields user_id , device_id ,  otp "))

    # bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id)
    bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_otp=otp)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "Please enter valid OTP"))
    else:
        pass_gen = bryuser_obj.values('t_pass')[0]['t_pass']
        # print(pass_gen)
        is_pass_generated = False
        if pass_gen:
            is_pass_generated = True
        # print(is_pass_generated)
        # hashed_password = hash_password(password)
        bryuser_obj.update(t_deviceid=device_id)
        bryUserSer = BryUserSerializer(bryuser_obj, many=True)
        mainData = bryUserSer.data[0]
        mainData["is_pass_generated"] = is_pass_generated
        return Response(my_response(False, HTTP_200_OK, 1, "Main Data", mainData))


@api_view(['POST'])
def create_password(request):
    user_id = request.data.get("user_id")
    device_id = request.data.get("device_id")
    password = request.data.get("password")

    if user_id is None or device_id is None or password is None or user_id == "" or device_id == "" or password == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields user_id , device_id ,  password "))

    # bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id)
    # today = datetime.now()
    # print(today)
    bryuser_obj = BryUser.objects.filter(t_usr=user_id)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "User not Exists"))
    else:
        hashed_password = hash_password(password)
        bryuser_obj.update(t_pass=hashed_password, t_deviceid=device_id, t_passdate=timezone.now())
        bryUserSer = BryUserSerializer(bryuser_obj, many=True)
        return Response(my_response(False, HTTP_200_OK, 1, "Main Data", bryUserSer.data))


@api_view(['POST'])
def main_login(request):
    user_id = request.data.get("user_id")
    device_id = request.data.get("device_id")
    password = request.data.get("password")

    if user_id is None or device_id is None or password is None or user_id == "" or device_id == "" or password == "":
        return Response(
            my_response(True, HTTP_200_OK, 200, "Please Fill all fields user_id , device_id ,  password "))

    bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id, t_isatuc=1)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 200, "User Id , Device Id  Status Mismatch"))
    elif((bryuser_obj.values('t_pass')[0]['t_pass']) == ""):
        return Response(my_response(True, HTTP_200_OK, 200, "Please set your password"))
    else:
        # print(password)
        # if((bryuser_obj.values('t_pass')[0]['t_pass']) == ""):
        #     print(bryuser_obj.values('t_pass')[0]['t_pass'])
        # return Response({"asd":password})
        hashed_password = check_password(bryuser_obj.values('t_pass')[0]['t_pass'], password)
        if not hashed_password:
            return Response(my_response(True, HTTP_200_OK, 200, "Invalid Password"))
        else:
            bryUserSer = BryUserSerializer(bryuser_obj, many=True)
            # print(pass_date)
            historyTable = Ttdphw026100(t_usid=user_id,t_deviceid=device_id,t_datetime=timezone.now(),t_actn='login')
            historyTable.save()
            pass_status = is_date_outside_three_months(user_id)
            # print(pass_status)
            return Response(my_response(False, HTTP_200_OK, 200, "Successfully Login", bryUserSer.data,
                                        {"is_date_outside_three_months": pass_status}))


@api_view(['POST'])
def forget_pass_clear_data_from_database(request):
    user_id = request.data.get("user_id")

    if user_id is None or user_id == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields user_id"))

    bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_isatuc=1)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "User not Exists"))
    else:
        bryuser_obj.update(t_pass="")
        print(bryuser_obj.values())
        return Response(my_response(False, HTTP_200_OK, 1, "Success", {"password_cleaned": "Success"}))


@api_view(['POST'])
def change_password(request):
    user_id = request.data.get("user_id")
    device_id = request.data.get("device_id")
    password = request.data.get("old_password")
    new_password = request.data.get("new_password")

    if user_id is None or device_id is None or password is None or new_password is None or user_id == "" or device_id == "" or password == "" or new_password == "":
        return Response(
            my_response(True, HTTP_200_OK, 1,
                        "Please Fill all fields user_id , device_id ,new_password ,  old_password "))

    bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "User not Exists"))
    else:
        hashed_password = check_password(bryuser_obj.values('t_pass')[0]['t_pass'], password)
        if not hashed_password:
            return Response(my_response(True, HTTP_200_OK, 1, "Invalid Password"))
        else:
            bryUserSer = BryUserSerializer(bryuser_obj, many=True)
            bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id)
            hashed_password_update = hash_password(new_password)
            bryuser_obj.update(t_pass=hashed_password_update)
            return Response(my_response(False, HTTP_200_OK, 1, "Successfully Updated", bryUserSer.data))


@api_view(['POST'])
def user_logout(request):
    user_id = request.data.get("user_id")
    device_id = request.data.get("device_id")

    if user_id is None or device_id is None  or user_id == "" or device_id == "" :
        return Response(
            my_response(True, HTTP_200_OK, 1,
                        "Please Fill all fields user_id , device_id"))

    bryuser_obj = BryUser.objects.filter(t_usr=user_id, t_deviceid=device_id)
    if not bryuser_obj:
        return Response(my_response(True, HTTP_200_OK, 1, "User not Exists"))
    else:

        lastLogin = Ttdphw026100.objects.filter(t_usid=user_id, t_deviceid=device_id,t_actn='login').order_by('-t_unid').values()

        if len(lastLogin) > 0 :
            # print(lastLogin[0]['t_datetime'])
            # print(timezone.now())
            # print(timezone.now() - lastLogin[0]['t_datetime'])
            # ,t_duration=(timezone.now() - lastLogin[0]['t_datetime'])
            historyTable = Ttdphw026100(t_usid=user_id, t_deviceid=device_id, t_datetime=timezone.now(),
                                        t_actn='logout',t_duration = (str(timezone.now() - lastLogin[0]['t_datetime'])).split('.')[0])
        else :
            historyTable = Ttdphw026100(t_usid=user_id, t_deviceid=device_id, t_datetime=timezone.now(),
                                        t_actn='logout')


        # print(lastLogin)

        # historyTable = Ttdphw026100(t_usid=user_id, t_deviceid=device_id, t_datetime=timezone.now(),
        #                             t_refcntd='logout')
        historyTable.save()
        # bryuser_obj.update(t_deviceid="")

        return Response(my_response(False, HTTP_200_OK, 1, "Logout Successfully", {"is_logout" : "success",'log_out_user_id': user_id}))



@api_view(['POST'])
def test(request):
    a = Ttdphw016200.objects.all().values()
    b = Ttdphw016200Serializer(a, many=True)

    # print(a)
    print(b.data)
    return Response({"data": b.data})


@api_view(['POST'])
def search_by_orderno(request):
    order_no = request.data.get('order_no')
    device_id = request.data.get('device_id')
    user_id = request.data.get('user_id')
    if order_no is None or device_id is None or user_id is None or order_no == "" or device_id == "" or user_id == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields order_no "
                                              ", device_id , user_id "))

    device_id_check = find_user_device_id_exists(device_id)
    # print(device_id_check)

    if device_id_check is None:
        return Response(
            my_response(True, HTTP_200_OK, 1, "Invalid device Id"))
    elif device_id_check != user_id:
        return Response(
            my_response(True, HTTP_200_OK, 1, "Mis match device Id and User"))

    auth_response = zone_division_auth(user_id, order_no)
    # print(auth_response)
    if not auth_response:
        return Response(
            my_response(True, HTTP_200_OK, 1,
                        "You are not Authorized to view data for this Zone and Division"))

    user_company = find_user_company(user_id=user_id)
    # return HttpResponse(user_company)
    # print(user_company)
    table_name_for_search = apps.get_model('api', 'Ttdphw016' + user_company)

    check_order_exists = table_name_for_search.objects.filter(t_orno=order_no).values()

    if not check_order_exists:
        return Response(
            my_response(True, HTTP_200_OK, 1,
                        "This Order No. Not Exists"))

    # print(check_order_exists)

    order_no_results = table_name_for_search.objects.filter(t_orno=order_no).values('t_unid', 't_orno', 't_sqnb',
                                                                                    't_pono', 't_cnama',
                                                                                    't_comp', 't_invto', 't_shpto',
                                                                                    't_sqnb', 't_pono', 't_idsca')
    # vikas
    # added more attribute as per abhisheck sir required
    # print(order_no_results)
    # return Response({'test': order_no_results})
    pass_status = is_date_outside_three_months(user_id)
    if not order_no_results:
        return Response(my_response(False, HTTP_200_OK, 1, "Successful", None,
                                    {"is_date_outside_three_months": pass_status}))
    else:
        pass_status = is_date_outside_three_months(user_id)
        return Response(my_response(False, HTTP_200_OK, 1, "Successful", order_no_results,
                                    {"is_date_outside_three_months": pass_status}))


# @api_view(['POST'])
# def search_by_name(request):
#     name = request.data.get('name')
#     device_id = request.data.get('device_id')
#     user_id = request.data.get('user_id')
#     #return HttpResponse(user_id)
#     if name is None or device_id is None or user_id is None:
#         return Response(
#             my_response(True, HTTP_400_BAD_REQUEST, 1, "Please Fill all fields name "
#                                                        ", device_id , user_id "))
#
#     user_company = find_user_company(user_id=user_id)
#     table_name_for_search = apps.get_model('api', 'Ttdphw016' + user_company)
#     user_zone = find_user_zone(user_id=user_id)
#     user_division = find_user_division(user_id=user_id)
#     print(user_zone)
#     print(user_division)
#     user_zones_for_search = []
#     user_div_for_search = []
#     for items in user_zone:
#         user_zones_for_search.append(items['t_zone'])
#
#     for items in user_division:
#         user_div_for_search.append(items['t_div'])
#     order_no_results = table_name_for_search.objects.filter(t_cnama__icontains=name,t_zone__in=user_zones_for_search).values()
#     # t_divs__in in not searching now in query
#     # order_no_results = table_name_for_search.objects.filter(t_cnama__icontains=name, t_zone__in=['N', 'N', 'E'],
#     #                                                         t_divs__in=['F', 'G', 'M','A']).values()
#     # print(order_no_results)
#     #return HttpResponse(order_no_results)
#     # return Response({"data" : "table_name_for_search"})
#     # return Response({'test': order_no_results})
#     return Response(my_response(False, HTTP_200_OK, 1, "Successful", order_no_results,
#                                 {"is_date_outside_three_months": is_date_outside_three_months(user_id)}))
#


@api_view(['POST'])
def search_by_name(request):
    name = request.data.get('name')
    device_id = request.data.get('device_id')
    user_id = request.data.get('user_id')
    if name is None or device_id is None or user_id is None or device_id == "" or user_id == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields name "
                                              ", device_id , user_id "))

    user_company = find_user_company(user_id=user_id)
    device_id_check = find_user_device_id_exists(device_id)
    # print(device_id_check)

    if device_id_check is None:
        return Response(
            my_response(True, HTTP_200_OK, 1, "Invalid device Id"))
    elif device_id_check != user_id:
        return Response(
            my_response(True, HTTP_200_OK, 1, "Invalid request"))

    table_name_for_search = apps.get_model('api', 'Ttdphw016' + user_company)
    user_zone = find_user_zone(user_id=user_id)
    user_division = find_user_division(user_id=user_id)

    user_zones_for_search = []
    user_div_for_search = []
    user_div_for_search_full_name_list = []
    for items in user_zone:
        user_zones_for_search.append(items['t_zone'])

    for items in user_division:
        user_div_for_search.append(items['t_div'])

    user_div_for_search_full_name = Ttdphw020100.objects.filter(t_ncmp=user_company,
                                                                t_ornoch__in=user_div_for_search).values()
    for items in user_div_for_search_full_name:
        user_div_for_search_full_name_list.append(items['t_div'])

    find_auth = Ttdphw019100.objects.filter(t_user=user_id).values()

    order_no_results = table_name_for_search.objects.filter(t_cnama__icontains=name, t_zone__in=user_zones_for_search,
                                                            t_divs__in=user_div_for_search_full_name_list).values()

    my_final_list = []

    # print(len(order_no_results))
    # print(len(find_auth))

    for i in find_auth:
        # print(i)
        div_name = Ttdphw020100.objects.filter(t_ncmp=user_company, t_ornoch=i['t_div']).values('t_div')[0]['t_div']
        # print(div_name)

        for j in order_no_results:
            # print(j)
            if ((div_name == j['t_divs']) and i['t_zone'] == j['t_zone']):
                my_final_list.append(j)

    # for data_order in range(0, len(order_no_results)):
    #
    #     for data in range(0, len(find_auth)):
    #         full_name = \
    #         Ttdphw020100.objects.filter(t_ncmp=user_company, t_ornoch=find_auth[data]['t_div']).values('t_div')[0][
    #             't_div']
    #         find_auth[data]['full_div_name'] = \
    #             Ttdphw020100.objects.filter(t_ncmp=user_company, t_ornoch=find_auth[data]['t_div']).values('t_div')[0][
    #                 't_div']
    #         print("(order_no_results[data_order]['t_zone'] :", (order_no_results[data_order]['t_zone']))
    #         print("find_auth[data]['t_zone'] :", find_auth[data]['t_zone'])
    #         print("order_no_results[data_order]['t_divs'] :", order_no_results[data_order]['t_divs'])
    #         print("full_name :", full_name)
    #         if ((order_no_results[data_order]['t_zone'] == find_auth[data]['t_zone']) and (
    #                 order_no_results[data_order]['t_divs'] == full_name)):
    #             my_final_list.append(order_no_results[data_order])

    # print(order_no_results[data_order])

    # print(order_no_results.query)
    # order_no_results = table_name_for_search.objects.filter(t_cnama__icontains=name, t_zone__in=['N', 'N', 'E'],
    #                                                         t_divs__in=['F', 'G', 'M','A']).values()
    # print(order_no_results)
    # return Response({"data" : "table_name_for_search"})
    # return Response({'test': order_no_results})
    return Response(my_response(False, HTTP_200_OK, 1, "Successful", my_final_list,
                                {"is_date_outside_three_months": is_date_outside_three_months(user_id)}))


@api_view(['POST'])
def final_listing(request):
    order_id = request.data.get('order_id')
    device_id = request.data.get('device_id')
    user_id = request.data.get('user_id')
    if order_id is None or device_id is None or user_id is None or order_id == "" or device_id == "" or user_id == "":
        return Response(
            my_response(True, HTTP_200_OK, 1, "Please Fill all fields order_id "
                                              ", device_id , user_id "))
    device_id_check = find_user_device_id_exists(device_id)
    # print(device_id_check)

    if device_id_check is None:
        return Response(
            my_response(True, HTTP_200_OK, 1, "Invalid device Id"))
    elif device_id_check != user_id:
        return Response(
            my_response(True, HTTP_200_OK, 1, "Invalid User Id"))
    user_company = find_user_company(user_id=user_id)
    milestones_tb_2300 = get_company_milestones(company_name=user_company)
    milestone_list = []
    for x in milestones_tb_2300:
        milestone_list.append(x['t_mlcd'])
    fields_filter = Ttdphw022100.objects.filter(t_mlcd__in=milestone_list).order_by('t_unid').values('t_mdsca',
                                                                                                     't_linkf')
    table_name_for_search = apps.get_model('api', 'Ttdphw016' + user_company)
    # table_name_for_tar_date = apps.get_model('api', 'Ttdphw024' + user_company)
    table_name_for_tar_date_new = apps.get_model('api', 'Ttdphw025' + user_company)

    order_no_results = table_name_for_search.objects.filter(t_unid=order_id).values()
    # print(order_no_results)

    # target_date_result = table_name_for_tar_date.objects.filter(t_orno=order_no_results[0]['t_orno'],
    #                                                             t_pono=order_no_results[0]['t_pono'],
    #                                                             t_seqn=order_no_results[0]['t_sqnb']).values()

    target_date_result_new = table_name_for_tar_date_new.objects.filter(t_orno=order_no_results[0]['t_orno'],
                                                                        t_pono=order_no_results[0]['t_pono'],
                                                                        t_sqnb=order_no_results[0]['t_sqnb']).order_by(
        't_mlcd').values()


    #
    # if not target_date_result_new.exists() :
    #     return Response(
    #         my_response(True, HTTP_200_OK, 1, "Target Date Not Found"))
    #
    #
    # for x in fields_filter:
    #
    #     if order_no_results[0][x['t_linkf']] < datetime(1995, 1, 1):
    #         # print(order_no_results[0][x['t_linkf']])
    #         x['actual_date'] = "1970-01-01"
    #         x['target_date'] = "1970-01-01"
    #         continue
    #
    #     x['actual_date'] = remove_time_from_date(order_no_results[0][x['t_linkf']])
    #
    #     field_name = [x['t_linkf']]
    #     if field_name == ['t_cornodt'] or field_name == ['t_sldt'] or field_name == ['t_tncdt']:
    #         x['target_date'] = "NA"
    #     elif field_name == ['t_submitdt']:
    #         x['target_date'] = (target_date_result_new[8]['t_trdt'])
    #         x['revision_number'] = (order_no_results[0]['t_rvno'])
    #     elif field_name == ['t_apdt']:
    #         x['target_date'] = (target_date_result_new[9]['t_trdt'])
    #     elif field_name == ['t_reldt']:
    #         x['target_date'] = (target_date_result_new[10]['t_trdt'])
    #     elif field_name == ['t_puindate']:
    #         x['target_date'] = (target_date_result_new[11]['t_trdt'])
    #     elif field_name == ['t_podate']:
    #         x['target_date'] = (target_date_result_new[12]['t_trdt'])
    #     elif field_name == ['t_mfgdrwdt']:
    #         x['target_date'] = (target_date_result_new[13]['t_trdt'])
    #     elif field_name == ['t_prdorndt']:
    #         x['target_date'] = (target_date_result_new[1]['t_trdt'])
    #     elif field_name == ['t_mfgcdate']:
    #         x['target_date'] = (target_date_result_new[2]['t_trdt'])
    #     elif field_name == ['t_testdate']:
    #         x['target_date'] = (target_date_result_new[3]['t_trdt'])
    #     elif field_name == ['t_packdate']:
    #         x['target_date'] = (target_date_result_new[4]['t_trdt'])
    #     elif field_name == ['t_shpmdate']:
    #         x['target_date'] = (target_date_result_new[5]['t_trdt'])
    #
    #     if x['target_date'] != "NA" and x['target_date'] < datetime(1995, 1, 1) :
    #         x['actual_date'] = "1970-01-01"
    #         x['target_date'] = "1970-01-01"
    #         continue
    #
    #     x['target_date'] = remove_time_from_date(x['target_date'])
    #



    for x in fields_filter:

        if order_no_results[0][x['t_linkf']] < datetime(1995, 1, 1):
            # print(order_no_results[0][x['t_linkf']])
            x['actual_date'] = "1970-01-01"
            # x['target_date'] = "1970-01-01"
        else :
            x['actual_date'] = remove_time_from_date(order_no_results[0][x['t_linkf']])

        field_name = [x['t_linkf']]
        if field_name == ['t_cornodt'] or field_name == ['t_sldt'] or field_name == ['t_tncdt']:
            x['target_date'] = "NA"
        elif field_name == ['t_submitdt']:
            x['target_date'] = (target_date_result_new[8]['t_trdt'])
            x['revision_number'] = (order_no_results[0]['t_rvno'])
        elif field_name == ['t_apdt']:
            x['target_date'] = (target_date_result_new[9]['t_trdt'])
        elif field_name == ['t_reldt']:
            x['target_date'] = (target_date_result_new[10]['t_trdt'])
        elif field_name == ['t_puindate']:
            x['target_date'] = (target_date_result_new[11]['t_trdt'])
        elif field_name == ['t_podate']:
            x['target_date'] = (target_date_result_new[12]['t_trdt'])
        elif field_name == ['t_mfgdrwdt']:
            x['target_date'] = (target_date_result_new[13]['t_trdt'])
        elif field_name == ['t_prdorndt']:
            x['target_date'] = (target_date_result_new[1]['t_trdt'])
        elif field_name == ['t_mfgcdate']:
            x['target_date'] = (target_date_result_new[2]['t_trdt'])
        elif field_name == ['t_testdate']:
            x['target_date'] = (target_date_result_new[3]['t_trdt'])
        elif field_name == ['t_packdate']:
            x['target_date'] = (target_date_result_new[4]['t_trdt'])
        elif field_name == ['t_shpmdate']:
            x['target_date'] = (target_date_result_new[5]['t_trdt'])

        if x['target_date'] != "NA" and x['target_date'] < datetime(1995, 1, 1) :
            # x['actual_date'] = "1970-01-01"
            x['target_date'] = ""
            continue

        x['target_date'] = remove_time_from_date(x['target_date'])




    rv_date = remove_time_from_date(add_days_to_date((order_no_results[0]['t_reldt']), 70))
    return Response(my_response(False, HTTP_200_OK, 1, "Successfull", fields_filter,
                                {"rev_no": order_no_results[0]['t_rvno'], "name": order_no_results[0]['t_cnama'],
                                 "order_no": order_no_results[0]['t_orno'], "rv_date": rv_date,
                                 "is_date_outside_three_months": is_date_outside_three_months(user_id)}))


def convert_date(main_date):
    main_date = str(main_date)
    datew = main_date.split(' ', 1)
    date_parsed = datetime.strptime(datew[0], '%Y-%m-%d')
    return date_parsed


def remove_time_from_date(main_date):
    main_date = str(main_date)
    datew = main_date.split(' ', 1)
    return datew[0]


def add_days_to_date(main_date, days):
    if main_date is not None:
        new_date = main_date + timedelta(days=days)
        return new_date
    return


def is_date_outside_three_months(user_id):
    bryuser_obj = BryUser.objects.filter(t_usr=user_id)
    pass_date = bryuser_obj.values('t_passdate')[0]['t_passdate']
    if pass_date < (datetime.now() - timedelta(days=90)):
        return True
    return False


def send_otp(bryuser_obj, user_id, user_mobile):
    otp = randint(1000, 9999)
    bryuser_obj.update(t_otp=otp)
    otpobj = sendotp.sendotp('OTP_KEY',
                             'Thank you for using our service . Please Use this OTP  {{otp}} , keep otp with you.')
    # print(bryuser_obj)
    user_comp = int(find_user_company(user_id))
    # print(user_comp)
    msg_label = 'APP'
    if user_comp == 100:
        msg_label = 'BRYAPP'
    elif user_comp == 200:
        msg_label = 'DRIAPP'
    elif user_comp == 300:
        msg_label = 'DAIAPP'
    mobile_no_for_otp = int('91' + user_mobile)
    # print(type(a))
    # print(91+int(user_mobile))
    otpobj.send(mobile_no_for_otp, msg_label, otp)
