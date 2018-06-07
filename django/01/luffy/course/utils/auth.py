from rest_framework.authentication import BaseAuthentication
from course import models
from rest_framework.exceptions import AuthenticationFailed


class Auth(BaseAuthentication):
    def authenticate(self, request):
        '''
        用户认证
        '''
        #从URL中获取token
        token = request.query_params.get('token')
        obj = models.UserAuthToken.objects.get(token=token)
        if not obj:
            raise AuthenticationFailed({'code':4000,'error':'认证失败'})
        return (obj.user.username,obj)
