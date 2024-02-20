import json
sample_data = "C:/Users/user/Downloads/sample-data.json"
with open(sample_data, 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<40} {:<20} {:<8}".format("DN", "Description", "Speed"))
print("-" * 80)

for item in data['imdata'][:3]:
    attributes = item['l1PhysIf']['attributes']
    print("{:<40} {:<20} {:<8}".format(
        attributes['dn'],
        attributes['descr'],
        attributes['speed'],
        attributes['mtu']
    ))