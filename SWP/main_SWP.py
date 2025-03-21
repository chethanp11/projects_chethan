class SWPCalculator:
    def __init__(self, initial_investment, annual_withdrawal, annual_return_rate, years):
        self.initial_investment = initial_investment
        self.annual_withdrawal = annual_withdrawal
        self.annual_return_rate = annual_return_rate
        self.years = years

    def calculate_yearly_balances(self):
        balances = []
        current_balance = self.initial_investment

        for year in range(1, self.years + 1):
            interest_earned = current_balance * self.annual_return_rate
            end_of_year_balance = current_balance + interest_earned - self.annual_withdrawal
            balances.append({
                'Year': year,
                'Starting Balance': current_balance,
                'Interest Earned': interest_earned,
                'Annual Withdrawal': self.annual_withdrawal,
                'End of Year Balance': end_of_year_balance
            })
            current_balance = end_of_year_balance

        return balances