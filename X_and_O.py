GAME_OVER=False

pole_start=[[" ", "1", "2", "3"],
            ["1", "-", "-", "-"],
            ["2", "-", "-", "-"],
            ["3", "-", "-", "-"]]
pole=[[znach for znach in ryad] for ryad in pole_start]
player=1
start=True

name1=input("Введите имя первого игрока: ")
name2=input("Введите имя второго игрока: ")

def pokaz_pole():
    print("-----")
    print("Игровое поле на данный момент")
    for row in pole:
        print(*row, end='\n')
    print("-----")

def p1hod():
    global player
    pokaz_pole()
    while True:
        print(f"Игрок {name1}, введите Ваш ход в формате 'строка столбец'")
        hod = input("Ваш ход: ")
        hodcheck=str(hod)
        hodcheck=hodcheck.replace(" ","")
        if not hodcheck.isdigit():
            print("Пожалуйста, вводите только цифры координат.")
        else:
            hod=list(map(int,hod.split()))
            if len(hod)!=2:
                print("Вы ошиблись в вводе, введите, пожалуйста, правильные координаты.")
            elif hod[0]>=len(pole) or hod[0]<=0 or hod[1]>=len(pole) or hod[1]<=0:
                print("Ваши координаты указывают за пределы игрового поля, перепроверьте Ваш ход.")
            else:
                if pole[hod[0]][hod[1]]=="-":
                    pole[hod[0]][hod[1]]="x"
                    player=2
                    break
                else:
                    print("Ячейка уже занята, перепроверьте, пожалуйста, Ваш ход.")

def p2hod():
    global player
    pokaz_pole()
    while True:
        print(f"Игрок {name2}, введите Ваш ход в формате 'строка столбец'")
        hod=input("Ваш ход: ")
        hodcheck=str(hod)
        hodcheck=hodcheck.replace(" ", "")
        if not hodcheck.isdigit():
            print("Пожалуйста, вводите только цифры координат.")
        else:
            hod=list(map(int, hod.split()))
            if len(hod)!=2:
                print("Вы ошиблись в вводе, введите, пожалуйста, правильные координаты.")
            elif hod[0]>=len(pole) or hod[0]<=0 or hod[1]>=len(pole) or hod[1]<=0:
                print("Ваши координаты указывают за пределы игрового поля, перепроверьте Ваш ход.")
            else:
                if pole[hod[0]][hod[1]]=="-":
                    pole[hod[0]][hod[1]]="o"
                    player=1
                    break
                else:
                    print("Ячейка уже занята, перепроверьте, пожалуйста, Ваш ход.")

def draw():
    if "-" in [znach for ryad in pole for znach in ryad]:
        return False
    elif not "-" in [znach for ryad in pole for znach in ryad] and GAME_OVER:
        None
    else:
        pokaz_pole()
        print("Ничья!")
        return True

def win():
    if pole[1][1]==pole[2][2]==pole[3][3]=="x" or pole[1][3]==pole[2][2]==pole[3][1]=="x":
        pokaz_pole()
        print(f"Игрок {name1} победил! Поздравляем!")
        print("**************************************")
        return True
    elif pole[1][1]==pole[2][2]==pole[3][3]=="o" or pole[1][3]==pole[2][2]==pole[3][1]=="o":
        pokaz_pole()
        print(f"Игрок {name2} победил! Поздравляем!")
        print("**************************************")
        return True
    for ryad in range(1,4):
        if pole[ryad][1]==pole[ryad][2]==pole[ryad][3]=="x":
            pokaz_pole()
            print(f"Игрок {name1} победил! Поздравляем!")
            print("**************************************")
            return True
        elif pole[ryad][1]==pole[ryad][2]==pole[ryad][3]=="o":
            pokaz_pole()
            print(f"Игрок {name2} победил! Поздравляем!")
            print("**************************************")
            return True
    for stolb in range(1,4):
        if pole[1][stolb]==pole[2][stolb]==pole[3][stolb]=="x":
            pokaz_pole()
            print(f"Игрок {name1} победил! Поздравляем!")
            print("**************************************")
            return True
        elif pole[1][stolb]==pole[2][stolb]==pole[3][stolb]=="o":
            pokaz_pole()
            print(f"Игрок {name2} победил! Поздравляем!")
            print("**************************************")
            return True
    else:
        return False


while not GAME_OVER:
    if start:
        print("**************************************")
        print(f"Добро пожаловать в игру, {name1} и {name2}!")
        print("Начнём!")
        start=False
    if player==1:
        p1hod()
    elif player==2:
        p2hod()
    GAME_OVER=win() or draw()
    if GAME_OVER:
        print("Заново? Введите '+', если да.")
        restart=input(": ")
        if restart=="+":
            pole=[[znach for znach in ryad] for ryad in pole_start]
            player=1
            print(" ")
            name1 = input("Введите имя первого игрока: ")
            name2 = input("Введите имя второго игрока: ")
            start=True
            GAME_OVER=False
        else:
            print("~~~~~~~~~~~~~~~~~")
            print("СПАСИБО ЗА ИГРУ!")
            print("~~~~~~~~~~~~~~~~~")














