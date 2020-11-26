import random
import string

# 生成随机字符串
def get_random_str():
    code_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    print(code_str)
    return code_str


if __name__ == '__main__':
    get_random_str()
