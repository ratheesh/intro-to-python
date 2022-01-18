name1 = input()
dob1  = input()
name2 = input()
dob2 = input()

yr1 = int(dob1[-4:])
yr2 = int(dob2[-4:])
if (yr1 < yr2):
  dob = 2
elif (yr1 > yr2):
  dob = 1
else:
  dob = 0

if (dob == 0):
  mm1 = int(dob1[3:5])
  mm2 = int(dob2[3:5])
  if (mm1 < mm2):
    dob = 2
  elif (mm1 > mm2):
    dob = 1
  else:
    dob = 0
  
  if (dob == 0):
    dd1 = int(dob1[0:2])
    dd2 = int(dob2[0:2])
    if (dd1 < dd2):
      dob = 2
    elif (dd1 > dd2):
      dob = 1
    else:
      dob = 0

if (dob == 1):
  print(name1)
elif (dob == 2):
  print(name2)
if (dob == 0):
  if (name1 < name2):
    print(name1)
  else:
    print(name2)
