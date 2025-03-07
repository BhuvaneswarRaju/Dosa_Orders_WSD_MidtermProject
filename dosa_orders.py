import json
import sys
import re

def format_phone_number(phone):
    
    cleaned = re.sub(r'\D', '', phone)  
    return f"{cleaned[:3]}-{cleaned[3:6]}-{cleaned[6:]}" if len(cleaned) == 10 else phone

def dosa_orders(input_file):
    
    try:
        with open(input_file, 'r') as f:
            orders = json.load(f)

        customers = {}  
        items = {}

        for order in orders:
            if "phone" not in order or "name" not in order:
                print(f"Skipping invalid order: {order}")
                continue  

            phone = format_phone_number(order["phone"])
            customers[phone] = order["name"]  

            for item in order["items"]:
                name = item.get("name", "Unknown Item")
                price = item.get("price", 0)

                if name not in items:
                    items[name] = {"price": price, "orders": 0}

                items[name]["orders"] += 1

        with open("customers.json", 'w') as f:
            json.dump(customers, f, indent=4)

        with open("items.json", 'w') as f:
            json.dump(items, f, indent=4)

        print("Completed updating please check customers.json and items.json files.")

    except Exception as e:
        print(f"Error processing orders: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python dosa_orders.py <input_file>")
        sys.exit(1)

    input_filename = sys.argv[1]
    dosa_orders(input_filename)