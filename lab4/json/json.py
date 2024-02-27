import json


with open('sample-data.json') as file:
    data = json.load(file)

imdata = data.get('imdata', [])

print("Interface Status")
print("=" * 100)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 100)

for data in imdata:
    phys_if = data.get('l1PhysIf', {})
    attributes = phys_if.get('attributes', {})
    dn = attributes.get('dn', '')
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', 'unspecified')

    print("{:<50} {:<20} {:<10} {:<10}".format(dn, descr, speed, mtu))


