def solution(N, stages):
    answer = []
    mmap = [0] * (N)
    for stage in stages:
        if stage > N:
            continue
        mmap[stage - 1] += 1
    total = len(stages)
    answer_two_list = []
    for i in range(len(mmap)):
        stuck = mmap[i]
        if stuck == 0 or total== 0:
            answer_two_list.append([0, i + 1])
        else:
            answer_two_list.append([stuck / total, i + 1])
        total -= stuck
    sort_list = sorted(answer_two_list, key = lambda x : (-x[0], x[1]))
    return [w[1] for w in sort_list]