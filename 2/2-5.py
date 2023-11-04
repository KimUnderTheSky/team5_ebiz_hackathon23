#5-1
def print_pattern(rows):
    for i in range(rows): #시간복잡도 O(1)
        left_spaces = i
        stars = 2 * (rows - i) - 1 # star 한 row별로 양옆에 "*" 삭제한 개수
        right_spaces = i
        line = " " * left_spaces + "*" * stars + " " * right_spaces
        print(line)

print_pattern(4)

#5-2
def print_pattern(rows):
    pattern = []  # 출력할 패턴을 저장할 빈 리스트를 만듭니다.

    # 위쪽 부분을 생성
    for i in range(rows, 0, -1):
        spaces = rows - i  # 왼쪽 공백의 개수 계산
        stars = 2 * i       # 별의 개수 계산
        line = " " * spaces + "*" * stars  # 현재 행의 문자열을 생성
        pattern.append(line)  # 패턴 리스트에 추가

    # 아래쪽 부분을 생성하기 위해 위쪽 부분을 역순으로 추가
    pattern += pattern[:-1][::-1] # 마지막 행 제외하고 역순으로 정렬

    # 생성된 패턴을 출력
    for line in pattern:
        print(line)

# 함수를 호출하여 4행짜리 패턴 출력
print_pattern(4)

#5-3
def print_pattern(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            line = '*' * (2 * rows)
        else:
            line = '*' + ' ' * (2 * rows - 2) + '*'
        print(line)

print_pattern(5)
