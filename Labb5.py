from bintreeFile import Bintree
from linkedQFile import *
import sys

def BintreeMaker(ordlista):
    svenska = Bintree()   
    with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip() 
            if ordet not in svenska:
                ordlista.append(ordet)
                svenska.put(ordet)
    return svenska, ordlista

class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word
        self.parent = parent

def main():
    ordlista = []
    svenska, ordlista = BintreeMaker(ordlista)
    q = LinkedQ()
    gamla = Bintree()
    objektlista = []
    startordInput = input('Choose a start word')    
    slutordInput = input('Choose an end word')
    if startordInput in svenska and slutordInput in svenska:
        gamla.put(startordInput)
        q.enqueue(startordInput)
        while not q.isEmpty():
            node = q.dequeue()
            makechildren(node, objektlista, gamla, q, ordlista)
            if slutordInput in gamla:
                print('Det finns en väg till ' + slutordInput)
                pathfinder(startordInput, slutordInput, objektlista)
                print(slutordInput)
                sys.exit()

            elif q.isEmpty():
                print('Det finns ingen väg till ' + slutordInput)
    else:
        print('The word is not in the dictionary')
        main()
        return 


def makechildren(ordet, objektlista, gamla, q, ordlista):
    startord = bokstavsBytare(ordet)
    for ord in ordlista:
        a = bokstavsBytare(ord)
        for i in a:
            if i in startord and ord not in gamla:
                q.enqueue(ord)
                gamla.put(ord)
                parentPointer = ParentNode(ord, ordet) #För att kunna hitta kedjan
                objektlista.append(parentPointer)
    return objektlista, gamla, q, ordlista

def bokstavsBytare(ord):
    checklista = []
    for i in range(3):
        checklista.append(ord[:i] + '?' + ord[i+1:])
    return checklista


def pathfinder(urmoder, urbarn, objektlista):
    for objekt in objektlista:
        if urbarn == objekt.word:
            urbarn = objekt.parent
            pathfinder(urmoder, urbarn, objektlista)
            print(urbarn)

            
main()
#Clas Blank och Julia Liu
