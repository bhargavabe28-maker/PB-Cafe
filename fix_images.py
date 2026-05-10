import re

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Fallbacks
html_content = re.sub(r'src="https://images\.unsplash\.com/[^"]+".*?alt="(.*?)".*?class="menu-item-img"', 
                      lambda m: f'src="assets/images/coffee.png" alt="{m.group(1)}" class="menu-item-img"' if 'Coffee' in m.group(1) or 'Latte' in m.group(1) or 'Roast' in m.group(1) or 'Brew' in m.group(1) or 'Americano' in m.group(1) or 'Cappuccino' in m.group(1) or 'White' in m.group(1) or 'Pour-Over' in m.group(1)
                      else f'src="assets/images/toast.png" alt="{m.group(1)}" class="menu-item-img"' if 'Toast' in m.group(1) or 'Smash' in m.group(1) or 'Melt' in m.group(1) or 'Sourdough' in m.group(1) or 'Fig' in m.group(1) or 'Berry' in m.group(1)
                      else f'src="assets/images/drink.png" alt="{m.group(1)}" class="menu-item-img"', 
                      html_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Fixed broken Unsplash links by falling back to local generated assets.")
