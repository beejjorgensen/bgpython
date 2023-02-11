import zipfile

# Important: make sure example.zip is in the same directory
# as this program!

zf = zipfile.ZipFile('example.zip')

zf.printdir()