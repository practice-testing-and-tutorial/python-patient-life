import random
from MasterViru import Viru
from FlueViru import Flue
from DengueViru import Dengue

class Patient:

    __DEBUG = False
    __MIN_HEALTH = 1000
    __MAX_HEALTH = 9000

    __MIN_VIRU = 10
    __MAX_VIRU = 20

    def __init__(self, patientName):
        if Patient.__DEBUG: print("Patient: __init__")
        self.name = patientName
        self.__init_health()
        self.__m_state = 1
        self.__virus_chain = []
        self.__do_sick()
        if Patient.__DEBUG: print("Patient: total virus: " + str(self.count_viru()))

    def __del__(self):
        if Patient.__DEBUG:
            if self.__m_state == 0:
                print("Patient: " + self.name + " has died. 1 object deleted")
            else: print("Patient: " + self.name + " sudah sehat. 1 object deleted")

    def __init_health(self):
        if Patient.__DEBUG: print("Patient: init_health")
        random.seed()
        self.__m_health = random.randint(Patient.__MIN_HEALTH, Patient.__MAX_HEALTH)
        if Patient.__DEBUG:
            print("Patient: m_health = " + str(self.__m_health))

    def __do_sick(self):
        if Patient.__DEBUG: print("Patient: do_sick")
        random.seed()
        random_total_viru = random.randint(Patient.__MIN_VIRU, Patient.__MAX_VIRU)
        if Patient.__DEBUG: print("Patient: random_total_viru = " + str(random_total_viru))
        
        for i in range(random_total_viru):
            random.seed()
            dice = random.randint(1,2)
            flu = Flue()
            denge = Dengue()
            if dice == 1:
                self.__virus_chain.append(flu)
            else:
                self.__virus_chain.append(denge)
        if Patient.__DEBUG:
            print("\nViruses in the list: ")
            self.print_virus_list(self.__virus_chain)

    def get_state(self):
        if Patient.__DEBUG: print("Patient: get_state = " + str(self.__m_state))
        return self.__m_state
    
    def count_viru(self):
        return len(self.__virus_chain)

    def __incubating_viru(self):
        if Patient.__DEBUG: print("Patient: incubating_viru")
        viru_clones = []
        for obj in self.__virus_chain:
            if obj.type == Flue.TYPE:
                viru_clones.append(obj.do_clone())
            if obj.type == Dengue.TYPE:
                dengue_clone_list = obj.do_clone()
                for clon in dengue_clone_list:
                    viru_clones.append(clon)
        # append viru_clones to viru_chain
        if Patient.__DEBUG:
            print("Patient: current virus: ")
            self.print_virus_list(self.__virus_chain)
            print("Patient: clones virus: ")
            self.print_virus_list(viru_clones)
        for obj in viru_clones:
            self.__virus_chain.append(obj)
        if Patient.__DEBUG: print("Patient: total virus: " + str(self.count_viru()))

    def __diggest_medicine(self, medicine_power):
        if Patient.__DEBUG: print("Patient: diggest_medicine")
        i = 0
        not_end_of_list = True
        while not_end_of_list == True:
            viru_count = self.count_viru()
            if i < viru_count:
                if(self.__virus_chain[i].reduce_resistance(medicine_power) == True):
                    del self.__virus_chain[i]
                    i -= 1
                i += 1
            else:
                not_end_of_list = False
            if Patient.__DEBUG: print("Patient: virus count = " + str(self.count_viru()) + " pointer position = " + str(i))
        self.__incubating_viru()

    def get_viru_total_resistance(self):
        total_resistance = 0
        for viru in self.__virus_chain:
            total_resistance += viru.get_resistance()
        if Patient.__DEBUG: print("Patient: get_viru_total_resistance = " + str(total_resistance))
        return total_resistance

    def __do_die(self):
        if Patient.__DEBUG: print("Patient: do_die")
        self.__m_state = 0
        #release all the viru object on the list
        viru_remain = True
        while viru_remain == True:
            count_viru = self.count_viru()
            if count_viru > 0:
                self.__virus_chain[0].do_die()
            else:
                viru_remain = False
        del self

    def take_medicine(self, use_effect = True):
        if Patient.__DEBUG: print("Patient: take_medicine")
        med_power = 0
        if use_effect == True:
            random.seed()
            med_power = random.randint(1, 60)
        self.__diggest_medicine(med_power)
        if self.__m_health < self.get_viru_total_resistance():
            self.__do_die()
    
    def print_virus_list(self, virus_list):
        i = 1
        for obj in virus_list:
            print(str(i) + ". ")
            print(obj.__dict__)
            i += 1



# # testing fungsionalitas class Flue
# a = Flue()
# b = Flue()
# c = Flue()

# a.do_die()
# b.do_die()
# c.do_die()

# # testing fungsionalitas class Dengue
# d = Dengue()
# e = Dengue()
# f = Dengue()

# d.do_die()
# e.do_die()
# f.do_die()