import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    olist_sellers = os.environ.get('olist_sellers')
    olist_order_items = os.environ.get('olist_order_items')
    olist_customer = os.environ.get('olist_customers')
    olist_orders = os.environ.get('olist_orders')