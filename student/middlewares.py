import time

from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin


# class TimeItMiddleware(MiddlewareMixin):
class TimeItMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        costed = time.time() - start_time
        print(f'request to response cose: {costed:.2f}s')

        return response


    # def process_request(self, request):
    #     self.start_time = time.time()
    #     return
    
    def process_view(self, request, func, *args, **kwargs):
        if request.path != reverse('student:index'):
            return None
        
        start = time.time()
        response = func(request)
        costed = time.time() - start
        print(f'process view: {costed:.2f}s')
        return response
    
    def process_exception(self, request, exception):
        pass

    def process_template_response(self, request, response):
        return response
    
    # def process_response(self, request, response):
    #     costed = time.time() - self.start_time
    #     print(f'request to response cose: {costed:.2f}s')
    #     return response
