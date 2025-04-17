import matplotlib.pyplot as plt
import csv
import pandas as pd

steps_list = []
sleep_list = []
calories_list = []
water_list = []

def add_data():
    print("\n--- Enter Today's Data ---")
    steps = int(input("Steps walked: "))
    sleep = float(input("Hours slept: "))
    calories = int(input("Calories consumed: "))
    water = float(input("Water intake (in liters): "))

    steps_list.append(steps)
    sleep_list.append(sleep)
    calories_list.append(calories)
    water_list.append(water)
    print("Data saved!\n")

def bmi_calculator():
    print("\n--- BMI Calculator ---")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    bmi = weight / (height * height)
    print("Your BMI is:", round(bmi, 2))


def show_report():
    print("\n--- Weekly Report ---")
    if len(steps_list) == 0:
        print("No data available yet.")
        return

    print("Average steps:", sum(steps_list) // len(steps_list))
    print("Average sleep (hours):", round(sum(sleep_list) / len(sleep_list), 1))
    print("Average calories:", sum(calories_list) // len(calories_list))
    print("Average water intake (liters):", round(sum(water_list) / len(water_list), 1))

def hydration_reminder():
    print("\nHydration Reminder")
    print("Remember to drink water every 2 hours!\n")

def main():
    while True:
        print("===== HEALTH TRACKER MENU =====")
        print("1. Add Today's Data")
        print("2. Calculate BMI")
        print("3. Show Weekly Report")
        print("4. Hydration Reminder")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_data()
        elif choice == '2':
            bmi_calculator()
        elif choice == '3':
            show_report()
        elif choice == '4':
            hydration_reminder()
        elif choice == '0':
            print("Goodbye! Stay healthy!")
            break
        else:
            print("Invalid option. Please try again.")
main()
