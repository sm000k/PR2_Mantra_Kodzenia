

def get_greatest_commmon_divisior(a, b):
    while b != 0:
        [x,c] = divmod(a, b)
        a = b
        b = c
    return a




if __name__ == "__main__":
    print(get_greatest_commmon_divisior(1989,867))
