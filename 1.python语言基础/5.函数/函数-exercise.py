"""
练习1：实现计算求最大公约数和最小公倍数的函数。
"""
def gcd(x, y):
    """求最大公约数"""
    (x, y) = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor


def lcm(x, y):
    """求最小公倍数"""
    return x * y // gcd(x, y)

"""
练习2：实现判断一个数是不是回文数的函数。
回文数:
    “回文”是指正读反读都能读通的句子，它是古今中外都有的一种修辞方式和文字游戏，如“我为人人，人人为我”等。
    在数学中也有这样一类数字有这样的特征，成为回文数（palindrome number）。
    设n是一任意自然数。若将n的各位数字反向排列所得自然数n1与n相等，则称n为一回文数。
    例如，若n=1234321，则称n为一回文数；但若n=1234567，则n不是回文数。
"""
def is_palindrome(num):
    """判断一个数是不是回文数"""
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

"""
练习3:写一个程序判断输入的正整数是不是回文素数。
    回文素数是指，对一个整数n（n≥11）从左向右和从右向左读其结果值相同且是素数，即称n为回文素数。
"""
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)