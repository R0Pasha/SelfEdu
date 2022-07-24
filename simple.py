import sys
from tkinter import W
q = str(sys.argv[1])
w = str(sys.argv[2])
x = int(q)
y = int(w)
numbers = [x,y]
numbers.sort (reverse=True)
while numbers[0]>=numbers[1]:
        if numbers[0]%2!=0:
            print (numbers[0])
        numbers[0]=numbers[0]-1