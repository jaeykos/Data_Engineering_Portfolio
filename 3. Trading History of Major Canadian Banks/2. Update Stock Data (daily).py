from datetime import date
from datetime import timedelta
from datetime import datetime
import pandas as pd
from pandasql import sqldf
import gspread
import gspread_dataframe as gd
from oauth2client.service_account import ServiceAccountCredentials
import yfinance as yf

# access google sheet
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("stock-367302-c665cb9043f9.json", scope)
client = gspread.authorize(creds)
wb = client.open("Canadian Bank Stock Price 3yrs")  # access google sheet file with the name in quote

# set up lists for populating each Google sheet through loop
bankList = ["TD", "RB", "Scotia", "CIBC", "BMO", "NB"]  # tab names in Google sheet
tickerList = ["TD.TO", "RY.TO", "BNS.TO", "CM.TO", "BMO.TO", "NA.TO"]  # tickers of stocks for yfinance api

today = date.today() # today's date
strToday = today.strftime('%Y-%m-%d')  

# update each sheet
for bankName, ticker in zip(bankList, tickerList):

    sheet = wb.worksheet(bankName)
    last_row = len(sheet.col_values(1))  # last row in sheet
    lastDay = datetime.strptime(sheet.cell(last_row, 1).value, '%Y-%m-%d').date()  # date of last row
    dayAfterLastDay = lastDay + timedelta(days=1)  # 1 day after LastDay
    strDayAfterLastDay = dayAfterLastDay.strftime('%Y-%m-%d')  # convert to string for yfinance api

    # only update sheet if strToday is later than strDayAfterLastDay
    if today > dayAfterLastDay:

        # get stock information. yfinance returns pandas dataframe with Date as primary key
        bankData = yf.download(ticker, start=strDayAfterLastDay, end=strToday)

        # extract Date, Close and Volume columns. also filter dates as yfinance sometimes return earlier dates
        bankData = sqldf('SELECT date(Date) as Date, Close, Volume from bankData where Date >= \''
                         + strDayAfterLastDay + '\' ', globals())

        # covert dataframe to list of rows as gspread api cannot handle dataframe
        rowsToAppend = bankData.values.tolist()

        # append table
        sheet.append_rows(rowsToAppend)

        # delete the first rows; delete same number of new rows added
        sheet.delete_rows(2, 2 + len(rowsToAppend) - 1)
