import urllib.request as req
from bs4 import BeautifulSoup
import os.path
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "C:/section4/forecast.xml"

if not os.path.exists(savename):
    req.urlretrieve(url, savename)

xml = open(savename, 'r', encoding= 'utf-8').read()
soup = BeautifulSoup(xml, 'html.parser')
info = {}

for location in soup.find_all("location"):
    loc = location.find("city").string
    #print(loc)
    weather = location.find_all("tmn")

    if not (loc in info):
        info[loc] = []
    for i in weather:
        info[loc].append(i.string)
#print(info)
with open('c:/section4/forecast.txt', 'wt') as f:
    for loc in sorted(info.keys()):
        print('+', loc)
        f.write(str(loc) + '\n')
        for n in info[loc]:
            print('-', n)
            f.write('\t' + str(n) + '\n')
