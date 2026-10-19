import json
from saisir import saisir_depense
from validation import depense_valide
from creer import creer_depense
from supprimer import supprimer_depense


with open("data/depenses.json","a") as f:
    pass
with open("data/depenses.json","r") as f:
    temp = f.read()
    if not temp  :
        depenses = []
    else :
        depenses = json.loads(temp) 
           

valide = True
while valide :
    
    if not depenses :
        pass
    else:
        sup = input("supprimer une depense (y/n) : ")
        if sup == "y":
            sup_id = int(input("entrer id de la depense a supprimer : "))
            supprimer_depense(sup_id,depenses)
            with open("data/depenses.json","w") as f:
                json.dump(depenses,f)
        else :
            pass                   

    
    date , type_d , montant = saisir_depense()
    if depense_valide(date,type_d,montant) is True :
        if not depenses :
            depense = creer_depense(1,date,type_d,montant)
            depenses.append(depense)
        else:
            id = depenses[-1]["id"] + 1
            depense = creer_depense(id,date,type_d,montant)
            depenses.append(depense)

        with open("data/depenses.json","w") as f:
                json.dump(depenses,f)
                
    else :
        print("la depense n'est pas valide")
    

    with open("data/depenses.json","r") as f:
            print(json.load(f))

    var = input("ajouter une autre depense (y/n) : ")
    if var == "n" :
        valide = False
