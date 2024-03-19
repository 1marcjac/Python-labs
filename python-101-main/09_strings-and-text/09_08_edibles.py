# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
#print (len(s))
#print (s.rfind('flour'))
print (s[68:73:1])
#print (s.rfind ('egg'))
print (s[26:29:1]+''+s[74])
#print (s.rfind ('s'))
#print (s.rfind ('butter'))
print (s[57:63:1])
#print (s.rfind('grap'))
print (s[5:9:1]+''+s[11]+''+s[74])