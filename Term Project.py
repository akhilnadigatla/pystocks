### Modules ###

# Citations:
# Animation Framework : 15-112 Course Website
# Random Point Generation: The Beginner Programmer Website

# Allow access to the Internet
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

# Mathematical libraries
import pandas
import numpy

# Website scraping libraries
import requests
from yahoo_fin import stock_info as si
from forex_python.converter import CurrencyRates
c = CurrencyRates()

# Time and date libraries
from datetime import datetime
from datetime import time
import ssl

# Image and animation libraries
from tkinter import *
from PIL import ImageTk
from PIL import Image
import tkinter as tk
import threading
import imageio

### Animation Setup ###

def init(data):    
    # Headings of columns in .csv files
    colnames1 = ["Date", "Time", "Open", "High", "Low", "Close", "Volume", "OpenInt"]
    colnames2 = ["Date", "Open", "High", "Low", "Close", "Decimal"]
    colnames3 = ["Scores"]
    
    data.scores = pandas.read_csv("Scores.csv", names = colnames3)
    
    # Exxon Data
    XOMdata = pandas.read_csv('xom.us.txt', names = colnames1)
    data.xom = list(map(float, XOMdata.Close.tolist()[1:902]))
    data.startXOM = 0
    data.endXOM = 0
    data.minXOM = min(data.xom)
    data.maxXOM = max(data.xom)
    data.lineSegmentsXOM = []
    data.XOMLive = [si.get_live_price("xom")]
    data.XOMLive.append(si.get_live_price("xom"))
    
    # JP Morgan data
    JPMdata = pandas.read_csv('jpm.us.txt', names = colnames1)
    data.jpm = list(map(float, JPMdata.Close.tolist()[1:902]))
    data.startJPM = 0
    data.endJPM = 0
    data.minJPM = min(data.jpm)
    data.maxJPM = max(data.jpm)
    data.lineSegmentsJPM = []
    data.JPMLive = [si.get_live_price("jpm")]
    
    # Boeing Data
    BAdata = pandas.read_csv('ba.us.txt', names = colnames1)
    data.ba = list(map(float, BAdata.Close.tolist()[1:902]))
    data.startBA = 0
    data.endBA = 0
    data.minBA = min(data.ba)
    data.maxBA = max(data.ba)
    data.lineSegmentsBA = []
    data.BALive = [si.get_live_price("ba")]
    
    # Google Data
    GOOGLdata = pandas.read_csv('googl.us.txt', names = colnames1)
    data.googl = list(map(float, GOOGLdata.Close.tolist()[1:902]))
    data.startGOOGL = 0
    data.endGOOGL = 0
    data.minGOOGL = min(data.googl)
    data.maxGOOGL = max(data.googl)
    data.lineSegmentsGOOGL = []
    data.GOOGLLive = [si.get_live_price("googl")]
    
    # Dinsey Data
    DISdata = pandas.read_csv('dis.us.txt', names = colnames1)
    data.dis = list(map(float, DISdata.Close.tolist()[1:902]))
    data.startDIS = 0
    data.endDIS = 0
    data.minDIS = min(data.dis)
    data.maxDIS = max(data.dis)
    data.lineSegmentsDIS = []
    data.DISLive = [si.get_live_price("dis")]
    
    # USD-EUR Data
    EURdata = pandas.read_csv('EUR-USD.csv', names = colnames2)
    data.eur = list(map(float, EURdata.Close.tolist()[1:902]))
    data.startEUR = 0
    data.endEUR = 0
    data.minEUR = 1 / max(data.eur)
    data.maxEUR = 1 / min(data.eur)
    data.lineSegmentsEUR = []
    data.EURLive = [c.get_rate("USD", "EUR")]
    data.EURLive.append(c.get_rate("USD", "EUR"))
    
    # USD-GBP Data
    GBPdata = pandas.read_csv('GBP-USD.csv', names = colnames2)
    data.gbp = list(map(float, GBPdata.Close.tolist()[1:902]))
    data.startGBP = 0
    data.endGBP = 0
    data.minGBP = 1 / max(data.gbp)
    data.maxGBP = 1 / min(data.gbp)
    data.lineSegmentsGBP= []
    data.GBPLive = [c.get_rate("USD", "GBP")]
    
    # USD-CAD Data
    CADdata = pandas.read_csv('USD-CAD.csv', names = colnames2)
    data.cad = list(map(float, CADdata.Close.tolist()[1:902]))
    data.startCAD = 0
    data.endCAD = 0
    data.minCAD = min(data.cad)
    data.maxCAD = max(data.cad)
    data.lineSegmentsCAD = []
    data.CADLive = [c.get_rate("USD", "CAD")]
    
    # USD-JPY Data
    JPYdata = pandas.read_csv('USD-JPY.csv', names = colnames2)
    data.jpy = list(map(float, JPYdata.Close.tolist()[1:902]))
    data.startJPY = 0
    data.endJPY = 0
    data.minJPY = min(data.jpy)
    data.maxJPY = max(data.jpy)
    data.lineSegmentsJPY = []
    data.JPYLive = [c.get_rate("USD", "JPY")]
    
    # USD-ZAR Data
    ZARdata = pandas.read_csv('USD-ZAR.csv', names = colnames2)
    data.zar = list(map(float, ZARdata.Close.tolist()[1:902]))
    data.startZAR = 0
    data.endZAR = 0
    data.minZAR = min(data.zar)
    data.maxZAR = max(data.zar)
    data.lineSegmentsZAR = []
    data.ZARLive = [c.get_rate("USD", "ZAR")]
    
    # Challenge Benchmark Data
    data.challengePoints1 = [100]
    data.challengePoints2 = [250]
    data.challengePoints3 = [500]
    data.challengePoints4 = [750]
    data.challengePoints5 = [1000]
    
    data.timer = 0
    data.remainingTime = 900
    data.dX = 1
    data.gameMode = "title"
   
    # Portfolio statistics for each game mode
    data.startMoney = 5000
    data.liquidMoney = 5000
    data.account = []
    data.portfolio = []
    data.exchange = {"EUR" : 0, "GBP" : 0, "CAD" : 0, "JPY" : 0, "ZAR" : 0}
    data.totalValue = 0
    data.stock = "XOM"
    data.forex = "EUR"
    data.challengeStock = "stock1"
    
    # Detals about current date and time
    data.now = datetime.now()
    data.hour = data.now.hour
    data.min = data.now.minute

# Determines whether NYSE is open on a given day
def isBusinessDay(date):
    return bool(len(pandas.bdate_range(date, date)))
    
# Determines whether NYSE is open at a given time
def isTimeBetween(start, end, current = None):
    current = current or datetime.utcnow().time()
    if start < end:
        return current >= start and current <= end
    else:
        return current >= start or current <= end

# Determines whether the stock is showing an upwards or downward trend
def getColor(startPrice, endPrice):
    if startPrice > endPrice:
        return "red"
    else:
        return "green"

# Resets all crucial variables upon completion of one round
def reset(data):
    data.remainingTime = 900
    data.timer = 0
    data.liquidMoney = 5000
    data.portfolio = []
    data.totalValue = 0
    data.lineSegmentsXOM = []
    data.lineSegmentsJPM = []
    data.lineSegmentsBA = []
    data.lineSegmentsGOOGL = []
    data.lineSegmentsDIS = []
    data.lineSegmentsEUR = []
    data.lineSegmentsGBP = []
    data.lineSegmentsCAD = []
    data.lineSegmentsJPY = []
    data.lineSegmentsYEN = []
    data.account = []
    data.challengePoints1 = [100]
    data.challengePoints2 = [250]
    data.challengePoints3 = [500]
    data.challengePoints4 = [750]
    data.challengePoints5 = [1000]
    data.XOMLive = [si.get_live_price("xom")]
    data.XOMLive.append(si.get_live_price("xom"))
    data.JPMLive = [si.get_live_price("jpm")]
    data.BALive = [si.get_live_price("ba")]
    data.GOOGLLive = [si.get_live_price("googl")]
    data.DISLive = [si.get_live_price("dis")]
    data.EURLive = [c.get_rate("USD", "EUR")]
    data.EURLive.append(c.get_rate("USD", "EUR"))
    data.GBPLive = [c.get_rate("USD", "GBP")]
    data.CADLive = [c.get_rate("USD", "CAD")]
    data.JPYLive = [c.get_rate("USD", "JPY")]
    data.ZARLive = [c.get_rate("USD", "ZAR")]

# Generates random prices for the 'Challenge' section
def getNewPrice(previousPrice, mean = 0.1, stdev = 2):
    probability = numpy.random.normal(0, 1, 1)
    newPrice = previousPrice + previousPrice * (mean / 255 + stdev / numpy.sqrt(225) * probability)
    return float(newPrice)
    
def mousePressed(event, data):
    # TITLE SCREEN SELECTION
    if data.gameMode == "title":
        if 2 * (data.width / 20) <= event.x <= 6 * (data.width / 20) and 10 * (data.height / 14) <= event.y <= 11 * (data.height / 14):
            data.gameMode = "tips"
        elif 8 * (data.width / 20) <= event.x <= 12 * (data.width / 20) and 10 * (data.height / 14) <= event.y <= 11 * (data.height / 14):
            data.gameMode = "stocks"
        elif 14 * (data.width / 20) <= event.x <= 18 * (data.width / 20) and 10 * (data.height / 14) <= event.y <= 11 * (data.height / 14):
            data.gameMode = "currency"
        elif 5 * (data.width / 20) <= event.x <= 9 * (data.width / 20) and 12 * (data.height / 14) <= event.y <= 13 * (data.height / 14):
            data.gameMode = "tutorial"
        elif 11 * (data.width / 20) <= event.x <= 15 * (data.width / 20) and 12 * (data.height / 14) <= event.y <= 13 * (data.height / 14):
            data.gameMode = "challenge"
    
    # TIPS SCREEN SELECTION
    elif data.gameMode == "tips":
        if 1 * (data.width / 20) <= event.x <= 3 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            data.gameMode = "title"
    
    # STOCK SIMULATOR SCREEN SELECTION
    elif data.gameMode == "stocks":
        if 9 * (data.width / 20) <= event.x <= 11 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.stock = "XOM"
        elif 11 * (data.width / 20) <= event.x <= 13 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.stock = "JPM" 
        elif 13 * (data.width / 20) <= event.x <= 15 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.stock = "BA" 
        elif 15 * (data.width / 20) <= event.x <= 17 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.stock = "GOOGL" 
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.stock = "DIS" 
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            data.gameMode = "stockSummary"
        elif 14 * (data.width / 20) <= event.x <= 16 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            reset(data)
            data.gameMode = "title"
            
    # STOCK SIMULATOR SUMMARY SCREEN SELECTION
    elif data.gameMode == "stockSummary":
        if 14 * (data.width / 20) <= event.x <= 16 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            reset(data)
            data.gameMode = "stocks"
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            reset(data)
            data.gameMode = "title"
    
    # FOREX SIMULATOR SCREEN SELECTION
    elif data.gameMode == "currency":
        if 9 * (data.width / 20) <= event.x <= 11 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.forex = "EUR"
        elif 11 * (data.width / 20) <= event.x <= 13 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.forex = "GBP"
        elif 13 * (data.width / 20) <= event.x <= 15 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.forex = "CAD"
        elif 15 * (data.width / 20) <= event.x <= 17 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.forex = "JPY" 
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.forex = "ZAR"
        
        # Buy a currency in 50, 100, 500, and 1000 denominations
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 1.5 * (data.height / 14):
            if data.forex == "EUR":
                if data.liquidMoney >= 50 / data.startEUR:
                    data.exchange["EUR"] += 50
                    data.liquidMoney -= 50 / data.startEUR
            elif data.forex == "GBP":
                if data.liquidMoney >= 50 / data.startGBP:
                    data.exchange["GBP"] += 50
                    data.liquidMoney -= 50 / data.startGBP
            elif data.forex == "CAD":
                if data.liquidMoney >= 50 / data.startCAD:
                    data.exchange["CAD"] += 50
                    data.liquidMoney -= 50 / data.startCAD
            elif data.forex == "JPY":
                if data.liquidMoney >= 50 / data.startJPY:
                    data.exchange["JPY"] += 50
                    data.liquidMoney -= 50 / data.startJPY
            elif data.forex == "ZAR":
                if data.liquidMoney >= 50 / data.startZAR:
                    data.exchange["ZAR"] += 50
                    data.liquidMoney -= 50 / data.startZAR
        
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 1.5 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            if data.forex == "EUR":
                if data.liquidMoney >= 100 / data.startEUR:
                    data.exchange["EUR"] += 100
                    data.liquidMoney -= 100 / data.startEUR
            elif data.forex == "GBP":
                if data.liquidMoney >= 100 / data.startGBP:
                    data.exchange["GBP"] += 100
                    data.liquidMoney -= 100 / data.startGBP
            elif data.forex == "CAD":
                if data.liquidMoney >= 100 / data.startCAD:
                    data.exchange["CAD"] += 100
                    data.liquidMoney -= 100 / data.startCAD
            elif data.forex == "JPY":
                if data.liquidMoney >= 100 / data.startJPY:
                    data.exchange["JPY"] += 100
                    data.liquidMoney -= 100 / data.startJPY
            elif data.forex == "ZAR":
                if data.liquidMoney >= 100 / data.startZAR:
                    data.exchange["ZAR"] += 100
                    data.liquidMoney -= 100 / data.startZAR
                    
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 2 * (data.height / 14) <= event.y <= 2.5 * (data.height / 14):
            if data.forex == "EUR":
                if data.liquidMoney >= 500 / data.startEUR:
                    data.exchange["EUR"] += 500
                    data.liquidMoney -= 500 / data.startEUR
            elif data.forex == "GBP":
                if data.liquidMoney >= 500 / data.startGBP:
                    data.exchange["GBP"] += 500
                    data.liquidMoney -= 500 / data.startGBP
            elif data.forex == "CAD":
                if data.liquidMoney >= 500 / data.startCAD:
                    data.exchange["CAD"] += 500
                    data.liquidMoney -= 500 / data.startCAD
            elif data.forex == "JPY":
                if data.liquidMoney >= 500 / data.startJPY:
                    data.exchange["JPY"] += 500
                    data.liquidMoney -= 500 / data.startJPY
            elif data.forex == "ZAR":
                if data.liquidMoney >= 500 / data.startZAR:
                    data.exchange["ZAR"] += 500
                    data.liquidMoney -= 500 / data.startZAR
                    
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 2.5 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            if data.forex == "EUR":
                if data.liquidMoney >= 1000 / data.startEUR:
                    data.exchange["EUR"] += 1000
                    data.liquidMoney -= 1000 / data.startEUR
            elif data.forex == "GBP":
                if data.liquidMoney >= 1000 / data.startGBP:
                    data.exchange["GBP"] += 1000
                    data.liquidMoney -= 1000 / data.startGBP
            elif data.forex == "CAD":
                if data.liquidMoney >= 1000 / data.startCAD:
                    data.exchange["CAD"] += 1000
                    data.liquidMoney -= 1000 / data.startCAD
            elif data.forex == "JPY":
                if data.liquidMoney >= 1000 / data.startJPY:
                    data.exchange["JPY"] += 1000
                    data.liquidMoney -= 1000 / data.startJPY
            elif data.forex == "ZAR":
                if data.liquidMoney >= 1000 / data.startZAR:
                    data.exchange["ZAR"] += 1000
                    data.liquidMoney -= 1000 / data.startZAR
        
        # Sell a currency in 50, 100, 500, and 1000 denominations
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 3 * (data.height / 14) <= event.y <= 3.5 * (data.height / 14):
            if data.forex == "EUR":
                if data.exchange["EUR"] >= 50:
                    data.liquidMoney += 50 / data.startEUR
                    data.exchange["EUR"] -= 50
            elif data.forex == "GBP":
                if data.exchange["GBP"] >= 50:
                    data.liquidMoney += 50 / data.startGBP
                    data.exchange["GBP"] -= 50
            elif data.forex == "CAD":
                if data.exchange["CAD"] >= 50:
                    data.liquidMoney += 50 / data.startCAD
                    data.exchange["CAD"] -= 50
            elif data.forex == "JPY":
                if data.exchange["JPY"] >= 50:
                    data.liquidMoney += 50 / data.startJPY
                    data.exchange["JPY"] -= 50
            elif data.forex == "ZAR":
                if data.exchange["ZAR"] >= 50:
                    data.liquidMoney += 50 / data.startZAR
                    data.exchange["ZAR"] -= 50
        
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 3.5 * (data.height / 14) <= event.y <= 4 * (data.height / 14):
            if data.forex == "EUR":
                if data.exchange["EUR"] >= 100:
                    data.liquidMoney += 100 / data.startEUR
                    data.exchange["EUR"] -= 100
            elif data.forex == "GBP":
                if data.exchange["GBP"] >= 100:
                    data.liquidMoney += 100 / data.startGBP
                    data.exchange["GBP"] -= 100
            elif data.forex == "CAD":
                if data.exchange["CAD"] >= 100:
                    data.liquidMoney += 100 / data.startCAD
                    data.exchange["CAD"] -= 100
            elif data.forex == "JPY":
                if data.exchange["JPY"] >= 100:
                    data.liquidMoney += 100 / data.startJPY
                    data.exchange["JPY"] -= 100
            elif data.forex == "ZAR":
                if data.exchange["ZAR"] >= 100:
                    data.liquidMoney += 100 / data.startZAR
                    data.exchange["ZAR"] -= 100
        
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 4.5 * (data.height / 14):
            if data.forex == "EUR":
                if data.exchange["EUR"] >= 500:
                    data.liquidMoney += 500 / data.startEUR
                    data.exchange["EUR"] -= 500
            elif data.forex == "GBP":
                if data.exchange["GBP"] >= 500:
                    data.liquidMoney += 500 / data.startGBP
                    data.exchange["GBP"] -= 500
            elif data.forex == "CAD":
                if data.exchange["CAD"] >= 500:
                    data.liquidMoney += 500 / data.startCAD
                    data.exchange["CAD"] -= 500
            elif data.forex == "JPY":
                if data.exchange["JPY"] >= 500:
                    data.liquidMoney += 500 / data.startJPY
                    data.exchange["JPY"] -= 500
            elif data.forex == "ZAR":
                if data.exchange["ZAR"] >= 500:
                    data.liquidMoney += 500 / data.startZAR
                    data.exchange["ZAR"] -= 500
        
        elif 6 * (data.width / 20) <= event.x <= 8 * (data.width / 20) and 4.5 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            if data.forex == "EUR":
                if data.exchange["EUR"] >= 1000:
                    data.liquidMoney += 1000 / data.startEUR
                    data.exchange["EUR"] -= 1000
            elif data.forex == "GBP":
                if data.exchange["GBP"] >= 1000:
                    data.liquidMoney += 1000 / data.startGBP
                    data.exchange["GBP"] -= 1000
            elif data.forex == "CAD":
                if data.exchange["CAD"] >= 1000:
                    data.liquidMoney += 1000 / data.startCAD
                    data.exchange["CAD"] -= 1000
            elif data.forex == "JPY":
                if data.exchange["JPY"] >= 1000:
                    data.liquidMoney += 1000 / data.startJPY
                    data.exchange["JPY"] -= 1000
            elif data.forex == "ZAR":
                if data.exchange["ZAR"] >= 1000:
                    data.liquidMoney += 1000 / data.startZAR
                    data.exchange["ZAR"] -= 1000

        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            data.gameMode = "currencySummary"
        elif 14 * (data.width / 20) <= event.x <= 16 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            reset(data)
            data.gameMode = "title"
    
    # FOREX SIMULATOR SUMMARY SCREEN SELECTION
    elif data.gameMode == "currencySummary":
        if 14 * (data.width / 20) <= event.x <= 16 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            reset(data)
            data.gameMode = "currency"
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            reset(data)
            data.gameMode = "title"

    # TUTORIAL SCREEN SELECTION
    elif data.gameMode == "tutorial":
        if 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 12 * (data.height / 14) <= event.y <= 13 * (data.height / 14):
            data.gameMode = "title"
    
    # CHALLENGE SCREEN SELECTION
    elif data.gameMode == "challenge":
        if 9 * (data.width / 20) <= event.x <= 11 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.challengeStock = "stock1"
        elif 11 * (data.width / 20) <= event.x <= 13 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.challengeStock = "stock2"
        elif 13 * (data.width / 20) <= event.x <= 15 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.challengeStock = "stock3"
        elif 15 * (data.width / 20) <= event.x <= 17 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.challengeStock = "stock4"
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 3 * (data.height / 14):
            data.challengeStock = "stock5"
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            data.gameMode = "challengeSummary"
        elif 14 * (data.width / 20) <= event.x <= 16 * (data.width / 20) and 4 * (data.height / 14) <= event.y <= 5 * (data.height / 14):
            reset(data)
            data.gameMode = "title"
    
    # CHALLENGE SUMMARY SCREEN SELECTION
    elif data.gameMode == "challengeSummary":
        if 14 * (data.width / 20) <= event.x <= 16 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            reset(data)
            data.gameMode = "challenge"
        elif 17 * (data.width / 20) <= event.x <= 19 * (data.width / 20) and 1 * (data.height / 14) <= event.y <= 2 * (data.height / 14):
            reset(data)
            data.gameMode = "title"
        
def keyPressed(event, data):
    if data.gameMode == "stocks":
        # Buy stock when up arrow is hit
        if event.keysym == "Up":
            if data.stock == "XOM":
                if data.startXOM <= data.liquidMoney:
                    data.portfolio.append("XOM")
                    data.liquidMoney -= data.startXOM
            elif data.stock == "JPM":
                if data.startJPM <= data.liquidMoney:
                    data.portfolio.append("JPM")
                    data.liquidMoney -= data.startJPM
            elif data.stock == "BA":
                if data.startBA <= data.liquidMoney:
                    data.portfolio.append("BA")
                    data.liquidMoney -= data.startBA
            elif data.stock == "GOOGL":
                if data.startGOOGL <= data.liquidMoney:
                    data.portfolio.append("GOOGL")
                    data.liquidMoney -= data.startGOOGL
            elif data.stock == "DIS":
                if data.startDIS <= data.liquidMoney:
                    data.portfolio.append("DIS")
                    data.liquidMoney -= data.startDIS
        
        # Sell stock when down arrow is hit
        if event.keysym == "Down":
            if data.stock == "XOM":
                if data.portfolio.count("XOM") > 0:
                    data.portfolio.remove("XOM")
                    data.liquidMoney += data.startXOM
            elif data.stock == "JPM":
                if data.portfolio.count("JPM") > 0:
                    data.portfolio.remove("JPM")
                    data.liquidMoney += data.startJPM
            elif data.stock == "BA":
                if data.portfolio.count("BA") > 0:
                    data.portfolio.remove("BA")
                    data.liquidMoney += data.startBA
            elif data.stock == "GOOGL":
                if data.portfolio.count("GOOGL") > 0:
                    data.portfolio.remove("GOOGL")
                    data.liquidMoney += data.startGOOGL
            elif data.stock == "DIS":
                if data.portfolio.count("DIS") > 0:
                    data.portfolio.remove("DIS")
                    data.liquidMoney += data.startDIS
                    
    if data.gameMode == "challenge":
        # Buy stock when up arrow is hit
        if event.keysym == "Up":
            if data.challengeStock == "stock1":
                if data.challengePoints1[-2] <= data.liquidMoney:
                    data.account.append("stock1")
                    data.liquidMoney -= data.challengePoints1[-2]
            elif data.challengeStock == "stock2":
                if data.challengePoints2[-2] <= data.liquidMoney:
                    data.account.append("stock2")
                    data.liquidMoney -= data.challengePoints2[-2]
            elif data.challengeStock == "stock3":
                if data.challengePoints3[-2] <= data.liquidMoney:
                    data.account.append("stock3")
                    data.liquidMoney -= data.challengePoints3[-2]
            elif data.challengeStock == "stock4":
                if data.challengePoints4[-2] <= data.liquidMoney:
                    data.account.append("stock4")
                    data.liquidMoney -= data.challengePoints4[-2]
            elif data.challengeStock == "stock5":
                if data.challengePoints5[-2] <= data.liquidMoney:
                    data.account.append("stock5")
                    data.liquidMoney -= data.challengePoints5[-2]
        
        # Sell stock when down arrow is hit
        if event.keysym == "Down":
            if data.challengeStock == "stock1":
                if data.account.count("stock1") > 0:
                    data.account.remove("stock1")
                    data.liquidMoney += data.challengePoints1[-2]
            elif data.challengeStock == "stock2":
                if data.account.count("stock2") > 0:
                    data.account.remove("stock2")
                    data.liquidMoney += data.challengePoints2[-2]
            elif data.challengeStock == "stock3":
                if data.account.count("stock3") > 0:
                    data.account.remove("stock3")
                    data.liquidMoney += data.challengePoints3[-2]
            elif data.challengeStock == "stock4":
                if data.account.count("stock4") > 0:
                    data.account.remove("stock4")
                    data.liquidMoney += data.challengePoints4[-2]
            if data.challengeStock == "stock5":
                if data.account.count("stock5") > 0:
                    data.account.remove("stock5")
                    data.liquidMoney += data.challengePoints5[-2]

def timerFired(data):
    if data.gameMode == "stocks":
        data.remainingTime -= 1
        data.timer += 1
        
        # Determine whether to use live or historic data
        if isBusinessDay(data.now) == False or isTimeBetween(time(9, 30), time(16, 0), time(data.hour, data.min)) == False or data.XOMLive[0] == data.XOMLive[1]:
            try:
                data.startXOM = (data.xom[data.timer - 1])
                data.endXOM = (data.xom[data.timer])
            except IndexError:
                data.endXOM = 0
            x1XOM = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1XOM = 13 * (data.height / 14) - ((data.startXOM - data.minXOM) / (data.maxXOM - data.minXOM) * 7 * (data.height / 14))
            x2XOM = 1 * (data.width / 20) + data.dX * data.timer
            y2XOM = 13 * (data.height / 14) - ((data.endXOM - data.minXOM) / (data.maxXOM - data.minXOM) * 7 * (data.height / 14))
            x3XOM = 1 * (data.width / 20) + data.dX * data.timer
            y3XOM = 13 * (data.height / 14)
            data.lineSegmentsXOM.append((x1XOM, y1XOM, x2XOM, y2XOM, x3XOM, y3XOM))
            
            try:
                data.startJPM = (data.jpm[data.timer - 1])
                data.endJPM = (data.jpm[data.timer])
            except IndexError:
                data.endJPM = 0
            x1JPM = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1JPM = 13 * (data.height / 14) - ((data.startJPM - data.minJPM) / (data.maxJPM - data.minJPM) * 7 * (data.height / 14))
            x2JPM = 1 * (data.width / 20) + data.dX * data.timer
            y2JPM = 13 * (data.height / 14) - ((data.endJPM - data.minJPM) / (data.maxJPM - data.minJPM) * 7 * (data.height / 14))
            x3JPM = 1 * (data.width / 20) + data.dX * data.timer
            y3JPM = 13 * (data.height / 14)
            data.lineSegmentsJPM.append((x1JPM, y1JPM, x2JPM, y2JPM, x3JPM, y3JPM))
            
            try:
                data.startBA = (data.ba[data.timer - 1])
                data.endBA = (data.ba[data.timer])
            except IndexError:
                data.endBA = 0
            x1BA = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1BA = 13 * (data.height / 14) - ((data.startBA - data.minBA) / (data.maxBA - data.minBA) * 7 * (data.height / 14))
            x2BA = 1 * (data.width / 20) + data.dX * data.timer
            y2BA = 13 * (data.height / 14) - ((data.endBA - data.minBA) / (data.maxBA - data.minBA) * 7 * (data.height / 14))
            x3BA = 1 * (data.width / 20) + data.dX * data.timer
            y3BA = 13 * (data.height / 14)
            data.lineSegmentsBA.append((x1BA, y1BA, x2BA, y2BA, x3BA, y3BA))
            
            try:
                data.startGOOGL = (data.googl[data.timer - 1])
                data.endGOOGL = (data.googl[data.timer])
            except IndexError:
                data.endGOOGL = 0
            x1GOOGL = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1GOOGL = 13 * (data.height / 14) - ((data.startGOOGL - data.minGOOGL) / (data.maxGOOGL - data.minGOOGL) * 7 * (data.height / 14))
            x2GOOGL = 1 * (data.width / 20) + data.dX * data.timer
            y2GOOGL = 13 * (data.height / 14) - ((data.endGOOGL - data.minGOOGL) / (data.maxGOOGL - data.minGOOGL) * 7 * (data.height / 14))
            x3GOOGL = 1 * (data.width / 20) + data.dX * data.timer
            y3GOOGL = 13 * (data.height / 14)
            data.lineSegmentsGOOGL.append((x1GOOGL, y1GOOGL, x2GOOGL, y2GOOGL, x3GOOGL, y3GOOGL))
        
            try:
                data.startDIS = (data.dis[data.timer - 1])
                data.endDIS = (data.dis[data.timer])
            except IndexError:
                data.endDIS = 0
            x1DIS = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1DIS = 13 * (data.height / 14) - ((data.startDIS - data.minDIS) / (data.maxDIS - data.minDIS) * 7 * (data.height / 14))
            x2DIS = 1 * (data.width / 20) + data.dX * data.timer
            y2DIS = 13 * (data.height / 14) - ((data.endDIS - data.minDIS) / (data.maxDIS - data.minDIS) * 7 * (data.height / 14))
            x3DIS = 1 * (data.width / 20) + data.dX * data.timer
            y3DIS = 13 * (data.height / 14)
            data.lineSegmentsDIS.append((x1DIS, y1DIS, x2DIS, y2DIS, x3DIS, y3DIS))
        
        else:
            data.XOMLive.append(si.get_live_price("xom"))
            data.startXOM = data.XOMLive[-2]
            data.endXOM = data.XOMLive[-1]
            
            data.JPMLive.append(si.get_live_price("jpm"))
            data.startJPM = data.JPMLive[-2]
            data.endJPM = data.JPMLive[-1]
            
            data.BALive.append(si.get_live_price("ba"))
            data.startBA = data.BALive[-2]
            data.endBA = data.BALive[-1]
            
            data.GOOGLLive.append(si.get_live_price("googl"))
            data.startGOOGL = data.GOOGLLive[-2]
            data.endGOOGL = data.GOOGLLive[-1]
            
            data.DISLive.append(si.get_live_price("dis"))
            data.startDIS = data.DISLive[-2]
            data.endDIS = data.DISLive[-1]
            
        if data.remainingTime == 0:
            data.gameMode = "stockSummary"
        
        # Calculate total value at any given time
        XOMvalue = data.portfolio.count("XOM") * data.startXOM
        JPMvalue = data.portfolio.count("JPM") * data.startJPM
        BAvalue = data.portfolio.count("BA") * data.startBA
        GOOGLvalue = data.portfolio.count("GOOGL") * data.startGOOGL
        DISvalue = data.portfolio.count("DIS") * data.startDIS
        data.totalValue = round(XOMvalue + JPMvalue + BAvalue + GOOGLvalue + DISvalue, 2)
    
    elif data.gameMode == "currency":
        data.remainingTime -= 1
        data.timer += 1
        
        # Determine whether to use live or historic data
        if isBusinessDay(data.now) == False or isTimeBetween(time(9, 30), time(16, 0), time(data.hour, data.min)) == False or data.EURLive[0] == data.EURLive[1]:
            try:
                data.startEUR = 1 / (data.eur[data.timer - 1])
                data.endEUR = 1 / (data.eur[data.timer])
            except IndexError:
                data.endEUR = 0
            x1EUR = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1EUR = 13 * (data.height / 14) - ((data.startEUR - data.minEUR) / (data.maxEUR - data.minEUR) * 7 * (data.height / 14))
            x2EUR = 1 * (data.width / 20) + data.dX * data.timer
            y2EUR = 13 * (data.height / 14) - ((data.endEUR - data.minEUR) / (data.maxEUR - data.minEUR) * 7 * (data.height / 14))
            x3EUR = 1 * (data.width / 20) + data.dX * data.timer
            y3EUR = 13 * (data.height / 14)
            data.lineSegmentsEUR.append((x1EUR, y1EUR, x2EUR, y2EUR, x3EUR, y3EUR))
            
            try:
                data.startGBP = 1 / (data.gbp[data.timer - 1])
                data.endGBP = 1 / (data.gbp[data.timer])
            except IndexError:
                data.endGBP = 0
            x1GBP = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1GBP = 13 * (data.height / 14) - ((data.startGBP - data.minGBP) / (data.maxGBP - data.minGBP) * 7 * (data.height / 14))
            x2GBP = 1 * (data.width / 20) + data.dX * data.timer
            y2GBP = 13 * (data.height / 14) - ((data.endGBP - data.minGBP) / (data.maxGBP - data.minGBP) * 7 * (data.height / 14))
            x3GBP = 1 * (data.width / 20) + data.dX * data.timer
            y3GBP = 13 * (data.height / 14)
            data.lineSegmentsGBP.append((x1GBP, y1GBP, x2GBP, y2GBP, x3GBP, y3GBP))
            
            try:
                data.startCAD = (data.cad[data.timer - 1])
                data.endCAD = (data.cad[data.timer])
            except IndexError:
                data.endCAD = 0
            x1CAD = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1CAD = 13 * (data.height / 14) - ((data.startCAD - data.minCAD) / (data.maxCAD - data.minCAD) * 7 * (data.height / 14))
            x2CAD = 1 * (data.width / 20) + data.dX * data.timer
            y2CAD = 13 * (data.height / 14) - ((data.endCAD - data.minCAD) / (data.maxCAD - data.minCAD) * 7 * (data.height / 14))
            x3CAD = 1 * (data.width / 20) + data.dX * data.timer
            y3CAD = 13 * (data.height / 14)
            data.lineSegmentsCAD.append((x1CAD, y1CAD, x2CAD, y2CAD, x3CAD, y3CAD))
            
            try:
                data.startJPY = (data.jpy[data.timer - 1])
                data.endJPY = (data.jpy[data.timer])
            except IndexError:
                data.endJPY = 0
            x1JPY = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1JPY = 13 * (data.height / 14) - ((data.startJPY - data.minJPY) / (data.maxJPY - data.minJPY) * 7 * (data.height / 14))
            x2JPY = 1 * (data.width / 20) + data.dX * data.timer
            y2JPY = 13 * (data.height / 14) - ((data.endJPY - data.minJPY) / (data.maxJPY - data.minJPY) * 7 * (data.height / 14))
            x3JPY = 1 * (data.width / 20) + data.dX * data.timer
            y3JPY = 13 * (data.height / 14)
            data.lineSegmentsJPY.append((x1JPY, y1JPY, x2JPY, y2JPY, x3JPY, y3JPY))
            
            try:
                data.startZAR = (data.zar[data.timer - 1])
                data.endZAR = (data.zar[data.timer])
            except IndexError:
                data.endZAR = 0
            x1ZAR = 1 * (data.width / 20) + data.dX * (data.timer - 1)
            y1ZAR = 13 * (data.height / 14) - ((data.startZAR - data.minZAR) / (data.maxZAR - data.minZAR) * 7 * (data.height / 14))
            x2ZAR = 1 * (data.width / 20) + data.dX * data.timer
            y2ZAR = 13 * (data.height / 14) - ((data.endZAR - data.minZAR) / (data.maxZAR - data.minZAR) * 7 * (data.height / 14))
            x3ZAR = 1 * (data.width / 20) + data.dX * data.timer
            y3ZAR = 13 * (data.height / 14)
            data.lineSegmentsZAR.append((x1ZAR, y1ZAR, x2ZAR, y2ZAR, x3ZAR, y3ZAR))
            
        else:
            data.EURLive.append(c.get_rate("USD", "EUR"))
            data.startEUR = data.EURLive[-2]
            data.endEUR = data.EURLive[-1]
            
            data.GBPLive.append(c.get_rate("USD", "GBP"))
            data.startGBP = data.GBPLive[-2]
            data.endGBP = data.GBPLive[-1]
            
            data.CADLive.append(c.get_rate("USD", "CAD"))
            data.startCAD = data.CADLive[-2]
            data.endCAD = data.CADLive[-1]
            
            data.JPYLive.append(c.get_rate("USD", "JPY"))
            data.startJPY = data.JPYLive[-2]
            data.endJPY = data.JPYLive[-1]
            
            data.ZARLive.append(c.get_rate("USD", "ZAR"))
            data.startZAR = data.ZARLive[-2]
            data.endZAR = data.ZARLive[-1]
            
        if data.remainingTime == 0:
            data.gameMode = "currencySummary"
        
        # Calculate total value at any given time
        EURvalue = data.exchange["EUR"] * (1 / data.startEUR)
        GBPvalue = data.exchange["GBP"] * (1 / data.startGBP)
        CADvalue = data.exchange["CAD"] * (1 / data.startCAD)
        JPYvalue = data.exchange["JPY"] * (1 / data.startJPY)
        ZARvalue = data.exchange["ZAR"] * (1 / data.startZAR)
        data.totalValue = round(EURvalue + GBPvalue + CADvalue + JPYvalue + ZARvalue, 2)
    
    elif data.gameMode == "challenge":
        data.remainingTime -= 1
        data.timer += 1
        
        newPrice1 = getNewPrice(data.challengePoints1[-1])
        data.challengePoints1.append(newPrice1)
        
        newPrice2 = getNewPrice(data.challengePoints2[-1])
        data.challengePoints2.append(newPrice2)
        
        newPrice3 = getNewPrice(data.challengePoints3[-1])
        data.challengePoints3.append(newPrice3)
        
        newPrice4 = getNewPrice(data.challengePoints4[-1])
        data.challengePoints4.append(newPrice4)
        
        newPrice5 = getNewPrice(data.challengePoints5[-1])
        data.challengePoints5.append(newPrice5)
        
        if data.remainingTime == 0:
            data.gameMode = "challengeSummary"
            
        # Calculate total value at any given time
        ONEvalue = data.account.count("stock1") * data.challengePoints1[-1]
        TWOvalue = data.account.count("stock2") * data.challengePoints2[-1]
        THREEvalue = data.account.count("stock3") * data.challengePoints3[-1]
        FOURvalue = data.account.count("stock4") * data.challengePoints4[-1]
        FIVEvalue = data.account.count("stock5") * data.challengePoints5[-1]
        data.totalValue = round(ONEvalue + TWOvalue + THREEvalue + FOURvalue + FIVEvalue, 2)
            
def redrawAll(canvas, data):
    if data.gameMode == "title":
        # BACKGROUND
        background = Image.open('Title Background.jpg')
        canvas.background = ImageTk.PhotoImage(background)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.background)
        
        # LOGO
        logo = Image.open('Title Logo.png')
        canvas.logo = ImageTk.PhotoImage(logo)
        canvas.create_image(10 * (data.width / 20), 4 * (data.height / 14), image = canvas.logo)
        
        # BUTTONS
        tradingTips = Image.open('button_trading-tips.png')
        canvas.tradingTips = ImageTk.PhotoImage(tradingTips)
        canvas.create_image(2 * (data.width / 20), 10 * (data.height / 14), image = canvas.tradingTips, anchor = "nw")
        
        stockTrading = Image.open('button_stock-trading.png')
        canvas.stockTrading = ImageTk.PhotoImage(stockTrading)
        canvas.create_image(8 * (data.width / 20), 10 * (data.height / 14), image = canvas.stockTrading, anchor = "nw")
        
        forexTrading = Image.open('button_forex-trading.png')
        canvas.forexTrading = ImageTk.PhotoImage(forexTrading)
        canvas.create_image(14 * (data.width / 20), 10 * (data.height / 14), image = canvas.forexTrading, anchor = "nw")
        
        tutorial = Image.open('button_tutorial.png')
        canvas.tutorial = ImageTk.PhotoImage(tutorial)
        canvas.create_image(5 * (data.width / 20), 12 * (data.height / 14), image = canvas.tutorial, anchor = "nw")
        
        challenge = Image.open('button_challenge.png')
        canvas.challenge = ImageTk.PhotoImage(challenge)
        canvas.create_image(11 * (data.width / 20), 12 * (data.height / 14), image = canvas.challenge, anchor = "nw")
    
    elif data.gameMode == "stocks":
        # BACKGROUND
        image = Image.open('Stock Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # SUMMARY SPACE
        canvas.create_rectangle(1 * (data.width / 20), 1 * (data.height / 14), 8 * (data.width / 20), 5 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 1.5 * (data.height / 14), text = "Liquid Money: " + str(round(data.liquidMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 2.5 * (data.height / 14), text = "Total Portfolio Value: " + str(round(data.totalValue, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Net Profit/Loss: " + str(round(data.totalValue - data.startMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.5 * (data.height / 14), text = "Profit/Loss Multiplier: " + str(round(data.totalValue / data.startMoney, 3)), font = "Helvetica 14", anchor = "w")
        
        # TIMER
        canvas.create_rectangle(9 * (data.width / 20), 4 * (data.height / 14), 12 * (data.width / 20), 5 * (data.height / 14), fill = "white")
        canvas.create_text(10.5 * (data.width / 20), 4.5 * (data.height / 14), text = "%02d:%02d" % (divmod(data.remainingTime, 60)), font = "Helvetica 17")
        
        # TRADING OPTIONS
        canvas.create_rectangle(9 * (data.width / 20), 1 * (data.height / 14), 11 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startXOM, data.endXOM))
        canvas.create_text(10 * (data.width / 20), 1.5 * (data.height / 14), text = "Exxon", font = "Helvetica 14")
        canvas.create_text(10 * (data.width / 20), 2.0 * (data.height / 14), text = "XOM", font = "Helvetica 14 bold")
        canvas.create_text(10 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startXOM, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(11 * (data.width / 20), 1 * (data.height / 14), 13 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startJPM, data.endJPM))
        canvas.create_text(12 * (data.width / 20), 1.5 * (data.height / 14), text = "JP Morgan", font = "Helvetica 14")
        canvas.create_text(12 * (data.width / 20), 2.0 * (data.height / 14), text = "JPM", font = "Helvetica 14 bold")
        canvas.create_text(12 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startJPM, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(13 * (data.width / 20), 1 * (data.height / 14), 15 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startBA, data.endBA))
        canvas.create_text(14 * (data.width / 20), 1.5 * (data.height / 14), text = "Boeing", font = "Helvetica 14")
        canvas.create_text(14 * (data.width / 20), 2.0 * (data.height / 14), text = "BA", font = "Helvetica 14 bold")
        canvas.create_text(14 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startBA, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(15 * (data.width / 20), 1 * (data.height / 14), 17 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startGOOGL, data.endGOOGL))
        canvas.create_text(16 * (data.width / 20), 1.5 * (data.height / 14), text = "Google", font = "Helvetica 14")
        canvas.create_text(16 * (data.width / 20), 2.0 * (data.height / 14), text = "GOOGL", font = "Helvetica 14 bold")
        canvas.create_text(16 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startGOOGL, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(17 * (data.width / 20), 1 * (data.height / 14), 19 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startDIS, data.endDIS))
        canvas.create_text(18 * (data.width / 20), 1.5 * (data.height / 14), text = "Disney", font = "Helvetica 14")
        canvas.create_text(18 * (data.width / 20), 2.0 * (data.height / 14), text = "DIS", font = "Helvetica 14 bold")
        canvas.create_text(18 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startDIS, 2)), font = "Helvetica 14")
        
        # BUTTONS
        back = Image.open('button_back2.png')
        canvas.back = ImageTk.PhotoImage(back)
        canvas.create_image(14 * (data.width / 20), 4 * (data.height / 14), image = canvas.back, anchor = "nw")
        
        stop = Image.open('button_stop.png')
        canvas.stop = ImageTk.PhotoImage(stop)
        canvas.create_image(17 * (data.width / 20), 4 * (data.height / 14), image = canvas.stop, anchor = "nw")
        
        # GRAPH SPACE
        canvas.create_rectangle(1 * (data.width / 20), 6 * (data.height / 14), 19 * (data.width / 20), 13 * (data.height / 14), fill = "white")
        
        # Determine whether to use live or historic data for graphing
        if isBusinessDay(data.now) == False or isTimeBetween(time(9, 30), time(16, 0), time(data.hour, data.min)) == False or data.XOMLive[0] == data.XOMLive[1]:
            if data.stock == "XOM":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "XOM: " + str(data.portfolio.count("XOM")), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsXOM:
                    canvas.create_line(x1, y1, x2, y2, fill = "blue")
                    canvas.create_line(x2, y2, x3, y3, fill = "blue")
            
            elif data.stock == "JPM":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "JPM: " + str(data.portfolio.count("JPM")), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsJPM:
                    canvas.create_line(x1, y1, x2, y2, fill = "orange")
                    canvas.create_line(x2, y2, x3, y3, fill = "orange")
            
            elif data.stock == "BA":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "BA: " + str(data.portfolio.count("BA")), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsBA:
                    canvas.create_line(x1, y1, x2, y2, fill = "purple")
                    canvas.create_line(x2, y2, x3, y3, fill = "purple")
            
            elif data.stock == "GOOGL":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "GOOGL: " + str(data.portfolio.count("GOOGL")), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsGOOGL:
                    canvas.create_line(x1, y1, x2, y2, fill = "sea green")
                    canvas.create_line(x2, y2, x3, y3, fill = "sea green")
            
            elif data.stock == "DIS":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "DIS: " + str(data.portfolio.count("DIS")), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsDIS:
                    canvas.create_line(x1, y1, x2, y2, fill = "turquoise")
                    canvas.create_line(x2, y2, x3, y3, fill = "turquoise")
        
        else:
            if data.stock == "XOM":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "XOM: " + str(data.portfolio.count("XOM")), font = "Helvetica 14", anchor = "ne")
                for i in range(len(data.XOMLive) - 1):
                    cMin = min(data.XOMLive)
                    cMax = max(data.XOMLive)
                    
                    x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                    y1 = 13 * (data.height / 14) - ((data.startXOM - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x2 = 1 * (data.width / 20) + data.dX * i
                    y2 = 13 * (data.height / 14) - ((data.endXOM - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x3 = 1 * (data.width / 20) + data.dX * i
                    y3 = 13 * (data.height / 14)
                    
                    canvas.create_line(x1, y1, x2, y2, fill = "blue")
                    canvas.create_line(x2, y2, x3, y3, fill = "blue")
            
            elif data.stock == "JPM":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "JPM: " + str(data.portfolio.count("JPM")), font = "Helvetica 14", anchor = "ne")
                for i in range(len(data.JPMLive) - 1):
                    cMin = min(data.JPMLive)
                    cMax = max(data.JPMLive)
                    
                    x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                    y1 = 13 * (data.height / 14) - ((data.startJPM - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x2 = 1 * (data.width / 20) + data.dX * i
                    y2 = 13 * (data.height / 14) - ((data.endJPM - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x3 = 1 * (data.width / 20) + data.dX * i
                    y3 = 13 * (data.height / 14)
                    
                    canvas.create_line(x1, y1, x2, y2, fill = "orange")
                    canvas.create_line(x2, y2, x3, y3, fill = "orange")
                    
            elif data.stock == "BA":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "BA: " + str(data.portfolio.count("BA")), font = "Helvetica 14", anchor = "ne")
                for i in range(len(data.BALive) - 1):
                    cMin = min(data.BALive)
                    cMax = max(data.BALive)
                    
                    x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                    y1 = 13 * (data.height / 14) - ((data.startBA - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x2 = 1 * (data.width / 20) + data.dX * i
                    y2 = 13 * (data.height / 14) - ((data.endBA - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x3 = 1 * (data.width / 20) + data.dX * i
                    y3 = 13 * (data.height / 14)
                    
                    canvas.create_line(x1, y1, x2, y2, fill = "purple")
                    canvas.create_line(x2, y2, x3, y3, fill = "purple")
            
            elif data.stock == "GOOGL":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "GOOGL: " + str(data.portfolio.count("GOOGL")), font = "Helvetica 14", anchor = "ne")
                for i in range(len(data.GOOGLLive) - 1):
                    cMin = min(data.GOOGLLive)
                    cMax = max(data.GOOGLLive)
                    
                    x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                    y1 = 13 * (data.height / 14) - ((data.startGOOGL - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x2 = 1 * (data.width / 20) + data.dX * i
                    y2 = 13 * (data.height / 14) - ((data.endGOOGL - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x3 = 1 * (data.width / 20) + data.dX * i
                    y3 = 13 * (data.height / 14)
                    
                    canvas.create_line(x1, y1, x2, y2, fill = "sea green")
                    canvas.create_line(x2, y2, x3, y3, fill = "sea green")
            
            elif data.stock == "DIS":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "DIS: " + str(data.portfolio.count("DIS")), font = "Helvetica 14", anchor = "ne")
                for i in range(len(data.DISLive) - 1):
                    cMin = min(data.DISLive)
                    cMax = max(data.DISLive)
                    
                    x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                    y1 = 13 * (data.height / 14) - ((data.startDIS - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x2 = 1 * (data.width / 20) + data.dX * i
                    y2 = 13 * (data.height / 14) - ((data.endDIS - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                    x3 = 1 * (data.width / 20) + data.dX * i
                    y3 = 13 * (data.height / 14)
                    
                    canvas.create_line(x1, y1, x2, y2, fill = "turquoise")
                    canvas.create_line(x2, y2, x3, y3, fill = "turquoise")
    
    elif data.gameMode == "stockSummary":
        # BACKGROUND
        image = Image.open('Stock Summary Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # BUTTONS
        summary = Image.open('title_summary.png')
        canvas.summary = ImageTk.PhotoImage(summary)
        canvas.create_image(1 * (data.width / 20), 1 * (data.height / 14), image = canvas.summary, anchor = "nw")
        
        repeat = Image.open('button_repeat.png')
        canvas.repeat = ImageTk.PhotoImage(repeat)
        canvas.create_image(14 * (data.width / 20), 1 * (data.height / 14), image = canvas.repeat, anchor = "nw")

        next = Image.open('button_continue.png')
        canvas.next = ImageTk.PhotoImage(next)
        canvas.create_image(17 * (data.width / 20), 1 * (data.height / 14), image = canvas.next, anchor = "nw")
        
        # HIGHSCORE
        if data.totalValue > float(data.scores.iat[0, 0]):
            data.scores.iat[0, 0] = str(data.totalValue)
            data.scores.to_csv('Scores.csv', index = False, header = False)
        canvas.create_rectangle(1 * (data.width / 20), 10 * (data.height / 14), 6 * (data.width / 20), 11.5 * (data.height / 14), fill = "white")
        canvas.create_text(3.5 * (data.width / 20), 10.5 * (data.height / 14), text = "HIGHEST SCORE", font = "Helvetica 19 bold")
        canvas.create_text(3.5 * (data.width / 20), 11 * (data.height / 14), text = data.scores.iat[0, 0], font = "Helvetica 14 bold")
        
        # ACCOUNT SUMMARY
        canvas.create_rectangle(1 * (data.width / 20), 3 * (data.height / 14), 6 * (data.width / 20), 8 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Liquid Money: " + str(round(data.liquidMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.0 * (data.height / 14), text = "Total Portfolio Value: " + str(round(data.totalValue, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.5 * (data.height / 14), text = "Net Profit/Loss: " + str(round(data.totalValue - data.startMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 5.0 * (data.height / 14), text = "Profit/Loss Multiplier: " + str(round(data.totalValue / data.startMoney, 3)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 5.5 * (data.height / 14), text = "Exxon Shares: " + str(data.portfolio.count("XOM")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 6.0 * (data.height / 14), text = "JP Morgan Shares: " + str(data.portfolio.count("JPM")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 6.5 * (data.height / 14), text = "Boeing Shares: " + str(data.portfolio.count("BA")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 7.0 * (data.height / 14), text = "Google Shares: " + str(data.portfolio.count("GOOGL")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 7.5 * (data.height / 14), text = "Disney Shares: " + str(data.portfolio.count("DIS")), font = "Helvetica 14", anchor = "w")
        
        # SUMMARY MEME
        meme = Image.open('Stock Market Meme.jpg')
        canvas.meme = ImageTk.PhotoImage(meme)
        canvas.create_image(19 * (data.width / 20), 13 * (data.height / 14), image = canvas.meme, anchor = "se")

    elif data.gameMode == "currency":
        # BACKGROUND
        image = Image.open('Currency Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # SUMMARY SPACE
        canvas.create_rectangle(1 * (data.width / 20), 1 * (data.height / 14), 6 * (data.width / 20), 5 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 1.5 * (data.height / 14), text = "Liquid Money: " + str(round(data.liquidMoney, 2)),font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 2.5 * (data.height / 14), text = "Total Portfolio Value: " + str(round(data.totalValue, 2)),font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Net Profit/Loss: " + str(round(data.totalValue - data.startMoney, 2)),font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.5 * (data.height / 14), text = "Profit/Loss Multiplier: " + str(round(data.totalValue / data.startMoney, 3)), font = "Helvetica 14", anchor = "w")
        
        # BUY/SELL OPTIONS
        canvas.create_rectangle(6.5 * (data.width / 20), 1 * (data.height / 14), 8.5 * (data.width / 20), 1.5 * (data.height / 14), fill = "green")
        canvas.create_text(7.5 * (data.width / 20), 1.25 * (data.height / 14), text = "+50", font = "Helvetica 14")
        canvas.create_rectangle(6.5 * (data.width / 20), 1.5 * (data.height / 14), 8.5 * (data.width / 20), 2 * (data.height / 14), fill = "green")
        canvas.create_text(7.5 * (data.width / 20), 1.75 * (data.height / 14), text = "+100", font = "Helvetica 14")
        canvas.create_rectangle(6.5 * (data.width / 20), 2 * (data.height / 14), 8.5 * (data.width / 20), 2.5 * (data.height / 14), fill = "green")
        canvas.create_text(7.5 * (data.width / 20), 2.25 * (data.height / 14), text = "+500", font = "Helvetica 14")
        canvas.create_rectangle(6.5 * (data.width / 20), 2.5 * (data.height / 14), 8.5 * (data.width / 20), 3 * (data.height / 14), fill = "green")
        canvas.create_text(7.5 * (data.width / 20), 2.75 * (data.height / 14), text = "+1000", font = "Helvetica 14")
        
        canvas.create_rectangle(6.5 * (data.width / 20), 3 * (data.height / 14), 8.5 * (data.width / 20), 3.5 * (data.height / 14), fill = "red")
        canvas.create_text(7.5 * (data.width / 20), 3.25 * (data.height / 14), text = "-50", font = "Helvetica 14")
        canvas.create_rectangle(6.5 * (data.width / 20), 3.5 * (data.height / 14), 8.5 * (data.width / 20), 4 * (data.height / 14), fill = "red")
        canvas.create_text(7.5 * (data.width / 20), 3.75 * (data.height / 14), text = "-100", font = "Helvetica 14")
        canvas.create_rectangle(6.5 * (data.width / 20), 4 * (data.height / 14), 8.5 * (data.width / 20), 4.5 * (data.height / 14), fill = "red")
        canvas.create_text(7.5 * (data.width / 20), 4.25 * (data.height / 14), text = "-500", font = "Helvetica 14")
        canvas.create_rectangle(6.5 * (data.width / 20), 4.5 * (data.height / 14), 8.5 * (data.width / 20), 5 * (data.height / 14), fill = "red")
        canvas.create_text(7.5 * (data.width / 20), 4.75 * (data.height / 14), text = "-1000", font = "Helvetica 14")
        
        # TIMER
        canvas.create_rectangle(9 * (data.width / 20), 4 * (data.height / 14), 12 * (data.width / 20), 5 * (data.height / 14), fill = "white")
        canvas.create_text(10.5 * (data.width / 20), 4.5 * (data.height / 14), text = "%02d:%02d" % (divmod(data.remainingTime, 60)), font = "Helvetica 17")
        
        # TRADING OPTIONS
        canvas.create_rectangle(9 * (data.width / 20), 1 * (data.height / 14), 11 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startEUR, data.endEUR))
        canvas.create_text(10 * (data.width / 20), 1.5 * (data.height / 14), text = "Euro", font = "Helvetica 14")
        canvas.create_text(10 * (data.width / 20), 2.0 * (data.height / 14), text = "EUR", font = "Helvetica 14 bold")
        canvas.create_text(10 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startEUR, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(11 * (data.width / 20), 1 * (data.height / 14), 13 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startGBP, data.endGBP))
        canvas.create_text(12 * (data.width / 20), 1.5 * (data.height / 14), text = "Pound", font = "Helvetica 14")
        canvas.create_text(12 * (data.width / 20), 2.0 * (data.height / 14), text = "GBP", font = "Helvetica 14 bold")
        canvas.create_text(12 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startGBP, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(13 * (data.width / 20), 1 * (data.height / 14), 15 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startCAD, data.endCAD))
        canvas.create_text(14 * (data.width / 20), 1.5 * (data.height / 14), text = "Dollar", font = "Helvetica 14")
        canvas.create_text(14 * (data.width / 20), 2.0 * (data.height / 14), text = "CAD", font = "Helvetica 14 bold")
        canvas.create_text(14 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startCAD, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(15 * (data.width / 20), 1 * (data.height / 14), 17 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startJPY, data.endJPY))
        canvas.create_text(16 * (data.width / 20), 1.5 * (data.height / 14), text = "Yen", font = "Helvetica 14")
        canvas.create_text(16 * (data.width / 20), 2.0 * (data.height / 14), text = "JPY", font = "Helvetica 14 bold")
        canvas.create_text(16 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startJPY, 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(17 * (data.width / 20), 1 * (data.height / 14), 19 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.startZAR, data.endZAR))
        canvas.create_text(18 * (data.width / 20), 1.5 * (data.height / 14), text = "Rand", font = "Helvetica 14")
        canvas.create_text(18 * (data.width / 20), 2.0 * (data.height / 14), text = "ZAR", font = "Helvetica 14 bold")
        canvas.create_text(18 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.startZAR, 2)), font = "Helvetica 14")
        
        # BUTTONS
        back = Image.open('button_back2.png')
        canvas.back = ImageTk.PhotoImage(back)
        canvas.create_image(14 * (data.width / 20), 4 * (data.height / 14), image = canvas.back, anchor = "nw")
        
        stop = Image.open('button_stop.png')
        canvas.stop = ImageTk.PhotoImage(stop)
        canvas.create_image(17 * (data.width / 20), 4 * (data.height / 14), image = canvas.stop, anchor = "nw")
        
        # GRAPH SPACE
        canvas.create_rectangle(1 * (data.width / 20), 6 * (data.height / 14), 19 * (data.width / 20), 13 * (data.height / 14), fill = "white")
        
        # Determine whether to use live or historic data for graphing
        if isBusinessDay(data.now) == False or isTimeBetween(time(9, 30), time(16, 0), time(data.hour, data.min)) == False or data.EURLive[0] == data.EURLive[1]:
            if data.forex == "EUR":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "EUR: " + str(data.exchange["EUR"]), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsEUR:
                    canvas.create_line(x1, y1, x2, y2, fill = "blue")
                    canvas.create_line(x2, y2, x3, y3, fill = "blue")
           
            elif data.forex == "GBP":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "GBP: " + str(data.exchange["GBP"]), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsGBP:
                    canvas.create_line(x1, y1, x2, y2, fill = "orange")
                    canvas.create_line(x2, y2, x3, y3, fill = "orange")
            
            elif data.forex == "CAD":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "CAD: " + str(data.exchange["CAD"]), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsCAD:
                    canvas.create_line(x1, y1, x2, y2, fill = "purple")
                    canvas.create_line(x2, y2, x3, y3, fill = "purple")
            
            elif data.forex == "JPY":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "JPY: " + str(data.exchange["JPY"]), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsJPY:
                    canvas.create_line(x1, y1, x2, y2, fill = "sea green")
                    canvas.create_line(x2, y2, x3, y3, fill = "sea green")
            
            elif data.forex == "ZAR":
                canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "ZAR: " + str(data.exchange["ZAR"]), font = "Helvetica 14", anchor = "ne")
                for x1, y1, x2, y2, x3, y3 in data.lineSegmentsZAR:
                    canvas.create_line(x1, y1, x2, y2, fill = "turquoise")
                    canvas.create_line(x2, y2, x3, y3, fill = "turquoise")
            
            else:
                if data.forex == "EUR":
                    canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "EUR: " + str(data.exchange["EUR"]), font = "Helvetica 14", anchor = "ne")
                    for i in range(len(data.EURLive) - 1):
                        cMin = min(data.EURLive)
                        cMax = max(data.EURLive)
                        
                        x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                        y1 = 13 * (data.height / 14) - ((data.startEUR - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x2 = 1 * (data.width / 20) + data.dX * i
                        y2 = 13 * (data.height / 14) - ((data.endEUR - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x3 = 1 * (data.width / 20) + data.dX * i
                        y3 = 13 * (data.height / 14)
                        
                        canvas.create_line(x1, y1, x2, y2, fill = "blue")
                        canvas.create_line(x2, y2, x3, y3, fill = "blue")
                
                elif data.forex == "GBP":
                    canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "GBP: " + str(data.exchange["GBP"]), font = "Helvetica 14", anchor = "ne")
                    for i in range(len(data.GBPLive) - 1):
                        cMin = min(data.GBPLive)
                        cMax = max(data.GBPLive)
                        
                        x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                        y1 = 13 * (data.height / 14) - ((data.startGBP - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x2 = 1 * (data.width / 20) + data.dX * i
                        y2 = 13 * (data.height / 14) - ((data.endGBP - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x3 = 1 * (data.width / 20) + data.dX * i
                        y3 = 13 * (data.height / 14)
                        
                        canvas.create_line(x1, y1, x2, y2, fill = "orange")
                        canvas.create_line(x2, y2, x3, y3, fill = "orange")
                
                elif data.forex == "CAD":
                    canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "CAD: " + str(data.exchange["CAD"]), font = "Helvetica 14", anchor = "ne")
                    for i in range(len(data.CADLive) - 1):
                        cMin = min(data.CADLive)
                        cMax = max(data.CADLive)
                        
                        x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                        y1 = 13 * (data.height / 14) - ((data.startCAD - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x2 = 1 * (data.width / 20) + data.dX * i
                        y2 = 13 * (data.height / 14) - ((data.endCAD - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x3 = 1 * (data.width / 20) + data.dX * i
                        y3 = 13 * (data.height / 14)
                        
                        canvas.create_line(x1, y1, x2, y2, fill = "purple")
                        canvas.create_line(x2, y2, x3, y3, fill = "purple")
                
                elif data.forex == "JPY":
                    canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "JPY: " + str(data.exchange["JPY"]), font = "Helvetica 14", anchor = "ne")
                    for i in range(len(data.JPYLive) - 1):
                        cMin = min(data.JPYLive)
                        cMax = max(data.JPYLive)
                        
                        x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                        y1 = 13 * (data.height / 14) - ((data.startJPY - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x2 = 1 * (data.width / 20) + data.dX * i
                        y2 = 13 * (data.height / 14) - ((data.endJPY - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x3 = 1 * (data.width / 20) + data.dX * i
                        y3 = 13 * (data.height / 14)
                        
                        canvas.create_line(x1, y1, x2, y2, fill = "sea green")
                        canvas.create_line(x2, y2, x3, y3, fill = "sea green")
                
                if data.forex == "ZAR":
                    canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "ZAR: " + str(data.exchange["ZAR"]), font = "Helvetica 14", anchor = "ne")
                    for i in range(len(data.ZARLive) - 1):
                        cMin = min(data.ZARLive)
                        cMax = max(data.ZARLive)
                        
                        x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                        y1 = 13 * (data.height / 14) - ((data.startZAR - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x2 = 1 * (data.width / 20) + data.dX * i
                        y2 = 13 * (data.height / 14) - ((data.endZAR - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                        x3 = 1 * (data.width / 20) + data.dX * i
                        y3 = 13 * (data.height / 14)
                        
                        canvas.create_line(x1, y1, x2, y2, fill = "turquoise")
                        canvas.create_line(x2, y2, x3, y3, fill = "turquoise")
        
    elif data.gameMode == "currencySummary":
        # BACKGROUND
        image = Image.open('Currency Summary Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # BUTTONS
        summary = Image.open('title_summary.png')
        canvas.summary = ImageTk.PhotoImage(summary)
        canvas.create_image(1 * (data.width / 20), 1 * (data.height / 14), image = canvas.summary, anchor = "nw")
        
        repeat = Image.open('button_repeat.png')
        canvas.repeat = ImageTk.PhotoImage(repeat)
        canvas.create_image(14 * (data.width / 20), 1 * (data.height / 14), image = canvas.repeat, anchor = "nw")

        next = Image.open('button_continue.png')
        canvas.next = ImageTk.PhotoImage(next)
        canvas.create_image(17 * (data.width / 20), 1 * (data.height / 14), image = canvas.next, anchor = "nw")
        
        # HIGHSCORE
        if data.totalValue > float(data.scores.iat[1, 0]):
            data.scores.iat[1, 0] = str(data.totalValue)
            data.scores.to_csv('Scores.csv', index = False, header = False)
        canvas.create_rectangle(1 * (data.width / 20), 10 * (data.height / 14), 6 * (data.width / 20), 11.5 * (data.height / 14), fill = "white")
        canvas.create_text(3.5 * (data.width / 20), 10.5 * (data.height / 14), text = "HIGHEST SCORE", font = "Helvetica 19 bold")
        canvas.create_text(3.5 * (data.width / 20), 11 * (data.height / 14), text = data.scores.iat[1, 0], font = "Helvetica 14 bold")
        
        # ACCOUNT SUMMARY
        canvas.create_rectangle(1 * (data.width / 20), 3 * (data.height / 14), 6 * (data.width / 20), 8 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Liquid Money: " + str(round(data.liquidMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.0 * (data.height / 14), text = "Total Portfolio Value: " + str(round(data.totalValue, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.5 * (data.height / 14), text = "Net Profit/Loss: " + str(round(data.totalValue - data.startMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 5.0 * (data.height / 14), text = "Profit/Loss Multiplier: " + str(round(data.totalValue / data.startMoney, 3)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 5.5 * (data.height / 14), text = "Euros Held: " + str(data.exchange["EUR"]), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 6.0 * (data.height / 14), text = "Pounds Held: " + str(data.exchange["GBP"]), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 6.5 * (data.height / 14), text = "Dollars Held: " + str(data.exchange["CAD"]), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 7.0 * (data.height / 14), text = "Yen Held: " + str(data.exchange["JPY"]), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 7.5 * (data.height / 14), text = "Rand Held: " + str(data.exchange["ZAR"]), font = "Helvetica 14", anchor = "w")
        
        # SUMMARY MEME
        meme = Image.open('Forex Market Meme.jpg')
        canvas.meme = ImageTk.PhotoImage(meme)
        canvas.create_image(19 * (data.width / 20), 13 * (data.height / 14), image = canvas.meme, anchor = "se")
    
    elif data.gameMode == "challenge":
        # BACKGROUND
        image = Image.open('Settings Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # SUMMARY SPACE
        canvas.create_rectangle(1 * (data.width / 20), 1 * (data.height / 14), 8 * (data.width / 20), 5 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 1.5 * (data.height / 14), text = "Liquid Money: " + str(round(data.liquidMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 2.5 * (data.height / 14), text = "Total Portfolio Value: " + str(round(data.totalValue, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Net Profit/Loss: " + str(round(data.totalValue - data.startMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.5 * (data.height / 14), text = "Profit/Loss Multiplier: " + str(round(data.totalValue / data.startMoney, 3)), font = "Helvetica 14", anchor = "w")
        
        # TIMER
        canvas.create_rectangle(9 * (data.width / 20), 4 * (data.height / 14), 12 * (data.width / 20), 5 * (data.height / 14), fill = "white")
        canvas.create_text(10.5 * (data.width / 20), 4.5 * (data.height / 14), text = "%02d:%02d" % (divmod(data.remainingTime, 60)), font = "Helvetica 17")
        
        # TRADING OPTIONS
        canvas.create_rectangle(9 * (data.width / 20), 1 * (data.height / 14), 11 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.challengePoints1[-2], data.challengePoints1[-1]))
        canvas.create_text(10 * (data.width / 20), 1.5 * (data.height / 14), text = "Stock", font = "Helvetica 14")
        canvas.create_text(10 * (data.width / 20), 2.0 * (data.height / 14), text = "ONE", font = "Helvetica 14 bold")
        canvas.create_text(10 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.challengePoints1[-1], 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(11 * (data.width / 20), 1 * (data.height / 14), 13 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.challengePoints2[-2], data.challengePoints2[-1]))
        canvas.create_text(12 * (data.width / 20), 1.5 * (data.height / 14), text = "Stock", font = "Helvetica 14")
        canvas.create_text(12 * (data.width / 20), 2.0 * (data.height / 14), text = "TWO", font = "Helvetica 14 bold")
        canvas.create_text(12 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.challengePoints2[-1], 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(13 * (data.width / 20), 1 * (data.height / 14), 15 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.challengePoints3[-2], data.challengePoints3[-1]))
        canvas.create_text(14 * (data.width / 20), 1.5 * (data.height / 14), text = "Stock", font = "Helvetica 14")
        canvas.create_text(14 * (data.width / 20), 2.0 * (data.height / 14), text = "THREE", font = "Helvetica 14 bold")
        canvas.create_text(14 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.challengePoints3[-1], 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(15 * (data.width / 20), 1 * (data.height / 14), 17 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.challengePoints4[-2], data.challengePoints4[-1]))
        canvas.create_text(16 * (data.width / 20), 1.5 * (data.height / 14), text = "Stock", font = "Helvetica 14")
        canvas.create_text(16 * (data.width / 20), 2.0 * (data.height / 14), text = "FOUR", font = "Helvetica 14 bold")
        canvas.create_text(16 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.challengePoints4[-1], 2)), font = "Helvetica 14")
        
        canvas.create_rectangle(17 * (data.width / 20), 1 * (data.height / 14), 19 * (data.width / 20), 3 * (data.height / 14), fill = getColor(data.challengePoints5[-2], data.challengePoints5[-1]))
        canvas.create_text(18 * (data.width / 20), 1.5 * (data.height / 14), text = "Stock", font = "Helvetica 14")
        canvas.create_text(18 * (data.width / 20), 2.0 * (data.height / 14), text = "FIVE", font = "Helvetica 14 bold")
        canvas.create_text(18 * (data.width / 20), 2.5 * (data.height / 14), text = str(round(data.challengePoints5[-1], 2)), font = "Helvetica 14")
        
        # BUTTONS
        back = Image.open('button_back2.png')
        canvas.back = ImageTk.PhotoImage(back)
        canvas.create_image(14 * (data.width / 20), 4 * (data.height / 14), image = canvas.back, anchor = "nw")
        
        stop = Image.open('button_stop.png')
        canvas.stop = ImageTk.PhotoImage(stop)
        canvas.create_image(17 * (data.width / 20), 4 * (data.height / 14), image = canvas.stop, anchor = "nw")
        
        # GRAPH SPACE
        canvas.create_rectangle(1 * (data.width / 20), 6 * (data.height / 14), 19 * (data.width / 20), 13 * (data.height / 14), fill = "white")
        
        if data.challengeStock == "stock1":
            canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "ONE: " + str(data.account.count("stock1")), font = "Helvetica 14", anchor = "ne")
            for i in range(len(data.challengePoints1) - 1):
                cMin = min(data.challengePoints1)
                cMax = max(data.challengePoints1)
                start = data.challengePoints1[i]
                end = data.challengePoints1[i + 1]
                
                x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                y1 = 13 * (data.height / 14) - ((start - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x2 = 1 * (data.width / 20) + data.dX * i
                y2 = 13 * (data.height / 14) - ((end - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x3 = 1 * (data.width / 20) + data.dX * i
                y3 = 13 * (data.height / 14)
                
                canvas.create_line(x1, y1, x2, y2, fill = "blue")
                canvas.create_line(x2, y2, x3, y3, fill = "blue")
        
        elif data.challengeStock == "stock2":
            canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "TWO: " + str(data.account.count("stock2")), font = "Helvetica 14", anchor = "ne")
            for i in range(len(data.challengePoints2) - 1):
                cMin = min(data.challengePoints2)
                cMax = max(data.challengePoints2)
                start = data.challengePoints2[i]
                end = data.challengePoints2[i + 1]
                
                x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                y1 = 13 * (data.height / 14) - ((start - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x2 = 1 * (data.width / 20) + data.dX * i
                y2 = 13 * (data.height / 14) - ((end - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x3 = 1 * (data.width / 20) + data.dX * i
                y3 = 13 * (data.height / 14)
                
                canvas.create_line(x1, y1, x2, y2, fill = "orange")
                canvas.create_line(x2, y2, x3, y3, fill = "orange")
        
        elif data.challengeStock == "stock3":
            canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "THREE: " + str(data.account.count("stock3")), font = "Helvetica 14", anchor = "ne")
            for i in range(len(data.challengePoints3) - 1):
                cMin = min(data.challengePoints3)
                cMax = max(data.challengePoints3)
                start = data.challengePoints3[i]
                end = data.challengePoints3[i + 1]
                
                x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                y1 = 13 * (data.height / 14) - ((start - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x2 = 1 * (data.width / 20) + data.dX * i
                y2 = 13 * (data.height / 14) - ((end - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x3 = 1 * (data.width / 20) + data.dX * i
                y3 = 13 * (data.height / 14)
                
                canvas.create_line(x1, y1, x2, y2, fill = "purple")
                canvas.create_line(x2, y2, x3, y3, fill = "purple")
        
        elif data.challengeStock == "stock4":
            canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "FOUR: " + str(data.account.count("stock4")), font = "Helvetica 14", anchor = "ne")
            for i in range(len(data.challengePoints4) - 1):
                cMin = min(data.challengePoints4)
                cMax = max(data.challengePoints4)
                start = data.challengePoints4[i]
                end = data.challengePoints4[i + 1]
                
                x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                y1 = 13 * (data.height / 14) - ((start - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x2 = 1 * (data.width / 20) + data.dX * i
                y2 = 13 * (data.height / 14) - ((end - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x3 = 1 * (data.width / 20) + data.dX * i
                y3 = 13 * (data.height / 14)
                
                canvas.create_line(x1, y1, x2, y2, fill = "sea green")
                canvas.create_line(x2, y2, x3, y3, fill = "sea green")
        
        elif data.challengeStock == "stock5":
            canvas.create_text(18.25 * (data.width / 20), 6.25 * (data.height / 14), text = "FIVE: " + str(data.account.count("stock5")), font = "Helvetica 14", anchor = "ne")
            for i in range(len(data.challengePoints5) - 1):
                cMin = min(data.challengePoints5)
                cMax = max(data.challengePoints5)
                start = data.challengePoints5[i]
                end = data.challengePoints5[i + 1]
                
                x1 = 1 * (data.width / 20) + data.dX * (i - 1)
                y1 = 13 * (data.height / 14) - ((start - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x2 = 1 * (data.width / 20) + data.dX * i
                y2 = 13 * (data.height / 14) - ((end - cMin) / (cMax - cMin) * 7 * (data.height / 14))
                x3 = 1 * (data.width / 20) + data.dX * i
                y3 = 13 * (data.height / 14)
                
                canvas.create_line(x1, y1, x2, y2, fill = "turquoise")
                canvas.create_line(x2, y2, x3, y3, fill = "turquoise")
                
    elif data.gameMode == "challengeSummary":
        # BACKGROUND
        image = Image.open('Challenge Summary Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # BUTTONS
        summary = Image.open('title_summary.png')
        canvas.summary = ImageTk.PhotoImage(summary)
        canvas.create_image(1 * (data.width / 20), 1 * (data.height / 14), image = canvas.summary, anchor = "nw")
        
        repeat = Image.open('button_repeat.png')
        canvas.repeat = ImageTk.PhotoImage(repeat)
        canvas.create_image(14 * (data.width / 20), 1 * (data.height / 14), image = canvas.repeat, anchor = "nw")

        next = Image.open('button_continue.png')
        canvas.next = ImageTk.PhotoImage(next)
        canvas.create_image(17 * (data.width / 20), 1 * (data.height / 14), image = canvas.next, anchor = "nw")
        
        # HIGHSCORE
        if data.totalValue > float(data.scores.iat[2, 0]):
            data.scores.iat[2, 0] = str(data.totalValue)
            data.scores.to_csv('Scores.csv', index = False, header = False)
        canvas.create_rectangle(1 * (data.width / 20), 10 * (data.height / 14), 6 * (data.width / 20), 11.5 * (data.height / 14), fill = "white")
        canvas.create_text(3.5 * (data.width / 20), 10.5 * (data.height / 14), text = "HIGHEST SCORE", font = "Helvetica 19 bold")
        canvas.create_text(3.5 * (data.width / 20), 11 * (data.height / 14), text = data.scores.iat[2, 0], font = "Helvetica 14 bold")
        
        # ACCOUNT SUMMARY
        canvas.create_rectangle(1 * (data.width / 20), 3 * (data.height / 14), 6 * (data.width / 20), 8 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Liquid Money: " + str(round(data.liquidMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.0 * (data.height / 14), text = "Total Portfolio Value: " + str(round(data.totalValue, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 4.5 * (data.height / 14), text = "Net Profit/Loss: " + str(round(data.totalValue - data.startMoney, 2)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 5.0 * (data.height / 14), text = "Profit/Loss Multiplier: " + str(round(data.totalValue / data.startMoney, 3)), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 5.5 * (data.height / 14), text = "Stock 1 Shares: " + str(data.account.count("stock1")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 6.0 * (data.height / 14), text = "Stock 2 Shares: " + str(data.account.count("stock2")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 6.5 * (data.height / 14), text = "Stock 3 Shares: " + str(data.account.count("stock3")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 7.0 * (data.height / 14), text = "Stock 4 Shares: " + str(data.account.count("stock4")), font = "Helvetica 14", anchor = "w")
        canvas.create_text(1.5 * (data.width / 20), 7.5 * (data.height / 14), text = "Stock 5 Shares: " + str(data.account.count("stock5")), font = "Helvetica 14", anchor = "w")
        
        # SUMMARY MEME
        meme = Image.open('Challenge Market Meme.jpg')
        canvas.meme = ImageTk.PhotoImage(meme)
        canvas.create_image(19 * (data.width / 20), 13 * (data.height / 14), image = canvas.meme, anchor = "se")
    
    elif data.gameMode == "tutorial":
        # BACKGROUND
        image = Image.open('Tutorial Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # LOGO
        instructions = Image.open('title_instructions.png')
        canvas.instructions = ImageTk.PhotoImage(instructions)
        canvas.create_image(1 * (data.width / 20), 1 * (data.height / 14), image = canvas.instructions, anchor = "nw")
        
        # TUTORIAL IMAGES
        stock = Image.open('Stock Trading Screen.png')
        canvas.stock = ImageTk.PhotoImage(stock)
        canvas.create_image(1 * (data.width / 20), 2.5 * (data.height / 14), image = canvas.stock, anchor = "nw")
        
        forex = Image.open('Forex Trading Screen.png')
        canvas.forex = ImageTk.PhotoImage(forex)
        canvas.create_image(19 * (data.width / 20), 2.5 * (data.height / 14), image = canvas.forex, anchor = "ne")
        
        # TUTORIAL SPACE
        canvas.create_rectangle(1 * (data.width / 20), 8.5 * (data.height / 14), 9 * (data.width / 20), 11.5 * (data.height / 14), fill = "white")
        canvas.create_rectangle(11 * (data.width / 20), 8.5 * (data.height / 14), 19 * (data.width / 20), 11.5 * (data.height / 14), fill = "white")
        
        canvas.create_text(1.25 * (data.width / 20), 8.75 * (data.height / 14), text = "Stock Trading/Challenge Simulator:\n\n15 minute time limit\nSelect one stock out of five to trade\nUse up arrow to buy one share of the selected stock\nUse down arrow to sell one share of the selected stock\nAim to maximize profit\nChallenge - prices vary drastically", font = "Helvetica 14", anchor = "nw")
        canvas.create_text(11.25 * (data.width / 20), 8.75 * (data.height / 14), text = "Forex Trading Simulator:\n\n15 minute time limit\nSelect one currency out of five to trade\nBuy either 50, 100, 500, 1000 of selected currency\nSell either 50, 100, 500, 1000 of selected currency\nAim to maximize profit\nAll values against the US Dollar", font = "Helvetica 14", anchor = "nw")
        
        # BUTTONS
        back = Image.open('button_back2.png')
        canvas.back = ImageTk.PhotoImage(back)
        canvas.create_image(17 * (data.width / 20), 12 * (data.height / 14), image = canvas.back, anchor = "nw")
    
    elif data.gameMode == "tips":
        # BACKGROUND
        image = Image.open('Tips Background.jpg')
        canvas.image = ImageTk.PhotoImage(image)
        canvas.create_image(data.width / 2, data.height / 2, image = canvas.image)
        
        # BUTTON
        back = Image.open('button_back1.png')
        canvas.back = ImageTk.PhotoImage(back)
        canvas.create_image(1 * (data.width / 20), 1 * (data.height / 14), image = canvas.back, anchor = "nw")
        
        # LOGO
        tradingTips = Image.open('title_trading-tips.png')
        canvas.tradingTips = ImageTk.PhotoImage(tradingTips)
        canvas.create_image(13 * (data.width / 20), 1 * (data.height / 14), image = canvas.tradingTips, anchor = "nw")
        
        # TIPS/VIDEO SPACE
        canvas.create_rectangle(1 * (data.width / 20), 3 * (data.height / 14), 6 * (data.width / 20), 11 * (data.height / 14), fill = "white")
        canvas.create_text(1.5 * (data.width / 20), 3.5 * (data.height / 14), text = "General Trading Tips:\n\n 1. Research the market\n\n 2. Set aside a specific amount\n\n 3. Set aside time for trading\n\n 4. Start with small amounts\n\n 5. Avoid penny stocks\n\n 6. Observe right trade times\n\n 7. Be patient\n\n 8. Be realistic about profits\n\n 9. Stick to your plan\n\n 10. Think a decision through", font = "Helvetica 14", anchor = "nw")
        canvas.create_rectangle(7.5 * (data.width / 20), 3 * (data.height / 14), 12.5 * (data.width / 20), 11 * (data.height / 14), fill = "white")
        canvas.create_text(8 * (data.width / 20), 3.5 * (data.height / 14), text = "Most Popular Stocks:\n\nAdvanced Micro Devices (AMD)\nApple (AAPL)\nFord (F)\nGeneral Electric (GE)\nFacebook (FB)\nGoPro (GPRO)\nMicrosoft (MSFT)\nFitbit (FIT)\nSnapchat (SNAP)\nMerill Lynch (MER)\nTesla (TSLA)\nTwitter (TWTR)\nNvidia (NVDA)\nAlibaba (BABA)\nAmazon (AMZN)\nNetflix (NFLX)\nMicron Technology (MU)\nSquare (SQ)\nDisney (DIS)\nChesapeake Energy (CHK)", font = "Helvetica 14", anchor = "nw")
        canvas.create_rectangle(14 * (data.width / 20), 3 * (data.height / 14), 19 * (data.width / 20), 11 * (data.height / 14), fill = "white")
        canvas.create_text(14.5 * (data.width / 20), 3.5 * (data.height / 14), text = "Stock Market Terminology:\n\nBearish Stock\n Stock on a downward trend\n\nBullish Stock\n Stock on a upward trend\n\nBlue Chip Stock\n Shares with high dividends\n\nPink Sheet Stock\n Shares outside the market\n\nPenny Stock\n Stock of low price\n\nInitial Public Offering\n Company's first flotation\n\nPortfolio\n Collection of investments", font = "Helvetica 14", anchor = "nw")
        
        # HELPFUL LINKS SPACE
        canvas.create_rectangle(1 * (data.width / 20), 12 * (data.height / 14), 19 * (data.width / 20), 13 * (data.height / 14), fill = "white")
        canvas.create_text(10 * (data.width / 20), 12.5 * (data.height / 14), text = "Helpful Links: nyse.com - investopedia.com - robinhood.com - marketwatch.com - thestreet.com - nasdaq.com - finance.yahoo.com", font = "Helvetica 14")
            
### Animation Framework ###

def run(width = 1000, height = 700):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height, fill = 'white', width = 0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)

    class Struct(object): 
        pass
    
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 1000
    
    root = Tk()
    root.resizable(width = False, height = False)
    init(data)
    canvas = Canvas(root, width = data.width, height = data.height)
    canvas.configure(bd = 0, highlightthickness = 0)
    canvas.pack()
    
    root.bind("<Button-1>", lambda event: mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event: keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    root.mainloop()
    
    print("Now You Have Experimented With Trading! Come Back Soon!")

run()