import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "The Araku Signature Latte": "https://loremflickr.com/400/400/latte",
    "Banjara Hills Dark Roast": "https://loremflickr.com/400/400/black,coffee",
    "Velvet Flat White": "https://loremflickr.com/400/400/flat,white,coffee",
    "Malabar Spice Cappuccino": "https://loremflickr.com/400/400/cappuccino",
    "Artisanal Pour-Over": "https://loremflickr.com/400/400/pourover,coffee",
    "Midnight Cold Brew": "https://loremflickr.com/400/400/cold,brew,coffee",
    "Hyderabad Hazelnut Frappé": "https://loremflickr.com/400/400/frappe",
    "Iced Sea Salt Mocha": "https://loremflickr.com/400/400/iced,mocha",
    "The Jubilee Iced Americano": "https://loremflickr.com/400/400/iced,americano",
    "Coconut Milk Brew": "https://loremflickr.com/400/400/coconut,coffee",
    "The Avocado Smash": "https://loremflickr.com/400/400/avocado,toast",
    "Truffle Mushroom Melt": "https://loremflickr.com/400/400/mushroom,toast",
    "Pesto Caprese Toast": "https://loremflickr.com/400/400/caprese,toast",
    "Spiced Paneer Sourdough": "https://loremflickr.com/400/400/paneer,toast",
    "Burrata & Honey Fig": "https://loremflickr.com/400/400/fig,toast",
    "The Classic Nutella Berry": "https://loremflickr.com/400/400/nutella,toast",
    "Hyderabad Sunset Fizz": "https://loremflickr.com/400/400/orange,cocktail",
    "Passionfruit Iced Tea": "https://loremflickr.com/400/400/iced,tea",
    "Blueberry Basil Lemonade": "https://loremflickr.com/400/400/blueberry,drink",
    "The Green Detox": "https://loremflickr.com/400/400/green,juice",
    "Wild Rose & Lychee Cooler": "https://loremflickr.com/400/400/pink,drink",
    "Belgian Dark Chocolate Shake": "https://loremflickr.com/400/400/chocolate,shake",
    "Seasonal Mango & Mint Splash": "https://loremflickr.com/400/400/mango,drink"
}

for alt, url in replacements.items():
    # Use re.IGNORECASE just in case there are minor case differences
    pattern = re.compile(rf'<img src="[^"]+" alt="{re.escape(alt)}" class="menu-item-img">', re.IGNORECASE)
    replacement = rf'<img src="{url}?lock=1" alt="{alt}" class="menu-item-img">'
    content = pattern.sub(replacement, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated images to LoremFlickr successfully.")
