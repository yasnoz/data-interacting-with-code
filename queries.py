# pylint: disable=missing-docstring, C0103

def directors_count(db):

    #return the number of directors contained in the database
    query = (""" SELECT COUNT(*) AS total_director
             FROM directors AS d
             """)
    db.execute(query)
    results = db.fetchone()
    # results in a list (rows) of tuples (columns)
    return int(results[0])


def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = ("""SELECT name
             FROM directors As d
             ORDER BY d.name
            """)
    db.execute(query)
    results = db.fetchall()
    return [directors[0] for directors in results]
    #directors_list = []
    #for i in results:
    #    directors_list.append([])
    #    return tuple(directors_list)
    # results in a list (rows) of tuples (columns)

def love_movies(db):
    # return the list of all movies which contain the exact word "love"
    # in their title, sorted in alphabetical order
    query = (""" SELECT title
        FROM movies
        WHERE UPPER(title) LIKE '% LOVE %'
        OR UPPER(title) LIKE 'LOVE %'
        OR UPPER(title) LIKE '% LOVE'
        OR UPPER(title) LIKE 'LOVE'
        OR UPPER(title) LIKE '% LOVE''%'
        OR UPPER(title) LIKE '% LOVE.'
        OR UPPER(title) LIKE 'LOVE,%'
        ORDER BY title
            """)
    db.execute(query)
    results = db.fetchall()
    return [movies[0] for movies in results]


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = f""" SELECT COUNT(*)
             FROM directors AS d
             WHERE d.name LIKE '%{name}%'
             """
    db.execute(query)
    results = db.fetchone()
    return int(results[0])

def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration,
    # sorted in the alphabetical order
    query = f""" SELECT title AS movie_title
             FROM movies AS m
             WHERE minutes > '{min_length}'
             ORDER BY m.title ASC
             """
    db.execute(query)
    results = db.fetchall()

    movie_list = [result[0] for result in results]

    return movie_list
