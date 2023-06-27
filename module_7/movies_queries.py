import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print(f"Database user {config['user']} connected to MySQL on host {config['host']} with database {config['database']}\n")

    cursor = db.cursor()

    # Select and display Studio records
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print(f"Studio ID: {studio[0]}\nStudio Name: {studio[1]}\n")

    # Select and display Genre records
    print()
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print(f"Genre ID: {genre[0]}\nGenre Name: {genre[1]}\n")

    # Select and display short films
    print()
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print(f"Film Name: {film[0]}\nRuntime: {film[1]}\n")

    # Select and display films ordered by director
    print()
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
    films = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\n")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
