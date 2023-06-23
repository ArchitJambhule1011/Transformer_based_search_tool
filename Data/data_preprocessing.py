import json
import pandas as pd
import random

#orignal_file = 'News_Category_Dataset_v3.json'

def data_prep(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            try:
                item = json.loads(line)
                data.append(item)
            except json.JSONDecodeError:
                print(f"Ignoring line: {line}")

    df = pd.DataFrame(data)
    df['id'] = [random.randint(1, 1000000) for _ in range(len(df))]
    df_2 = df.drop(['category', 'authors'], axis=1)
    return df_2

#Implementation given in Semantic_search_Noteboook



