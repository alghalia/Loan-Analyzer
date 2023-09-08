#!/usr/bin/env python
# coding: utf-8

# In[4]:


loan_costs = [500, 600, 200, 1000, 450]
# Print the number of loans from the list
print("The total number of loans from the list =",(len(loan_costs)))


# In[7]:


# Print the total value of the loans

print("the total value of the loans =",(sum(loan_costs)))


# In[8]:


# Print the average loan amount
def average(loan_costs):
    avg = sum(loan_costs)/len(loan_costs)
    return avg

loan_costs = [500, 600, 200, 1000, 450]
average = average(loan_costs)
print("The average loan amount =",average)


# In[27]:


loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}
# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
future_value=loan.get("future_value")
print(future_value)
remaining_months=loan.get("remaining_months")
print(remaining_months)


# In[47]:


# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
Annual_Discount_Rate=.20
present_value =(future_value/(1+Annual_Discount_Rate/12)**remaining_months)
print(round(present_value))


# In[68]:


# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if present_value >= 500:
    print("the loan is worth at least the cost to buy it")

else:
    print("loan is too expensive and not worth the price")


# In[5]:


# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

def calculate_present_value(future_value,remaining_months,annual_discount_rate):
    present_value =(future_value/(1+annual_discount_rate/12)**remaining_months)
    return(present_value)

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
    
annual_discount_rate = 0.20    
present_value = calculate_present_value(
    new_loan["future_value"],
    new_loan["remaining_months"],
    annual_discount_rate)
print(f"The present value of the loan is:{round(present_value)}")

    


# In[654]:


# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = [] 
# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan_price in loans:     
    if (loan_price['loan_price']) <= 500:
        inexpensive_loans.append(loan_price)
        # @TODO: Print the `inexpensive_loans` list
print(inexpensive_loans)


# In[9]:


import csv
from pathlib import Path

inexpensive_loans = [
    {'loan_price': 500, 
     'remaining_months': 13,
     'repayment_interval': 'bullet',
     'future_value': 1000}, 
    
    {'loan_price': 200,
     'remaining_months': 16,
     'repayment_interval': 'bullet',
     'future_value': 1000}

]

header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

output_path = Path("inexpensive_loans.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

# @TODO: Use the csv library and `csv.writer` to write the header row
    csvwriter.writerow(header)

# and each row of `loan.values()` from the `inexpensive_loans` list.
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())
   

