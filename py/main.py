from historical_salary_scrapper import HistoricalSalaryScrapper

DATA_PATH = '../data/'

def main():
    histSalScrapper = HistoricalSalaryScrapper(data_path=DATA_PATH)
    histSalScrapper.get_historical_draftkings_data()
    histSalScrapper.get_historical_fanduel_data()
    histSalScrapper.get_historical_yahoo_data()
    
if __name__ == '__main__':
    main()