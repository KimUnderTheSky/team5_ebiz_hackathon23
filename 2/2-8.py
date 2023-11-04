n = 4
array = [
  [3, 0, 8, 4],
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0]
]

# 행별 최솟값을 저장할 리스트 초기화
min_values_by_row = []

# 각 행별로 최솟값을 찾아서 min_values_by_row 리스트에 추가
for row in array:
    min_row_value = min(row)
    min_values_by_row.append(min_row_value)

# 열별 최솟값을 저장할 리스트 초기화
min_values_by_col = []

# 각 열별로 최솟값을 찾아서 min_values_by_col 리스트에 추가
for col in range(n):
    column_values = [array[row][col] for row in range(n)]
    min_col_value = min(column_values)
    min_values_by_col.append(min_col_value)

# 결과 출력
print("행별 최솟값:", min_values_by_row)
print("열별 최솟값:", min_values_by_col)

# 행별 최솟값: [0, 2, 2, 0]
# 열별 최솟값: [0, 0, 1, 0]

# 행별 최대값을 저장할 리스트 초기화
max_values_by_row = []

# 각 행별로 최대값을 찾아서 max_values_by_row 리스트에 추가
for row in array:
    max_row_value = max(row)
    max_values_by_row.append(max_row_value)

# 열별 최대값을 저장할 리스트 초기화
max_values_by_col = []

# 각 열별로 최대값을 찾아서 max_values_by_col 리스트에 추가
for col in range(n):
    column_values = [array[row][col] for row in range(n)]
    max_col_value = max(column_values)
    max_values_by_col.append(max_col_value)

# 결과 출력
print("행별 최대값:", max_values_by_row)
print("열별 최대값:", max_values_by_col)

# 행별 최대값: [8, 7, 9, 3]
# 열별 최대값: [9, 4, 8, 7]





# 결과
# 행별 최솟값: [0, 2, 2, 0]
# 열별 최솟값: [0, 0, 1, 0]

# 행별 최대값: [8, 7, 9, 3]
# 열별 최대값: [9, 4, 8, 7]
# 행렬별 최대최소 값을 추출하여 추가적으로 쌓을 수 있는 레고 블록의 개수를 구할 수 있습니다.

