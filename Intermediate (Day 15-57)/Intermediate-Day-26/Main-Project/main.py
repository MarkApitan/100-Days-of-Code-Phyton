# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
"""start of code for main project"""

#TODO 1. Create a dictionary in this format:
import pandas
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet_dict = {row.letter:row.code for (index,row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a Word: ")
word_to_nato_alphabet_list = [nato_alphabet_dict[letter] for letter in user_input.upper() if letter in nato_alphabet_dict]
print(word_to_nato_alphabet_list)