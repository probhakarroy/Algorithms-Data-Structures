# python3


def covering_segments_by_points(segments):
    points, n = [], len(segments)

    while n > 0:
        points.append(segments[0][1])
        covered = []
        for i in segments:
            if points[-1] >= i[0] and points[-1] <= i[1]:
                covered.append(i)

        for i in covered:
            segments.remove(i)

        n = len(segments)

    return points


if __name__ == "__main__":
    n = int(input())
    segments = [[int(i) for i in input().split()] for j in range(n)]

    segments = sorted(segments, key=lambda x: x[1])
    points = covering_segments_by_points(segments)
    
    print(len(points))
    [print(i, end=' ') for i in points]
    print()
