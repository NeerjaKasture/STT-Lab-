import json
from collections import defaultdict

with open("capture.json", "r", encoding="utf-16") as f:
    content = f.read().strip()

dependencies = json.loads(content)

fan_in = defaultdict(int)
fan_out = defaultdict(int)

for module, data in dependencies.items():
    imported_by = data.get("imported_by", [])
    imports = data.get("imports", [])

    fan_in[module] = len(imports)  
    fan_out[module] = len(imported_by) 

print("\n Fan-in and Fan-out analysis:")
print("Module".ljust(50), "Fan-in".ljust(10), "Fan-out")
print("=" * 80)
for module in sorted(set(fan_in.keys()).union(set(fan_out.keys()))):
    print(module.ljust(50), str(fan_in[module]).ljust(10), fan_out[module])
