from django.conf.urls import url
from course.views import course,account,order,new_order




urlpatterns = [
    url(r'course/$',course.Course.as_view()),
    # url(r'course/(?P<pk>\d+)/$',course.Course.as_view()),
    url(r'coursedetial/(?P<pk>\d+)/$',course.CourseDetial.as_view()),

    url(r'article/$',course.Article.as_view()),
    url(r'article/(?P<pk>\d+)/$',course.Article.as_view()),

    url(r'auth/$',account.Auth.as_view()),
    url(r'resiger/$',account.AuthResiger.as_view()),

    url(r'shoppingcar/(?P<pk>\d+)/$',new_order.ShoppingCart.as_view({'post':'create'})),

    # url(r'order/(?P<pk>\d+)$',order.ShoppingCart.as_view({'git':'list'})),


    # url(r'^$',course.Course.as_view()),
]
