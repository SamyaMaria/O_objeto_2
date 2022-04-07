class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def to_give_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()


class Movies(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def prints(self):
        print("Nome do filme: {}  Ano: {}  Duração: {} min  Likes: {}".format(self._name, self.year, self.duration,
                                                                              self._likes))


class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def prints(self):
        print("Nome da série: {}  Ano: {}  Temporadas: {}  Likes: {}".format(self._name, self.year, self.season,
                                                                             self._likes))


movie1 = Movies('vingadores-guerra infinita', 2018, 160)
movie1.to_give_likes()

movie2 = Movies('animais fantásticos', 2017, 180)

serie1 = Series('atlanta', 2018, 3)
serie1.to_give_likes()
serie1.to_give_likes()

movies_e_series = [movie1, serie1, movie2]
for program in movies_e_series:
    program.prints()
