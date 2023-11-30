import random

def guess_the_number():
    print("Bienvenue dans le jeu de devinette !")
    print("Je pense à un nombre entre 1 et 100. À vous de deviner !")

    # Choisir un nombre aléatoire entre 1 et 100
    number_to_guess = random.randint(1, 100)

    attempts = 0

    while True:
        user_guess = int(input("Entrez votre devinette : "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Le nombre à deviner est plus grand. Essayez à nouveau.")
        elif user_guess > number_to_guess:
            print("Le nombre à deviner est plus petit. Essayez à nouveau.")
        else:
            print(f"Félicitations ! Vous avez deviné le nombre en {attempts} tentatives.")
            break

if __name__ == "__main__":
    guess_the_number()
