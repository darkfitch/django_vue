import json
from course import models
from course import serializer
from rest_framework.viewsets import GenericViewSet

from course.redis_pool import conn



class ShoppingCart(GenericViewSet):
    queryset =models.Order.objects.all()
    serializer_class = serializer.OrderViewSer

    def list(self,request,*args,**kwargs):
        # return self.list(request, *args, **kwargs)
        #存入数据库的数据结构为整个购物车大字典下,每个用户都是一个键为用户名/id,值为课程列表的字典
        user = request.user
        user_list = conn.get('shopping_car')
        user_list = json.loads(user_list)
        order_list = user_list.get(user.id)
        return [{'title':row.title,'img':row.img,'price':row.policy,'choise_pric':row.choise_pric} for row in order_list]

    def post(self,request,*args,**kwargs):
        try:
            conn.hset('shopping_car',{})
            user = request.user
            course_id = request.post.get('course')
            choise_pric_id = request.post.get('choise_pric')
            choise_pric_obj = models.PricePolicy.objects.get(id=choise_pric_id)
            course_obj = models.Course.objects.get(id=course_id)
            pric_list = course_obj.price_policy.all()
            if choise_pric_obj in pric_list:
                user_dic = {}


        except Exception as e:
            pass
