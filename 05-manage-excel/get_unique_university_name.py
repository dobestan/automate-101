import pandas as pd


# 학교명 리스트를 뽑아내서 따로 엑셀파일로 저장하기
# 공공데이터 포털 접속 > 파일 데이터 > 다운로드 순 정렬 > 교육기본통계(대학교) 자료 다운로드


df = pd.read_excel('original_modified.xlsx')


print(df['학교명'].unique())
pd.DataFrame(df['학교명'].unique()).to_excel('universities.xlsx', index=False, header=False)
