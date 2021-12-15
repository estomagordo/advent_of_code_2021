from collections import Counter, defaultdict, deque
from functools import reduce
from heapq import heappop, heappush
from itertools import combinations, permutations, product
from helpers import chunks, chunks_with_overlap, columns, digits, distance, distance_sq, eight_neighs, eight_neighs_bounded, grouped_lines, ints, manhattan, multall, n_neighs, neighs, neighs_bounded


def solve(lines):
    # def transform(n):
    #     m = n+1
    #     if m == 10:
    #         m = 1
    #     return m

    # newlines = [list(line) for line in lines]

    # for line in lines:
    #     newline = list(map(transform, line))

    height = len(lines)
    width = len(lines[0])

    newlines = []

    for bigy in range(5):
        for y in range(height):
            line = []
            for bigx in range(5):
                for val in lines[y]:
                    line.append(val+bigy+bigx)
                    if line[-1] > 9:
                        line[-1] -= 9

            newlines.append(line)

    lines = newlines


    height = len(lines)
    width = len(lines[0])        
    

    frontier = [(0, 0, 0)]
    seen = {(0, 0): 0}

    while True:
        score, y, x = heappop(frontier)

        if y == height-1 and x == width-1:
            return score

        for ny, nx in neighs_bounded(y, x, 0, height-1, 0, width-1):
            newscore = score+lines[ny][nx]
            if (ny, nx) not in seen or seen[(ny, nx)] > newscore:
                seen[(ny, nx)] = newscore
                heappush(frontier, (newscore, ny, nx))


def main():
    lines = []

    with open('15.txt') as f:
        for line in f.readlines():
            lines.append(digits(line))
            
    return solve(lines)


if __name__ == '__main__':
    print(main())
