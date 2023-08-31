import pandas as pd
from bs4 import BeautifulSoup
import requests
import io

class HistoricalSalaryScrapper():
    def __init__(self, data_path='../data/'):
        self.data_path = data_path
        self.BASE_URL = "http://rotoguru1.com/cgi-bin/fyday.pl?game=GAME&scsv=1&week=WEEK&year=YEAR"
        self.YEARS_FD = list(map(str, range(2011, 2022)))
        self.YEARS_DK = list(map(str, range(2014, 2022)))
        self.YEARS_YH = list(map(str, range(2016, 2022)))
        self.WEEKS = list(map(str,range(1,18)))
        
    def get_historical_draftkings_data(self):
        df = pd.DataFrame()
        for yr in self.YEARS_DK:
            for wk in self.WEEKS:
                url = self.BASE_URL.replace("WEEK" ,wk).replace("YEAR" ,yr).replace("GAME","dk")
                doc=BeautifulSoup(requests.get(url).text, "html.parser")
                df = pd.concat([df, pd.read_csv(io.StringIO(doc.find_all('pre')[0].text),sep=';')])
        df.columns = df.columns.str.replace(' ',"_").str.lower()
        df = df[~df.dk_salary.isna()]
        df['team'] = df['team'].str.upper()
        df['oppt'] = df['oppt'].str.upper()
        df.reset_index(drop=True).to_pickle(self.data_path + 'draftkings_historical.pkl')
    
    def get_historical_fanduel_data(self):
        df = pd.DataFrame()
        for yr in self.YEARS_FD:
            for wk in self.WEEKS:
                url = self.BASE_URL.replace("WEEK" ,wk).replace("YEAR" ,yr).replace("GAME","fd")
                doc=BeautifulSoup(requests.get(url).text, "html.parser")
                df = pd.concat([df, pd.read_csv(io.StringIO(doc.find_all('pre')[0].text),sep=';')])
        df.columns = df.columns.str.replace(' ',"_").str.lower()
        df = df[~df.fd_salary.isna()]
        df['team'] = df['team'].str.upper()
        df['oppt'] = df['oppt'].str.upper()
        df.reset_index(drop=True).to_pickle(self.data_path + 'fanduel_historical.pkl')
    
    def get_historical_yahoo_data(self):
        df = pd.DataFrame()
        for yr in self.YEARS_FD:
            for wk in self.WEEKS:
                url = self.BASE_URL.replace("WEEK" ,wk).replace("YEAR" ,yr).replace("GAME","yh")
                doc=BeautifulSoup(requests.get(url).text, "html.parser")
                df = pd.concat([df, pd.read_csv(io.StringIO(doc.find_all('pre')[0].text),sep=';')])
        df.columns = df.columns.str.replace(' ',"_").str.lower()
        df = df[~df.yh_salary.isna()]
        df['team'] = df['team'].str.upper()
        df['oppt'] = df['oppt'].str.upper()
        df.reset_index(drop=True).to_pickle(self.data_path + 'yahoo_historical.pkl')