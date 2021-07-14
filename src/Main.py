#! /usr/bin/env python
from MasterPatient import Patient

def tanya_minum_obat():
    minum_obat = input("minum obat? [y/n] : ")
    if minum_obat == "y" or minum_obat == "Y":
        ucup.take_medicine()
    elif minum_obat == "n" or minum_obat == "N":
        ucup.take_medicine(False)
    else:
        tanya_minum_obat()
        return True
    return True

ucup = Patient("Ucup Surucup")

play = True

while play is True:
    print("\n\n")
    tanya = input("type other than 'exit' to play/continue the game: ")
    if tanya == "exit":
        play = False
    else:
        tanya_minum_obat()
        if ucup.get_viru_total_resistance() <= 0:
            print(ucup.name + " sudah sehat")
            play = False