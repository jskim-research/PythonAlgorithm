"""
취업을 위한 코딩테스트 시각 문제풀이
시작 시간: 2022.07.23 03:38
끝 시간: 2022.07.23 03:53
걸린 시간: 15분
병목 원인: 문제 이해를 제대로 못함
개선 방법: 그냥 숫자들 0부터 세보고 테스트 케이스 출력이랑 맞는지 빨리 비교해봐야했음.
"""

# 3 13 23 30~39 43 53
# hour 3이 있는 경우 + 3600
# minute 3이 있는 경우 15*60 = 900
# second 3이 있는 경우 제외 45*15 = 675
# 1575 * 5 + 3600

n = int(input())

if n < 13:
    print(3600 + n * 1575)
else:
    print(7200 + n * 1575)