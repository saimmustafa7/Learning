collection = {
    "rock": 1,
    "paper": -1,
    "scissors": 0
}
import random

reverse_dic = {
    1: "rock",
    -1: "paper",
    0: "scissors"
}

while True:
    computer = random.choice([1, -1, 0])
    you = input("chose your action rock/paper/scissors: ").lower()
    your_choise = collection[you]
    print(f"you choose {reverse_dic[your_choise]} and computer choose {reverse_dic[computer]}")
    # here it is the pattern of win
    # rock(1) - paper(-1)=2(win), paper(-1) - scissors(0) = scissors(0) - rock(1) = -1 (win)
    if computer == your_choise:
        print("It is a draw 🤝:)")
    elif (computer - your_choise == 2) or (computer - your_choise == -1):
        print("you Win! 🎉")
    else:
        print("you lose, better luck next time ")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again != "yes":
        break
  
