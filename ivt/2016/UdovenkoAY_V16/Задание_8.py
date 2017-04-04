# Задача 8. Вариант 16.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так, чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку в том случае, если у него нет никаких предположений. Разработайте систему начисления очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех, кто запросил подсказку.
# Udovenko A. Y.
# 14.03.2017
import random
WORDS = ("программирование", "разработка", "хакер", "уязвимость", "алгоритм", "практика", "профессионал", "информатика", "проектирование")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word [position]
    word = word[:position]+word[(position+1):]
print (
    """
\t\t\tДобро пожаловать в игру Анаграммы!
Надо переставить буквы так, чтобы получилось осмысленное слово.
Если у Вас нет никаких предположений, введите "помощь" и на экране появится подсказка.
Внимание! У Вас ограничеснное количество подсказок: 3 штуки. За каждую подсказку Ваши очки будут уменьшаться. 
\t\t\tПриятной игры.
    """
)
print ("Вот Ваша анаграмма:", jumble)
guess = input("\nВаше предположение: ")
total = 1000
l = 0
while guess.lower() != correct and guess != "":
    if guess.lower() != "помощь":
        print ("Неврно!\n")
    else:
        if l!=3:
            help = int(input("Какую по счету букву Вы хотите открыть? "))
            print ("Это буква ", correct[(help-1)], "\n")
            total -= 250
            l += 1
        else:
            print ("Лимит подсказок исчерпан.\n")
    guess = input ("Ваше предположение: ")
if guess.lower() == correct:
    print("Правильно! Поздравляю! Вы набрали", total, "очков.\a")
print("Спасибо за увлекательнейшую интеллектуальную игру!")
input("\n\nНажмите Enter, чтобы выйти")
