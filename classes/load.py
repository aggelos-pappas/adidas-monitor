import json
import requests
import time 
def load_products():
  totalproducts = 288
  start = 0
  headers = {
      "authority":
      f"www.adidas.nl",
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "accept-language":
      "en-US,en;q=0.9,el;q=0.8",
      "cache-control":
      "max-age=0",
      "pragma":
      "no-cache",
      "sec-ch-ua":
      '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
      "sec-ch-ua-mobile":
      "?1",
      "sec-ch-ua-platform":
      '"Android"',
      "sec-fetch-dest":
      "document",
      "sec-fetch-mode":
      "navigate",
      "sec-fetch-site":
      "none",
      "sec-fetch-user":
      "?1",
      "sec-gpc":
      "1",
      "upgrade-insecure-requests":
      "1",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
  }


  config_file_path = 'config.json'

  with open(config_file_path, 'r') as file:
      config = json.load(file)
    
  if 'products' not in config:
      config['products'] = []
  keywords = ["campus","samba","yeezy", "gazelle", "sean", "sporty","wales"]
  while start < totalproducts:
    url = f"https://www.adidas.nl/api/plp/content-engine?query=shoes-new_arrivals&start={start}"
    datar = requests.get(url,
                              headers=headers,
                              timeout=10)
    data = datar.json()
    for item in data["raw"]["itemList"]["items"]:
      name = item["displayName"]
      if any(keyword in name.lower() for keyword in keywords): 
        sku = item["productId"]
        product = {
          "region": "nl",
          "pid": f"{sku}"
        }
        
        if product not in config['products'] : 
          config['products'].append(product)
      time.sleep(1)


    
    with open(config_file_path, 'w') as file:
      json.dump(config, file, indent=4)

    start += 48
    