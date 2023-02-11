multtable = []   # Will contain rows

for row_num in range(13): # 0-12, inclusive
    row = []              # Will hold products for this row
    multtable.append(row) # Add it to the table

    for col_num in range(13):
        row.append(row_num * col_num) # Add product to the row

print(multtable[5][6])    # 30
print(multtable[6][5])    # 30
print(multtable[4][7])    # 28
print(multtable[0][0])    # 0
print(multtable[12][12])  # 144

# Test to verify ALL values are correct:

for row_num in range(13):
    for col_num in range(13):
        product = row_num * col_num
        if multtable[row_num][col_num] != product:
            print(f"Bad data: {row_num} x {col_num} != {product}")

# No news is good news
