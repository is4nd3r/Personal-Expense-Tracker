def supprimer_depense(id,depense):
    for i in range(len(depense)):
        if depense[i]["id"] == id :
            depense.pop(i)
            return
    print("la depense n'existe pas")