import random

class Viru:
    
    __DEBUG = True

    _TOTAL_VIRU = 0

    def __init__(self):
        if Viru.__DEBUG: print("Viru: __init__")
        self._m_dna = " "
        self._m_resistance = 0
        self.type = ""

    def __del__(self):
        if Viru.__DEBUG: print("Viru: object deleted")

    def _load_dna_information(self):
        if Viru.__DEBUG: print("Viru: load dna information")
        self._m_dna = "ATTGCTGAAGGTGCGG"

    def _do_born(self):
        if Viru.__DEBUG: print('Viru: do_born')
        Viru._TOTAL_VIRU += 1
    
    def _do_clone(self):
        if Viru.__DEBUG: print('Viru: do_clone')

    def _do_die(self):
        if Viru.__DEBUG: print('Viru: do_die')
        Viru._TOTAL_VIRU -= 1
        del self

    def reduce_resistance(self, medicine_power = 0):
        if Viru.__DEBUG: print("Viru: reduce_resistance. med_power= " + str(medicine_power))
        self._m_resistance = self._m_resistance - medicine_power
        if self._m_resistance <= 0:
            return True
        else: return False

    def _init_resistance(self):
        if Viru.__DEBUG: print("Viru: init_resistance")
    
    def get_resistance(self):
        return self._m_resistance

    def get_total_viru(self):
        return Viru._TOTAL_VIRU