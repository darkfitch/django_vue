from course import models
from rest_framework.views import APIView
from rest_framework.response import Response
from course import serializer




# class Course(APIView):
#     '''
#     课程表的视图
#     '''
#     def get(self,request,pk=None,*args,**kwargs):
#         '''
#         未封装,可以实现效果
#         :param request:
#         :param pk:
#         :param args:
#         :param kwargs:
#         :return:
#         '''
#         ret = {'code': 1000, 'data': None}
#         if not pk:
#             obj = models.Course.objects.all()
#         else:
#
#             obj = models.Course.objects.filter(id=pk).first()
#
#         ret['data'] = serializer.CourseSer(obj,many=(not pk)).data
#         return Response(ret)




def use_try(obj,ser,pk=None,*args,**kwargs):
    '''.
    封装出try序列化的函数.
    :param obj: quesrset/obj对象
    :param ser: 序列化方法.
    :param pk: 是否是查询单个
    :param args:
    :param kwargs:
    :return: 返回序列化后的参数,并且在这里将返回值一起封装了
    '''
    ret = {'code': 1000, 'data': None}
    try:
        ser_obj  = ser(obj,many=not pk)
        print(ser_obj)
        ret['data'] = ser_obj.data
    except Exception as e:
        ret['code'] = 4000
        ret['error'] = '数据获取失败,请稍后再试'
    return ret


class Course(APIView):
    '''
    课程表的视图
    '''
    def get(self,request,pk=None,*args,**kwargs):
        '''
        get方法根据是否有pk返回单条或多条数据
        :param request:
        :param pk:
        :param args:
        :param kwargs:
        :return:
        '''
        if not pk:
            obj = models.Course.objects.all()
        else:
            obj = models.Course.objects.filter(id=pk).first()
        ret = use_try(obj, serializer.CourseSer, pk)
        return Response(ret)


