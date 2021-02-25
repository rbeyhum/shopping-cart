# shopping_cart.py

import os 
import datetime

from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "item"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "fruits", "aisle": "all fruits", "price": 0.79, "price_per": "pound"}
] 
# based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# defining my grocery store by giving it a name, web address, etc.

grocery_name = "SHOPPERS"
grocery_web = "https://www.shoppers.com"
grocery_num = "(202) 398-7642"
grocery_checkout = datetime.datetime.now()

load_dotenv()

TAX_RATE = os.getenv("TAX_RATE", default=0.0875)


price_total = 0
matching_products = []

while True:
    selected_id = input("Please input a product identfier (1-21 are valid), or 'DONE' if there are no more items: ")
    if selected_id.upper() == "DONE":
        break
    elif int(selected_id) > 21 or int(selected_id) < 1:
        print("Please input a valid identifier. You can resume scanning your items!")   

    for item in products:
        if str(item["id"]) == str(selected_id):
            matching_product = item
    if matching_product["price_per"] == "item":
        num = int(input("Please enter the number of items desired: "))
    elif matching_product["price_per"] == "pound":
        num = float(input("Please enter the number of pounds desired: "))
    matching_products.append((matching_product,num))


# printing the final receipt
receipt_content = ""
email_content = ""

receipt_content += "------------------"+"\n" + grocery_name + "\n" + "------------------" + "\n" + "Web: " + grocery_name + "\n" + "Phone: " + grocery_num + "\n" + "Checkout Time: " + grocery_checkout.strftime("%Y-%m-%d %I:%M:%S %p") + "\n" + "------------------" + "\n" + "SHOPPING CART ITEMS: " + "\n"
email_content += "------------------"+"<br>" + grocery_name + "<br>" + "------------------" + "<br>" + "Web: " + grocery_name + "<br>" + "Phone: " + grocery_num + "<br>" + "Checkout Time: " + grocery_checkout.strftime("%Y-%m-%d %I:%M:%S %p") + "<br>" + "------------------" + "<br>" + "SHOPPING CART ITEMS: " + "<br>"
print("------------------")
print(grocery_name)
print("------------------")
print("Web: ",grocery_web)
print("Phone: ",grocery_num)
print("Checkout Time: ",grocery_checkout.strftime("%Y-%m-%d %I:%M:%S %p"))
print("------------------")
print("SHOPPING CART ITEMS: ")


for product in matching_products:
    matching_product = product[0]
    num = product[1]
    price_total += matching_product["price"]*num
    receipt_content += "+"+str(num) + " "+ matching_product["name"]+"("+str(to_usd(matching_product["price"]))+")" + "\n"
    email_content += "+"+str(num) + " "+ matching_product["name"]+"("+str(to_usd(matching_product["price"]))+")" + "<br>"
    print("+",num, matching_product["name"],"(",to_usd(matching_product["price"]),")") 



tax = price_total*float(TAX_RATE)
total_price = price_total + tax
receipt_content += "------------------" + "\n" + "SUBTOTAL: " + to_usd(price_total) +"\n" + "TAX: " + to_usd(tax) + "\n" + "TOTAL: " + to_usd(total_price) + "\n" + "------------------" + "\n" + "THANK YOU, SEE YOU AGAIN SOON!" + "\n" + "------------------"
email_content += "------------------" + "<br>" + "SUBTOTAL: " + to_usd(price_total) +"<br>" + "TAX: " + to_usd(tax) + "<br>" + "TOTAL: " + to_usd(total_price) + "<br>" + "------------------" + "<br>" + "THANK YOU, SEE YOU AGAIN SOON!" + "<br>" + "------------------"
print("------------------")
print("SUBTOTAL: ",to_usd(price_total))
print("TAX: ",to_usd(tax))
print("TOTAL: ",to_usd(total_price))
print("------------------")
print("THANK YOU, SEE YOU AGAIN SOON!")
print("------------------")


# ask customer whether customer wants copy of their receipt as a text file 
copy = input("Would you like to receive a copy of your receipt as a text file [y/n]?")
if copy == "y":
    file_name = "my_receipt.txt" # a relative filepath
    with open(file_name, "w") as file: # "w" means "open the file for writing"
        file.write(receipt_content)
elif copy == "n": 
    exit


# ask customer whether they would like a copy of their receipt sent via email using the sendgrid package 

email = input("Would you like to receive a copy of your receipt sent to your email? [y/n]")
if email == "y":
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
    print("CLIENT:", type(client))

    subject = "Your Receipt from Shoppers"
    html_content = email_content
    print("HTML:", html_content)

    # FYI: we'll need to use our verified SENDER_ADDRESS as the `from_email` param
    # ... but we can customize the `to_emails` param to send to other addresses
    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err) 
elif email == "n":
    exit