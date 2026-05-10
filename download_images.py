import os
import re
import urllib.request

# Ensure the assets/images directory exists
os.makedirs('assets/images', exist_ok=True)

with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Find all unsplash image URLs
pattern = r'src="(https://images\.unsplash\.com/[^"]+)" alt="([^"]+)"'
matches = re.findall(pattern, html_content)

for i, (url, alt_text) in enumerate(matches):
    # Create a safe filename from the alt text
    safe_name = re.sub(r'[^a-zA-Z0-9]', '_', alt_text).lower()
    filename = f"assets/images/menu_{safe_name}.jpg"
    
    print(f"Downloading {alt_text}...")
    try:
        urllib.request.urlretrieve(url, filename)
        # Replace the URL in HTML with the local file path
        html_content = html_content.replace(url, filename)
        print(f"Saved to {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Save the updated HTML
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Finished downloading images and updating index.html!")
