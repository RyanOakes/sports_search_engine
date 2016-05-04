import csv
import psycopg2


def create_table():
    try:
        conn = psycopg2.connect("dbname=tennis user=Oakes host=/tmp/")
        cur = conn.cursor()
        cur.execute("CREATE TABLE rankings(id serial PRIMARY KEY, name varchar, matches numeric, wins numeric, losses numeric, win_percentage numeric, bagels_served numeric, bagels_eaten numeric); ")
        with open('rankings.csv') as rankings:
            rankings = csv.reader(rankings, delimiter='\t')
            for row in rankings:
                cur.execute("INSERT INTO rankings (id, name, matches, wins, losses, win_percentage, bagels_served, bagels_eaten) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", row)
        conn.commit()
        cur.close()
        conn.close()
    except:
        pass



# SELECT * FROM rankings
#
# """Write a program that connects to the database and asks the user to search for a player.
# Start with just the name but think about further criteria you could include (position? age?).
# For a given result set, have the program display the results in a clean manner to the user.
# Add a feature to your program that allows a user to insert new players into the database.
# Prompt the user for every column that you will need them to provide custom information on. Name?, Age?, etc."""



def talk_to_database(where, order):
    conn = psycopg2.connect("dbname=tennis user=Oakes host=/tmp/")
    cur = conn.cursor()

    cur.execute('SELECT name, bagels_served, wins from rankings WHERE ' + where + ' ORDER BY ' + order)
    for row in cur.fetchall():
        print(row[0], row[1], row[2])

    conn.commit()
    cur.close()
    conn.close()

talk_to_database(where='bagels_served >= ' + input('enter number of bagels served: '), order='wins DESC')


create_table()







# def create_table():
#
#     conn = psycopg2.connect("dbname=test user=Oakes host=/tmp/")
# ​
#     cur = conn.cursor()
# ​
#     cur.execute("CREATE TABLE rankings(id serial PRIMARY KEY, name varchar, matches integer, wins integer, losses int, win_percentage real, bagels_served int, bagels_eaten int); ")
# ​
#     cur.execute("INSERT INTO exercise (name, age) VALUES (%s, %s)", ("Cameron", 29))
#
#     cur.execute("SELECT * FROM exercise;")
# ​
# cur.execute("UPDATE exercise SET age = 30 WHERE name = 'Scott';")
# cur.execute("DELETE from exercise WHERE name = 'Ryan';")
# ​
# conn.commit()
# cur.close()
# conn.close()
#
# def
#
#
# with open('students.csv') as f: # automatically closes the file when done
#     reader = csv.reader(f)
#     headers = next(reader)
#     print(headers)
#     print('------')
#     for row in reader:
#         print(row)


# conn = psycopg2.connect("dbname=test user=Oakes host=/tmp/")
