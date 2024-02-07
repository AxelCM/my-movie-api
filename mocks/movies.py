movies = [
    {
        "id": 1,
        "name": "Back to the Future",
        "year": 1985,
        "director": "Robert Zemeckis",
        "category": "Science Fiction"
    },
    {
        "id": 2,
        "name": "The Matrix",
        "year": 1999,
        "director": "The Wachowskis",
        "category": "Science Fiction"
    },
    {
        "id": 3,
        "name": "The Lord of the Rings: The Fellowship of the Ring",
        "year": 2001,
        "director": "Peter Jackson",
        "category": "Fantasy"
    },
    {
        "id": 4,
        "name": "The Dark Knight",
        "year": 2008,
        "director": "Christopher Nolan",
        "category": "Superhero"
    },
    {
        "id": 5,
        "name": "The Shawshank Redemption",
        "year": 1994,
        "director": "Frank Darabont",
        "category": "Drama"
    }
]

MOVIES_DICT = {movie['id']: movie for movie in movies}
MOVIES_OBJ = [movie for movie in MOVIES_DICT.values()]