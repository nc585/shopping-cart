# shopping_cart.py

import datetime

import datetime as dt

import csv 

products = [] #TO DO: read from csv file

csv_file_path = "products.csv" # a relative filepath
with open(csv_file_path, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    # reader = csv.reader(csv_file) # if your CSV doesn't have headers
    for row in reader:
        #d = dict(row)
        d = {"id": row["id"], "name": row["name"], "price": float(row["price"])}
        #print(type(d),(d["name"], d["price"])
        products.append(d)

t = datetime.datetime.now()

running_total = 0

product_ids = []
while True:
    selected_id = input("Please select a product id (1-20) or 'DONE' if there are no more items: ")
    if selected_id == "DONE":
        break
    if not selected_id.isdigit():
        print("Please enter a valid product id")
    if int(selected_id) not in range (1,21):
        print("Please enter a valid product id from 1 to 20")
    else:  
        product_ids.append(selected_id)

print("--------------")
print("TRADER NINA'S")
print("WWW.TRADERNINAS.COM")
print("1.202.234.5678")
print("--------------")
print("CHECKOUT AT: " + t.strftime("%Y-%m-%d %H:%M:%S"))
print("--------------")
print("SELECTED PRODUCTS:")

for selected_id in product_ids:
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    price = matching_product["price"]
    running_total = running_total + price
    print("+ " + matching_product["name"] + " " + "($" + str(round(price,2)) + ")")

print("--------------")
print("SUBTOTAL: $", round(running_total,2))
print("DC SALES TAX: $", round(.06*running_total,2))
print("TOTAL AMOUNT DUE: $", round(1.06*running_total,2))
print("--------------")
print("THANK YOU! SEE YOU NEXT TIME!")
print("--------------")