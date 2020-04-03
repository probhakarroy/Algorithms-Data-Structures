# python3


def max_gold_knapsack(W, n, gold_bars):
    weight = [[0 for i in range(n+1)] for j in range(W+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            weight[w][i] = weight[w][i-1]
            if gold_bars[i-1] <= w:
                wgt = weight[w - gold_bars[i-1]][i-1] + gold_bars[i-1]
                if weight[w][i] < wgt:
                    weight[w][i] = wgt

    return weight[W][n]


if __name__ == "__main__":
    W, n = [int(i) for i in input().split()]
    gold_bars = [int(i) for i in input().split()]

    print(max_gold_knapsack(W, n, gold_bars))
