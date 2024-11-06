data = input()
check = False   # 괄호 안의 문자인지 확인용
reverse = []    # 뒤집을 단어
answer = ''

for i in data:
    if i == '<':
        check = True
        for _ in range(len(reverse)):
            answer += reverse.pop()
        answer += '<'

    elif i == '>':
        check = False
        answer += '>'
    
    # 태그 안에 있는 경우
    elif check == True:
        answer += i

    # 공백인 경우
    elif i == ' ':
        for _ in range(len(reverse)):
            answer += reverse.pop()
        answer += ' '

    else:
        reverse.append(i)

# 아직 reverse에 남아있는 경우
for _ in range(len(reverse)):
    answer += reverse.pop()

print(answer)