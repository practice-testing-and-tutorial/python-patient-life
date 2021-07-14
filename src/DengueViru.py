import random #nanti dipakai untuk generate random number
import copy #nanti dipakai untuk ngopy object
from MasterViru import Viru

class Dengue(Viru):

    TYPE = "dengue"

    __DEBUG = False

    __TOTAL_DENGUE = 0

    __PROT_NS3 = "NS3"
    __PROT_NS5 = "NS5"
    __PROT_E = "E"

    def __init__(self):
        if Dengue.__DEBUG:
            print("\n")
            print("Dengue: __init__")
        Viru.__init__(self)
        self.__m_protein = ""
        self.__do_born()
        self.__init_resistance()
        if Dengue.__DEBUG: print("Dengue: total Dengue virus object = " + str(Dengue.__TOTAL_DENGUE))
    
    def __del__(self):
        Dengue.__TOTAL_DENGUE -= 1
        if Dengue.__DEBUG:
            print("\n")
            print("Dengue: __del__")
            print("Dengue: total Dengue virus object = " + str(Dengue.__TOTAL_DENGUE))

    def __do_born(self):
        if Dengue.__DEBUG: print("Dengue: do_born")
        Viru._do_born(self)
        Viru._load_dna_information(self)
        random.seed()
        i = random.randint(1, 3)
        if i == 1: self.__m_protein = Dengue.__PROT_NS3
        elif i == 2: self.__m_protein = Dengue.__PROT_NS5
        else: self.__m_protein = Dengue.__PROT_E
        self.type = Dengue.TYPE
        Dengue.__TOTAL_DENGUE += 1
        if Dengue.__DEBUG:
            print("Dengue: m_protein = " + self.__m_protein)
            print("Dengue: m_dna = " + self._m_dna)

    def do_clone(self):
        if Dengue.__DEBUG: print("Dengue: do_clone")
        Viru._do_clone(self)
        clones = [copy.deepcopy(self), copy.deepcopy(self)]
        return clones #return clone list

    def do_die(self):
        if Dengue.__DEBUG:
            print("\n")
            print("Dengue: do_die")
        Viru._do_die(self)

    def __init_resistance(self):
        Viru._init_resistance(self)
        random.seed()
        if self.__m_protein == Dengue.__PROT_NS3:
            self._m_resistance = random.randint(1, 10)
        elif self.__m_protein == Dengue.__PROT_NS5:
            self._m_resistance = random.randint(11, 20)
        elif  self.__m_protein == Dengue.__PROT_E:
            self._m_resistance = random.randint(21, 30)
        if Dengue.__DEBUG:
            print("Dengue: init_resistance")
            print("Dengue: m_resistance = " + str(self._m_resistance))