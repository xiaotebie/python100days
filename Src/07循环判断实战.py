def isprime():
    # 初级的判断质数
    number = int(input("输入数字:"))
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def find_prime(maximum):
    # 初级寻找质数，在序列中找一遍
    primes = []
    for tar in range(3, maximum):
        is_prime = True  # 假设是质数
        for i in range(2, tar):
            if tar % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(tar)
    return primes


def find_prime2(maximum):
    # 使用for else
    primes = []
    for tar in range(3, maximum):
        is_prime = True  # 假设是质数
        for i in range(2, tar):
            if tar % i == 0:
                break
        else:  # 循环没有被 break 中断才执行
            primes.append(tar)
    return primes


def find_prime3(maximum):
    # 只检查到平方根
    primes = []
    for tar in range(3, maximum + 1):
        for i in range(2, int(tar**0.5) + 1):
            if tar % i == 0:
                break
        else:  # 循环没有被 break 中断才执行
            primes.append(tar)
    return primes


def fibonacci_sequence(fibonacci_length):
    # 斐波那契数列
    fibonacci = [1, 1]
    while len(fibonacci) < fibonacci_length:
        l = len(fibonacci)
        fibonacci.append(fibonacci[l - 2] + fibonacci[l - 1])
    return fibonacci


def find_narcissistic():
    a = 100
    b = 999
    narcissistic_list = []
    for i in range(100, 1000):
        end = 0
        str_nar = str(i)

        l = len(str_nar)
        for j in range(0, l):

            curr = (int(str_nar[j])) ** l
            end = end + curr
            # print(f'当前的一位是  {int(str_nar[j])}，计算结果是{curr} 当前end是 {end} 当前的 i 是 {i}')
        if end == i:
            narcissistic_list.append(i)

    return narcissistic_list


def buy_checken():
    for i in range(0, 21):
        for j in range(0, 34):
            for k in range(0, 301):
                if i + j + k == 100 and i * 5 + j * 3 + k // 3 == 100 and k % 3 == 0:
                    print(f"Cock:{i} hen:{j} chick:{k}")


def buy_checken2():
    for i in range(0, 21):
        for j in range(0, 34):
            k = 100 - i - j
            if i * 5 + j * 3 + k // 3 == 100 and k % 3 == 0:
                print(f"Cock:{i} hen:{j} chick:{k}")


def craps_game():
    import random
    import time
    money = 1000
    loop = 0
    while money > 0:
        print(f"总资产为:{money}元")
        while True:
            debt = int(input("请下注"))
            if 0 < debt <= money:
                break
        loop +=1
        time.sleep(0.6)
        print(f'正在摇骰子...')
        a = int((random.random()) * 6 + 1)
        b = int((random.random()) * 6 + 1)
        res = a + b
        print(f'玩家点数为:{a} {b} -> {res}\n')
        first_res = res
        
        if res == 7 or res == 11:
            print('玩家胜!')
            money = money + debt
        elif res == 2 or res == 3 or res == 12:
            print('庄家胜!')
            money = money - debt
        else:
            #重新摇骰子
            while money > 0:
                time.sleep(0.6)
                print(f'正在摇骰子...')
                a = int((random.random()) * 6 + 1)
                b = int((random.random()) * 6 + 1)
                res = a + b
                print(f'玩家点数为:{a} {b} -> {res}\n')
                if res == 7:
                    money = money - debt
                    print('庄家胜!')
                    break
                elif res == first_res:
                    money = money + debt
                    print('玩家胜!')
                    break
        print(f"总共玩了{loop}把")
    print('已破产！ GAME OVER!')


if __name__ == "__main__":

    # print(f'isprime? -> {True==isprime()}')
    # prime_list = find_prime3(100000000)
    # print(f'prime list is -> {prime_list} \ninclude {len(prime_list)} primes')
    # print(fibonacci_sequence(100))
    # a = 14897
    # b = str(a)
    # print(b[1])
    # print(find_narcissistic())
    # buy_checken()
    craps_game()
