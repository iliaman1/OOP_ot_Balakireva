class Server:
    ip = 1

    def __init__(self):
        self.ip = Server.ip
        self.buffer = []
        self.router = None
        Server.ip += 1

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        res = self.buffer[:]
        self.buffer.clear()
        return res

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.connected = {}

    def link(self, server):
        self.connected[server.ip] = server
        server.router = self

    def unlink(self, server):
        trying = self.connected.pop(server.ip, False)
        if trying:
            trying.router = None

    def send_data(self):
        for i in self.buffer:
            if i.ip in self.connected:
                self.connected[i.ip].buffer.append(i)
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
