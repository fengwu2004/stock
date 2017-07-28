# 寻找上升趋势中的调整浪
# from wave_strategy import WaveStrategyUnit

def checkInAdjustWave (waveUnit):
    if len(waveUnit.maxs) < 2 or len(waveUnit.mins) < 1:
        return False
    
    maxsLength = len(waveUnit.maxs)
    
    minsLength = len(waveUnit.mins)
    
    # 高点依次增加
    if waveUnit.maxs[maxsLength - 1].close * 0.90 <= waveUnit.maxs[maxsLength - 2].close:
        return False
    
    # 最后一个低点的时间在最后一个高点的前面
    if waveUnit.mins[minsLength - 1].date > waveUnit.maxs[maxsLength - 1].date:
        return False
    
    # 当前价格比最近的低点高
    if waveUnit.lastday.close < waveUnit.mins[minsLength - 1].close:
        return False
    
    return True