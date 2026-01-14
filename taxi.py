fare = 0
def taxi():
  try:
    dis = int(input("Enter distance in km: "))
    if 0 < dis <= 10:
     fare = 15000 + (dis - 1) * 13500
     print("Fare: ", fare)
    elif 10 < dis < 120:
     fare = 15000 + (dis - 1) * 13500 + (dis - 10) * 11000
     print("Fare: ", fare)
    elif dis >= 120:
     fare = 15000 + (dis - 1) * 13500 + (dis - 10) * 11000 * 0.9
     print("Fare: ", fare)
  except:
    print("Invalid distance")
    taxi()
taxi()