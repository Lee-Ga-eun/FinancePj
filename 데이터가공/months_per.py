
import pandas as pd
csv_data = pd.read_csv("데이터가공/코스피_주가이익비율__PER__20221115215348.csv", sep = ",",encoding='utf-8')
csv_data=csv_data[['2022.04','2022.05','2022.06','2022.07','2022.08','2022.09']]
# 2022.04,2022.05,2022.06,2022.07,2022.08,2022.09

csv_data.to_json("데이터가공/months_per.json", force_ascii=False, orient = "records")