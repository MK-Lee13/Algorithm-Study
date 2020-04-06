import math

def solution(progresses, speeds):
    deploys = []
    nextDeploy = 0
    for index, progress in enumerate(progresses):
        restProgress = (100 - progress)
        currentDeploy = (restProgress / speeds[index])
        currentDeploy = math.ceil(currentDeploy)
        print(currentDeploy)
        if currentDeploy > nextDeploy:
            deploys.append(1)
            nextDeploy = currentDeploy
        else:
            deployCount = deploys.pop() + 1
            deploys.append(deployCount)
    answer = deploys
    return answer