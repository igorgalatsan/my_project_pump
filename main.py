"""
откачка - картинка(2 насоса, номера клапанов, выбор номера клапана, показывает какие клапана открыть), таймер добавить и 
и сохранение замеров(в  таблицу №танка и сколько см осталось и  в тоннах показывать))

Можно лучше начать балластные операции кнопка
там выбор откачка или закачка потом выбор танка и показвваем что за операция какой номер 
клапана какой танк и какой насос  и таймер
закачка - как откачка, номер клапанов другие

схема - просто таблица или кртинка, фото - расположение клапанов

время - таблица с номером танка и кол-во времени на закачку и откачку

Замеры по всем операциям за сутки(можно еще геолокацию писать)

"""

import time
from keyboard import KBHit
from My_Variables import *
#OPENED = "opened"
#CLOSED = "closed"


KB = KBHit()

def _set_new_time(
    pump_number:str, 
    kl: str, 
    times_dict: dict,
    branch: dict
    ):
    print(f"номер клапана {branch.get(kl)}, \
    {PUMP_FROM_TWO} и  насос №{pump_number}")
    # добавить время страта таймера
    times_dict[kl] = int(time.time()) + D_TIMES_PUMP_FROM[kl]


def set_new_timer() -> None:
    KB.set_normal_term()
    while True:
        question = input("Введите  Закачка или Откачка: ").lower()
        if question == "откачка":

            klapan = input("ВВедите номер клапана: ").upper()
                # валидацию клапана в соответствии со сипском
            

            if CLAPANS_RIGHT_BRANCH.get(klapan):
                _set_new_time(
                    pump_number="2", 
                    kl=klapan, 
                    times_dict=D_TIMES_PUMP_FROM, 
                    branch=CLAPANS_RIGHT_BRANCH
                    )
                break
            elif CLAPANS_LEFT_BRANCH.get(klapan):
                _set_new_time(
                    pump_number="1", 
                    kl=klapan,
                    times_dict=D_TIMES_PUMP_FROM, 
                    branch=CLAPANS_RIGHT_BRANCH
                    )
                break
            
            else:
                print("Нет такого клапана!")  
        
        elif question =="закачка":
            klapan = input("ВВедите номер клапана: ").upper()
            if CLAPANS_RIGHT_BRANCH.get(klapan):

                _set_new_time(
                    pump_number="1", 
                    kl=klapan,
                    times_dict=D_TIMES_PUMP_IN, 
                    branch=CLAPANS_RIGHT_BRANCH,
                    )
                break
            
            elif CLAPANS_LEFT_BRANCH.get(klapan):
                _set_new_time(
                    pump_number="1", 
                    kl=klapan,
                    times_dict=D_TIMES_PUMP_IN, 
                    branch=CLAPANS_RIGHT_BRANCH,
                    )
                break
            else:
                print("Нет такого клапана!")      
        # валидацию клапана в соответствии со сипском 
              
    # вернуться в меню
DT_ALARM = int(time.time())

def alarm_func(times_dict: dict):
    global DT_ALARM
    if int(time.time()) > DT_ALARM + 1:
        DT_ALARM = int(time.time())
        print(D_TIMES_PUMP_FROM, D_TIMES_PUMP_IN)
        print(f'current time: {DT_ALARM}')
        for clapan, start_time in times_dict.items():
            dt = times_dict[clapan]
            end_time = start_time + dt
            current_time = int(time.time())
        
            # проверить вышло ли время для клапана
            if current_time > end_time:
                # если вышло, то напечатать для какого клапана
                print(f"{clapan} Смотри манометры!!")


def main():
    D_TIMES_PUMP_IN.clear()
    D_TIMES_PUMP_FROM.clear()
    print("ВВедит q чтобы установить ноый таймер")
    while True:
        if KB.kbhit():
            c = KB.getch()

            if ord(c) == 99:
                close_timer()

            if ord(c) == 113:
                set_new_timer()
                
        # печатать только раз в секунду !!!
        
        alarm_func(D_TIMES_PUMP_FROM)
        alarm_func(D_TIMES_PUMP_IN)

        
#
if __name__ == "__main__":
    main()
    # pip install keyboard