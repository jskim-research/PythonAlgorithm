"""
programmers 올바른 괄호 문제풀이

시작 시간: 2022.08.20 22:00
끝 시간: 2022.08.20 22:07
걸린 시간: 7분
병목 원인:
개선 방법:
"""


def solution(s):
    answer = True
    stack = []

    for i in range(len(s)):
        if len(stack) == 0 and s[i] == ')':
            return False
        else:
            if s[i] == ')':
                stack.pop()
            else:
                stack.append('(')
    # if len(stack) != 0:
    #     return False
    # return 문에서 줄일 수 있음
    
    # 또는 stack 에 굳이 저장할 필요 없이 stack의 length를 변수로 잡고 x + 1, x - 1 만으로도 가능
    return len(stack) == 0
