class roi:
    def __init__(self, initial_investment, final_value):
        self.initial_investment = initial_investment
        self.final_value = final_value

    def roi(self):
        if self.initial_investment == 0:
            return "Помилка: початкова інвестиція дорівнює нулю"
        else:
            return (self.final_value - self.initial_investment) / self.initial_investment * 100


class finmetrics:
    def __init__(self, revenue, expenses, tax_rate):
        self.revenue = revenue
        self.expenses = expenses
        self.tax_rate = tax_rate

    def net_profit(self):
        return self.revenue - self.expenses

    def profit_before_tax(self):
        return self.calculate_net_profit() / (1 - self.tax_rate)

    def profit_margin(self):
        return (self.calculate_net_profit() / self.revenue) * 100

    def return_on_investment(self, initial_investment):
        return (self.calculate_net_profit() / initial_investment) * 100

class assetvm:
    def __init__(self, rf_rate, m_return, d_rate):
        self.rf_rate = rf_rate
        self.m_return = m_return
        self.d_rate = d_rate

    def capm_valuation(self, beta):
        return self.rf_rate + beta * (self.m_return - self.rf_rate)

    def dcf_valuation(self, cash_flows):
        pv = 0
        for period, cf in enumerate(cash_flows):
            pv += cf / ((1 + self.d_rate) ** (period + 1))
        return pv
    

class finsys:
    def __init__(self, **kwargs):
        self.data = kwargs

    @staticmethod
    def liquidity_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities

    @staticmethod
    def return_on_assets(net_income, total_assets):
        return net_income / total_assets
    
    @staticmethod
    def return_on_equity(net_income, shareholder_equity):
        return net_income / shareholder_equity

    @staticmethod
    def interest_coverage_ratio(earnings_before_interest_and_taxes, interest_expenses):
        return earnings_before_interest_and_taxes / interest_expenses
    
    @staticmethod
    def debt_ratio(total_debt, total_assets):
        return total_debt / total_assets

    @staticmethod
    def inventory_turnover_ratio(cost_of_goods_sold, average_inventory):
        return cost_of_goods_sold / average_inventory


