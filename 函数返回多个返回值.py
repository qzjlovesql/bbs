"""
验证一下，当函数有多个返回值的时候
返回的结果是什么类型！！！
"""


def get_random_color():
    return 255, 0, 0


ret = get_random_color()
print(ret, type(ret))
