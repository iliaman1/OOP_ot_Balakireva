class Aircraft:
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float)):
        if type(model) != str or mass < 1 or speed < 1 or top < 1:
            raise TypeError('неверный тип аргумента')
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top


class PassengerAircraft(Aircraft):
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float), chairs: int):
        super().__init__(model, mass, speed, top)
        if type(chairs) != int or chairs < 1:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):
    def __init__(self, model: str, mass: (int, float), speed: (int, float), top: (int, float), weapons: dict):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict:
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
