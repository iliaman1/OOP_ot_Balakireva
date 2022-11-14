class RetriveMixin:
    def get(self, request: dict) -> str:
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request: dict) -> str:
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request: dict) -> str:
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request: dict) -> str:
        if request.get('method') not in self.allowed_methods:
            raise TypeError(f"Метод {request.get('method')} не разрешен.")

        return self.__getattribute__(request.get('method').lower())(request)


class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', 'PUT',)
