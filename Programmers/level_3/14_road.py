def solution(m, n, puddles):
    p_map = make_map(m, n)
    p_map[0][0] = 1
    for i in range(0, n):
        for j in range(0, m):
            if [j + 1, i + 1] in puddles or [i, j] == [0, 0]:
                continue
            if i == 0:
                p_map[i][j] = p_map[i][j - 1]
            elif j == 0:
                p_map[i][j] = p_map[i - 1][j]
            else:
                p_map[i][j] = p_map[i - 1][j] + p_map[i][j - 1]
    return p_map[n - 1][m - 1] % 1000000007


def make_map(m, n):
    return [[0] * (m) for _ in range(n)]