# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-05 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_teacher', models.FloatField(blank=True, default=0, null=True, verbose_name='讲师讲解是否清晰')),
                ('about_video', models.FloatField(blank=True, default=0, null=True, verbose_name='内容实用')),
                ('about_course', models.FloatField(blank=True, default=0, null=True, verbose_name='课程内容通俗易懂')),
                ('review', models.TextField(blank=True, max_length=1024, null=True, verbose_name='评价')),
                ('disagree_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='踩')),
                ('agree_number', models.IntegerField(blank=True, default=0, null=True, verbose_name='赞同数')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='评价日期')),
                ('is_recommend', models.BooleanField(default=False, verbose_name='热评推荐')),
                ('hide', models.BooleanField(default=False, verbose_name='不在前端页面显示此条评价')),
                ('enrolled_course', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
            ],
            options={
                'verbose_name_plural': '13. 课程评价（购买课程后才能评价）',
            },
        ),
    ]