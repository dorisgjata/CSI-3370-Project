import psycopg2

def connect():
    conn = None
    #reading the table.sql file to execute commands
    fd = open('tables.sql', 'r')
    sqlFile=fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    try:
        print('Connecting to the PostgreSQL database')
        conn = psycopg2.connect(host="localhost", database="dinning", user="postgres", password="postgres")
        cur=conn.cursor()
        for command in sqlCommands:
            #the file contains comments that are parsed into emty strngs
            if command !="":
                cur.execute(command)
        cur.close()
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    


if __name__ == '__main__':
    connect()