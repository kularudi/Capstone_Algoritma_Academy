# Web Scrapping using BeautifulSoup

## About
This set of Notebooks provides a complete set of code to be able scrap data from site using BeautifulSoup and deploy simple dashboard using Flask. This repository contains three project:
1. Scrap Ethereum trade data from [www.coingecko.com](https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-06-30#panel)
2. Scrap IDR-USD exchange rate data from [www.exchange-rates.com](https://www.exchange-rates.org/history/IDR/USD/T)
3. Scrap IMDb movie data from from [www.imdb.com](https://www.imdb.com/search/title/?release_date=2021-01-01,2021-12-31)

## Steps
**Step 1.** Clone this repository to your computer
<pre>
git clone https://github.com/kularudi/Capstone_Algoritma_Academy.git
</pre>

**Step 2.** Create a new virtual environments with Python 3.8
<pre>
# For venv
python -m venv webscrap python=3.8

# For conda
conda create --name webscrap python=3.8
</pre>

**Steps 3.** Activate your virtual environment
<pre>
# For venv
source webscrap/bin/activate # Linux
.\webscrap\Scripts\activate # Windows

# For conda
conda activate webscrap
</pre>

**Step 4.** Install dependencies and add virtual environment to Python kernel
<pre>
python -m pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=webscrap --display-name="Web Scrap"
</pre>

**Step 5.** Install requirements.txt
<pre>
# Navigate to Web_Scrapping
cd .\Data_Analytics\Web_Scrapping

# Install requirements.txt
pip install requirements.txt
</pre>

**Step 6.** Follow each step in each Notebook. Ensure you change the kernel to the "Web Scrap" virtual environment

## Contact
If you found any errors or have improvement, feel free to contact me via
- [contact@rudiharyanto.com](mailto:contact@rudiharyanto.com)
- [t.me/kularudi](https://t.me/kularudi)

Thanks
