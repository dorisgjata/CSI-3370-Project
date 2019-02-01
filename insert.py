import psycopg2

def insert(param):
    conn = None
    sql = "INSERT INTO campusLocations(locationId, locationName) VALUES (%s, %s)"

    try:
        print('Connecting to the PostgreSQL database')
        conn = psycopg2.connect(host="localhost", database="dinning", user="postgres", password="postgres")
        cur=conn.cursor()

        cur.executemany(sql,param)
        conn.commit()
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
  #  insert([(1,'Hillcrest'),(2,'Vanderberg')])