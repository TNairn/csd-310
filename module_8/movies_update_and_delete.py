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

    def show_films(cursor, title):

        # inner join query
        cursor.execute("SELECT film_name AS Name, "
                       "film_director AS Director, "
                       "genre_name AS Genre, "
                       "studio_name AS 'Studio Name' "
                       "FROM film "
                       "INNER JOIN genre ON film.genre_id = genre.genre_id "
                       "INNER JOIN studio ON film.studio_id = studio.studio_id;")
        films = cursor.fetchall()

        # Iterate over and display the query results
        print(f"\n -- {title} -- ")
        for film in films:
            print(f"Film Name: {film[0]}\n"
                  f"Director: {film[1]}\n"
                  f"Genre Name ID: {film[2]}\n"
                  f"Studio Name: {film[3]}\n")


    # Connect to database
    db = mysql.connector.connect(**config)
    print(f"Database user {config['user']} "
          f"connected to MySQL on host {config['host']} "
          f"with database {config['database']}\n")

    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS")

    # Insert movie and display
    cursor.execute("INSERT INTO film (film_name, film_releaseDate, film_runtime, film_Director, studio_id, genre_id) "
                   "VALUES('Jurassic Park', '1993', 127, 'Steven Spielberg', 3, 2);")
    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update movie and display
    cursor.execute("UPDATE film "
                   "SET genre_id = 1 "
                   "WHERE film_name = 'Alien';")
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete movie and display
    cursor.execute("DELETE FROM film "
                   "WHERE film_name = 'Gladiator'")
    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
