import os

# Install packages in list
with open('packagelist.txt') as file:
	lines = map(str.strip, file.readlines())
	packages = "\" \"".join(lines)
	cmd = "apm install \"" + packages + "\"" 
	print(cmd)
	os.system(cmd)
