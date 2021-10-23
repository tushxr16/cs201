from bs4 import BeautifulSoup
import requests
import os
import re

urls = [
    "https://www.imdb.com/search/title/?genres=horror&explore=title_type,genres&view=simple",
    "https://www.imdb.com/india/top-rated-indian-movies/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=8a7876cd-2844-4017-846a-2c0876945b7b&pf_rd_r=TV4C768XA0EW1CH1XRNZ&pf_rd_s=right-5&pf_rd_t=15506&pf_rd_i=toptv&ref_=chttvtp_india_tr_rhs_1",
    "https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=Z4V13V8W15Z0Q6KQBGG7&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=tvmeter&ref_=chttvm_ql_6",
    "https://www.imdb.com/chart/tvmeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=S0PD9BM5MC7FB3BKG4PA&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=topenglish&ref_=chttentp_ql_5",
    "https://www.imdb.com/chart/top-english-movies?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=BDZBDR4Z69H9KFH1JB6B&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_4",
    "https://www.imdb.com/chart/moviemeter?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=QE8SCET94B82QJB72X10&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_2",
    "https://www.imdb.com/chart/top?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=JNH7P8893ZR8F51ENGNN&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=moviemeter&ref_=chtmvm_ql_3"
]


def getTitleAndRatingAsString(url):
    movieString = ""
    fullContent = BeautifulSoup(requests.get(url).content, 'html.parser')
    tbody = fullContent.find('tbody', class_="lister-list")
    fin = tbody.find_all('tr')
    for t in fin:
        try:
            title = (t.find('td', class_="titleColumn")).find('a').get_text()
            rating = (t.find('td', class_="ratingColumn imdbRating")
                      ).find('strong').get_text()
            movieString = movieString+title+":"+rating+"\n"
        except:
            pass
    return movieString


def getTitleAndRatingAsList(url):
    movieList = []
    fullContent = BeautifulSoup(requests.get(url).content, 'html.parser')
    tbody = fullContent.find('tbody', class_="lister-list")
    fin = tbody.find_all('tr')
    for t in fin:
        try:
            title = (t.find('td', class_="titleColumn")).find('a').get_text()
            rating = (t.find('td', class_="ratingColumn imdbRating")
                      ).find('strong').get_text()
            movieList.append((title, rating))
        except:
            pass
    return movieList


fileWriteAsString = ""
fileWriteAsSet = set()
fileWriteAsSetString = ""

for i in range(len(urls)):
    fileWriteAsString = fileWriteAsString + getTitleAndRatingAsString(urls[i])
    tmp = getTitleAndRatingAsList(urls[i])
    for _ in tmp:
        fileWriteAsSet.add(_)

for tmp in fileWriteAsSet:
    fileWriteAsSetString = fileWriteAsSetString + str(tmp[0])+"#"+str(tmp[1])+"\n"

print(fileWriteAsSetString)
print(len(fileWriteAsSet))


def fileMaker():
    try:
        os.remove('C:\\movieListAndRating\\data.txt')
        os.rmdir("C:\\movieListAndRating\\")
    except:
        pass
    path = 'C:\\'
    os.chdir(path)
    os.makedirs('movieListAndRating')
    path = 'C:\\movieListAndRating\\'
    os.chdir(path)
    fileMaker = open(str("data.txt"), 'w')
    fileMaker.write(fileWriteAsSetString)
    fileMaker.close()


fileMaker()
