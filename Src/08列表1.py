import random




def 列表的运算():
    items5 = [35, 12, 99, 45, 66]
    items6 = [45, 58, 29]
    items7 = ["Python", "Java", "JavaScript"]
    print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
    print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
    items5 += items6
    print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
    print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
    print(
        items7 * 2
    )  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
    print(29 in items6)  # True
    print(99 in items6)  # False
    print("C++" not in items7)  # True
    print("Python" not in items7)  # False


def 列表的索引():
    items8 = ["apple", "waxberry", "pitaya", "peach", "watermelon"]
    print(items8[0])  # apple
    print(items8[2])  # pitaya
    print(items8[4])  # watermelon
    items8[2] = "durian"
    print(items8)  # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
    print(items8[-5])  # 'apple'
    print(items8[-4])  # 'waxberry'
    print(items8[-1])  # watermelon
    items8[-4] = "strawberry"
    print(items8)  # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']
    print(items8[1:3:1])  # ['strawberry', 'durian']
    print(items8[0:3:1])  # ['apple', 'strawberry', 'durian']
    print(items8[0:5:2])  # ['apple', 'durian', 'watermelon']
    print(items8[-4:-2:1])  # ['strawberry', 'durian']
    print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
    print(items8[-2:-6:1])  # []
    # 修改列表元素


def 切片修改元素():
    items8 = ["apple", "waxberry", "pitaya", "peach", "watermelon"]
    items8[1:3] = ["x", "o"]
    print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']


def 列表关系运算():
    nums1 = [1, 2, 3, 4]
    nums2 = list(range(1, 5))
    nums3 = [3, 2, 1]
    print(nums1 == nums2)  # True
    print(nums1 != nums2)  # False
    print(nums1 <= nums3)  # True
    print(nums2 >= nums3)  # False


def 元素遍历1():
    language = ["Python", "C", "Java", "C++"]
    for index in range(len(language)):
        print(language[index])


def 元素遍历2():
    languages = ["Python", "Java", "C++", "Kotlin"]
    for language in languages:
        print(language)

def 骰子计数1():
    from collections import Counter

    res_list = []
    for _ in range(6000):
        face = random.randrange(1, 7)
        res_list.append(face)
    counts = Counter(res_list)
    for item, count in sorted(counts.items()):
        print(f"'{item}' 出现了 {count} 次")

def 骰子计数2():
    import random

    counters = [0] * 6
    print(counters)
    for _ in range(6000):
        face = random.randrange(1, 7)
        counters[face - 1] += 1
    print(counters)
    for face in range(1, 7):
        print(f"{face}出现了{counters[face - 1]}次")


if __name__ == "__main__":
    骰子计数2()
