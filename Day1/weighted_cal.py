''' Weight Calculator
Assignment marks weight is !0%
Exam Weight is 35%
'''

ass_score = list(map(int,input().split()))
exam_score = list(map(int,input().split()))

weighted_score = .10*sum(ass_score) + .35*sum(exam_score)

print(weighted_score)

input()
