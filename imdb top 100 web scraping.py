from bs4 import BeautifulSoup
import requests

url = ["https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc",
       "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt"]
movie_names = []
movie_indexes = []
movie_years = []
for i in url:
    contents = requests.get(i).text
    soup = BeautifulSoup(contents, "html.parser")
    indexes = soup.select(".lister-item-index")
    names = soup.select(".lister-item-header a")
    years = soup.select(".lister-item-year")
    movie_indexes.extend(indexes)
    movie_names.extend(names)
    movie_years.extend(years)


for i in range(len(movie_indexes)):
    print(f"{movie_indexes[i].text} {movie_names[i].text} {movie_years[i].text}")
    print("******************************************************")
