class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def render_request(self, request: dict, method: (tuple, list)):
        if method.upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')

        res = getattr(self, method.lower(), False)

        if res:
            return res(request)

    def get(self, request: dict):
        if type(request) != dict:
            raise TypeError('request не является словарем')

        if 'url' not in request:
            raise TypeError('request не содержит обязательного ключа url')

        return f"url: {request['url']}"
