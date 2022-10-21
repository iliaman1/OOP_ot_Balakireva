class Track:
    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.list_track_lines = []

    def add_track(self, tr):
        self.list_track_lines.append(tr)

    def get_tracks(self):
        return tuple(self.list_track_lines)

    def __len__(self):
        current_x = self.start_x
        current_y = self.start_y
        distance = 0
        for i in self.list_track_lines:
            current_distance = ((i.to_x - current_x) ** 2 + (i.to_y - current_y) ** 2) ** 0.5
            distance += current_distance
            current_x = i.to_x
            current_y = i.to_y
        return int(distance)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)


class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
print(res_eq)
