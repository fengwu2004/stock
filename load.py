import time
from unit import Stock, DayValue

def getLines(file):

    lines = [line.rstrip('\n') for line in open(file)]

    lines.pop(1)

    lines.pop()
    
    return lines

def getTime(value):
    
    return time.strptime(value, '%Y/%m/%d')

def formatData(lines):
    
    stock = Stock()
    
    if len(lines) > 1:
        
        values = lines[0].split(' ')
        
        stock.id = values[0]
        
        stock.name = values[1]
        
        lines.pop(0)

    if len(lines) <= 1:
        
        return stock
    
    for line in lines:
        
        dayvalue = DayValue()
    
        values = line.split('\t')

        dayvalue.date = getTime(values[0])
        
        if dayvalue.date < time.strptime('2017/1/01', '%Y/%m/%d'):
            
            continue

        dayvalue.open = float(values[1])

        dayvalue.max = float(values[2])

        dayvalue.min = float(values[3])

        dayvalue.close = float(values[4])

        dayvalue.tradeamount = float(values[5])

        dayvalue.tradevolume = float(values[6])

        stock.dayvalues.append(dayvalue)
        
    return stock