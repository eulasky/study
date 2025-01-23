N = int(input())
selectN = list(map(int, input().split()))
student = []
student_L = []

for i in range(0, N):
    student.append(i+1)
    student[i-selectN[i]] = student[i]
    student[i-selectN[i]+1:] = student_L[i-selectN[i]:]
    student_L = student[::]

print(*student)