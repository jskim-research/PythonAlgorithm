"""
programmers 괄호 회전하기 풀이

시작 시간: 2022.09.22 17:20~34  18시 21분~22분
끝 시간: 2022.09.22 ...
걸린 시간: 15분
병목 원인:
개선 여지:
"""


def check(s):
    stack = []
    for c in s:
        if stack and ((stack[-1] == '{' and c == '}') or (stack[-1] == '(' and c == ')') or (stack[-1] == '[' and c == ']')):
            stack.pop()
        else:
            stack.append(c)
    return len(stack) == 0


def solution(s):
    answer = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if check(s):
            answer += 1
    return answer

