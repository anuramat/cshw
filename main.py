from math import sin

class important_business:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'name: {self.name}'

def main():
    print('this is a really complex piece of software')
    for i in range(40):
        n = int((sin(i/6)+ 1)*60)
        print('*'*n + ' '*(60-n))

if __name__ == '__main__':
    main()
