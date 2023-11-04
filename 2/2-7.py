def find_tuples(N):
    tuples = []

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i * j == N: # 곱셈이 N이 되는 튜플 찾기
                tuples.append((i, j))

    return tuples

def find_minimal_sum_tuple(tuples):
    min_sum = float('inf') # 최소 값으로 비교하기 위한 초기 설정, 양의 무한대 값으로 초기값 설정
    min_tuple = None

    for i, j in tuples:
        current_sum = i**2 + j**2 # 제곱합을 구함
        if current_sum < min_sum: # 현재 제곱합이 최소 제곱합보다 작으면 
            min_sum = current_sum # 최소 제곱합 최신화
            min_tuple = (i, j)

    return min_tuple

N = int(input("N을 입력하세요: "))
tuples = find_tuples(N) # 곱셈을 만드는 튜플 return
minimal_sum_tuple = find_minimal_sum_tuple(tuples) # 제곱합의 최솟값 튜플 return
minimum_distance = (minimal_sum_tuple[0] + minimal_sum_tuple[1]) - 2 # 최솟값을 만드는 패턴을 통한 최소 거리 return

print("최소 이동횟수: ",minimum_distance)
