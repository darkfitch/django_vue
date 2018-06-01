from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey,GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.utils.safestring import mark_safe
import hashlib

# Create your models here.

class CourseCategory(models.Model):
    '''
    课程大分类
    '''
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '01.课程大类'


class CourseSubCategory(models.Model):
    '''
    课程子类
    '''
    category = models.ForeignKey('CourseCategory')
    name = models.CharField(max_length=64,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '02.课程子类'


class DegreeCourse(models.Model):
    '''
    学位课程
    '''
    name = models.CharField(max_length=64,unique=True)
    course_img = models.CharField(max_length=255,verbose_name='缩略图')
    brief = models.TextField(verbose_name='课程简介')
    total_scholarship = models.PositiveIntegerField(verbose_name='总奖学金(贝里)',default=40000)
    mentor_compenstaion_bonus = models.PositiveIntegerField(verbose_name='导师辅导费',default=15000)
    period = models.PositiveIntegerField(verbose_name='建议学习周期(day)',default=150)
    prerequisite = models.TextField(verbose_name='课程先修要求',max_length=1024)
    teachers = models.ManyToManyField('Teacher',verbose_name='课程讲师')

    # 用于GenericForeignKey反向查询， 不会生成表字段，切勿删除
    # coupon = GenericRelation("Coupon")

    # 用于GenericForeignKey反向查询,不会生成表字段
    degreecourse_price_policy = GenericRelation('PricePolicy')

    # 查询常见问题
    asked_question = GenericRelation('OftenAskedQuestion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '03.学位课'


class Teacher(models.Model):
    '''
    导师/讲师表
    '''
    name = models.CharField(max_length=32)
    role_choices = ((0,'讲师'),(1,'导师'))
    role = models.SmallIntegerField(choices=role_choices,default=0)
    title = models.CharField(max_length=64,verbose_name='职位/职称')
    signature = models.CharField(max_length=255,verbose_name='导师签名',null=True,blank=True)
    image = models.CharField(max_length=128)
    brief = models.TextField(max_length=1024)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '04.导师或讲师'


class Scholarship(models.Model):
    '''
    学位课程奖学金
    '''
    degree_course = models.ForeignKey('DegreeCourse')
    time_percent = models.PositiveSmallIntegerField(verbose_name='奖励等级(时间百分比)',help_text='只填数值,eg:10表示10%')
    value = models.PositiveIntegerField(verbose_name='奖学金金额')

    def __str__(self):
        return '%s:%s'%(self.degree_course,self.value)

    class Meta:
        verbose_name_plural = '05.学位课奖学金'


class Course(models.Model):
    '''
    专题课程/学位课模块
    '''
    name = models.CharField(max_length=128,unique=True)
    course_img = models.CharField(max_length=255)
    sub_category = models.ForeignKey('CourseSubCategory')
    course_type_choices = ((0,'付费'),(1,'VIP专享'),(2,'学位课程'))
    course_type = models.SmallIntegerField(choices=course_type_choices)
    degree_course = models.ForeignKey('DegreeCourse',blank=True,null=True,help_text='如果是学位课,关联学位表')
    beief = models.TextField(verbose_name='课程(模块)概述',max_length=2048)
    level_choices = ((0,'初级'),(1,'中级'),(2,'高级'))
    level = models.SmallIntegerField(choices=level_choices,default=1)
    pub_data = models.DateField(verbose_name='发布日期',blank=True,null=True)
    period = models.PositiveIntegerField(verbose_name='建议学期周期(day)',default=7)
    order = models.IntegerField(verbose_name='课程顺序',help_text='从上一个课程的数字往后排')
    attachment_path = models.CharField(max_length=128,verbose_name='课件路径',blank=True,null=True)
    status_choices = ((0,'上线'),(1,'下线'),(2,'预上线'))
    status = models.SmallIntegerField(choices=status_choices)
    template_id = models.SmallIntegerField(verbose_name='模版编号',default=1)

    # 如果是专题课时，获取相关优惠券
    # coupon = GenericRelation("Coupon")

    # 用于GenericForeignKey反向查询，不会生成表字段
    price_prlicy = GenericRelation('PricePolicy')

    # 查询常见问题
    asked_question = GenericRelation("OftenAskedQuestion")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '06.课程'


class CourseDetail(models.Model):
    '''
    课程详情页内容
    '''
    course = models.ForeignKey('Course')
    hours = models.IntegerField('课时')
    course_slogan = models.CharField(max_length=125,blank=True,null=True)
    video_brief_link = models.CharField(verbose_name='课程介绍',max_length=255,blank=True,null=True)
    why_study = models.TextField(verbose_name='为什么学习这门课')
    what_to_study_brief = models.TextField(verbose_name='我将学习到那些内容')
    career_improvement = models.TextField(verbose_name='课程先求要求',max_length=1024)
    recommend_courses = models.ManyToManyField('Course',related_name='recommend_by',blank=True)
    teachers = models.ManyToManyField('Teacher',verbose_name='课程讲师')

    def __str__(self):
        return self.course.name

    class Meta:
        verbose_name_plural = '07.课程或学位模块详细'


class OftenAskedQuestion(models.Model):
    '''
    常见问题
    '''
    content_type= models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    question = models.CharField(max_length=255)
    answer = models.TextField(max_length=1024)

    def __str__(self):
        return '%s-%s'%(self.content_object,self.question)

    class Meta:
        unique_together = ('content_type','object_id','question')
        verbose_name_plural = '08.常见问题'


class CourseOutline(models.Model):
    '''
    课程大纲
    '''
    course_detail = models.ForeignKey('CourseDetail')
    order = models.PositiveSmallIntegerField(default=1,help_text='前端显示顺序')
    title= models.CharField(max_length=128)
    content = models.TextField('内容',max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '09.课程大纲'
        unique_together = ('course_detail','title')


class CourseChapter(models.Model):
    '''
    课程章节
    '''
    course = models.ForeignKey('Course',related_name='courserchapters')
    chapter = models.SmallIntegerField(verbose_name='第几章',default=1)
    name = models.CharField(max_length=128)
    summary = models.TextField(verbose_name='章节介绍',blank=True,null=True)

    def __str__(self):
        return '%s:(第%s章)%s'%(self.course,self.chapter,self.name)

    class Meta:
        unique_together = ('course','chapter')
        verbose_name_plural = '10.课程章节'


class CourseSection(models.Model):
    '''
    课时目录
    '''
    chapter = models.ForeignKey('CourseChapter',related_name='coursesections')
    name = models.CharField(max_length=128)
    order = models.PositiveSmallIntegerField(verbose_name='课时排序',help_text='建议每个课时之间空1至2个值，以备后续插入课时')
    section_type_choices = ((0,'文档'),(1,'联系'),(2,'视频'))
    section_type= models.SmallIntegerField(choices=section_type_choices,default=2)
    section_link = models.CharField(max_length=255,blank=True,null=True,help_text='若是video，填vid,若是文档，填link')
    video_time = models.CharField(verbose_name='视频时长',blank=True,null=True,max_length=32,help_text='只在前端展示用')
    pub_date = models.DateField(verbose_name='发布时间',auto_now_add =True)
    free_trail = models.BooleanField('是否可以试看',default=False)

    def __str__(self):
        return "%s-%s" % (self.chapter, self.name)

    class Meta:
        unique_together = ('chapter', 'section_link')
        verbose_name_plural = "11. 课时"


class Homework(models.Model):
    '''
    作业
    '''
    chapter = models.ForeignKey("CourseChapter")
    title = models.CharField(max_length=128, verbose_name="作业题目")
    order = models.PositiveSmallIntegerField("作业顺序", help_text="同一课程的每个作业之前的order值间隔1-2个数")
    homework_type_choices = ((0, '作业'), (1, '模块通关考核'))
    homework_type = models.SmallIntegerField(choices=homework_type_choices, default=0)
    requirement = models.TextField(max_length=1024, verbose_name="作业需求")
    threshold = models.TextField(max_length=1024, verbose_name="踩分点")
    recommend_period = models.PositiveSmallIntegerField("推荐完成周期(天)", default=7)
    scholarship_value = models.PositiveSmallIntegerField("为该作业分配的奖学金(贝里)")
    note = models.TextField(blank=True, null=True)
    enabled = models.BooleanField(default=True, help_text="本作业如果后期不需要了，不想让学员看到，可以设置为False")

    class Meta:
        unique_together = ("chapter", "title")
        verbose_name_plural = "12. 章节作业"

    def __str__(self):
        return "%s - %s" % (self.chapter, self.title)








class PricePolicy(models.Model):
    '''
    价格和课程有效期表
    '''
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    valid_period_choices = (
        (1, '1天'), (3, '3天'),
        (7, '1周'), (14, '2周'),
        (30, '1个月'),(60, '2个月'),
        (90, '3个月'),(180, '6个月'),
        (210, '12个月'),(540, '18个月'),
        (720, '24个月'),)
    valid_period = models.SmallIntegerField(choices=valid_period_choices)
    price = models.FloatField()

    class Meta:
        unique_together = ("content_type", 'object_id', "valid_period")
        verbose_name_plural = "15. 价格策略"

    def __str__(self):
        return "%s(%s)%s" % (self.content_object, self.get_valid_period_display(), self.price)

###########################文章相关##################################


class ArticleSource(models.Model):
    """文章来源"""
    name = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name_plural = "16. 文章来源"

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章资讯"""
    # db_index是数据库索引
    title = models.CharField(max_length=255, unique=True, db_index=True, verbose_name="标题")
    source = models.ForeignKey("ArticleSource", verbose_name="来源")
    article_type_choices = ((0, '资讯'), (1, '视频'))
    article_type = models.SmallIntegerField(choices=article_type_choices, default=0)
    brief = models.TextField(max_length=512, verbose_name="摘要")
    head_img = models.CharField(max_length=255)
    content = models.TextField(verbose_name="文章正文")
    pub_date = models.DateTimeField(verbose_name="上架日期")
    offline_date = models.DateTimeField(verbose_name="下架日期")
    status_choices = ((0, '在线'), (1, '下线'))
    status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="状态")
    order = models.SmallIntegerField(default=0, verbose_name="权重", help_text="文章想置顶，可以把数字调大，不要超过1000")
    vid = models.CharField(max_length=128, verbose_name="视频VID", help_text="文章类型是视频, 则需要添加视频VID", blank=True, null=True)
    comment_num = models.SmallIntegerField(default=0, verbose_name="评论数")
    agree_num = models.SmallIntegerField(default=0, verbose_name="点赞数")
    view_num = models.SmallIntegerField(default=0, verbose_name="观看数")
    collect_num = models.SmallIntegerField(default=0, verbose_name="收藏数")

    # tags = models.ManyToManyField("Tags", blank=True, verbose_name="标签")
    date = models.DateTimeField(auto_now_add=True, verbose_name="创建日期")

    position_choices = ((0, '信息流'), (1, 'banner大图'), (2, 'banner小图'))
    position = models.SmallIntegerField(choices=position_choices, default=0, verbose_name="位置")
    comment = GenericRelation("Comment")  # 用于GenericForeignKey反向查询， 不会生成表字段，切勿删除，如有疑问请联系老村长

    class Meta:
        verbose_name_plural = "17. 文章"

    def __str__(self):
        return "%s-%s" % (self.source, self.title)


class Collection(models.Model):
    """收藏"""
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    account = models.ForeignKey("Account")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('content_type', 'object_id', 'account')
        verbose_name_plural = "18. 通用收藏表"

# ----------------------------------------
    def __str__(self):
        return self.__name__


class Comment(models.Model):
    """通用的评论表"""
    # 关联ContentType表
    content_type = models.ForeignKey(ContentType, blank=True, null=True,verbose_name="类型")
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    p_node = models.ForeignKey("self", blank=True, null=True, verbose_name="父级评论")
    content = models.TextField(max_length=1024)
    account = models.ForeignKey("Account", verbose_name="会员名")
    disagree_number = models.IntegerField(default=0, verbose_name="踩")
    agree_number = models.IntegerField(default=0, verbose_name="赞同数")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "19. 通用评论表"


class Account(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField('password', max_length=128,
                                help_text=mark_safe('''<a class='btn-link' href='password'>重置密码</a>'''))

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '临时用户表'


class UserAuthToken(models.Model):
    """
    用户Token表
    """
    user = models.OneToOneField(to="Account")
    token = models.CharField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "23. 用户Token"

    def save(self, *args, **kwargs):
        import datetime
        # 根据用户名和时间生成唯一标识

        self.token = self.generate_key()
        self.created = datetime.datetime.utcnow()
        return super(UserAuthToken, self).save(*args, **kwargs)

    def generate_key(self):
        import datetime

        """根据用户名和时间生成唯一标识"""
        username = self.user.username
        now = str(datetime.datetime.now()).encode('utf-8')
        md5 = hashlib.md5(username.encode('utf-8'))
        md5.update(now)
        return md5.hexdigest()

    def __str__(self):
        return self.__name__


