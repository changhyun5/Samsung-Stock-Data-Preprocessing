import pandas as pd
from pathlib import Path
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# 1: 데이터 로드 및 수치형 변환 함수
def load_samsung_data():
    csv_path = Path(r'C:\Users\CENOTech\Desktop\My_project\datasets\samsung_data.csv')
    df = pd.read_csv(csv_path)

    # 수치형 변환
    price_cols = ['종가', '시가', '고가', '저가']
    for col in price_cols:
        df[col] = df[col].astype(str).str.replace(',', '').astype(float)

    df['거래량'] = df['거래량'].astype(str).str.replace('M', '').astype(float) * 1000000
    df['변동 %'] = df['변동 %'].astype(str).str.replace('%', '').astype(float)
    df['날짜'] = pd.to_datetime(df['날짜'])

    # 시계열 순서 정렬
    df = df.sort_values('날짜').reset_index(drop=True)
    return df


# 2: 데이터 변환 (Scaling) 함수
def apply_scaling(df):
    # 정규화 (Min-Max)
    norm_scaler = MinMaxScaler()
    df['종가_정규화'] = norm_scaler.fit_transform(df[['종가']])

    # 표준화 (Standard)
    std_scaler = StandardScaler()
    df['종가_표준화'] = std_scaler.fit_transform(df[['종가']])
    return df


# 3: 데이터 분할 (Split) 함수
def split_data(df):
    # 전체 20개 중 80%(16개) 학습용, 20%(4개) 테스트용
    train = df.iloc[:16]
    test = df.iloc[16:]
    return train, test


# 4: 실제 실행 구문
if __name__ == '__main__':
    # 1. 데이터 불러오기 및 수치화
    samsung = load_samsung_data()

    # 2. 스케일링 적용
    samsung_final = apply_scaling(samsung)

    # 3. 결과 출력
    print("--- 스케일링 결과 확인 (상단 5행) ---")
    print(samsung_final[['날짜', '종가', '종가_정규화', '종가_표준화']].head())

    print("\n--- 통계량 확인 ---")
    print(f"정규화 최댓값: {samsung_final['종가_정규화'].max()}")
    print(f"정규화 최솟값: {samsung_final['종가_정규화'].min()}")
    print(f"표준화 평균(약 0): {round(samsung_final['종가_표준화'].mean(), 2)}")

    # 4. 데이터 분할 실행
    train_set, test_set = split_data(samsung_final)
    print(f"\n데이터 분할 완료: 학습용({len(train_set)}개), 테스트용({len(test_set)}개)")
