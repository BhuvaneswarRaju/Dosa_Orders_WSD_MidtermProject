# Midterm Project - IS601

## Overview
The main objective of this project is to extract and organize order details. The designed python script reads a JSON file containing order records and generates two separate JSON files called "customers.json" which stores unique customer information by mapping phone numbers to names and "items.json" which lists all ordered items, their prices, and the total number of times each item was purchased.

## How this python script works
- First it reads and processes order data from a JSON file.
- It ensures each phone number appears only once in the customer records.
- It aggregates item details and tracks the number of orders for each product.
- It saves the processed data into both JSON files acccordingly for easy access.

## Required downloads
1. Python (Preferably latest version)
2. Any IDE (Ex: - VS Code, Google Colab)

## Setup & Usage
1. Open the IDE that you installed.
2. Make sure you have Python working in it.
3. Place the script in your project folder.
4. Ensure the JSON file containing order data (example_orders.json) is in the same folder.
5. Now to execute the script, open a terminal, navigate to the script's directory, and run: - python dosa_orders.py example_orders.json

## Result
Now you can see both customers.json and items.json files are created based on data in example_orders.json file.