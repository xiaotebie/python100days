def yearload():
    year = int(input('请输入年份: '))
    if year % 400 == 0:
        print(f"{year}是闰年")
        return  True
    if year % 100 == 0:
        print(f"{year}不是闰年")
        return False
    if year % 4 ==0:
        print(f"{year}是闰年")
        return  True
    print(f"{year}不是闰年")
    return False
yearload()