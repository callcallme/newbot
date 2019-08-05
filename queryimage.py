import psycopg2
def QueryImage(phototype):
    
    conn = psycopg2.connect(database = 'd2er58k3jvhj8r',user = 'zvqtnxxlgxrbzb' , password = 'e6b48c591ffb1e0d4dc9f6f8c13d00e682457d2aba1f4bbbd35df8fbf8dacb7e', host = 'ec2-54-235-181-55.compute-1.amazonaws.com', port ='5432')
    cursor = conn.cursor()


    imglink = ''
    cursor.execute("select photo_url from album where photo_type = {}order by random() limit 1 ".format(phototype))
    row = cursor.fetchall()
    
    for r in row:
        imglink = r[0]
    conn.close()
    return imglink








