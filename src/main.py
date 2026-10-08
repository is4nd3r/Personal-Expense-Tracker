from saisir import saisir_depense
from validation import depense_valide
from creer import creer_depense

valide = True
depenses = []

while valide :
    date , type_d , montant = saisir_depense()
    if depense_valide(date,type_d,montant) is True :
        if not depenses :
            depense = creer_depense(1,date,type_d,montant)
            depenses.append(depense)
        else:
            id = depenses[-1]["id"] + 1
            depense = creer_depense(id,date,type_d,montant)
            depenses.append(depense)
    else :
        print("la depense n'est pas valide")
    
    print(depenses)
    
    var = input("ajouter une autre depense (y/n) : ")
    if var == "n" :
        valide = False