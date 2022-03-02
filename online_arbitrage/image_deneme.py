from PIL import Image
import imagehash
from glob import glob
import pandas as pd

path = 'C:/Users/Mahmut/Desktop/Online_Arbitrage/online_arbitrage_files/etsy_images/*.jpg'
all_images = glob(path)    

rows=[]

for i,k in zip(all_images[0::2], all_images[1::2]):
    
    hash = imagehash.average_hash(Image.open(i))
    otherhash = imagehash.average_hash(Image.open(k))
    im_sim_score = hash-otherhash
    rows.append(im_sim_score)

df1 = pd.read_csv('C:\\Users\Mahmut\\Desktop\\Online_Arbitrage\\online_arbitrage_files\\etsy\\etsy_ciceksepeti_2021-07-13_TakiSaatAksesuar_Max100_DegerlendirilenTest.csv', sep=';')


df2 = pd.DataFrame(rows, columns=['im_sim_score'])

df_col_merged = pd.concat([df1, df2], axis=1)

df_col_merged.to_csv('C:\\Users\Mahmut\\Desktop\\Online_Arbitrage\\online_arbitrage_files\\etsy\\etsy_ciceksepeti_2021-07-13_TakiSaatAksesuar_Max100_DegerlendirilenTestSon.csv', sep=';', encoding='utf-8-sig', index=False)
