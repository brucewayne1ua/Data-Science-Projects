# roi_calculator.pyx
def ROI():
    
    profit = float(input())
    cost = float(input())
    return ((profit - cost) / cost) * 100
