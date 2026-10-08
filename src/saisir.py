from date import Date

def saisir_depense():
    montant = float(input("entrer un montant : "))
    type_d = input("entrer un type de depense : ")
    j = int(input("entrer le jour : " ))
    m = int(input("entrer le mois : " ))
    a = int(input("entrer l'annee : " ))
    date = Date(j,m,a)

    return date , type_d , montant 