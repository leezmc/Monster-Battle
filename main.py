# FILENAME: main.py
# Purpose: Creates a tournament between a monster and hero
# Author: Michael Lee
# Date: April 28 2023




import random
from characters import Monster, Hero 

# This function has two Characters fight
# it returns the winner or None on a tie
def monster_battle(h1, m1):
   
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(h1.getName() + ": " + h1.getDescription())
    
    #Whose turn is it?
    attacker = None
    defender = None

   
    coinFlip = random.randint(0, 1)
    if coinFlip == 0:
        attacker = m1
        defender = h1
    else: 
        attacker = h1
        defender = m1
    
    print(attacker.getName()+" goes first.")
    
    
    #Loop until someone is unconsious (health < 1) or choose to stop
    stop = False
    while( m1.getHealth() > 0 and h1.getHealth() > 0 and not stop ):
        
        #It will be nice for output to record the damage done
        before_health = defender.getHealth()            

        #Check if the attacker is a monster
        if(isinstance(attacker, Monster)):
            #check if defender is defending, if so print out info about the defense
            if(defender.isDefending()):
                print("Our hero is defending with", defender.getDefenseName(), "!")
            print(defender.react())
            defender.attack(defender)
            print_results(attacker, defender ,defender.getWeaponName(), before_health - defender.getHealth())
        else:
            # Ask the user for the next action: attack, defend, or stop.
            action = input('Pick one of these (a)ttack, (d)efend, or sto(p): ')
            if action == 'a':
                print(h1.react())
                h1.attack(defender)
                print_results(h1, m1, h1.getWeaponName(), before_health - defender.getHealth())
            elif action == 'd':
                h1.defend()
            elif action == 'p':
                stop = True

 
        attacker, defender = defender, attacker
        

    if m1.getHealth() <= 0:
        print("Battle is over. let's see who has won...")
        print(h1.getName() + " is victorious!")
        return h1
    elif h1.getHealth() <= 0:
        print("Battle is over. let's see who has won...")
        print(m1.getName() + " is victorious!")
        return m1
    else:
        tie = "The battle has ended in a tie."
        return tie
    
        

    
    
#This function prints the status updates
def print_results(attacker, defender, attack, hchange):
    res = attacker.getName() + " used " + attack
    res += " on " + defender.getName() + "\n"
    res += "The attack did " + str(hchange) + " damage."
    print(res)
    print(attacker.getName() + " at " + str(attacker.getHealth()))
    print(defender.getName() + " at " + str(defender.getHealth()))


#----------------------------------------------------
if __name__=="__main__":
    random.seed(0)
    
    monsterName = input("Enter monster's name: ")
    monsterDescription = input("Enter monster's description: ")
    monsterMaxHealth = int(input("Enter a number for monster's health: "))
    monsterWeaponName = input("Enter monster's weapon name: ")
    monsterWeaponDamage = float(input("Enter monster's weapon damage (as a number): "))
    monsterMotivation = (input("Enter monster's motivation: "))
    myMonster = Monster(monsterName, monsterDescription, monsterMaxHealth, monsterWeaponName, monsterWeaponDamage, monsterMotivation)  

    heroName = input("Enter hero's name: ")
    heroDesc = input("Enter the hero's description: ")
    heroMaxHealth = int(input("Enter a number for the hero's health: "))
    heroWeaponName = input("Enter hero's weapon name: ")
    heroWeaponDamage = float(input("Enter hero's weapon damage (as a number): "))
    heroDefenseName = input("Enter the hero's defense name: ")
    myHero = Hero(heroName, heroDesc, heroMaxHealth, heroWeaponName, heroWeaponDamage, heroDefenseName)
    winner = monster_battle(myHero, myMonster)
   
