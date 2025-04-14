import json

import json

# 1. Open and read the JSON file
with open('datav2.json', 'r') as file:
    data = json.load(file)  # Load actual JSON content

# 2. Count URLs
print(f"Total URLs: {len(data)}")