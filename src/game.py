import random

def start_game():
    secret_number = random.randint(1, 20)
    print("Игра: Угадай число от 1 до 20!")
    
    while True:
        guess = int(input("Твой вариант: "))
        
        if guess < secret_number:
            print("Мало! Попробуй число больше.")
        elif guess > secret_number:
            print("Много! Попробуй число меньше.")
        else:
            print("УРА! Ты угадала!")
            break

if __name__ == "__main__":
    start_game()
