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

#set date variables of last updated date and tomorrow

wb = client.open("Canadian Bank Stock Price 3yrs") # access google sheet file with the name in quote
sheet = wb.worksheet("TD") #access the first sheet "TD" in the file
last_row = len(sheet.col_values(1)) # the last row in the sheet
strLastDay = sheet.cell(last_row, 1).value # the date of last row
LastDay = datetime.strptime(strLastDay, '%Y-%m-%d') #convert to datetime variable for date calculation
DayAfterLastDay = LastDay + timedelta(days = 1) #calculate 1 day after last date in table
strDayAfterLastDay = DayAfterLastDay.strftime('%Y-%m-%d') # convert to string (yfinance only takes string)
strToday = (date.today()).strftime('%Y-%m-%d') # today's date in string

# set up lists for populating each Google sheet through loop
bankList = ["TD", "RB", "Scotia", "CIBC", "BMO", "NB"]  # these are tab names in Google sheet
tickerList = ["TD.TO", "RY.TO", "BNS.TO", "CM.TO", "BMO.TO", "NA.TO"]  # these are tickers of stocks

# update each sheet
if strDayAfterLastDay != strToday: # if the dates are equal, that means table is already up-to-date
    for bankName, ticker in zip(bankList, tickerList):
        bankData = yf.download(ticker, start=strDayAfterLastDay, end=strToday)  # obtain stock information. yfinance returns pandas dataframe with Date as primary key
        bankData = sqldf('SELECT date(Date) as Date, Close, Volume from bankData', globals())  # only keep Date, Close and Volume columns

        sheet = wb.worksheet(bankName)  # access tab in Google sheet that correspond to bank name
        rowsToAppend = bankData.values.tolist()  # covert dataframe to list of rows as gspread api cannot handle dataframe
        sheet.append_rows(rowsToAppend) #append table
        sheet.delete_rows(2, 2 + len(rowsToAppend) - 1) # delete the first rows; delete same number of new rows added
