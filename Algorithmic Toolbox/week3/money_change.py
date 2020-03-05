# python3


def money_change(m):
    change = 0
    
    if m >= 10:
        change += m//10
        m %= 10
    
    if m >= 5:
        change += m//5
        m %= 5
    
    if m > 0:
        change += m
        m = 0

    return change


if __name__ == "__main__":
    m = int(input())
    print(money_change(m))
