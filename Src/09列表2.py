import random
import time


def 添加元素():
    # 在尾部加入
    language = ["Python", "Java", "C++"]
    language.append("Javascrip")
    print(language)
    # 指定位置插入
    language.insert(1, "SQL")
    print(language)


def 删除元素():
    languages = ["Python", "SQL", "Java", "C++", "Javascrip"]

    if "Java" in languages:
        languages.remove("Java")
    if "SQL" in languages:
        languages.remove("SQL")
    print("移除 Java 和 SQL 后:", languages)

    languages.pop()
    print("pop() 删除最后一个元素后:", languages)

    temp = languages.pop()
    print("再次 pop() 并保存到 temp 后:", languages)
    print("temp 的值是:", temp)

    languages.append(temp)
    print("把 temp 重新 append 回去后:", languages)

    del languages[0]
    print("使用del 删除第一个元素:", languages)

    languages.clear()
    print("clear() 清空后:", languages)


def 元素位置和频次():
    items = ["Python", "Java", "Java", "C++", "Kotlin", "Python"]
    print(items.index("Python"))  # 0
    # 从索引位置1开始查找'Python'
    print(items.index("Python", 1))  # 5
    print(items.count("Python"))  # 2
    print(items.count("Kotlin"))  # 1
    print(items.count("Swfit"))  # 0
    # 从索引位置3开始查找'Java'
    print(items.index("Java", 3))  # ValueError: 'Java' is not in list


def 元素排序和反转():
    items = ["Python", "Java", "C++", "Kotlin", "Swift"]
    print(f"排序前：{items}")
    items.sort()
    print(f"排序后：{items}")

    items.reverse()
    print(f"反转后：{items}")  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']


def 推导式增加元素():
    scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
    print(scores)


def 手写进度条(total=50):

    for i in range(total + 1):
        进度 = i / total  # 当前进度比例
        已完成 = int(进度 * 30)  # 用30个字符表示总长度
        条形图 = "█" * 已完成 + "-" * (30 - 已完成)
        print(f"\r进度: |{条形图}| {进度*100:.1f}%", end="")
        time.sleep(0.05)
    print()  # 最后换行，避免后续打印被挤在同一行


def 双色球抽奖():

    red_balls = list(range(1, 34))
    selected = []
    for _ in range(6):
        red = random.randrange(len(red_balls))
        selected.append(red_balls.pop(red))
    selected.sort()
    blue_ball = random.randrange(1, 17)
    selected.append(blue_ball)
    return selected


def 双色球带颜色输出():
    import random

    from rich.console import Console
    from rich.table import Table

    # 创建控制台
    console = Console()
    table = Table(show_header=True)
    n = int(input("生成几注号码？"))
    red_balls = list(range(1, 34))
    selected = []
    blue_balls = list(range(1, 17))

    for col_name in ("序号", "红球", "蓝球"):
        table.add_column(col_name, justify="center")

    for i in range(n):
        selected = random.sample(red_balls, 6)
        selected.sort()
        blue_ball = random.choice(blue_balls)
        table.add_row(
            str(i + 1),
            f'[red]{" ".join([f"{ball:0>2d}" for ball in selected])}[/red]',
            f"[blue]{blue_ball:0>2d}[/blue]",
        )
    console.print(table)


if __name__ == "__main__":
    双色球带颜色输出()
