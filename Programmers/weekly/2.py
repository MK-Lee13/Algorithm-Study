def solution(scores):
    answer = ''
    for i in range(len(scores)):
        avg_student_score = 0
        student_scores = returnMyScores(scores, i) 
        my_score = student_scores[i]
        max_score = max(student_scores)
        min_score = min(student_scores)
        
        if max_score == my_score and student_scores.count(max_score) == 1:
            student_scores.pop(i)
        elif min_score == my_score and student_scores.count(min_score) == 1:
            student_scores.pop(i)
            
        avg_student_score = sum(student_scores) / len(student_scores)
        answer += returnMatchScore(avg_student_score)
        
    return answer

def returnMyScores(scores, i):
    result = []
    for score in scores:
        result.append(score[i])
    return result

def returnMatchScore(avg_student_score):
    if avg_student_score >= 90:
        return "A"
    elif avg_student_score >= 80:
        return "B"
    elif avg_student_score >= 70:
        return "C"
    elif avg_student_score >= 50:
        return "D"
    else:
        return "F"
        