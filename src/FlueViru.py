import random #nanti dipakai untuk generate random number
import copy #nanti dipakai untuk ngopy object
from MasterViru import Viru

class Flue(Viru):

    TYPE = "flue"
    
    __DEBUG = False

    __TOTAL_FLUE = 0

    __MIN_RES = 10
    __MAX_RES_BLUE = 15
    __MAX_RES_RED = 20

    __COLOR_RED = "0xff0000"
    __COLOR_BLUE = "0x0000ff"

    def __init__(self):
        if Flue.__DEBUG:
            print("\n")
            print("Flue: __init__")
        Viru.__init__(self)
        self.__m_color = ""
        self.__do_born()
        self.__init_resistance()
        if Flue.__DEBUG: print("Flue: total flue virus object = " + str(Flue.__TOTAL_FLUE))
    
    def __del__(self):
        Flue.__TOTAL_FLUE -= 1
        if Flue.__DEBUG:
            print("\n")
            print("Flue: __del__")
            print("Flue: total flue virus object = " + str(Flue.__TOTAL_FLUE))

    def __do_born(self):
        if Flue.__DEBUG: print("Flue: do_born")
        Viru._do_born(self)
        Viru._load_dna_information(self)
        random.seed()
        i = random.randint(1, 2)
        if i == 1: self.__m_color = Flue.__COLOR_BLUE #blue
        else: self.__m_color = Flue.__COLOR_RED #red
        self.type = Flue.TYPE
        Flue.__TOTAL_FLUE += 1
        if Flue.__DEBUG:
            print("Flue: m_color = " + self.__m_color)
            print("Flue: m_dna = " + self._m_dna)

    def do_clone(self):
        if Flue.__DEBUG: print("Flue: do_clone")
        Viru._do_clone(self)
        clone = copy.deepcopy(self)
        return clone

    def do_die(self):
        if Flue.__DEBUG:
            print("\n")
            print("Flue: do_die")
        Viru._do_die(self)

    def __init_resistance(self):
        Viru._init_resistance(self)
        random.seed()
        if self.__m_color == Flue.__COLOR_BLUE:
            self._m_resistance = random.randint(Flue.__MIN_RES, Flue.__MAX_RES_BLUE)
        elif self.__m_color == Flue.__COLOR_RED:
            self._m_resistance = random.randint(Flue.__MIN_RES, Flue.__MAX_RES_RED)
        if Flue.__DEBUG:
            print("Flue: init_resistance")
            print("Flue: m_resistance = " + str(self._m_resistance))



