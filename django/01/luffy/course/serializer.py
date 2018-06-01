from rest_framework import serializers
from course import models


class CurrentSer(object):
    '''
    旨在序列化的时候可以简化操作
    '''
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_choise_ser(self,name):
        new_name = serializers.CharField(source='get_%s_display'%name)
        return new_name

    def get_related_ser(self):
        pass




def get_choise_ser(name=None):
    '''
    尝试用函数封装一次序列化方法
    :param name:
    :return:
    '''
    new_name = serializers.CharField(source='get_%s_display'%name)
    return new_name




# class CourseSer(serializers.ModelSerializer):
#     '''
#     序列化课程表
#     '''
#     temp_a = CurrentSer()
#
#     course_type = temp_a.get_choise_ser(name='course_type')
#     print(course_type)
#
#
#     # 使用函数封装
#     # course_type = get_choise_ser(name='course_type')
#     # print(course_type)
#
#     # course_type = serializers.CharField(source='get_%s_display'%'course_type')
#     # print(course_type)
#     # course_type = serializers.CharField(source='get_course_type_display')
#     sub_category = serializers.CharField(source='sub_category.name')
#
#     class Meta:
#         model = models.Course
#         fields = ['name', 'course_img', 'sub_category', 'course_type']




#---------------------------------------------------------------------------------


# class CourseSer(serializers.ModelSerializer):
#     '''
#     序列化课程表 第一版
#     '''
#     course_type = serializers.CharField(source='get_course_type_display')
#     sub_category = serializers.CharField(source='sub_category.name')
#     class Meta:
#         model = models.Course
#         fields = ['name','course_img','sub_category','course_type']


class CourseSer(serializers.ModelSerializer):
    '''
    序列化课程表第二版
    '''
    temp_a = CurrentSer()
    course_type = temp_a.get_choise_ser(name='course_type')
    sub_category = serializers.CharField(source='sub_category.name')

    class Meta:
        model = models.Course
        fields = ['name', 'course_img', 'sub_category', 'course_type']


