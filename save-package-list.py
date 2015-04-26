import os
package_dir = "packages"
if not os.path.isdir(package_dir):
    print("This script must be run from the .atom folder.")
    print("(Could not find package directory)")
    exit(1)

packages = []
ignored_packages = [
    'cheesy-dark-syntax'
]

# Read package list
for p in os.listdir(package_dir):
    if p[0] == '.' or not os.path.isdir(package_dir + "/" + p):
        continue
    if p in ignored_packages:
        continue
    packages.append(p);

# Save to file
with open('packagelist.txt', 'w') as file:
    for p in packages:
        file.write(p + "\n")
