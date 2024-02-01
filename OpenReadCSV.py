# Project: Opening and Reading CSV Files
# Arlo
# 1/31/2024

import csv

def get_user_name():
  return input("What is your name? ")

def get_user_age():
  return input("What is your age? ")

def get_user_city():
  return input("Which city are you from? ")

def get_user_position():
  return input("What is your work position? ")

def append_to_csv(row_data):
  with open('positions.csv', 'a', newline='') as position:
    writer = csv.writer(position)
    print("Data appended to CSV file.")

def main():
  user_name = get_user_name()
  user_age = get_user_age()
  user_city = get_user_city()
  user_position = get_user_position()
  row_data = [user_name,user_age,user_city,user_position]
  append_to_csv(row_data)

if __name__ == "__main__":
  main()
