from course import models
from course.redis_pool import conn
from rest_framework.response import Response
from course.utils.auth import Auth
from rest_framework.viewsets import GenericViewSet
from course.utils.response import Baseresponse
from django_redis import get_redis_connection




class ShoppingCart(GenericViewSet):
    authentication_classes = [Auth]

    def create(self,request,*args,**kwargs):
        ret = Baseresponse()
        try:
            user_id = request.data.get('user')
            # user_obj = models.Account.objects.get(id=user_id)
            price_id = request.data.get('priceid')
            course_id = request.data.get('courseid')
            course_obj = models.Course.objects.get(id=course_id)
            price_obj = models.PricePolicy.objects.get(price_id)
            course_price_list = course_obj.price_policy.all()

            total_key = 'choppingcar_%s_%s'%(user_id,price_id)
            if price_obj in course_price_list:
                pass

        except Exception as e:
            ret.code = 4000
            ret.error = '数据获取失败'
        return Response(ret.dict)