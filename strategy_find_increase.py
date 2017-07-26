# 寻找上升趋势中的调整浪
def checkInAdjustWave (waveUnit):
    if len(waveUnit.maxs) < 2 and len(waveUnit.mins) < 1:
        return False
    
    maxsLength = len(waveUnit.maxs)
    
    minsLength = len(waveUnit.mins)
    
    # 高点依次增加
    if waveUnit.maxs[maxsLength - 1].close <= waveUnit.maxs[maxsLength - 2].close:
        return False
    
    # 上一个低点的时间在最后一个高点的前面
    if waveUnit.mins[minsLength - 1].date < waveUnit.maxs[maxsLength - 1].date:
        return True
    
    return False