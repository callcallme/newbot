import psycopg2
conn = psycopg2.connect(database = 'd2er58k3jvhj8r',user = 'zvqtnxxlgxrbzb' , password = 'e6b48c591ffb1e0d4dc9f6f8c13d00e682457d2aba1f4bbbd35df8fbf8dacb7e', host = 'ec2-54-235-181-55.compute-1.amazonaws.com', port ='5432')
cursor = conn.cursor()

cursor.execute("insert into album(photo_url, photo_type) value('https://images.chinatimes.com/newsphoto/2019-08-05/900/20190805000009.png',1)")
cursor.execute("insert into album(photo_url, photo_type) value('https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Han_Kuo-yu%28cropped%29.jpg/250px-Han_Kuo-yu%28cropped%29.jpg',1)")
cursor.execute("insert into album(photo_url, photo_type) value('https://doqvf81n9htmm.cloudfront.net/data/annahu_151/181115/1920_PKH_5051_.jpg',1)")
cursor.execute("insert into album(photo_url, photo_type) value('https://images.chinatimes.com/newsphoto/2019-08-05/900/20190805000743.jpg',1)")
cursor.execute("insert into album(photo_url, photo_type) value('https://img5.cna.com.tw/www/WebPhotos/1024/20190715/800x600_86173643417.jpg',1)")

conn.commit()
print('新增成功')
conn.close()


