import sys
import zipfile

arg_count = len(sys.argv)

# Make sure the user specified the right number of arguments, and
# help them out if they didn't
if arg_count < 2 or arg_count > 3:
    print("usage: zipextract.py zipfile [memberfile]")
    sys.exit(1)  # Exit program, indicating error code 1

# Name of the ZIP file
zip_filename = sys.argv[1]

if arg_count == 3:
    # Name of the file we want to extract from the ZIP file
    member_filename = sys.argv[2]
else:
    # Sentinel value to let us know it wasn't specified
    member_filename = None

# Open the ZIP file
zf = zipfile.ZipFile(zip_filename)

if member_filename is not None:
    # If the user specified a file to extract, extract it
    zf.extract(member_filename)
else:
    # Otherwise, extract everything
    zf.extractall()