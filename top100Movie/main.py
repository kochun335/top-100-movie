from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, features="html.parser")
movie_list_with_tags = soup.select(".listicleItem_listicle-item__title__BfenH")
movie_list = [movie.getText() for movie in movie_list_with_tags]
print(movie_list)

with open("movie_list.txt", "w+") as movie_list_file:
    for i in range(len(movie_list)-1, -1, -1):
        movie_list_file.write(movie_list[i] + "\n")
        print(movie_list[i])
