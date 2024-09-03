movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
]
#extract movies from specific genre
Crime=[movie for movie in movies if movie['genre']=='Crime']
print('Crime movies\n')
for movie in Crime:
    print(f"{movie['title']}:{movie['genre']}")
#extract all the genres
genres=[movie['genre'] for movie in movies]
genre_count={genre:genres.count(genre) for genre in genres }
print(genre_count)