import shopify
import json
from flask import Flask, render_template

app = Flask(__name__)

with open('.env', 'r') as f:
    parsed_json = json.load(f)

API_KEY = parsed_json['API_KEY']
PASSWORD = parsed_json['PASSWORD']
SHOP_NAME = parsed_json['SHOP_NAME']

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

# products = shopify.Product.find()
# for product in products:
#     print product.title

def orders():
    orders = shopify.Order.find()
    for order in orders:
        customer_id = order.customer.id
        print customer_id
        customer = shopify.Customer.find(customer_id)
        print customer.first_name + ' ' + customer.last_name + " - " + customer.note



@app.route("/")
def hello():
    # orders()
     return render_template('hello.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
