nombre_a_gauche = input("Entrez un nombre: ")
nombre_a_droite = input("Entrez un nombre: ")
operation = input("Entrez le symbole de l'opération: ")
resultat = 0

a = nombre_a_gauche.isnumeric()
b = nombre_a_droite.isnumeric()

if a == False or b == False:
  print("Erreur: les deux nombres doivent être des nombres entiers")

else:
  nombre_a_gauche = int(nombre_a_gauche)
  nombre_a_droite = int(nombre_a_droite)

match operation :
  case "+":
    resultat = nombre_a_gauche + nombre_a_droite
    print("Resultat : ", resultat)    
  case "-":
    resultat = nombre_a_gauche - nombre_a_droite
    print("Resultat : ", resultat)    
  case "*":
    resultat = nombre_a_gauche * nombre_a_droite
    print("Resultat : ", resultat)
  case "/":
    if nombre_a_droite == 0:
      print("Erreur: division par 0 impossible")      
    else:
      resultat = nombre_a_gauche / nombre_a_droite
      print("Resultat : ", resultat)    
  case _:
    resultat = "Erreur: le symbole d'opération doit être '+', '-', '*' ou '/'."
    print("Resultat : ", resultat)
