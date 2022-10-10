"""
programmers 다리를 지나는 트럭 풀이

시작 시간: 2022.10.10 20:29
끝 시간: 2022.10.10 21:51
걸린 시간: 1시간 22분
병목 원인: 문제가 될만한 요소를 구현중 떠올렸는데 따로 체크를 안해놔서 더욱 디버깅에 시간이 걸림
개선 여지: 문제가 될 수 있는 부분을 떠올렸을 경우 최소한 기록이라도 해둘 것
"""
from collections import deque


def solution(bridge_length, weight, truck_weights):
    # 경과 시간: 들어간 시점 + bridge_length
    # 들어가는 시점은 아무 트럭도 다리에 없고 가능한 만큼 채우는 경우 or 앞의 트럭이 나가면서 무게에 여유가 생긴 경우
    truck_queue = deque(truck_weights)
    bridge_queue = deque()
    current_weight = 0
    current_time = 0

    while truck_queue or bridge_queue:
        if truck_queue and truck_queue[0] + current_weight <= weight and len(bridge_queue) < bridge_length:
            # 들어갈 수 있는 상황
            truck_weight = truck_queue.popleft()
            current_weight += truck_weight
            current_time += 1
            bridge_queue.append((truck_weight, current_time))

            # 새로운 차가 들어올 때 시간이 변하면서 앞의 차가 빠져나가야 하는 시간이 될 수 있음
            if current_time == bridge_queue[0][1] + bridge_length:
                front_truck = bridge_queue.popleft()
                current_weight -= front_truck[0]
        else:
            # 들어갈 수 없는 상황
            # 즉, 다리 위에 최소 하나의 차량이 있기 때문 => 없애주자
            front_truck = bridge_queue.popleft()
            current_weight -= front_truck[0]
            current_time = front_truck[1] + bridge_length
            # 없애준 후에 들어갈 수 있으면 다른 차량 넣기
            if truck_queue and truck_queue[0] + current_weight <= weight and len(bridge_queue) < bridge_length:
                # 들어갈 수 있는 상황, 앞의 차가 빠지는 동시에 들어가므로 current_time의 update는 없음
                truck_weight = truck_queue.popleft()
                current_weight += truck_weight
                bridge_queue.append((truck_weight, current_time))

    return current_time
