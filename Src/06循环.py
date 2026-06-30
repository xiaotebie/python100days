def 乘法表99():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(f'{i}x{j}={i*j}', end='\t')
        print()


def isprime():
    number = int(input("输入数字:"))
    for i in range(2, number):
        if number % i == 0:
            print(f'{number}不是素数！')
            break
        print(f'{number}是素数！')


def greatest_common_divisor():
    x = int(input("input x: "))
    y = int(input("input y: "))
    for i in range(x,0,-1):
        if x%i==0 and y%i==0:
            print(f'{i}\tis greatest_common_divisor of {x}and{y}')
            break
def guess_number():
    import random
    answer = random.randrange(1, 101)
    counter = 0
    while True:
        player_number=int(input(f'输入数字：'))
        if player_number== answer:
            print("Congratulations!")
            counter +=1 
            break
        elif player_number>answer:
            print('too big , input a smaller number!')
            counter +=1 
        elif player_number<answer:
            print('too small, input a bigger number!')
            counter +=1 
        print(f'Attempt count is : {counter}')
    print(f'Finall attempt count is : {counter}')
if __name__ == "__main__":
    guess_number()
