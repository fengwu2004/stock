import time

class DayValue(object):
    
    def __init__(self):
        
        self.open = 0
        
        self.close = 0
        
        self.min = 0
        
        self.max = 0
        
        self.date = time.strptime('2013/1/01', '%Y/%m/%d')
        
        self.tradeamount = 0
        
        self.tradevolume = 0
        

class Stock(object):
    
    def __init__ (self):
        
        self.id = 0
        
        self.name = ''
        
        self.dayvalues = []