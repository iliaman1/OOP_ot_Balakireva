class SmartPhone:
    def __init__(self, model):
        self.model = model
        self.apps = []

    def add_app(self, app):
        flag = 0
        for i in self.apps:
            if app.name == i.name:
                flag += 1
        if flag == 0:
            self.apps.append(app)

    def remove_app(self, app):
        self.apps.remove(app)


class AppVK:
    def __init__(self):
        self.name = "ВКонтакте"


class AppYouTube:
    def __init__(self, memory):
        self.name = "YouTube"
        self.memory_max = memory


class AppPhone:
    def __init__(self, numbers):
        self.name = "Phone"
        self.phone_list = numbers


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)