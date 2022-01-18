# Introduction to if statement

#Let us consider the movie "Avengers". This is 13+ movie.

print("Please enter your Year of Birth")
birth_year=int(input())
current_year=2021

age = current_year-birth_year
if (age < 13):
  print('You are under age, you can not watch this movie!')
  print('Wait until you are old enough to watch this movie')
else:
  print("You are old enough to watch Avengers! Enjoy!")
  print("Don't forget to watch its prequels and sequels")

print('Have a nice time!')