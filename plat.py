
from copyreg import pickle
from re import I
import os


T=[]
class plat:
    def __init__(self,numeroplat,nomplat,prix):
        self.numeroplat = numeroplat
        self.nomplat = nomplat
        self.prix = prix

    """fonction pour chercher doublon"""
    def recherche(plat):
        for i in range(len(T)):
            if T[i].numeroplat == plat:
                return i
        return -1

    """fonction pour ajouter un plat"""
    def creerplat():
        numeroplat = input("Donner le numéro du plat :")
        while plat.recherche(numeroplat) != -1:
            numeroplat = input("numéro de plat déja utiliser, donnez on un autre :")
        nomplat = input("Donner le nom du plat")
        prix =input("mettre le prix")
        T.append(plat(nomplat,prix))
        print("Le plat est ajouter avec succes")
        plat.majTableauToFichier()

    """fonction pour supprimer un plat"""
    def supprimerplat():
        numeroplat = input("Entrer le numero du plat :")
        if plat.recherche(numeroplat) != -1:
            del T[plat.recherche(numeroplat)]
        else:
            print("Le plat est introuvable")
        print("Le plat est supprimer avec succes")
        plat.majTableauToFichier()

    """fonction pour modifier un plat"""
    def modifierplat():
        numeroplat1= input("Donner le numéro du plat a modifier :")
        numeroplat2= input("Donner le nouveau numero du plat :")
        while plat.recherche(numeroplat2) != -1 and plat.recherche(numeroplat1) != plat.recherche(numeroplat2):
            numeroplat2 = input("Le numero du plat saisie est deja utiliser par un autre plat, donner le numero de plat :")
        nomplat = input("Donner le nouveau nom")
        prix = input("Donner le nouveau prix")
        x = plat(numeroplat2,nomplat,prix)
        T[plat.recherche(numeroplat1)]= x
        print("Le plat est modifier avec succes")
        plat.majTableauToFichier()

    """fonction pour remplir un tableau a partir d'un fichier"""
    def FichierToTableau():
        T.clear()
        try:
            f= open("plats.txt","rb")
            u= pickle.load(f)
            for i in range(len(u)):
                T.append(u[i])
            f.close()
        except EOFError:
            print("fichier vide")
        except FileNotFoundError:
            print("Fichier introuvable")
            f = open("plats.txt","wb")
        except IOError:
            print("Erreur d'entrer et de sortie")
    
    """fonction qui rempli le fichier avec les donnees du tableau"""
    def majTableauToFichier():
        f= open("plats.txt","wb")
        pickle.dump(T, f)
        f.close()
    
    """fonction qui affiche tout les elements du tableau"""
    def printT():
        plat.FichierToTableau()
        for i in range(len(T)):
            print("------------------------")
            print("Numéro du plat :", T[i].numeroplat)
            print("Nom du plat :", T[i].nomplat)
            print("Le prix du plat :",T[i].prix)
            print("------------------------")
        input("Appuyer sur une touche pour continuer")

    """fonction pour afficher le menu"""
    def menuplat():
        while True:
            os.system('cls')
            print("1. Ajouter un plat")
            print("2. Modifier un plat")
            print("3. Supprimer un plat")
            print("4. Afficher la liste des plats")

            menu = {
                1 : plat.numeroplat,
                2 : plat.nomplat,
                3 : plat.prix,
            }
            choix = int(input("Entrez votre choix :"))
            menu[choix]()

plat.FichierToTableau()
plat.menuplat()