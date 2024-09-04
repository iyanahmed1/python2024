from collections import Counter
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
genres=[movie['genre'] for movie in movies]#Extract all movie genres
genre_count={genre:genres.count(genre) for genre in genres }
print(genre_count)
#filter movies according to ratings
rating=[movie for movie in movies if movie['rating']>=9.0]
print('\n Highly ratings')
for movie in rating:
    print(f"{movie['title']}:{movie['rating']}")
#sort the movies based on their ratings in desc order
#modify the code using the sorted() function wioth a lambda function
#as the key sort ot sort the movies
sorted_movies=sorted(movies, key=lambda movie:movie['rating'],reverse=True)
print('Movies sorted  by their ratings in Desc order')
for movie in  sorted_movies:
    print(f"{movie['title']}:{movie['rating']}")
# another way to get the count of genres
movie_genres={movie['genre']:sum(1 for m in movies if m['genre']==movie['genre'])for movie in movies}
#use collections module to get the genre counts
genrecount=Counter(movie['genre']for movie in movies)
print(genrecount)