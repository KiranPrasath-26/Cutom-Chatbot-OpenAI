# Chatbot for a dataframe using PANDASAI

from dotenv import load_dotenv
import os

import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

load_dotenv()

def read_csv(directory):
    data = []
    for csv_file in os.listdir(directory):
        if(csv_file.endswith(".csv")):
            csv_file_path = os.path.join(directory, csv_file)
            with open(csv_file_path, 'rb') as csv_file_:
                data.append(pd.read_csv(csv_file_))
    return data

train_directory = "train_folder/"

csv = read_csv(train_directory)

llm1 = OpenAI()

pandas_ai = PandasAI(llm1)

query  = "what is the sum of walk heads in month of january 2023, the date format is yyyy-mm-dd"
 
response = pandas_ai.run(csv, query)
print(query)
print(response)