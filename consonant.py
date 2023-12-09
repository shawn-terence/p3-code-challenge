def Value_adder(word):
    # Define vowels
    vowels = 'aeiou'
    # Initialize an empty list to store consonants
    consonant_list = []
    # Initialize an empty string to build the current consonant substring
    current_string = ''

    # Iterate through each character in the input word
    for char in word:
        # Check if the character is not a vowel
        if char not in vowels:
            # If not a vowel, append the character to the current substring
            current_string += char
        else:
            if current_string:
                # Append the current substring to the list
                consonant_list.append(current_string)
            current_string = ''

    # Handle  when the last character in the word is a consonant
    if current_string:
        consonant_list.append(current_string)

    # Initialize max value to have a value of 0
    max_value = 0
    for substring in consonant_list:
        value = 0
        for char in substring:
            # Calculate the  value of the character and add it to the total value
            value += ord(char) - ord('a') + 1
        # Update the maximum value with the maximum of its current value and the value of the current substring
        max_value = max(max_value, value)

    # Return the maximum value of all consonant substrings
    return max_value


print(Value_adder(""))#put any word inside the quotations  