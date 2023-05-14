# FILENAME: characters.py
# Purpose: Defines classes for monster and hero
# Author: Michael Lee
# Date: April 28

# This class defines a generic Character
# It includes attributes and many implemented methods, in addition to an abstract
# methods __str__ and react
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS Character CLASS ####
class Character(ABC):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__health = maxHealth
        self.__description = description
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def react(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getWeaponName(self):
        return self.__weaponName
    
    def getWeaponDamage(self):
        return self.__weaponDamage
    
    def attack(self, enemy):
        enemy.takeDamage(self.__weaponDamage)
    
    def takeDamage(self, amount):
        self.__health -= amount
    
    def getHealth(self):
        return self.__health
    
    
## TODO: Create a Monster class that inherits from the Character class.
class Monster(Character):
    def __init__(self, name, description, maxHealth , weaponName, weaponDamage, motivation):
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)
        self.__motivation = motivation
        
    def __str__(self):
        return f'{super().getName()} is a {super().getDescription()}\nWeapon: {super().getWeaponName()}\nCurrent Health: {super().getHealth()}\nMotivation: {self.__motivation}'
    
    def react(self):
        return f'{super().getName()} laughs maniacally.'
    def getMotivation(self):
        return self.__motivation

## TODO: Create a Hero class that inherits from the Character class.
class Hero(Character):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage, defenseName):
        super().__init__(name, description, maxHealth, weaponName, weaponDamage)
        self.__defenseName = defenseName
        self.__defending = False
        
    def __str__(self):
        return f'Our hero {super().getName()} is a {super().getDescription()}\nWeapon: {super().getWeaponName()}\nDefense: {self.__defenseName}\nCurrent Health: {super().getHealth()}\nDefense Status: {self.__defending}'
        
    def react(self):
        return f'{super().getName()} charges bravely.'
        
    def getDefenseName(self):
        
        return self.__defenseName
    
    def isDefending(self):
        return self.__defending
    
    def defend(self):
        self.__defending = True
        
    def takeDamage(self, amount):
        if self.__defending:
            amount /= 2
            self.__defending = False
        super().takeDamage(amount)
