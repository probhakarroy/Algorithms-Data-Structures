# python3


def money_change_dp(money, coins=[1, 3, 4]):
    min_num_coins = [float('inf')] * (money+1)
    min_num_coins[0] = 0

    for m in range(1, money+1):
        for j in coins:
            if m >= j:
                n_coins = min_num_coins[m - j] + 1
                if n_coins < min_num_coins[m]:
                    min_num_coins[m] = n_coins

    return min_num_coins[money]


if __name__ == "__main__":
    money = int(input())
    print(money_change_dp(money))