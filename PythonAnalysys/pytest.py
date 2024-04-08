import fintech as ft
import pandas as pd
from fintech import finsys

x = ft.roi(initial_investment=500, final_value=1000)
result = x.roi()
print("ROI:", result)

# Створення DataFrame з даними
data = {
    'current_assets': [10000, 12000, 15000],
    'current_liabilities': [5000, 6000, 7500],
    'net_income': [8000, 10000, 12000],
    'total_assets': [40000, 45000, 50000],
    'shareholder_equity': [30000, 35000, 40000],
    'earnings_before_interest_and_taxes': [15000, 18000, 20000],
    'interest_expenses': [2000, 2500, 3000],
    'total_debt': [10000, 12000, 15000],
    'cost_of_goods_sold': [5000, 6000, 7000],
    'average_inventory': [2000, 2500, 3000]
}

df = pd.DataFrame(data)

# Створення об'єкта finsys
finsys_obj = finsys()

# Застосування функцій до відповідних стовпців DataFrame
df['liquidity_ratio'] = finsys_obj.liquidity_ratio(df['current_assets'], df['current_liabilities'])
df['return_on_assets'] = finsys_obj.return_on_assets(df['net_income'], df['total_assets'])
df['return_on_equity'] = finsys_obj.return_on_equity(df['net_income'], df['shareholder_equity'])
df['interest_coverage_ratio'] = finsys_obj.interest_coverage_ratio(df['earnings_before_interest_and_taxes'], df['interest_expenses'])
df['debt_ratio'] = finsys_obj.debt_ratio(df['total_debt'], df['total_assets'])
df['inventory_turnover_ratio'] = finsys_obj.inventory_turnover_ratio(df['cost_of_goods_sold'], df['average_inventory'])

# Виведення результатів
print(df)