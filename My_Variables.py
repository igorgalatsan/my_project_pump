# Клапана правой ветки
CLAPANS_RIGHT_BRANCH = {"FP": 1, "DB1S": 3, "ST1S": 5, "DB1C": 7, "DB2S": 8, "ST2S":10,
                "DB3S": 13, "ST3S": 15, "DB3C": 17, "DB4P":20, "ST4S": 21}

# Клапана левой ветки
CLAPANS_LEFT_BRANCH = {"DT":2, "DB1P":4, "ST1P":6, "DB2P":9, "ST2P":11,"DB2C":12,
              "DB3P":14, "ST3P":16, "DB4C":18, "DB4S":19, "ST4P":22, "ST7S":29,
              "ST7P":30, "STTS":47, "STTP":48}

# время начала таймера
TIMERS = {'FP': 1552400, 'DT': 145920, 'DB1S': 1141200, 'DB1P': 1201, 'ST1S': 2280,
                'ST1P': 2281,'DB1C': 2401, 'DB2S': 1440, 'DB2P': 1441, 'ST2S': 4440,
                'ST2P': 4441, 'DB2C': 1020, 'DB3S': 1560, 'DB3P': 1560, 'ST3S': 3600,
                'ST3P': 3601, 'DB3C': 3420, 'DB4C': 1800, 'DB4S': 1801, 'DB4P': 1802,
                'ST4S': 3060, 'ST4P': 3060, 'ST7S': 180, 'ST7P': 181, 'STTS': 780,
                'STTP': 781

    # время старта закачки в сек
}
# Cпросить про значения могут ли в словарях повторяться
# Время на закачку все танки
D_TIMES_PUMP_IN = {
    'FP': 2400, 'DT': 1920, 'DB1S': 1200, 'DB1P': 1201, 'ST1S': 2280,
    'ST1P': 2281,'DB1C': 2401, 'DB2S': 1440, 'DB2P': 1441, 'ST2S': 4440,
    'ST2P': 4441, 'DB2C': 1020, 'DB3S': 1560, 'DB3P': 1560, 'ST3S': 3600,
    'ST3P': 3601, 'DB3C': 3420, 'DB4C': 1800, 'DB4S': 1801, 'DB4P': 1802,
    'ST4S': 3060, 'ST4P': 3060, 'ST7S': 180, 'ST7P': 181, 'STTS': 780,
    'STTP': 781,
}
    # dtime in sec
    
# Время на откачку все танки
D_TIMES_PUMP_FROM ={
    'FP': 3000, 'DT': 2520, 'DB1S': 1800, 'DB1P': 1801, 'ST1S': 2880,
    'ST1P': 2881, 'DB1C': 3001, 'DB2S': 2040, 'DB2P': 2041, 'ST2S': 5400,
    'ST2P': 5401, 'DB2C': 1802, 'DB3S': 1803, 'DB3P': 1804, 'ST3S': 4200,
    'ST3P': 4201, 'DB3C': 4202, 'DB4C': 2400, 'DB4S': 2401, 'DB4P': 2402,
    'ST4S': 3600, 'ST4P': 3601, 'ST7S': 300, 'ST7P': 301, 'STTS': 1500,
    'STTP': 1501,
}


class Clapan:
    def __init__(
        self, 
        name:str, 
        number:int,
        time_in:int, 
        time_out:int,
        branch: str,
    ) -> None:
        self.name = name
        self.number = number
        self.time_in = time_in
        self.time_out = time_out
        self.branch = branch


CLAPPANS = {
'FP': Clapan(name='FP',number=1, time_in=2400, time_out=3000, branch= "StarSide"),
"DB1S": Clapan(name="DB1S",number=3,time_in=1200, time_out=1800,branch="StarSide"),
"ST1S": Clapan(name="ST1S",number=5,time_in=2280, time_out=2880, branch="StarSide"),
"DB1C": Clapan(name="DB1C",number=7,time_in=2400,time_out=3000,branch="StarSide"), 
"DB2S": Clapan(name="DB2S", number=8, time_in=1440,time_out=2040,branch="StarSide"),
"ST2S": Clapan(name="ST2S",number=10,time_in=4440,time_out=5400,branch="StarSide"),
"DB3S": Clapan(name="DB3S",number=13,time_in=1560,time_out=1800,branch="StarSide"),
"ST3S": Clapan(name="ST3S",number=15,time_in=3600,time_out=4200,branch="StarSide"),
"DB3C": Clapan(name="DB3C",number=17,time_in=3420,time_out=4200,branch="StarSide"),
"DB4P": Clapan(name="DB4P",number=20,time_in=1800,time_out=2400,branch="StarSide"),
"ST4S": Clapan(name="ST4S",number=21,time_in=3060,time_out=3600,branch="StarSide"),
"DT":Clapan(name="DT",number=2,time_in=1920,time_out=2520,branch="PortSide"),
"DB1P":Clapan(name="DB1P",number=4,time_in=1200,time_out=1800,branch="PortSide"),
"ST1P":Clapan(name="ST1P",number=6,time_in=2280,time_out=2880,branch="PortSide"),
"DB2P":Clapan(name="DB2P",number=9,time_in=1440,time_out=2040,branch="PortSide"),
"ST2P":Clapan(name="ST2P",number=11,time_in=4440,time_out=5400,branch="PortSide"),
"DB2C":Clapan(name="DB2C",number=12,time_in=1020,time_out=1800,branch="PortSide"),
"DB3P":Clapan(name="DB3P",number=14,time_in=1560,time_out=1800,branch="PortSide"),
"ST3P":Clapan(name="ST3P",number=16,time_in=3600,time_out=4200,branch="PortSide"),
"DB4C":Clapan(name="DB4C",number=18,time_in=1800,time_out=2400,branch="PortSide"),
"DB4S":Clapan(name="DB4S",number=19,time_in=1800,time_out=2400,branch="PortSide"),
"ST4P":Clapan(name="ST4P",number=22,time_in=3060,time_out=3600,branch="PortSide"),
"ST7S":Clapan(name="ST7S",number=29,time_in=180,time_out=300,branch="PortSide"),
"ST7P":Clapan(name="ST7P",number=30,time_in=180,time_out=300,branch="PortSide"),
"STTS":Clapan(name="STTS",number=47,time_in=780,time_out=1500,branch="PortSide"),
"STTP":Clapan(name="STTP",number=48,time_in=780,time_out=1500,branch="PortSide")

}


#class Clappans:
 #   def __init__(self) -> None:
  #      self._clappans = []


D_TIMES = {
    'FP': 16124123412, # время окончания процесса (закачки или откачки)
     "DT" : 16124123412 + CLAPPANS["DT"].time_in
}
#clappan_name : time.time() + CLAPPANS[name].time_in 


# подумать какой тип данных подойдет
# Номера клапанов на откачку и закачку первого и второго насоса
PUMP_IN_ONE = {74,83}
PUMP_FROM_ONE ={70,82}
PUMP_IN_TWO = {72,81}
PUMP_FROM_TWO ={71,84}

if __name__ == "__main__":
    question = "DB1C"
    clapan = D_TIMES["FP"]
    clapan_1 =D_TIMES["DT"]
    print(D_TIMES["FP"])
    print(D_TIMES["DT"])
    
    print(CLAPPANS[question].number,CLAPPANS[question].branch)
    print(*PUMP_FROM_ONE)
    print(*PUMP_FROM_ONE)