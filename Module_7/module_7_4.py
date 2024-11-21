# Домашнее задание по теме "Форматирование строк"

class Team:
    def __init__(self, name: str, member_count: int, score: int, time: float):
        self.name = name
        self.member_count = member_count
        self.score = score
        self.time = time

    def win(self, other):
        if self.score > other.score or self.score == other.score and self.time > other.time:
            return f'Победа команды {self.name}!'
        elif self.score < other.score or self.score == other.score and self.time < other.time:
            return f'Победа команды {other.name}!'
        else:
            return 'Ничья!'


team1 = Team('Мастера кода', 5, 40, 1552.512)
team2 = Team('Волшебники данных', 6, 42, 2153.31451)

# Использование %:
print('В команде %s участников: %d!' % (team1.name, team1.member_count))
print('Итого сегодня в командах участников: %d и %d!' % (team1.member_count, team2.member_count))
print()

# Использование format():
print('Команда {} решила задач: {}!'.format(team2.name, team2.score))
print('{} решили задачи за {}c!'.format(team2.name, team2.time))
print()

# Использование f-строк:
print(f'Команды решили {team1.score} и {team2.score} задач.')
print(f'Сегодня было решено {team1.score + team2.score} задач, в среднем по '
      f'{round((team1.time + team2.time)/(team1.score + team2.score), 2)} секунды на задачу!')
print(team1.win(team2))