from django.utils.deprecation import MiddlewareMixin

from django.middleware.common import CommonMiddleware



class Cors(MiddlewareMixin):

    def process_response(self,request,response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method =='OPTIONS':
            response['Access-Control-Allow-Headers'] = "Content-Type"
            response['Access-Control-Allow-Methods'] = "PUT,DELETE,POST,GET"
        return response