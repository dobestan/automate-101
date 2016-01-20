import pandas as pd


# 대학교명을 기준으로 파일을 나누는 스크립트

# 공공데이터 포털 접속 > 파일 데이터 > 다운로드 순 정렬 > 교육기본통계(대학교) 자료 다운로드


df = pd.read_excel('original_modified.xlsx')

# 일단은 엑셀 파일이 제대로 불렸는지 한번 체크해보자.
print(df.columns)

# 출력 결과
# Index(['연도', '학제', '시도', '학교명', '본분교', '학교상태', '설립', '우편번호', '주소', '전화번호',
#        '팩스번호', '홈페이지', '학과 계열', 'Unnamed: 13', 'Unnamed: 14', '학과상태', '학과명'],
#       dtype='object')



# 학교명 리스트 출력하기
# print(df['학교명'].unique())

# 학교명 리스트를 다시 엑셀 파일로 저장하기
# pd.DataFrame(df['학교명'].unique()).to_excel('universities.xlsx', index=False, header=False)
