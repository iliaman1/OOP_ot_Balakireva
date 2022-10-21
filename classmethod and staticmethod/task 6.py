class Viber:
    d_mes = []

    @classmethod
    def add_message(cls, msg):
        cls.d_mes.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.d_mes.remove(msg)

    @classmethod
    def set_like(cls, msg):
        if msg.fl_like == False:
            msg.fl_like = True
        else:
            msg.fl_like = False

    @classmethod
    def show_last_message(cls, number):
        (print(i.text) for i in cls.d_mes[-number:])

    @classmethod
    def total_messages(cls):
        return len(cls.d_mes)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)