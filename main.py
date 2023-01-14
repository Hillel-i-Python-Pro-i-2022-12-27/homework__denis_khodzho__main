from random import choice

def print_hi(name    ):
    print(f'Hi, {name} random int = {choice(list(range(1,10)))}')

if __name__ == '__main__':
    print_hi('PyCharm')

