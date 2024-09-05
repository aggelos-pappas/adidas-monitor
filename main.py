# written by SD
# twitter.com/ciphersuites

from classes.adidas_monitor import AdidasMonitor
from classes.load import load_products
import json
import time 

try:
    config = json.load(open('config.json'))


    refresh_time = config['refresh_time']
    products = config['products']

    print("Loaded %d proxies"%len(open('proxies.txt').readlines()))

    #load_products()
    for product in products:
        monitor = AdidasMonitor(product['region'], product['pid'], refresh_time)
        
        monitor.start()
        time.sleep(3)

# case where config file is missing
except FileNotFoundError:
    print("FATAL ERROR: Could not find config file")

# case where config file is not valid json
except json.decoder.JSONDecodeError:
    print("FATAL ERROR: Could not read config file, invalid JSON")

# case where we don't know the cause of the exception
except Exception as e:
    print("Unknown error: " + str(e))