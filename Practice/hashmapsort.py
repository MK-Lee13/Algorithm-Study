# 해쉬맵으로 카운트해서 정렬하기

def hashMapSort_ASC(hashMap):
  answer = sorted(hashMap.items(), key=lambda x: x[1])
  return answer

def hashMapSort_DESC(hashMap):
  answer = sorted(hashMap.items(), key=lambda x: -x[1])
  return answer

h = {'1': 1,'2': 2,'3': 3,'4': 4,'10': 10,'9': 9,'8': 8,'7': 7,'6': 6,'5': 5}
print(hashMapSort_ASC(h))
print(hashMapSort_DESC(h))