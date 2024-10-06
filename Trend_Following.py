import yfinance as yf
import pandas as pd
import datetime as dt

asset = 'TSLA'

intrday = yf.download(asset, start='2021-03-01' , end= '2021-03-02' , interval='1m')

# Remaber data is in one min intervel  

def myfun(df ,  entry , exit):
    # find interval till 120th colun of data 
    ret_120min  = df.iloc[120].Open/df.iloc[0].Open-1
    # find change in percentage
    tickret_ret = df.Open.pct_change()
    # if 
    if ret_120min > entry:
        buyprice = df.iloc[121].Open
        buytime = df.iloc[121].name
        # find the cumulated 
        cumulated_ret = (tickret_ret.loc[buytime:]+1).cumprod()-1
        # exit (booling indexing)
        exittime = cumulated_ret[(cumulated_ret< -exit) | (cumulated_ret>exit)].first_valid_index()
        if exittime == None:
                  exitprice  = df.ilco[-1].Open
        else:
            exitprice = df.loc[exitprice+ df.timedatla(minute=1)].Open
        profit  = exitprice-buyprice
        profit_relative  = profit/buyprice
        return profit_relative             

    else:
        return None    



myfun(intrday , 0.01, 0.01)       
