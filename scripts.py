# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:46:03 2026

@author: martina
"""

#Esercizi di Hackerank 


# ---------------- https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction ----------------------
#Say 'Hello World' 
stringa= 'Hello, World!'
print(stringa)

#-----------

#Python if-else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n % 2 !=0: 
    print('Weird')
if n % 2 == 0:
    if n>=2 and n<=5: 
        print('Not Weird')
    if n>=6 and n<=20: 
        print ('Weird')
    if n>20: 
        print ('Not Weird')
# --------------

#Arithmetic operators
a= int(input())
b= int(input())
print(a+b)
print(a - b)  
print( a*b )

# ---------------

#Python division
a = int(input())
b = int(input())
print(a // b) 
print(a / b) 
     
    
# ---------

#loops 
n = int(input())
for i in range(n): 
    print(i*i)

# --------

#wite a function
def is_leap(year):
    leap = False
    four= year % 4 
    hund= year % 100 
    thou= year % 400 
    if four == 0: 
        if hund != 0: 
            leap = True 
        else: 
            if thou == 0: 
                leap = True 
    else: 
        leap=False 
    
    return leap

year = int(input())
print(is_leap(year))

# ----------
#print function 
if __name__ == '__main__':
    n = int(input())
    s=str()
    for i in range(1,n+1):
        s+=str(i)
    print(s)

# ------------------- https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-basic-data-types ------------------------
#list comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[i, j, k] for i in range(x + 1)
                  for j in range(y + 1)
                  for k in range(z + 1)
                  if i + j + k != n])
# ---------

#find the runner-up
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    m=max(arr)
    runner_up=0
    for i in range(n):
        if arr[i] < m: 
            if runner_up==0 or arr[i] > runner_up: 
                runner_up=arr[i] 
    print (runner_up)

# -------

#nested lists
if __name__ == '__main__':
    votiStudenti=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        votiStudenti.append([name,score])
        
    voti=[]
    for lista in votiStudenti: 
        for char in lista: 
            if not isinstance(char,str):
                voti.append(char)
    voti=list(set(voti))
    voti.sort()
    secLowest=voti[1]
    
    studenti=[]
    for lista in votiStudenti: 
            if secLowest in lista: 
                for char in lista: 
                    if isinstance(char, str): 
                        studenti.append(char)
    studenti.sort() 
    for char in studenti: 
        print(char)
    
# -------- 

#finding the percentage 
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    punteggi: []
    for d in student_marks: 
        if d == query_name: 
            punteggi=student_marks[d]

    perc= sum(punteggi)/len(punteggi)
    print(f"{perc:.2f}")    

# ------

#lists
if __name__ == '__main__':
    n = int(input())
    lista = []
    
    for _ in range(n):
        comando = input().split()
        
        if comando[0] == "insert":
            posizione = int(comando[1])
            numero = int(comando[2])
            lista.insert(posizione, numero)
            
        elif comando[0] == "print":
            print(lista)
            
        elif comando[0] == "remove":
            numero = int(comando[1])
            lista.remove(numero)
            
        elif comando[0] == "append":
            numero = int(comando[1])
            lista.append(numero)
            
        elif comando[0] == "sort":
            lista.sort()
            
        elif comando[0] == "pop":
            lista.pop()
            
        elif comando[0] == "reverse":
            lista.reverse()

            
            
            
# --------------------------------------- https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-strings -------------------
#swap case
def swap_case(s):
    s=list(s)
 
    for i in range(len(s)): 
        if s[i].isupper():
            s[i]=s[i].lower()
        else: 
            s[i]=s[i].upper()
    result="".join(s)
            
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
# ------------------------
#string split and join 

def split_and_join(line):
    stringa=line.split(" ")
    stringa="-".join(stringa)
    return stringa
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# ----------------------
#what's your name ? 
def print_full_name(first, last):
    result = "Hello "+first+" "+last+"! You just delved into python."
    print(result)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# --------------------------
#mutations
def mutate_string(string, position, character):
    ls=list(string)
    if ls[position]!=character: 
        ls[position]=character
    ls="".join(ls)
    
    return ls

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
# -----------------
#find a string 
def count_substring(string, sub_string):
    ls=list(string)
    l=list()
    count=0
    for i in range(len(ls)): 
        if ls[i] == sub_string[0] and i <= (len(string)-len(sub_string)):
            l="".join(ls[i:i+len(sub_string)])
            if l == sub_string: 
                count+=1
            l=[]
            
  
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# ---------------------
#string validators
if __name__ == '__main__':
    s = input()
    result=[False, False, False, False, False]
    for char in s: 
        if char.isalnum(): 
            result[0]=True
            break 
        
    for char in s: 
        if char.isalpha(): 
            result[1]=True
            break 
        
    for char in s: 
        if char.isdigit(): 
            result[2]=True
            break 
       
    for char in s: 
        if char.islower(): 
            result[3]=True
            break 
       
    for char in s: 
        if char.isupper(): 
            result[4]=True
            break 
        
    for char in result: 
        print(char)

# -------------------------------
#text alignment 

thickness = int(input()) 
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
     print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
# -------------------
#text wrap
import textwrap

def wrap(string, max_width):
    result=[]
    i=0
    while i<len(string): 
        result.append(string[i:i+max_width])
        i+=max_width
    result="\n".join(result)
    return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# -----------------
#string formatting 
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(f"{dec:>{width}} {octa:>{width}} {hexa:>{width}} {bina:>{width}}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
# ---------

#capitalize 

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    s=list(s)
    s[0]=s[0].upper()
    
    for i in range(len(s)): 
        if s[i]==" ":
            s[i+1]=s[i+1].upper()
   
    result="".join(s)
    return result

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# ---------------
#the minion game 
def minion_game(string):
    vowels = 'AEIOU'
    n = len(string)
    kevin = 0
    stuart = 0
    
    for i, char in enumerate(string):
        if char in vowels:
            kevin += n - i
        else:
            stuart += n - i
    
    if kevin > stuart:
        print(f"Kevin {kevin}")
    elif stuart > kevin:
        print(f"Stuart {stuart}")
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


# ---------------------https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-sets----------------------------
#introduction to sets
def average(array):
    array=set(array)
    return sum(array)/len(array)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# ------------
#symmetric difference 
def create_set():
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))
    return a, b

def symmetric_difference(a, b):
    only_a = a - b
    only_b = b - a
    result = only_a.union(only_b)
    return result

if __name__ == '__main__':
    a, b = create_set()
    result = symmetric_difference(a, b)
    for num in sorted(result):
        print(num)
 
    

#---------------
#set.add()
def count_stamps(array): 
    set_stamps=set(array)
    return len(set_stamps)

if __name__ == '__main__':
    
    n = int(input())
    array = []
    for _ in range(n):
        stamp = input()
        array.append(stamp)
    
    result = count_stamps(array)
    print(result)

# -------------------
#set.discard().remove()&.pop()
n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    comando = input().split()
    
    if comando[0] == "pop":
        s.pop()
    elif comando[0] == "remove":
        s.remove(int(comando[1]))
    elif comando[0] == "discard":
        s.discard(int(comando[1]))

print(sum(s))
# -----------------

# set .union() Operation
n = int(input())
si = set(map(int, input().split()))

m = int(input())
sf = set(map(int, input().split()))

print(len(si | sf))

#--------------

# set .intersection() Operation
n = int(input())
si = set(map(int, input().split()))

m = int(input())
sf = set(map(int, input().split()))

print(len(si&sf))

#-------
# set .difference() Operation
n = int(input())
si = set(map(int, input().split()))

m = int(input())
sf = set(map(int, input().split()))

print(len(si - sf))

# -------------

# set .symmetric_difference() Operation
n = int(input())
si = set(map(int, input().split()))

m = int(input())
sf = set(map(int, input().split()))

print(len(si ^ sf))


# -------------------

# set mutations
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    other_set = set(map(int, input().split()))
    getattr(s, command[0])(other_set)

print(sum(s))

#--------------

# check subset
t = int(input())

for _ in range(t):
    input()  # numero di elementi in A (non serve)
    a = set(map(int, input().split()))
    input()  # numero di elementi in B (non serve)
    b = set(map(int, input().split()))
    print(a.issubset(b))

# --------

# check strict subset

A = set(map(int, input().split()))
n = int(input())
result = True

for _ in range(n):
    other = set(map(int, input().split()))
    if not (A.issuperset(other) and A != other):
        result = False
        break

print(result)

# --------------- https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-collections --------------

# collections.counter()

from collections import Counter

n = int(input())
sizes = Counter(map(int, input().split()))
c = int(input())

total = 0
for _ in range(c):
    size, price = map(int, input().split())
    if sizes[size] > 0:
        total += price
        sizes[size] -= 1

print(total)

# ----------------------------

# tutorial defaultDict 
from collections import defaultdict

n, m = map(int, input().split())

# Leggi le n parole del gruppo A e memorizza le posizioni (indice 1-based)
d = defaultdict(list)
for i in range(1, n + 1):
    word = input()
    d[word].append(i)

# Per ogni parola del gruppo B, stampa le posizioni o -1
for _ in range(m):
    word = input()
    if word in d:
        print(" ".join(map(str, d[word])))
    else:
        print(-1)

# ------------------ 




