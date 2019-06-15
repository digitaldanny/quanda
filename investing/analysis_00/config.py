'''
UPDATES:
06/15/2019 - Tax bracket thresholds
'''

# +----------+----------+----------+----------+
# |                   INCOME                  |
# +----------+----------+----------+----------+
ENGINEERING_SALARY          = 87000
ENGINEERING_BONUS           = 0
ENGINEERING_MAX_SALARY      = 200000
PERCENTAGE_ANNUAL_RAISE     = .04

# +----------+----------+----------+----------+
# |                  EXPENSES                 |
# +----------+----------+----------+----------+
monthly_expenses = {
    'MONTHLY_MORTGAGE'        : 1500,
    'MONTHLY_FOOD'            : 500,
    'MONTHLY_CAR_PAYMENT'     : 450,
    'MONTHLY_CAR_INSURANCE'   : 150,
    'MONTHLY_GAS'             : 160,
    'MONTHLY_MISC'            : 200
}

# +----------+----------+----------+----------+
# |                 RETIREMENT                |
# +----------+----------+----------+----------+
PERCENTAGE_SAVINGS = .20

# +----------+----------+----------+----------+
# |                    TAX                    |
# +----------+----------+----------+----------+
TAX_BRACKETS = [
    0,
    9700,
    39475,
    84200,
    160725,
    204100,
    510300,
]

TAX_RATES = [
    .10,
    .12,
    .22,
    .24,
    .32,
    .35,
    .37
]

# +----------+----------+----------+----------+
# |                 INVESTMENT                |
# +----------+----------+----------+----------+
PERCENTAGE_INVESTMENT_UNIT      = .25   # %
PERCENTAGE_FEEDBACK             = .75   # amount of money made in an investment that is fed back into itself
MORTGAGE                        = 1200  
PROPERTY_TENANT_COUNT           = 2     
PROPERTY_RENT                   = 450 
PROPERTY_DAMAGES_ANNUAL         = 1000  
PROPERTY_UPKEEP_ANNUAL          = 1200  
PROPERTY_MANAGER_ANNUAL         = 1200  
MAX_PROPERTY_COUNT              = 10

