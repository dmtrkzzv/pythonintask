#Задача6.Вариант13.

#Создайте игру, в которой компьютер загадывает название одного из двух
#спутников Марса, а игрок должен его угадать.

#Попова Маргарита Александровна
#22.03.2016

import random
sputnicki=['Фобос','Деймос']
variant=input('Назовите один из спутников Марса. Предложенные варианты: Фобос, Деймос' )
answer = random.choice(sputnicki)
if variant == answer:
 print('Вы угадали!!\nПравильный ответ:', answer)
else:
 print('Вы не угадали!!\nПравильный ответ:', answer)
input('Нажмите Enter для выхода')