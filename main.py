#FastAPI main file
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse, JSONResponse
from mocks.movies import MOVIES_OBJ
from entities import Movie

app = FastAPI()
app.title = "FastAPI Starter"
app.description = "This is a FastAPI starter template"
app.version = "0.1.0"


@app.get("/", tags=["Home"])
def message():
    return {"message": "Hello World"}

@app.get('/html', response_class=HTMLResponse, tags=['Home'])
def html_message():
    return '<h1>Hello World</h1>'

@app.get('/json', response_class=JSONResponse, tags=['Home'])
def json_message():
    return {"message": "Hello World"}


@app.get('/movies', tags=['Movies'])
def get_movies():
    return MOVIES_OBJ

@app.get('/movies/{movie_id}', tags=['Movies'])
def get_movie(movie_id: int):
    for movie in MOVIES_OBJ:
        if movie["id"] == movie_id:
            return movie
    return JSONResponse(status_code=404, content={"message": "Movie not found"})

@app.get("/movies/", tags=['Movies'])
def get_movies_by_category(category: str):
    movies_by_category = [movie for movie in MOVIES_OBJ if movie["category"].lower() == category.lower()]
    return { "query": category, "movies": movies_by_category}

@app.post("/movies/", tags=['Movies'])
def create_movie(movie: Movie = Body(...)):
    MOVIES_OBJ.append({
        "id": movie.id,
        "name": movie.name,
        "year": movie.year,
        "director": movie.director,
        "category": movie.category
    })
    return {"message": "Movie created successfully", "movie": MOVIES_OBJ[-1]}

@app.put("/movies/{movie_id}", tags=["Movies"])
def udpate_movie(movie_id: int, item: Movie):
    for movie in MOVIES_OBJ:
        if movie['id'] == movie_id:
            movie['name'] = item.name
            movie['year'] = item.year
            movie['director'] = item.director
            movie['category'] = item.category
            return {"message": "Movie updated successfully", "movie": movie}
    return JSONResponse(status_code=404, content={"message": "Movie not found"})

@app.delete("/movies/{movie_id}", tags=["Movies"])
def delete_movie(movie_id: int):
    for movie in MOVIES_OBJ:
        if movie['id'] == movie_id:
            MOVIES_OBJ.remove(movie)
            return {"message": "Movie deleted successfully"}
    return JSONResponse(status_code=404, content={"message": "Movie not found"})
