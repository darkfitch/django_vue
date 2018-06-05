
from rest_framework.views import APIView
from rest_framework.response import Response

from course import models

import uuid
class Auth(APIView):

    def post(self,request,*args,**kwargs):
        ret = {'code':1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')

        user_obj = models.Account.objects.filter(username=user,password=pwd).first()
        if not user_obj:
            ret['code'] = 4000
            ret['error'] = '用户名或密码错误'
        else:
            uid = str(uuid.uuid4())
            models.UserAuthToken.objects.update_or_create(user=user_obj,token=uid)
            ret['token']=uid
            print(ret)
        return Response(ret)


class AuthResiger(APIView):

    def post(self,request,*args,**kwargs):
        ret = {'code': 1000}
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        user_obj = models.Account.objects.filter(username=user).first()
        if not user_obj:
            uid = str(uuid.uuid4())
            models.Account.objects.create(username=user, password=pwd,defaults={'token': uid})
            ret['token'] = uid
        else:
            ret['code'] = 4000
            ret['error'] = '用户名已存在'
        return Response(ret)