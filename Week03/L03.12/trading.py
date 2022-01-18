# Find the profit/loss of each trader working in a trading firm. Information regarding number of traders and no. of transaction in unknown

empID = input('Enter the Employee ID: ')

while empID != '-1':
  profit_loss = 0
  trade = int(input('Enter trade value: '))
  while(trade != 0):
    profit_loss = profit_loss + trade
    trade = int(input('Enter trade value: '))
  print(f'Profit/loss of employee {empID} is ', profit_loss)
  empID = input('Enter the Employee ID: ')

