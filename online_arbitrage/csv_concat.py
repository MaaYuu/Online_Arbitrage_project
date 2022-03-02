from glob import glob
import os
from datetime import datetime

""" import pandas as pd
import os


path = '../online_arbitrage_files/ciceksepeti'

all_files = glob.glob(os.path.join(path, "*.csv"))     # advisable to use os.path.join as this makes concatenation OS independent

df_from_each_file = (pd.read_csv(f) for f in all_files)
df   = pd.concat(df_from_each_file, ignore_index=True)
# doesn't create a list, nor does it append to one


df.to_csv('../online_arbitrage_files/ciceksepeti/toplu_csv.csv', index=False, encoding='utf-8-sig')
 """

path = '../online_arbitrage_files/ciceksepeti'
all_files = glob(os.path.join(path, datetime.today().strftime('%Y_%m_%d')+'_ciceksepeti'+'*.csv'))

for file in all_files:
    print(os.path.basename(file))
