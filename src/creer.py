def creer_depense(id,date,type,montant):
    return {"id":id,"date":f"{date.jour}/{date.mois}/{date.annee}","type":type,"montant":montant}