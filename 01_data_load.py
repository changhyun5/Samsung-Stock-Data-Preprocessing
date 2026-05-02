import  pandas as pd
from pathlib import Path

def load_samsung_data():
    # samsung 주식 2026- 02- 06 - 2026- 03- 11 까지의 데이터를 csv로 저장한 후, 데이터값불러오는 코드
    csv_path = Path(r'C:\Users\CENOTech\Desktop\My_project\datasets\samsung_data.csv')
    return pd.read_csv(csv_path)

if __name__ == '__main__':
    #데이터 로드
    samsung = load_samsung_data()

    print("---samsung Data Head---")
    print(samsung.head())


    print("---samsung Data Info---")
    print(samsung.info())
