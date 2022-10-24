from math import sin
def main():
    print('this is a really complex piece of software')
    for i in range(40):
        n = int((sin(i/6)+ 1)*60)
        print('*'*n + ' '*(60-n))

if __name__ == '__main__':
    main()
