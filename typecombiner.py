# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:42:20 2019

@author: jupiter
"""
import numpy as np



normal = [np.array([1,2,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1]),'Normal']
fighting = [np.array([1,1,2,1,1,.5,.5,1,1,1,1,1,1,2,1,1,.5,2]),'Fighting']
flying = [np.array([1,.5,1,1,0,2,.5,1,1,1,1,.5,2,1,2,1,1,1]),'Flying']
poison = [np.array([1,.5,1,.5,2,1,.5,1,1,1,1,.5,1,2,1,1,1,.5]),'Poison']
ground = [np.array([1,1,1,.5,1,.5,1,1,1,1,2,2,0,1,2,1,1,1]),'Ground']
rock = [np.array([.5,2,.5,.5,2,1,1,1,2,.5,2,2,1,1,1,1,1,1]),'Rock']
bug = [np.array([1,.5,2,1,.5,2,1,1,1,2,1,.5,1,1,1,1,1,1]),'Bug']
ghost = [np.array([0,0,1,.5,1,1,.5,2,1,1,1,1,1,1,1,1,2,1]),'Ghost']
steel = [np.array([.5,2,.5,0,2,.5,.5,1,.5,2,1,.5,1,.5,.5,.5,1,.5]),'Steel']
fire = [np.array([1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,1]),'Fire']
water = [np.array([1,1,1,1,1,1,1,1,.5,.5,.5,2,2,1,.5,1,1,1]),'Water']
grass = [np.array([1,1,2,2,.5,1,2,1,1,2,.5,.5,.5,1,2,1,1,1]),'Grass']
electric = [np.array([1,1,.5,1,2,1,1,1,.5,1,1,1,.5,1,1,1,1,1]),'Electric']
psychic = [np.array([1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,1]),'Psychic']
ice = [np.array([1,2,1,1,1,2,1,1,2,2,1,1,1,1,.5,1,1,1]),'Ice']
dragon = [np.array([1,1,1,1,1,1,1,1,1,.5,.5,.5,.5,1,2,2,1,2]),'Dragon']
dark = [np.array([1,2,1,1,1,1,2,.5,1,1,1,1,1,0,1,1,.5,2]),'Dark']
fairy = [np.array([1,.5,1,2,1,1,.5,1,2,1,1,1,1,1,1,0,.5,1]),'Fairy']


def combtype(type1,type2):
    comb = type1[0]*type2[0]
    print('{} x {}'.format(type1[1],type2[1]))
    print('Normal {}\nFighting {}\nFlying {}\nPoison {}\nGround {}\nRock {}\nBug {}\nGhost {}\nSteel {}\nFire {}\nWater {}\nGrass {}\nElectric {}\n Psychic {}\nIce {}\nDragon {}\nDark {}\nFairy {}'.format(*comb))
    
    
    
combtype(dragon,steel)

