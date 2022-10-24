class important_business:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'name: {self.name}'

def printer(h: int, w: int):
    for i in range(h):
        print(''.join(['*' if (i+j)%2==0 else 'o' for j in range(w)]))

def main():
    print('this is a really complex piece of software')
    printer(40, 70)


if __name__ == '__main__':
    main()
