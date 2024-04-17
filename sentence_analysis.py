# Write a script that takes a sentence from the user and returns:
#the number of lower case letters" 
#the number of uppercase letters
#the number of punctuations characters
#the total number of characters
#Use a dictionary to store the count of each of the above.
#Note: ignore all spaces.


sentence = input('Enter a sentence and I will return the character and punctuaiton cunts for you.')
def analyze_sentence(sentence):

#remove spaces for an accurate acount 
    sentence = sentence.replace(" ","")

#initialize dictionary to hold counts
    counts = {
    'lower_case': 0,
    'upper_case': 0,
    'punctuation':0,
    'total_chars': len(sentence)

}
# Define a string of punctuation characters for comparison
    punctuation_chars = r"!\#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

# Iterate through each character in the sentence
    for char in sentence:
        if char.islower():
            counts["lower_case"] += 1
        elif char.isupper():
            counts["upper_case"] += 1
        elif char in punctuation_chars:
            counts["punctuation"] += 1
    return counts

# Example usage
print(sentence)
result = analyze_sentence(sentence)
print(f"Upper case: {result['upper_case']}, "
      f"Lower case: {result['lower_case']}, "
      f"Punctuation: {result['punctuation']}, "
      f"Total chars (excluding spaces): {result['total_chars']}")