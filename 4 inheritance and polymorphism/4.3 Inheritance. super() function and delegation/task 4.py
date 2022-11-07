class Callback:
    def __init__(self, path: str, router_cls):
        self.path = path
        self.router_cls = router_cls

    def __call__(self, func):
        self.router_cls.add_callback(self.path, func)


class Router:
    app = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func
