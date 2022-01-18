# variables: A programmer's perspective

# sample comment
# all statements starting with '#' are ignored by computer
ram_bank_balance=1000000
ram_loan=100000

laxman_bank_balance=500000
laxman_loan=50000

net_income=ram_bank_balance + laxman_bank_balance
net_liability=ram_loan+laxman_loan

final_value=net_income-net_liability # can be +/-

print("So, the family has", final_value)