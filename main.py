def main():
    print("Welcome to WanderMatch!")
    print("Answer a few questions and I will recommend your next travel destination.")
    print()

    travel_style = input("Do you prefer beach, city, nature, or festival? ")
    activity = input("Do you want relaxing, adventurous, cultural, or party activities? ")
    budget = input("What is your budget? low, medium, or high? ")
    weather = input("Do you prefer warm or cold weather? ")
    nightlife = input("Do you want nightlife? yes or no? ")

    print()
    print("Your travel profile:")
    print("Travel style: " + travel_style)
    print("Activity type: " + activity)
    print("Budget: " + budget)
    print("Weather preference: " + weather)
    print("Nightlife: " + nightlife)

    print()
    print("Your recommended destination is:")

    if travel_style == "beach" and weather == "warm":
        print("Bali, Indonesia")
    elif travel_style == "city" and activity == "cultural":
        print("Tokyo, Japan")
    elif travel_style == "city" and budget == "high":
        print("New York City, USA")
    elif travel_style == "nature" and activity == "adventurous":
        print("Cappadocia, Turkey")
    elif travel_style == "festival" or activity == "party":
        print("Belgium for Tomorrowland")
    elif travel_style == "city" and budget == "medium":
        print("Barcelona, Spain")
    else:
        print("Paris, France")

    print()
    print("Thanks for using WanderMatch!")


if __name__ == "__main__":
    main()
