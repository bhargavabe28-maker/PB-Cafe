import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def inject_price(match):
    full_match = match.group(0)
    data_price = match.group(1)
    return f'<span class="price">₹{data_price}</span>\\n                                {full_match}'

content = re.sub(r'<button class="order-btn" data-item="[^"]+" data-price="(\d+)">Order It</button>', inject_price, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Prices injected into menu cards.")
