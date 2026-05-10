import os
import urllib.request
import random

os.makedirs('assets/images', exist_ok=True)

items_to_update = {
    "Wild Rose & Lychee Cooler": ("assets/images/dish_wild_rose___lychee_cooler.jpg", "https://loremflickr.com/400/400/cocktail,pink"),
    "The Green Detox": ("assets/images/dish_the_green_detox.jpg", "https://loremflickr.com/400/400/green,smoothie"),
    "Spiced Paneer Sourdough": ("assets/images/dish_spiced_paneer_sourdough.jpg", "https://loremflickr.com/400/400/sandwich,paneer"),
    "Iced Sea Salt Mocha": ("assets/images/dish_iced_sea_salt_mocha.jpg", "https://loremflickr.com/400/400/iced,coffee,mocha"),
    "The Araku Signature Latte": ("assets/images/dish_the_araku_signature_latte.jpg", "https://loremflickr.com/400/400/latte,art"),
    "The Jubilee Iced Americano": ("assets/images/dish_the_jubilee_iced_americano.jpg", "https://loremflickr.com/400/400/americano,ice")
}

for name, (filepath, base_url) in items_to_update.items():
    url = f"{base_url}?lock={random.randint(1000, 9999)}"
    print(f"Downloading new image for {name}...")
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"Successfully updated {filepath}")
    except Exception as e:
        print(f"Failed to download {name}: {e}")
