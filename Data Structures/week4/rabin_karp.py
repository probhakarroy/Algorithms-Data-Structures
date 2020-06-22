# python3
import random


def polyhash(S, p, x):
    hash = 0
    for i in range(len(S)-1, -1, -1):
        hash = ((hash*x + ord(S[i])) % p)
    return hash


def precompute_hashes(T, p_len, p, x):
    H = [None] * (len(T) - p_len + 1)
    S = T[len(T)-p_len:]
    H[len(T)-p_len] = polyhash(S, p, x)

    y = 1
    for i in range(1, p_len+1):
        y = (y*x) % p

    for i in range(len(T)-p_len-1, -1, -1):
        H[i] = (x*H[i+1] + ord(T[i]) - y*ord(T[i + p_len])) % p

    return H


def rabin_karp(T, P):
    p = 1000000007
    x = random.randint(1, p-1)
    result = []

    pHash = polyhash(P, p, x)
    H = precompute_hashes(T, len(P), p, x)

    for i in range(len(T)-len(P)+1):
        if pHash != H[i]:
            continue

        if T[i:i+len(P)] == P:
            result.append(i)

    return result


if __name__ == "__main__":
    P = input()
    T = input()

    result = rabin_karp(T, P)
    for i in result:
        print(i, end=' ')
    print()
