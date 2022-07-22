# -*- coding: UTF-8 -*-
x = int(input("Введите первое  число:"))
y = int(input("Введите второе  число:"))
numbers = [x,y]
numbers.sort (reverse=True)
while numbers[0]>=numbers[1]:
        if numbers[0]%2!=0:
            print (numbers[0])
        numbers[0]=numbers[0]-1