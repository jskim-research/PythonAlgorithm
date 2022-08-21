"""
programmers 짝지어 제거하기 문제풀이

시작 시간: 2022.07.30 7:20
끝 시간: 2022.07.30 12:29
걸린 시간: 5시간 9분 (휴식시간 제외하면 3시간 정도)
병목 원인: divide & conquer 방식이 아닌 DP 문제로 오판.
         데이터를 보는 방식에 순서가 있기 때문에 모든 case를 보고 작은 case 들을 병합해나가는 과정보다
         divide 하고 순차적으로 병합하는 과정이 훨씬 빠름.
개선 방법: 문제의 가정 상황을 잘 이용해먹자.... !!!! 근데 그냥 stack (python 에선 list)만 이용해도 되는 문제임. 어떤 자료구조가 필요한지 항상 생각하자.

2차 시도
시작 시간: 2022.08.21 21:10
끝 시간: 2022.08.21 21:17
걸린 시간: 7분
"""
def divide_conquer(s):
    len_s = len(s)
    mid = len_s // 2

    if len_s < 2:
        return s

    left = divide_conquer(s[:mid])
    len_left = len(left)
    right = divide_conquer(s[mid:])
    len_right = len(right)

    min_len = min(len_left, len_right)
    matched_num = 0

    for i in range(0, min_len):
        if len_left - i - 1 >= 0:
            if left[len_left - i - 1] != right[i]:
                break
            else:
                matched_num += 1

    merged = left[:len_left-matched_num] + right[matched_num:]
    return merged


def solution(s):
    answer = 1 if divide_conquer(s) == "" else 0
    return answer


def simple_solution(s):
    answer = []
    for i in s:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                answer.pop()
            else:
                answer.append(i)
    answer = 1 if len(answer) == 0 else 0
    return answer


print(simple_solution("abba"))
print(simple_solution("abbc"))


def solution2(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

    return 1 if len(stack) == 0 else 0

