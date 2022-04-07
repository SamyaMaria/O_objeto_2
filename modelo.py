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

    def __str__(self):
        return f'Nome: {self.name}  Likes: {self.likes}'


class Movies(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f"Nome do filme: {self._name}  Ano: {self.year}  Duração: {self.duration} min  Likes: {self._likes}"


class Series(Program):
    def __init__(self, name, year, season):
        super().__init__(name, year)
        self.season = season

    def __str__(self):
        return f"Nome da série: {self._name}  Ano: {self.year}  Temporadas: {self.season}  Likes: {self._likes}"


class Playlist(list):
    def __init__(self, name, programs):
        self.name = name
        super().__init__(programs)



movie1 = Movies('vingadores-guerra infinita', 2018, 160)
movie1.to_give_likes()
movie1.to_give_likes()
movie1.to_give_likes()

movie2 = Movies('animais fantásticos', 2017, 180)
movie2.to_give_likes()

serie1 = Series('atlanta', 2018, 3)
serie1.to_give_likes()
serie1.to_give_likes()

serie2 = Series('the big bang theory', 2006, 12)
serie2.to_give_likes()
serie2.to_give_likes()
serie2.to_give_likes()
serie2.to_give_likes()

movies_and_series = [movie1, serie1, movie2, serie2]
playlist_weekend = Playlist('Fim de semana', movies_and_series)

print('tamanho da playlist: {}' .format(len(movies_and_series)))

for program in playlist_weekend:
    print(program)
