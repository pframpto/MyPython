#start by collecting weather from https://www.weatherzone.com.au/qld/brisbane/deception-bay 
#collect weather for Gold Coast, Brisbane, Deception Bay, Sydney, Canberra, and Melbourne
#After I have collected these values as variables write them to an Excel workbook in a sheet for the week of the year.

# Install modules
# pip install OpenPyXL
# pip install requests
# pip install beautifulsoup4

#Collect first temp
import bs4, requests, os, openpyxl

os.chdir('C:\\Users\\Administrator\\Documents\\MyPython\\weather_to_excel')
css_selector = '#top_obs_temp'


def getLocalTemp(bomUrl):
    
	res = requests.get(bomUrl)    
	res.raise_for_status()
    
	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elems = soup.select(css_selector)
    
	return elems[0].text.strip()

url = 'https://www.weatherzone.com.au/qld/brisbane/deception-bay'
dbay = getLocalTemp(url)
print(dbay)
url = 'https://www.weatherzone.com.au/qld/southeast-coast/coolangatta'
gc = getLocalTemp(url)
print(gc)
url = 'https://www.weatherzone.com.au/qld/brisbane/brisbane'
bne = getLocalTemp(url)
print(bne)
url = 'https://www.weatherzone.com.au/nsw/sydney/sydney'
syd = getLocalTemp(url)
print(syd)
url = 'https://www.weatherzone.com.au/act/act/canberra'
can = getLocalTemp(url)
print(can)
url = 'https://www.weatherzone.com.au/vic/melbourne/melbourne'
mlb = getLocalTemp(url)
print(mlb)

#Write to excel

wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = 'Gold Coast'
sheet['B1'] = gc
sheet['A2'] = 'Brisbane'
sheet['B2'] = bne
sheet['A3'] = 'Deception Bay'
sheet['B3'] = dbay
sheet['A4'] = 'Sydney'
sheet['B4'] = syd
sheet['A5'] = 'Canberra'
sheet['B5'] = can 
sheet['A6'] = 'Melbourne'
sheet['B6'] = mlb



wb.save('AustralianWeatherToday.xlsx')
