import matplotlib.pyplot as plt
# import csv
# import pandas as pd


# In-memory data storage
covid_data = []

def add_daily_data():
    date = input("Enter date (YYYY-MM-DD): ")
    city = input("Enter city: ")
    cases = int(input("Enter number of new cases: "))
    recoveries = int(input("Enter number of recoveries: "))
    deaths = int(input("Enter number of deaths: "))

    entry = {
        "date": date,
        "city": city.lower(),
        "cases": cases,
        "recoveries": recoveries,
        "deaths": deaths
    }

    covid_data.append(entry)
    print(" Data added successfully.\n")



def analyze_risk_zones():
    print("\n ~~~Risk Zone Analysis~~~")
    summary = {}

    for record in covid_data:
        city = record["city"]
        summary.setdefault(city, {"cases": 0})
        summary[city]["cases"] += record["cases"]

    for city, data in summary.items():
        cases = data["cases"]
        if cases > 1000:
            print(city.title()+ "is a High Risk Zone")
        elif cases > 500:
            print(city.title()+ "is a Medium Risk Zone")
        else:
            print(city.title()+ "is a Low Risk Zone")
    print()

def show_trend(city):
    city = city.lower()
    city_data = [r for r in covid_data if r["city"] == city]
    if not city_data:
        print(" No data for that city.\n")
        return

    print("\n--- Trend for" + city.title() )
    city_data.sort(key=lambda x: x["date"])
    for entry in city_data:
        print(f"{entry['date']}: Cases={entry['cases']} | Recoveries={entry['recoveries']} | Deaths={entry['deaths']}")
    print()

def predict_hotspots():
    print("\n--- Hotspot Prediction ---")
    recent_data = {}

    for record in reversed(covid_data):
        city = record["city"]
        if city not in recent_data:
            recent_data[city] = []
        if len(recent_data[city]) < 3:
            recent_data[city].append(record["cases"])

    found = False
    for city, recent_cases in recent_data.items():
        if len(recent_cases) == 3:
            avg = sum(recent_cases) / 3
            if avg > 100:
                print(city.title()+ "is a potential HOTSPOT (avg" + avg + "cases/day)")
                found = True

    if not found:
        print("No hotspots predicted today.\n")


def save_to_file():
    with open("covid_data.txt", "w") as f:
        for record in covid_data:
            line = f"{record['date']},{record['city']},{record['cases']},{record['recoveries']},{record['deaths']}\n"
            f.write(line)
    print("Data saved to covid_data.txt\n")

  


def menu():
    
    while True:
        print("===== COVID DASHBOARD MENU =====")
        print("1. Add Daily Data")
        print("2. Analyze Risk Zones")
        print("3. Show Trend for a City")
        print("4. Predict Hotspots")
        print("5. Save Data to File")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_daily_data()
        elif choice == "2":
            analyze_risk_zones()
        elif choice == "3":
            city = input("Enter city name: ")
            show_trend(city)
        elif choice == "4":
            predict_hotspots()
        elif choice == "5":
            save_to_file()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
 

menu()
