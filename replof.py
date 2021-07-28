from threading import Thread as th
from time import sleep
from random import choice

timing = 0




def handler():
    global timing
    try:

        timing = int(input(f'Тайминг равен ___{timing}___ в ведите новое значение если хотите поменять: '))

    except  Exception as e:
        print('Введи Цифру!!!')




def timing_strit():
    global  timing

    while True:
        if timing != 0:
            try:
                a = open('data.txt', 'r').read().strip().split('\n')
            except:
                print('Рядом с программой должен быть файл под названием data.txt\n закрой программу создай такой файл добавь данные и запусти заного')

            sleep(timing)

            with open('data.txt','w') as f:
                for i in range(len(a)):
                    c = choice(a)
                    a.remove(c)
                    f.write(str(c)+'\n')
        sleep(2)
th1 = th(target=timing_strit).start()
while True:
    handler()





