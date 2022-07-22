from io import StringIO
from dotenv import load_dotenv 
x = VAR_1
y = VAR_2
numbers = [x,y]
numbers.sort (reverse=True)
while numbers[0]>=numbers[1]:
        if numbers[0]%2!=0:
            print (numbers[0])
        numbers[0]=numbers[0]-1