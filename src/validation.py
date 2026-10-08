from date import Date

def depense_valide(type_d,date,montant):

    dates={ 1:31 , 2:28 , 3:31 , 4:30 , 5:31 , 6:30 , 7:31 , 8:31 , 9:30 , 10:31 , 11:30 , 12:31 }
    if date.mois not in dates.keys() or not (1 <= date.jour <= dates[date.mois]):
        return "depense invalide : date invalide"    
    
    types=["transport","food","rent","subscription","activity","others"]
    if (type_d not in types):
        return "depense invalide : type non autorise"
    
    if type(montant) is not float and type(montant) is not int or not (montant > 0) :
        return "depense invalide : montant invalide"

    return "depense valide"
