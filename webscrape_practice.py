from bs4 import BeautifulSoup as bs
import requests
import time

mname = ['Series', 'Yoruba']
def find_movie():
    link = requests.get('https://www.thenetnaija.co/videos').text
    soup = bs(link, 'lxml')
    movies = soup.find_all('article', class_ = 'file-one shadow')
    for index, movie in enumerate(movies):
        movietype = movie.find('div', class_='category').a.text
        if 'Movies' in movietype:
            moviename = movie.find('div', class_='info').h2.text.strip()
            posttime = movie.find('div', class_='inner').span.text.strip()
            movielink = movie.find('div', class_='info').h2.a['href']
            thelink = requests.get(movielink).text
            souper = bs(thelink,'lxml')
            movieabout = souper.find('article', class_='post-body')
            about = movieabout.find('p').text.strip()
            thrill = souper.find('div', class_='video-player')
            thriller = thrill.find('iframe')['src'].strip().replace(' ','')
            download = souper.find('a')['href']
            with open(f'movies/{index}.txt','w') as posts:
                posts.write(f'''Movie Category: {movietype}\nMovie name: {moviename}\nTime of post: {posttime}\nAbout Movie: {about}\n''')
                posts.write(f'''Movie Thriller: {thriller}\nDownload Link: {download}\n''')
            print(f'File saved: {index}')


if __name__ == '__main__':
    while True:
        find_movie()
        time_wait = 4
        print(f'waiting {time_wait} hours...')
        time.sleep(time_wait * 60* 60)