from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('tbody')
items = table.find_all('tr')

items = table.find_all('tr')

# Initiating a tuple as container
temp = []

for i in range(0, len(items)):
    
    # Scrapping process
    item = items[i]
    date = item.find('th').text.strip()
    market_cap = item.find_all('td')[0].text.strip().replace('$', '').replace(',','')
    volume = item.find_all('td')[1].text.strip().replace('$', '').replace(',','')
    open = item.find_all('td')[2].text.strip().replace('$', '').replace(',','')
    close = item.find_all('td')[3].text.strip().replace('$', '').replace(',','')
    
    # Store every data in temp
    temp.append((date, market_cap, volume, open, close)) 

# Change order of temp
temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns=('Date', 'Market Cap', 'Volume', 'Open', 'Close'))

#insert data wrangling here
df.replace({'N/A':int('0')}, inplace=True)
df['Date'] = df['Date'].astype('datetime64')
df[['Market Cap', 'Volume', 'Open', 'Close']] = df[['Market Cap', 'Volume', 'Open', 'Close']].astype('float')
df = df.set_index('Date')
#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f"{round(df['Volume'].mean(),2):,}"

	# udah jadi tapi harus dihapus fungsi .round(2) nya 

	# generate plot
	ax = df['Volume'].plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)