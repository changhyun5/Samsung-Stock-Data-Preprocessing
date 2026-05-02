import pandas as pd
from pathlib import Path


def load_samsung_data():
    csv_path = Path(r'C:\Users\CENOTech\Desktop\My_project\datasets\samsung_data.csv')

    df = pd.read_csv(csv_path)

    # 1. 날짜 변환
    df['날짜'] = pd.to_datetime(df['날짜'])

    # 2. 가격 관련 컬럼 (종가, 시가, 고가, 저가) 변환
    # 콤마(,)를 제거해야 숫자로 변환 가능합니다.
    price_cols = ['종가', '시가', '고가', '저가']
    for col in price_cols:
        df[col] = df[col].astype(str).str.replace(',', '').astype(float)

    # 3. 거래량 변환 (M 제거 후 100만 곱하기)
    # '24.30M' -> 24.30 -> 24300000.0
    df['거래량'] = df['거래량'].astype(str).str.replace('M', '').astype(float) * 1000000

    # 4. 변동 % 변환 (% 제거)
    # '1.12%' -> 1.12
    df['변동 %'] = df['변동 %'].astype(str).str.replace('%', '').astype(float)

    # 시계열 분석을 위해 날짜순 정렬
    df = df.sort_values('날짜').reset_index(drop=True)

    return df


if __name__ == '__main__':
    samsung = load_samsung_data()

    print("--- 변환 후 상단 데이터 ---")
    print(samsung.head())

    print("\n--- 최종 Dtype 확인 ---")
    print(samsung.info())
