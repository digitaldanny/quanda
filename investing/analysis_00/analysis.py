'''
INVESTMENT RULE:
- This investment analysis is based on a fixed "investment unit." Annual investment units
are placed into a new investment. 

- Original investments are required to feed back a certain percentage into themselves and send
the rest into savings.
'''

import config as cfg

def main():

    # initial annual earning after taxes for the first year out of college.
    year                = 2021
    years_after_college = 0
    investment_unit     = cfg.PERCENTAGE_INVESTMENT_UNIT * cfg.ENGINEERING_SALARY
    salary              = cfg.ENGINEERING_SALARY  # investment unit spent on housing investment
    bonus               = cfg.ENGINEERING_BONUS
    annual_income       = -investment_unit
    annual_income_pretax = 0
    savings             = 0
    debt                = 0
    new_investments     = cfg.PERCENTAGE_INVESTMENT_UNIT * cfg.ENGINEERING_SALARY
    
    # Make my initial investment in housing
    investmentList = []
    investmentList.append( housing(investment_unit) )

    while True:
        cmd = input("View next year's earnings? (y/n): ")
        if cmd == 'n': break
        
        year += 1
        years_after_college += 1
        print("\nYEAR: " + str(year))
        print("Years after college: " + str(years_after_college))
        
        # When the year restarts, my annual earnings are set back to 0.
        annual_income = float(0)
        annual_income += salary + bonus
        annual_income_pretax = salary + bonus
        print("Engineering salary: \n${:.2f}\n".format(salary))
        print("Engineering bonus: \n${:.2f}\n".format(bonus))
        
        # Remove annual savings before considering living
        # expenses.
        this_years_savings = annual_income * cfg.PERCENTAGE_SAVINGS
        savings += this_years_savings
        annual_income -= this_years_savings
        print("This year's savings: \n${:.2f}\n".format(this_years_savings))
        print("Total savings: \n${:.2f}\n".format(savings))
        
        # Remove annual living expenses
        living = annual_living_expenses()
        annual_income -= living
        print("Living expenses: \n${:.2f}\n".format(living))
        
        if annual_income < 0:
            debt += annual_income
            print("You are in debt by: \n${:.2f}\n".format(debt))
            
        # Update all investments
        else:
            # Wait to reach another investment unit
            unit = cfg.PERCENTAGE_INVESTMENT_UNIT * salary
            if annual_income > unit:
                annual_income -= unit
                new_investments += unit
                
                print("You made another large investment (not included in this script)\n")
        
            returned = investmentList[0].update() 
            annual_income += returned
            annual_income_pretax += returned
                
        # Remove annual taxes at the end of the year.
        tax = calc_tax(annual_income_pretax)
        annual_income -= tax
        print("Taxes: \n${:.2f}\n".format(tax))        
                
        # Update user excess income after bills, taxes, damages, new investments
        print("New investments made  : \n${:.2f}\n".format(new_investments))
        print("Your current annual excess is: \n${:.2f}\n".format(annual_income))
        print("\n\n")
        
        # Give annual raise
        salary += salary * cfg.PERCENTAGE_ANNUAL_RAISE
        if salary > cfg.ENGINEERING_MAX_SALARY:
            salary = cfg.ENGINEERING_MAX_SALARY
    
    print("Analysis complete.")
    
class housing:
    def __init__(self, initial_investment):
        self.name = "Housing"
        self.initial_investment     = initial_investment 
        self.total_investment       = initial_investment
        self.total_earnings         = -initial_investment # earnings since beginning the investment a year after college
        self.savings                = initial_investment # account holding the money fed back into this investment
        self.property_count         = 1
        
        
    '''
    SUMMARY: Run all object updates and return any money made after an investment unit is met.
    '''
    def update(self):     
        self.update_tenant()            
        returned = self.update_investment()  # returns 0 if there was no excess
        self.stats()
        return returned
        
        
    '''
    SUMMARY: Charge rent, pay for damages. Dump any income from rent into the savings account
    to be analyzed at the end of the year (in the update_investment function)
    '''
    def update_tenant(self):
        
        # Charge rent
        self.savings += self.property_count * cfg.PROPERTY_TENANT_COUNT * cfg.PROPERTY_RENT * 12
        
        # Repair damages and handle property maintainance
        self.savings -= self.property_count * (cfg.PROPERTY_DAMAGES_ANNUAL + cfg.PROPERTY_UPKEEP_ANNUAL)
        
        # Pay for property manager
        self.savings -= self.property_count * cfg.PROPERTY_MANAGER_ANNUAL
        
    '''
    SUMMARY: Update the total investment with the amount of money put into the effort
    '''
    def update_investment(self):
        returned = 0
        
        # just to keep track of the investment's success, take note of the leftovers
        self.total_earnings += self.savings
    
        if (self.savings >= 0 and self.property_count <= cfg.MAX_PROPERTY_COUNT):
        
            # Make sure I get my portion that should be returned to my annual income.
            returned = (1 - cfg.PERCENTAGE_FEEDBACK) * self.savings  
            self.savings -= returned
        
            # Buy more properties at the end of every year if I can.
            new_mortgage = cfg.MORTGAGE * 12
            while (self.savings > new_mortgage and self.property_count < cfg.MAX_PROPERTY_COUNT):
                self.savings -= new_mortgage # to be safe, make sure the income can pay for the mortage for a year
                self.total_investment += new_mortgage
                self.property_count += 1
        else:
            # Either going into debt or I've reached the max number of
            # properties I'm interested in buying.
            returned = self.savings
            
        return returned
        
        
    '''
    SUMMARY: Override the original stats method
    '''
    def stats(self):
        print("Investment Name      : " + self.name)
        print("Total Investment     : ${:.2f}".format(self.total_investment)) 
        print("Total Earnings       : ${:.2f}".format(self.total_earnings)) 
        print("Property Count       : " + str(self.property_count) + "\n")
            
            
'''
SUMMARY: Return my annual living expenses based on the configs.
'''    
def annual_living_expenses():
    total = 0
    for key, value in cfg.monthly_expenses.items():
        total += value
        
    total *= 12
    return total 
        
        
'''
SUMMARY: Tax calculator wrapper.
'''
def calc_tax(earning):
    tax = __recursive_tax(earning, 0)
    return tax
    
    
'''
SUMMARY: Recursively calculate federal taxes based on a total income.
'''
def __recursive_tax(earning, bracket):

    taxable = 0
    refilter = 0
    tax = 0
    
    # Only tax positive earnings and filter through a maximum of 7 times.
    if earning > 0 and bracket < 7:
    
        # define the thresholds between tax brackets and the tax rate
        next_bracket = bracket + 1              # index for the next tax bracket
        current = cfg.TAX_BRACKETS[bracket]     # current threshold
        next = cfg.TAX_BRACKETS[next_bracket]   # next threshold
        rate = cfg.TAX_RATES[bracket]           # current tax rate
    
        # (1) determine the amount to tax for this bracket
        # (2) calculate the amount to filter through again
        if earning > next:
            taxable = next - current
            refilter = earning - taxable
        else:
            taxable = earning
            refilter = 0
    
        # (3) calculate the tax at this bracket
        tax = rate * taxable
        
        '''
        print("Taxable: " + str(taxable))
        print("Refilter: " + str(refilter))
        print("Tax: " + str(tax))
        '''
        
        # (4) send the remaining money through the filter again
        tax += __recursive_tax(refilter, next_bracket)
        
    return tax
    
    
if __name__ == '__main__': 
    main()