from django.test import TestCase
from django.shortcuts import HttpResponse
from rest_framework.response import Response
from django.contrib.contenttypes.models import ContentType
# Create your tests here.



from course import models
from django.contrib.sessions.middleware import SessionMiddleware




# fields = [(field_name, attrs.pop(field_name)) for field_name, obj in list(attrs.items()) if isinstance(obj, Field)]

#
# def test1(version=None):
#     # questset =models.Course.degree_course
#     a = 'coursechapter'+'_set'
#     #
#     # questset=models.Course.objects.filter(id=1).first().a.all()
#     # questset = [row for row in questset]
#     # print(questset)
#
#
#     try:
#         questset=models.Course.objects.values(a).filter(id = 1)
#         print(questset)
#     except Exception as e:
#         print(str(e))
#
#         questset = models.Course.objects.values('coursechapter').filter(id = 1)
#
#
#     return HttpResponse([row for row in questset])



#
# def test1(version=None):
#     # ret = models.Course.objects.filter(id=1).first().coursechapter_set.all()
#     # temp_a = models.Course.objects.values('coursechapter_set')
#     # ret = models.Course.objects.values('coursechapter_set').filter(id=1)
#
#     # ret = models.Course.objects.filter(id = 1).values('coursechapter')
#     b = 'coursechapter'
#     a = b +'_set'
#
#     try:
#         ret = models.Course.objects.a.all()
#         print(type(ret))
#         print(ret)
#     except Exception as e:
#         print(e)
#         ret = models.Course.objects.a.all()
#         print(type(ret),'b')
#         print(ret,'b')
#     # ret = list(ret)
#     # print(type(ret))
#     # a = []
#     # for i in ret:
#     #     a.append(i.name)
#     # ret = a
#     print(type(ret))
#     return HttpResponse(ret)

def test1(version = None):
    # obj = models.CourseDetail.objects.filter(id=1).first().course.price_policy.all()
    obj = models.CourseDetail.objects.filter(id=1).first().course.asked_question.all()
    # obj = ContentType.objects.get(model='course')
    print(obj)
    print(type(obj))
    return HttpResponse(obj)




# class TestSer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Course
#         fields = ['coursechapter_set']
#
#     def get_coursechapter_set(self, obj):
#         ret = obj.coursechapter_set.all()
#         # return [{'id':row.id} for row in ret]
#         return ret

#
#
# def test1(version=None):
#     obj = models.Course.objects.all()
#     ret = TestSer(obj,many=True)
#     print(ret)
#     return HttpResponse(ret)




# def test2(*args):
#     a = '%s'%args
#     print(a)
#
# test2(*('asdf'))