player = input("Quel est ton nom?").lower()
age = int(input("Votre âge?"))

if (player == 'Jovenel' and age == 16) or player == 'jovenel':
    print("Salve BROTHER")
else:
    print(":(")
numero = 0
while numero < 5:
    print(numero)
    numero = numero + 1

liste = ['karate', 'english', 'french', 'creole'] 
for item in liste:
    print(item) 

for i in range(len(liste)-1, 0, -2):
    print(liste[i])