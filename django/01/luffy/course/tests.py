from django.test import TestCase

# Create your tests here.


from django.contrib.sessions.middleware import SessionMiddleware




# fields = [(field_name, attrs.pop(field_name)) for field_name, obj in list(attrs.items()) if isinstance(obj, Field)]

import sys
import inspect
def get_current_function_name():
    return inspect.stack()[1][3]

class A(object):

    def __init__(self,str):
        self.str = str
        setattr(self.__class__,self.str,self.test1)



    def test1(self):
        print(sys._getframe().f_code.co_name)
        print (self.__class__,'self.__class__')
        # print (self.__name__,'self.__name__')
        print(self.str,'self.str')
        print(self.test1,'self.test1')
        print("%s.%s invoked" % (self.__class__.__name__, get_current_function_name()))


if __name__=='__main__':
    a=A("haha")
    a.haha()