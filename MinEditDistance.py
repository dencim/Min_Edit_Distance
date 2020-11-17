# -*- coding: utf-8 -*-
"""
Minimum Edit Distance : Dynamic Programming
Implemented based on http://www.stanford.edu/class/cs124/lec/med.pdf

@author: Denis
"""

import numpy as np


#Helper function - works when all values less then 100
#Prints the array nicely
def pretty_print(word1, word2, vals):
    word2 = " " + word2
    print()
    #X-axis
    print("        ", end='')
    for letter in word1:
        print(letter + "  ", end=" ")
    print()
    
    #Line
    print("   ", end='')
    for letter in range(len(word1)*2 + 2):
        print("_", end="_")
    print()
    
    for i in range(len(word2)):
        print(word2[i], end=" | ")
        
        for j in vals[i]:
            num = j
            
            if num < 10:
                print(int(num), end='   ')
            else:
                print(int(num), end='  ')
        
        print()
    print()
        


#Function takes in 2 words and returns the minimum Edit distance between the two Strings
#Edits include Deletion, Insertion or Substitution 
#Call function with Levenshtein=True if substitutions should have cost of 2. Default is 1
def min_edit_distance(word1, word2, Levenshtein=False):
    
    #Determining cost based on type
    cost = 1
    if Levenshtein:
        cost = 2
    
    
    m = len(word1) #word1 is x
    n = len(word2) #word2 is y
    
    #direction_matrix = np.zeros([n, m]) #implement this if you want to allow backtracking
    value_table = np.zeros([n+1, m+1]) 
    
    
    #x
    for i in range(m+1):
        value_table[0, i] = i
    #print(value_table)
    
    #y
    for i in range(n+1):
        value_table[i, 0] = i
    #print(value_table)
    
    
    '''
    FORMULA being used
    D(i,j) = min{ 
            D(i-1,j)+1
            D(i,j-1)+1
            D(i-1,j-1) + {
                        1; if X(i) != Y(j)  #Change to 2 if using Levenshtein
                        0; if X(i) == Y(j) #X being word1, Y being word2
                        }
        }
    '''
    for i in range(1, m+1): 
        for j in range(1, n+1):
            #Do all checks in here
            possible_values = np.zeros(3)
            possible_values[0] = value_table[j, i-1] + 1 
            possible_values[1] = value_table[j-1, i] + 1
            
            possible_values[2] = value_table[j-1, i-1]
            if word1[i-1] != word2[j-1]:
                possible_values[2] = possible_values[2] + cost #cost: default 1, if Levenshtein then 2
                #else add zero so dont do anything
                
            value_table[j, i] = np.amin(possible_values)
            
        #Uncomment to print after each iteration
        #pretty_print(word1, word2, value_table)
        #print("------------------------------------------------")
    
    #Comment out below if you dont want to print final array
    pretty_print(word1, word2, value_table)
        
    return value_table[-1, -1]

print("Minimum Distance: ", min_edit_distance("intention", "execution"))
print("Minimum Distance (Levenshtein): ", min_edit_distance("intention", "execution", True))
print("------------------------------------------------")

print("Minimum Distance: ", min_edit_distance("spoof", "stool"))
print("Minimum Distance (Levenshtein): ", min_edit_distance("spoof", "stool", True))
print("------------------------------------------------")

print("Minimum Distance: ", min_edit_distance("podiatrist", "pediatrician"))
print("Minimum Distance (Levenshtein): ", min_edit_distance("podiatrist", "pediatrician", True))
print("------------------------------------------------")

print("Minimum Distance: ", min_edit_distance("blaming", "conning"))
print("Minimum Distance (Levenshtein): ", min_edit_distance("blaming", "conning", True))
print("------------------------------------------------")

