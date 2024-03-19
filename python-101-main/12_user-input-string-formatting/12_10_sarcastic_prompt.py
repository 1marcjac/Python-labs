# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

presidential_candidate = input('who are you voting for in 2024?: ') 

sarcastic_version = str("")

for i, char in enumerate (presidential_candidate):
    if i % 2 == 0 :
        sarcastic_version += char.lower()
    else:
        sarcastic_version += char.upper()
print(sarcastic_version)