import psycopg2

def insert(param):
    conn = None
    sql = "INSERT INTO campusLocations(locationId, locationName) VALUES (%s, %s)"
    filtersql = "INSERT INTO filters(filterId, filterName) VALUES (%s, %s)"
    usersql = "INSERT INTO users(userId, userName, userPassword, userPreferences, isAdmin ) VALUES (%s, %s, %s, %s, %s)"

    try:
        print('Connecting to the PostgreSQL database')
        conn = psycopg2.connect(host="localhost", database="dinning", user="postgres", password="postgres")
        cur=conn.cursor()

        cur.executemany(usersql,param)
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
  #  insert([(1,'Vegetarian'),(2,'Vegan'),(3,'Balanced'),(4,'Milk'),(5,'Tomato'),(6,'Gluten'),(7,'Wheat'),(8,'Nuts')])
    insert([(1,'dorisgjata', 'admin', 'none', True ),(2,'olivia', 'olivia', 'none', False )])
