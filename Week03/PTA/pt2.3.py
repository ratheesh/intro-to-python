teamA_1in_score = int(input())
teamA_1in_wkts = int(input())
teamA_2in_score = int(input())
teamA_2in_wkts = int(input())
teamB_1in_score = int(input())
teamB_1in_wkts = int(input())
teamB_2in_score = int(input())
teamB_2in_wkts = int(input())

if (teamB_2in_wkts == 10):
  if (teamA_1in_score + teamA_2in_score > teamB_1in_score + teamB_2in_score):
    print('Team A')
elif (teamA_1in_score + teamA_2in_score < teamB_1in_score + teamB_2in_score):
  print('Team B')
else:
  print('DRAW')

