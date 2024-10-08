import datetime as dt








if __name__ == "__main__":
  today = dt.datetime.now()
  print(today)
  print(today.strftime("%y-%m-%d %H:%M:%S"))
  print(today.year)
  print(today.month)
  print(today.day)
  print(today.hour)
  print(today.minute)
