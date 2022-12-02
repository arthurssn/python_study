class TvProgram:
    def __init__(self, name, year):
        self.__name = name.title()
        self.year = year
        self.__likes = 0

    def give_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.title()


class Movie(TvProgram):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Series(TvProgram):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avengers = Movie('Avengers - Endgame', 2019, 160)
for i in range(0, 1000):
    avengers.give_like()
print(f'Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration} - Likes: {avengers.likes}')

arrow = Series('Arrow', 2012, 8)
arrow.give_like()
print(f'Name: {arrow.name} - Year: {arrow.year} - Seasons: {arrow.seasons} - Likes: {arrow.likes}')
