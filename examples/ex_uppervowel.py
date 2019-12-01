s = "The quick brown fox jumps over the lazy dogs."

s2 = ""

for c in s.lower():
	if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
		c = c.upper()

	# A more concise way to write the above line is with "in", something
	# we haven't discussed yet:
	#if c in "aeiou":
	#	c = c.upper()

	# Build the new string a character at at time:
	s2 += c

print(s2)
