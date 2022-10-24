lst_in = ['Балакирев; 34; 2048',
          'Mediel; 27; 0',
          'Влад; 18; 9012',
          'Nina P; 33; 0']


class Player:
    def __init__(self, name: str, old: int, score: int) -> None:
        self.name = name
        self.old = old
        self.score = score

    def __len__(self):
        return self.score


players = [Player(i.split('; ')[0], int(i.split('; ')[1]), int(i.split('; ')[2])) for i in lst_in]
players_filtered = list(filter(bool, players))
print(players)
print(players_filtered)
