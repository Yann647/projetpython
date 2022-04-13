

T=[]
class commande:
    def __init__(self,numcom,etatcom,nomplat,prix):
        self.numcom = numcom
        self.etatcom = etatcom
        self.nomplat = nomplat
        self.prix = prix

    """fonction pour chercher doublon"""
    def recherche(commande):
        for i in range(len(T)):
            if T[i].numcom == commande:
                return i
        return -1
