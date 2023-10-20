import random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

def start():

    print("Let's play Rock,Paper,Scissors")
    while game():
        pass
    scores()

def game():

    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again()

def move():

    while True:
        print()
        player = int(input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move = "))
        try:
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("OOPS! I didn't understand that. Please enter 1, 2 or 3.")

def result(player, computer):
    print("1...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("Computer threw {0} ! ".format(names[computer]))

    global player_score, computer_score

    if player == computer:
        print("Tie game")
    elif rules[player] == computer:
        print("you have won !!!")
        player_score += 1
    else:
        print("you have lost...")
        computer_score += 1

def play_again():
    
    answer = input("would you like to play again? y/n")
    if answer in ("y","Y","yes","Yes","YES"):
        return answer
    else:
        print("Thank you for playing the game. See you next time !!!")

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("player : ",player_score)
    print("computer : ",computer_score)

if __name__ == '__main__':
    start()
    

