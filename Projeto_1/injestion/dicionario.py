from collections import namedtuple
from Projeto_1.settings import Config

dataset = namedtuple('dataset', ['lista', 'arquivos'])

mapa = [
    dataset('order_items',
            Config.olist_order_items),
    dataset('sellers',
            Config.olist_sellers),
    dataset('orders',
            Config.olist_orders),
    dataset('customer',
            Config.olist_customer)
]
