
from sqlalchemy import create_engine
import pandas as pd
#将Excel表格中的数据放到MySQL中
path = r'./book_list-科普-经典-生活-心灵-文学.xlsx'
data=pd.read_excel(path)

#这里是对data.columns进行处理
list = data.columns
new_list = []
for x in list:
    new_list.append(''.join(x.split()))
data.columns=new_list
engine = create_engine('mysql+pymysql://root:1234@127.0.0.1:3306/pachong?charset=utf8')
#if_exists三个模式：fail，若表存在，则不输出；replace：若表存在，覆盖原来表里的数据；append：若表存在，将数据写到原表的后面。默认为fail
sql_chengfen = data.to_sql(name='book10', con=engine, index=False,if_exists='replace')
