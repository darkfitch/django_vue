from rest_framework import serializers
from course import models

from django.db.models.query import QuerySet


class CurrentSer(object):
    '''
    旨在序列化的时候可以简化操作
    用类封装序列化方法
    '''
    # ret = {'code':1000,'data':''}
    def __init__(self,*args,**kwargs):
        self.args = args
        self.kwargs = kwargs

    def get_choise_ser(self,name):
        new_name = serializers.CharField(source='get_%s_display'%name)
        return new_name

    # def get_related_ser(self,fkfield=None,infkfield=None,tabel_name=None,obj=None,*args,**kwargs):
    #     '''
    #     针对外键的初始化操作,包括正向和反向  ---第一版 有错
    #     :param fkfield: 外键字段名
    #     :param infkfield: 该字段关联的外键表中需要的字段名
    #     :param tabel_name: 反向关联的表的小写表名
    #     :param obj:序列化的对象,反向查找时:obj.表名_set.all()获取
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     '''
    #     if not tabel_name:
    #         return serializers.CharField(source='%s.%s'%(fkfield,infkfield))
    #     else:
    #         field = tabel_name + '_set'
    #
    #         try:
    #             # queryset = models.Course.objects.values(field).filter(id=obj.id)
    #             queryset = models.Course.objects.values('coursechapter').filter(id=1)
    #         except Exception as e:
    #             # queryset = models.Course.objects.values(tabel_name).filter(id=obj.id)
    #             queryset = models.Course.objects.values('coursechapter_set').filter(id=1)
    #
    #
    #         return queryset.first().id
    #         # if args:
    #         #     # return [{'args':row.args} for row in queryset]
    #         #     # return [row for row in queryset]
    #         #     return queryset.id
    #         # else:
    #         #     return queryset.id


    # def get_related_ser(self, fkfield=None, infkfield=None, tabel_name=None, obj=None, *args, **kwargs):
    #     '''
    #     针对外键的初始化操作,包括正向和反向
    #     :param fkfield: 外键字段名
    #     :param infkfield: 该字段关联的外键表中需要的字段名
    #     :param tabel_name: 反向关联的表的小写表名
    #     :param obj:序列化的对象,反向查找时:obj.表名_set.all()获取
    #     :param args:
    #     :param kwargs:
    #     :return:
    #     '''
    #     if not tabel_name:
    #         return serializers.CharField(source='%s.%s' % (fkfield, infkfield))
    #     else:
    #         field = tabel_name + '_set'
    #         try:
    #             queryset = models.Course.objects.values(field).filter(id=obj.id)
    #             # queryset = models.Course.objects.values('coursechapter').filter(id=1)
    #         except Exception as e:
    #             queryset = models.Course.objects.values(tabel_name).filter(id=obj.id)
    #             # queryset = models.Course.objects.values('coursechapter_set').filter(id=1)
    #         # temp_list = []
    #         for item in queryset:
    #             if args:
    #
    #                 item = item.objects.values(args)
    #                 # temp_list.append(item)
    #             else:
    #                 item = item
    #             # temp_list.append(item)
    #         # return temp_list
    #         return item
    #
    #         # if args:
    #         #     # return [{'args':row.args} for row in queryset]
    #         #     # return [row for row in queryset]
    #         #     return queryset.id
    #         # else:
    #         #     return queryset.id

    def get_many_to_many(self,obj=None,mfield=None,tabel_name=None):
        if not mfield:
            try:
                ret = obj.mfield.all()
            except Exception as e:
                pass

        else:
            pass


    def get_related_ser(self, fkfield=None, infkfield=None, tabel_name=None, obj=None, *args, **kwargs):
        '''
        针对外键的初始化操作,包括正向和反向
        :param fkfield: 外键字段名
        :param infkfield: 该字段关联的外键表中需要的字段名
        :param tabel_name: 反向关联的表的小写表名
        :param obj:序列化的对象,反向查找时:obj.表名_set.all()获取
        :param args:
        :param kwargs:
        :return:
        '''
        if not tabel_name:
            return serializers.CharField(source='%s.%s' % (fkfield, infkfield))
        else:
            field = tabel_name + '_set'
            try:
                queryset = models.Course.objects.values(field).filter(id=obj.id)
            except Exception as e:
                queryset = models.Course.objects.values(tabel_name).filter(id=obj.id)

            # if args:
            #     item = [row.objects.values(args[0]) for row in queryset]
            #     # temp_list.append(item)
            # else:
            #     item = [row for row in queryset]
            return queryset
            # return queryset



# def get_recommends(self, obj):
#     # 获取推荐的所有课程
#     queryset = obj.recommend_courses.all()
#
#     return [{'id': row.id, 'title': row.title} for row in queryset]






#
# def get_choise_ser(name=None):
#     '''
#     尝试用函数封装一次序列化方法
#     :param name:
#     :return:
#     '''
#     new_name = serializers.CharField(source='get_%s_display'%name)
#     return new_name




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
    sub_category = temp_a.get_related_ser(fkfield='sub_category',infkfield='name')
    level = temp_a.get_choise_ser(name='level')

    coursechapter_set = serializers.SerializerMethodField()

    class Meta:
        model = models.Course
        fields = ['id','name','level','beief', 'course_img', 'sub_category', 'course_type','coursechapter_set']
        # fields = ['name','coursechapter_set']



    # def get_coursechapter_set(self,obj):
    #     currentser = CurrentSer()
    #     ret = currentser.get_related_ser(tabel_name='coursechapter')
    #     return [item.name for item in ret]
    #     # return ret



    def get_coursechapter_set(self, obj):
        ret = obj.coursechapter_set.all()
        # return [{'name':row.name} for row in ret]
        return [{'name':row.name,'id':row.id} for row in ret]



            # def get_degree_course(self,obj):
    #     questset = obj.degree_course.all()
    #     print(questset)
    #     return [row for row in questset]


class CourseDetailSer(serializers.ModelSerializer):
    '''
    课程详细
    '''
    recommend_courses = serializers.SerializerMethodField()
    coure_name = serializers.CharField(source='course.name')
    teachers = serializers.SerializerMethodField()
    coursechapter = serializers.SerializerMethodField()

    price_policy = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['coure_name','id','hours','course_slogan',
                  'video_brief_link','why_study',
                  'what_to_study_brief','career_improvement',
                  'coursechapter','teachers',
                  'recommend_courses',
                    'price_policy',
                  ]



    def get_teachers(self,obj):
        ret = obj.teachers.all()
        return [{'id':row.id,'name':row.name,'img':row.image,'brief':row.brief} for row in ret]
        # return [row.name for row in ret]

    # def get_teachers(self,obj):
    #     ret = []
    #     for item in obj:
    #         new_obj = item.teachers.all()
    #         ret.append(new_obj)
    #     return [{'id':row.id,'name':row.name,'img':row.image,'signature':row.signature} for row in ret]



    # def get_recommend_courses(self,obj):
    #     ret = obj.recommend_courses.all()
    #     return [{'id':row.id,'name':row.name} for row in ret]

    def get_coursechapter(self,obj):
        ret = obj.course.coursechapter_set.all()
        return [{'chapter':row.chapter,'name':row.name} for row in ret]

    def get_recommend_courses(self,obj):
        ret = obj.recommend_courses.all()
        return [{'id':row.id,'name':row.name} for row in ret]

    def get_price_policy(self,obj):
        ret = obj.course.price_policy.all()
        # return [{'id':row.id,'price':row.price,'valid_period':row.get_valid_period_display} for row in ret]
        return [{'id':row.id,'price':row.price,'valid_period':row.valid_period} for row in ret]


class Articleser(serializers.ModelSerializer):
    '''
    文章:深科技
    '''

    class Meta:
        model = models.Article
        fields = '__all__'