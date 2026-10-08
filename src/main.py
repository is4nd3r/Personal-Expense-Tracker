from saisir import saisir_depense
from validation import depense_valide

date , type_d , montant = saisir_depense()
valide = depense_valide(date,type_d,montant)
print(valide)