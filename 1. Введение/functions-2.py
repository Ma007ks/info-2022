# define (определить)

def print_mood(greeting):
    print(greeting)
    mood = input("Как у вас дела? ")
    print("Здорово, что у вас всё", mood)
    print()


def print_day(date):
    print("Привет! Сегодня", date)
    print_mood("Доброе утро!")
    print_mood("Добрый день!")
    print_mood("Добрый вечер!")
    print_mood("Доброй полночи!")
    print_mood("Доброй ночи!")


print_day("6 ноября")
print_day("7 ноября")
print_day("8 ноября")
