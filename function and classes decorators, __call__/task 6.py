class HandlerGET:
    def __init__(self, func):
        self.fn = func

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.fn, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"


@HandlerGET
def pops(request):
    return 'abobys'


print(pops({"method": "GET", "url": "contact.html"}))
