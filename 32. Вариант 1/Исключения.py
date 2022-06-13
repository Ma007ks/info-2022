while True:
    try:
        x = int(input())
        print(1 / x)
        break
    except ValueError:
        print("Ну ты и дурак! Ввёл плохое значение!")
    except ZeroDivisionError:
        print("А на ноль-то делить нельзя!")
    print("Попробуй снова!")
