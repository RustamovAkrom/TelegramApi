

class FirstMiddleware:
    def __init__(self, get_response):
        self._get_response = get_response
    
    def __call__(self, request):
        print("We are in FirstMiddleware before")
        response = self._get_response(request)
        print("We are in FirstMiddleware after")
        return response
    
    def process_exception(self, request, exception):
        print(f"Exception is {exception}")
        return None