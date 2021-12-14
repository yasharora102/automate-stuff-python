
print('Enter number:')
check = 0
def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print((3*number)+1)
        return (3*number)+1
while check!=1:
    number=int(input())
    check = collatz(number)