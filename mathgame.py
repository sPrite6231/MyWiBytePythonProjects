import random
import time
print("Hello Player! Let's see if you can find the answer to the following math problems. You need to find out what operation to do between the first and second numbers. Type in * for multiplication, + for addition, and - for subtraction. Enjoy!") 

num1 = int(input('Please tell me a number\n'))
num2 = int(input('Please tell me another number\n'))

op = random.randint(0, 2)

op_list = ['+', '-', '*']

if op == 0:
  rhs = num1 + num2

if op == 1:
  rhs = num1 - num2

if op == 2:
  rhs = num1 * num2



print('Can you tell me the missing operator\n')
qn = str(num1) + ' __ ' + str(num2) + ' = ' + str(rhs) + '\n'
answer = input(qn)


if answer == op_list[op]:
  print('Correct! Well Done!')
else: 
  print('pathetic')

print()
num3 = random.randint(1, 100)
print(num3)


op1 = random.randint(0, 1)
op2 = random.randint(0, 1)


if op1 == 0:
  rhs = num1 + num2

if op1 == 1:
  rhs = num1 - num2

if op2 == 0:
  rhs = rhs + num3

if op2 == 1:
  rhs = rhs - num3


print('Can you tell me the missing operator\n')
qn = str(num1) + ' __ ' + str(num2) + ' __ ' + str(num3) + ' = ' + str(rhs) + '\n'
answer = input(qn)


if answer[0] == op_list[op1] and answer[1] == op_list[op2]:
  print('Correct! Well Done!')
  time.sleep(2)
  print('You really are a math genius!')


else: 
  print('P')
  print('a')
  print('t')
  print('h')
  print('e')
  print('t')
  print('i')
  print('c')
