RECOMMENDATIONS = {
    "nature_low_warm_yes": "Chiang Mai",
    "nature_low_warm_no": "Cappadocia",
    "nature_low_cold_yes": "Tbilisi",
    "nature_low_cold_no": "Brasov",

    "nature_medium_warm_yes": "Bali",
    "nature_medium_warm_no": "Madeira",
    "nature_medium_cold_yes": "Bled",
    "nature_medium_cold_no": "Zakopane",

    "nature_high_warm_yes": "Costa Rica",
    "nature_high_warm_no": "Maui",
    "nature_high_cold_yes": "Reykjavik",
    "nature_high_cold_no": "Banff",

    "beach_low_warm_yes": "Koh Phangan",
    "beach_low_warm_no": "Koh Lanta",
    "beach_low_cold_yes": "Brighton",
    "beach_low_cold_no": "Varna",

    "beach_medium_warm_yes": "Rio de Janeiro",
    "beach_medium_warm_no": "Zanzibar",
    "beach_medium_cold_yes": "Porto",
    "beach_medium_cold_no": "Bergen",

    "beach_high_warm_yes": "Ibiza",
    "beach_high_warm_no": "Santorini",
    "beach_high_cold_yes": "Vancouver",
    "beach_high_cold_no": "Amalfi Coast",

    "city_low_warm_yes": "Bangkok",
    "city_low_warm_no": "Marrakech",
    "city_low_cold_yes": "Budapest",
    "city_low_cold_no": "Prague",

    "city_medium_warm_yes": "Istanbul",
    "city_medium_warm_no": "Seville",
    "city_medium_cold_yes": "Amsterdam",
    "city_medium_cold_no": "Tallinn",

    "city_high_warm_yes": "Barcelona",
    "city_high_warm_no": "Tokyo",
    "city_high_cold_yes": "London",
    "city_high_cold_no": "Copenhagen"
}


def main():
    print("Welcome to WanderMatch!")
    print("Answer a few questions and I will recommend your next travel destination.")
    print()

    travel_style = str(input("Do you prefer nature, beach, or city? ")).lower().strip()

    while travel_style != "nature" and travel_style != "beach" and travel_style != "city":
        print("I did not understand. Please answer with one of the options shown in the question.")
        travel_style = str(input("Do you prefer nature, beach, or city? ")).lower().strip()

    budget = str(input("What is your budget? low, medium, or high? ")).lower().strip()

    while budget != "low" and budget != "medium" and budget != "high":
        print("I did not understand. Please answer with one of the options shown in the question.")
        budget = str(input("What is your budget? low, medium, or high? ")).lower().strip()

    weather = str(input("Do you prefer warm or cold weather? ")).lower().strip()

    while weather != "warm" and weather != "cold":
        print("I did not understand. Please answer with one of the options shown in the question.")
        weather = str(input("Do you prefer warm or cold weather? ")).lower().strip()

    nightlife = str(input("Do you want nightlife? yes or no? ")).lower().strip()

    while nightlife != "yes" and nightlife != "no":
        print("I did not understand. Please answer with one of the options shown in the question.")
        nightlife = str(input("Do you want nightlife? yes or no? ")).lower().strip()

    key = travel_style + "_" + budget + "_" + weather + "_" + nightlife
    destination = RECOMMENDATIONS[key]

    print()
    print("Your travel profile:")
    print("Travel style: " + travel_style)
    print("Budget: " + budget)
    print("Weather preference: " + weather)
    print("Nightlife: " + nightlife)

    print()
    print("Your recommended destination is:")
    print(destination)

    print()
    print("Thanks for using WanderMatch!")


if __name__ == "__main__":
    main()
