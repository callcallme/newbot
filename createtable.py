# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import psycopg2

#連結heroku database
conn = psycopg2.connect(database = 'd2er58k3jvhj8r',
                        user = 'zvqtnxxlgxrbzb' , 
                        password = 'e6b48c591ffb1e0d4dc9f6f8c13d00e682457d2aba1f4bbbd35df8fbf8dacb7e', 
                        host = 'ec2-54-235-181-55.compute-1.amazonaws.com', 
                        port ='5432'
                        )





cursor = conn.cursor()



#在 heroku 建立圖片資料庫
sql =   '''
    create table album
    (id serial primary key ,
    photo_url varchar(255),
    photo_type int)
        '''
        
        
        
cursor.execute(sql)
conn.commit()















