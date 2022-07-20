"""
programmers 문자열압축 문제풀이

시작 시간: 2022.07.20 22:23
끝 시간: 2022.07.20 23:16
걸린 시간: 53분
병목 원인: 문제 추가 고려 요소 생각안함 (압축 시 추가되는 숫자가 10 이상의 값일 수 있다...)
개선 방법: Example 작성을 좀 더 많이 해보고 + Example이 확인하고자 하는 요소를 적어두어서 solution 작성 후 해결되는지 검토
"""

"""
몇 개 단위로 자르는 것이 가장 짧아지는가?

Example

abcabcdede
2개 단위
ab ca bc de de 
3개 단위
abc abc ded e
4개 단위
abca bcde e

추가 example => 확인하고자 하는 case = 압축 숫자에 따른 압축 결과
abc abc de de => 2abcdede (10-3+1)
abc abc abc de de => 3abcdede (13-3-3+1)
abc abc abc abc de de => 4abcdede(13-3-3-3+1)
...
10abcdede (13-3...+2) => 압축 숫자 자릿수에 따라 달라진다.

Pseudo code

min_len = len(string)
for m in range(2, len(string)):  # m개씩 자르기
    length = len(string)
    segments = segmentation(string, m)
    penalty = 1  # 초반 압축 시 숫자가 들어가므로 압축 손해를 봄 ==> 압축 숫자가 1의 자리, 10의 자리, 100의 자리, 그 이상일 수 있다. penalty = 1 은 부적절.
    for i in range(len(segments)-1):
        if segment[i] == segment[i+1]:
            length -= (m-penalty)
            penalty = 0
        else:
            penalty = 1
    min_len = min(min_len, length)
return min_len

시간복잡도: O(n^2)
"""
def count_digit(number: int):
    """
    숫자 자릿수 반환

    Args:
        number: positive integer
    """
    return len(str(number))


def solution(s):
    answer = len(s)
    for m in range(1, len(s)):  # m개씩 자르기
        length = len(s)
        segments = [s[i:i + m] for i in range(0, len(s), m)]
        segments.append("_")  # end string => for 문 체크 시 마지막 element가 무시되는 경우 해결
        count = 1
        for cur_segment, next_segment in zip(segments, segments[1:] + ['']):
            if cur_segment == next_segment:
                length -= m  # m만큼 압축
                count += 1  # 압축 개수 카운팅
            else:
                if count >= 2:
                    length += count_digit(count)  # f"{count}{compressed_char}" 이므로 count의 자릿수만큼 압축 손실 고려
                    count = 1
        answer = min(length, answer)
    return answer
