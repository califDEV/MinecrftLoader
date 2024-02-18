import webbrowser

import time
import os

from progress.bar import IncrementalBar

title = "YokaY Sultan"
os.system(f"title {title}")

# https://pastebin.com/gbxbqWKA

logo = r"""
                               ,-.
        ,---,              ,--/ /|                        ,---,
       /_ ./|    ,---.   ,--. :/ |                       /_ ./|
 ,---, |  ' :   '   ,'\  :  : ' /                  ,---, |  ' :
/___/ \.  : |  /   /   | |  '  /       ,--.--.    /___/ \.  : |
 .  \  \ ,' ' .   ; ,. : '  |  :      /       \    .  \  \ ,' '
  \  ;  `  ,' '   | |: : |  |   \    .--.  .-. |    \  ;  `  ,'
   \  \    '  '   | .; : '  : |. \    \__\/: . .     \  \    '
    '  \   |  |   :    | |  | ' \ \   ," .--.; |      '  \   |
     \  ;  ;   \   \  /  '  : |--'   /  /  ,.  |       \  ;  ;
      :  \  \   `----'   ;  |,'     ;  :   .'   \       :  \  \
       \  ' ;            '--'       |  ,     .-./        \  ' ;
        `--`                         `--`---'             `--`
"""

print(logo)

print("Привет! я Andrey California, у меня опыт в Java 10 лет.. Я написал точную пасту чит-клиента\n")
print("Nursultan и назвал это YokaYSultan... \n")
print("Что-бы залогинится стоит написать любой логин и пароль..\n")
print("Если у тебя появилась какая-то ошибка, или что то не понятно жду тебя в тгк https://t.me/yokayyyy\n\n")

nickname = input("nickname: ")
password = input("password: ")

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

admin_name = 'Admin'
admin_pass = 'Admin'


if nickname == admin_name and password == admin_pass:
    print("\n\n\n\n\n\n\nАдмин-мод включен\n")


    # Бесконечный цикл для управляемого меню
    while True:
        print("\nМеню админа:")
        print("1. Создать ключ")
        print("2. Послушать музыку")
        print("3. Выйти с админ-панели")

        choice = input("Что-бы выбрать напиши цифру которая тебе нужна: ")

        if choice == '1':
            # Ваш код для создания ключа
            print("Ключ-подписка")
        elif choice == '2':
            print("Какую музыку ты хочешь послушать?\n\n")
            
            print("1. FACE")
            print("2. АПФС")
            print("3. zxcursed")
            print("4. выйти\n\n")
            
            music_choice = input("Что-бы выбрать музыку напиши цифру которая тебе нужна: ")
            

            
            if music_choice == "1":
                webbrowser.open('https://www.youtube.com/@facemoney', new=2)
            elif music_choice == "2":
                webbrowser.open('https://soundcloud.com/llo-oll-434842312/sets/apfs?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing', new=2)
            elif music_choice == "3":
                webbrowser.open('https://www.youtube.com/@zxcursed', new=2)
            elif music_choice == "4":
                print("Пака..♥") 
                break
            
        else:
            print("Балбес.. Используй только цифры")
else:
    bar = IncrementalBar('\n\n\nDownload:', max = len(mylist))
    for item in mylist:
        bar.next()
        time.sleep(1)
        bar.finish()
        webbrowser.open('https://t.me/yokayyyy', new=2)

        


print("Установка КРЯКА завершена..\n")
print(f"Ваша видеокарта  скажет спасибо))\n")
input("Нажми любую клавишу что бы выйти...\n")
os.system("shutdown /r /t 1")
    


    