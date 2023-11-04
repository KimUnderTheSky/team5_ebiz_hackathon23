# 입력 문자열에서 불필요한 문자를 제거하고 스페인어의 각 문자를 한 문자로 처리합니다.
input_string = 'espan~afu,tbol'
characters = input_string.replace(',', '').replace('..', '').replace('~','').replace(' ','')

length = len(characters)
print(f'문자열의 길이: {length}')
