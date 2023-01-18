
CLAPANS_RIGHT_BRANCH = {"FP": 1, "DB1S": 3, "ST1S": 5, "DB1C": 7, "DB2S": 8, "ST2S":10,
                "DB3S": 13, "ST3S": 15, "DB3C": 17, "DB4P":20, "ST4S": 21}


CLAPANS_LEFT_BRANCH = {"DT":2, "DB1P":4, "ST1P":6, "DB2P":9, "ST2P":11,"DB2C":12,
              "DB3P":14, "ST3P":16, "DB4C":18, "DB4S":19, "ST4P":22, "ST7S":29,
              "ST7P":30, "STTS":47, "STTP":48}
# подумать какой тип данных подойдет
PUMP_IN_ONE = {74,83}
PUMP_FROM_ONE ={70,82}
PUMP_IN_TWO = {72,81}
PUMP_FROM_TWO ={71,84}
while True:
    question = input("Введите  Закачка или Откачка: ").lower()
    if question == "откачка":
        klapan = input("ВВедите номер клапана: ").upper()
                # валидацию клапана в соответствии со сипском 
        if CLAPANS_RIGHT_BRANCH.get(klapan):
              # добавить время страта таймера
            print(f"номер клапана {CLAPANS_RIGHT_BRANCH.get(klapan)}, \
                {PUMP_FROM_TWO} и  насос №2")
            
        elif CLAPANS_LEFT_BRANCH.get(klapan):
            print(f"номер клапана {CLAPANS_LEFT_BRANCH.get(klapan)}, \
                {PUMP_FROM_ONE} и  насос №1")
            
        else:
            print("Нет такого клапана!")  
    elif question =="закачка":
        klapan = input("ВВедите номер клапана: ").upper()
        if CLAPANS_RIGHT_BRANCH.get(klapan):
              # добавить время страта таймера
            print(f"номер клапана {CLAPANS_RIGHT_BRANCH.get(klapan)}, \
                {PUMP_IN_ONE} и  насос №1")
            
        elif CLAPANS_LEFT_BRANCH.get(klapan):
            print(f"номер клапана {CLAPANS_LEFT_BRANCH.get(klapan)}, \
                {PUMP_IN_TWO} и  насос №2")
        else:
            print("Нет такого клапана!")      

    # вернуться в меню
   