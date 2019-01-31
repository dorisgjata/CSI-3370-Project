import psycopg2

def connect():
    conn = None   
    try:
        print('Connecting to the PostgreSQL database')
        conn = psycopg2.connect(host="localhost", database="dinning", user="postgres", password="postgres")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()