#Data Adquisition
import requests
import io
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
from typing import Tuple, List
import re
from datetime import datetime

def get_soup(url: str) -> BeautifulSoup:
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_csv_from_url(url:str) -> pd.DataFrame:
    s=requests.get(url).content
    return pd.read_csv(io.StringIO(s.decode('utf-8')))

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

df = pd.read_csv("C:\\Users\\MIKID\\Documents\\Michelle - Facultad de Ciencias Físico Matemáticas\\7TO SEMESTRE\\MINERÍA DE DATOS\\netflix_titles.csv")
print_tabulate(df)


#LIMPIEZA DE DATOS

import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

df.drop(columns=['show_id','cast','date_added','rating','duration','listed_in','description'])


