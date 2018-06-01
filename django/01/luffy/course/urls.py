from django.conf.urls import url
from course.views import course


urlpatterns = [
    url(r'course/$',course.Course.as_view()),
    url(r'course/(?P<pk>\d+)/$',course.Course.as_view())

]
