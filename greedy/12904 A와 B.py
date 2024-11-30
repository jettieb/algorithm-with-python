"""
너무 어려움 ㅜㅜ
구글링 해보니 탑다운 방식으로 진행하면 편함. 
B -> ABBA로 만드는 방식이 아닌, ABBA -> B로 역으로 만들어가는게 편함.
문자열의 뒤에 A를 추가했다면, 역으로 맨 마지막 문자가 A일 것.
문자열을 뒤집고 뒤에 B를 추가했다면, 역으로 맨 마지막 문자가 B라면 다시 뒤집기.
"""
import sys
input = sys.stdin.readline

S = list(map(str, input().strip()))
T = list(map(str, input().strip()))

while len(S) != len(T): # 길이가 같을 때 까지 실행
    
    if T[-1] == 'A': # 마지막 줄이 A인 경우 A만 지우면 됨.
        T.pop()
    elif T[-1] == 'B': # 마지막 줄이 B인 경우 B 지우고 뒤집기
        T.pop()
        T.reverse()

if S == T:
    print(1)
else:
    print(0)