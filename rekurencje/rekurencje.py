def numerated_text(n, s):
    if n == 0:
        print(f'Blastoff!')
    else:
        if s == 'desc':
            print(f'text number : {n}')
        numerated_text(n - 1, s)
        if s == 'asc':
            print(f'text number : {n}')


if __name__ == '__main__':
    numerated_text(10, 'desc')
