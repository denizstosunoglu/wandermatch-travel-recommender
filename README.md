# WanderMatch: A Travel Destination Recommender 🌍

WanderMatch is a beginner-friendly Python console program that recommends a travel destination based on the user's preferences.

The program asks the user four simple questions about travel style, budget, weather, and nightlife. Based on the user's answers, it creates a unique combination and recommends one destination from 36 possible matches.

## Project File

You can view the main Python file here:

[main.py](main.py)

## Why I Built This Project

I created this project for my Code in Place final project because I love traveling and wanted to build something personal, fun, and useful.

Instead of making a random quiz, I wanted to create a simple travel assistant that gives a destination recommendation based on the user's own preferences.

## How It Works

The program asks the user these four questions:

1. Do you prefer nature, beach, or city?
2. What is your budget? low, medium, or high?
3. Do you prefer warm or cold weather?
4. Do you want nightlife? yes or no?

Each answer becomes part of a key. The program then uses that key to find a matching destination from a dictionary.

For example:

```text
nature + medium + warm + yes = Bali
city + high + cold + no = Copenhagen
beach + high + warm + yes = Ibiza
```

## Features

- Asks the user travel-related questions
- Recommends a destination from 36 possible combinations
- Uses valid answer checking
- If the user enters an unexpected answer, the program asks the question again
- Runs in the console
- Uses beginner-friendly Python code

## Python Concepts Used

- `input()`
- `print()`
- Variables
- Strings
- Dictionaries
- `if` statements
- `while` loops
- Functions
- Basic input validation

## Example Output

```text
Welcome to WanderMatch!
Answer a few questions and I will recommend your next travel destination.

Do you prefer nature, beach, or city? nature
What is your budget? low, medium, or high? medium
Do you prefer warm or cold weather? warm
Do you want nightlife? yes or no? yes

Your travel profile:
Travel style: nature
Budget: medium
Weather preference: warm
Nightlife: yes

Your recommended destination is:
Bali

Thanks for using WanderMatch!
```

## Example With Invalid Input

```text
Do you prefer nature, beach, or city? mountain
I did not understand. Please answer with one of the options shown in the question.

Do you prefer nature, beach, or city? nature
```

## How to Run

1. Download or clone this repository.
2. Open the project folder.
3. Run the program with Python:

```bash
python main.py
```

or:

```bash
python3 main.py
```

## Project Status

This project was created as a final project for Code in Place.

## Author

Created by Deniz Tosunoğlu.
