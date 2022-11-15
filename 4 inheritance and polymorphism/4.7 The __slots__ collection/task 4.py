class Note:
    def __init__(self, name: str, ton: int):
        if name not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си') or ton not in (-1, 0, 1):
            raise ValueError('недопустимое значение аргумента')

        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if key == '_name':
            if value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
                raise ValueError('недопустимое значение аргумента')

        if key == '_ton':
            if value not in (-1, 0, 1):
                raise ValueError('недопустимое значение аргумента')

        object.__setattr__(self, key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si', 'list_notes')
    __created = False

    def __new__(cls, *args, **kwargs):
        if cls.__created == False:
            cls.__created = super().__new__(cls, *args, **kwargs)
            return cls.__created

        return cls.__created

    def __init__(self):
        self._do = Note('до', 0)
        self._re = Note("ре", 0)
        self._mi = Note("ми", 0)
        self._fa = Note("фа", 0)
        self._solt = Note("соль", 0)
        self._la = Note("ля", 0)
        self._si = Note("си", 0)
        self.list_notes = [self._do, self._re, self._mi, self._fa, self._solt, self._la, self._si]

    def __getitem__(self, item):
        if type(item) != int or 0 > item or 6 < item:
            raise IndexError('недопустимый индекс')

        return self.list_notes[item]

    def __setitem__(self, key, value):
        self.list_notes[key] = value
