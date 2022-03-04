import sys

form = sys.stdin.readline().rstrip().split('-')

for i in range(len(form)):
    if '+' in form[i]:
        number = sum(list(map(int,form[i].split('+'))))
        form[i] = number

result = int(form[0])

for i in range(1,len(form)):
    result-=int(form[i])

print(result)