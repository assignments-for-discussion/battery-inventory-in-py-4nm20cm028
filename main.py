
def count_batteries_by_health(present_capacities):
   
  battery_life_dict = {
    "healthy": 0,
    "exchange": 0,
    "failed": 0
  }

  rated_capacity = 120 

  for i in present_capacities:
    SoH = (100*i)/rated_capacity

    if SoH<=100 and SoH>80: 
      battery_life_dict["healthy"]+=1
    elif SoH<=80 and SoH>62:
      battery_life_dict["exchange"]+=1
    elif SoH<=62 and SoH>=0:
      battery_life_dict["failed"]+=1


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
