from multiprocessing import Pool
import os
import time

# List containing all of the words in the english language
word_list = []
# List containing all of the word in the english language that are of length 5. Used for testing purposes
word_list5 = []
# List that will ultimately contain all words that can have ever letter removed once and still be a word
successful_word_list = []

# Function that takes a word and a list.  Splits the word into a list of all
# possible sub-words that the word can represent by removing each letter once at a time. Checks if each of these words
# is a word itself, and if true, appends this word to successful_word_list
# Example of sub-words for string: "apple"
#   ["pple", "aple", "aple", "appe", "appl"]
def list_check(word):
    #print(f"Searching for word: {word}")
    possible_words = []
    # Taking the word and breaking it down into all possible substrings that are missing a letter
    for i in range(len(word)):
        if i == 0:
            possible_words.append(word[1:len(word)])
        else:
            possible_words.append(word[0:i] + word[i+1:len(word)])

    # Check if each of the possible substrings exists in list parameter. If it ever doesn't exist, exit immediately
    for possible_word in possible_words:
        if possible_word not in word_list:
            return ""

    # If got here, every sub-string possibility for the word exists in the given list
    return word

# Simple function to split a list into a series of "n" smaller lists
def chunkify(lst,n):
    return [lst[i::n] for i in range(n)]

# Writing all words to word_list
with open('word.txt') as f:
    for word in f.readlines():
        word_list.append(word.strip().lower())
# Writing all words that are of length 5 to word_list5 for testing purposes
for w in word_list:
    if len(w) == 5:
        word_list5.append(w)

print(f"Length of word list: {len(word_list)}")
print(f"Length of word list of words that are length 5: {len(word_list5)}")

# Multiprocessing begins here

#Timing purposes
total_time_start = time.time()

# Starting a bunch of worker processes
pool = Pool(processes=os.cpu_count())

# Writing results to output.txt
with open('output.txt', 'w') as file:
    for result in pool.map(list_check, word_list):
        if not result == "":
            file.write(result + "\n")

total_time_final = time.time() - total_time_start
print(f"Took {(total_time_final)/60:.2f} minutes")
print('Done!')

with open('multiprocessing_analysis.txt', 'w') as file:
    file.write(f"Time taken to solve problem using multiprocessing: {total_time_final/60:.2f} minutes")
