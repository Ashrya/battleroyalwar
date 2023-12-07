import time
import math
import random
    #initial health
#Taking the name of user >>
name = input("\t\tEnter Your Name:")
print(f"\t\tHi {name}, Welcome to this game. \n\t\tUse your strangth to win this war")
print("Waiting for opponent")
timer = random.randint(1, 5)
time.sleep(timer)
print(f"It's took {timer} second to find the opponent")
enemy_nameList = ["Messi","Ronaldo","Haland","Saka","Pedri"]
enemy_name = random.choice(enemy_nameList)
print(f"\t\tLets Fight \n\t\t{name} VS {enemy_name} ")
    
while True:
    User = 100
    Enemy = 100
    #Creating the functtion for choose:
    
    def normal():
        global Enemy 
        Enemy -= 10
        print(f"Your normal attack damage -10 to {enemy_name} \nYour enemy has health:: {Enemy}")
        print(f"You have  health: {User}")
    
    def special():
        luck = random.choice([1, 2])
        if luck == 1:
           global Enemy
           Enemy -= 20
           global User
           User -= 5
           print(f"Your special attack damage -20 to {enemy_name} \nYour enemy has health:: {Enemy}")    
        else:
            User -= 5
            print(f"Enemy dodge your attack\nYour enemy has health:: {Enemy}")  
        print(f"But you got injured\nYou have  health: {User}")

    def healing():
        global User
        User += 15
        print(f"You have use your aid to boost your health by 15\nYour enemy has health:: {Enemy}")
        print(f"You have  health: {User}")
    
        #For enemy
    def normale():
        global User 
        User -= 10
        print(f"\t\tEnemy normal attack damage -10 to {name} \n\t\tYour enemy has health:: {Enemy}")
        print(f"\t\tYou have  health: {User}")
    
    def speciale():
        luck = random.choice([1, 2])
        if luck == 1:
            global Enemy
            global User
            User -= 20
            Enemy -= 5
            print(f"\t\tEnemy special attack damage -20 to {name} \n\t\tYour enemy has health:: {Enemy}")    
        else:
            Enemy -= 5 
            print(f"\t\tYou dodge Enemy attack\n\t\tBut Enemy got injured\n\t\tYour enemy has health:: {Enemy}") 
        print(f"\t\tYou have  health: {User}")

    def healinge():
        global Enemy
        Enemy += 15
        print(f"\t\tEnemy have use his aid to boost his health by 15\n\t\tYour enemy has health:: {Enemy}")
        print(f"\t\tYou have  health: {User}")
    #healing and attacking
    print("\t\tChoose Your Options \n1) Normal Attack \n2) Special Attack \n3) Healing")
    while User>1 and Enemy>1 :
        while True:
            choose = input("Enter Here: ")
            if choose.isdigit() :
                choose = int(choose)
                if 1<= choose < 3:
                    break
                elif choose ==3:
                    if User > 85:
                        print("Health more than 90. Choose different attack")
                    else:
                        break
                else:
                    print("Choose digit between 1-3: ")
            else:
                print("Enter your choice in provided digits: ")   
        if choose == 1:
            normal()
        elif choose == 2:
            special()
        elif choose == 3:
            healing()
        time.sleep(1)
        if Enemy < 1:
            break
        ##Enemy chosing their strategy
        print("\n\tEnemy is choosing his attack")
        time.sleep(3)
        while True:
            choose = random.choice([1, 2, 3])
            print(f"\n\t\tEnemy Choose attack {choose}")
            if 1<= choose < 3:
                break
            elif choose == 3:
                    if Enemy > 85:
                        print("Health more than 90. Choose different attack")
                    else:
                        break   
        if choose == 1:
            normale()
        elif choose == 2:
            speciale()
        elif choose == 3:
            healinge()
        time.sleep(2)

    if Enemy < 1:
        print("\n\n\t\tYou WON the Game")
        print(f"\t\tCongrulation !! {name}")
    elif User < 1:
        print("\t\t\tYou loose the game\n\t\t Better TRY next time")
    play_again = input(("Do you want to PLAY AGAIN (y/n)")).lower()
    if play_again == "y":
        print("Lets play again")
    else:
        print("\t\tExiting Game")
        break