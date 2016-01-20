import pandas as pd


# 대학교명을 기준으로 파일을 나누는 스크립트
# 공공데이터 포털 접속 > 파일 데이터 > 다운로드 순 정렬 > 교육기본통계(대학교) 자료 다운로드


df = pd.read_excel('original_modified.xlsx')


# 학교명을 기준으로 DataFrame 을 나누자.
university_groups = df.groupby('학교명')


for university_name in df['학교명'].unique():
    print(university_name)
    university_group = university_groups.get_group(university_name)
    university_group.to_excel('universities/{university_name}.xlsx'.format(university_name=university_name), index=False)
