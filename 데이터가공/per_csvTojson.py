import pandas as pd
csv_data = pd.read_csv("데이터가공/PERKOSPI100.csv", sep = ",",encoding='utf-8')
csv_data=csv_data[['종목명','PER']]

csv_data.to_json("데이터가공/PERKOSPI100.json", force_ascii=False, orient = "records")
