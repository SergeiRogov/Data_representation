import pandas as pd
import os
import re

# a set of unnecessary words
words_to_cut = {'to', 'is', 'a', 'an', 'the', 'of', 'as', 'and', 'in', 'on', 'at'}
vocabulary = []
all_files_tokens = []


def unique_words(sequence):
    '''Function cuts repeated words from a list of words'''
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def cut_stopwords(sequence):
    '''Function cuts words contained in a set "words_to_cut" from a list of words'''
    return [word for word in sequence if not (word in words_to_cut)]


def vectorize(tokens):
    '''Function forms a vector representing words from dictionary contained in a file'''
    vect = []
    for word in vocabulary:
        vect.append(1 if word in tokens else 0)
    return vect


# assign directory
directory = "/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Data_representation/files"

# making sure a list of files in a directory doesn't contain files like .DS_store
files_in_directory = filter(lambda c: c[0] != '.', os.listdir(directory))
# iterate over files in this directory
for file_index, filename in enumerate(sorted(files_in_directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f) as f:
            string = f.read().lower()  # making text lower case
            # splitting into tokens
            all_files_tokens.extend([re.findall(r"\w+|[^.,!?;:'*`~@=(){}\w\s]", string, re.UNICODE)])
            # getting rid of non-essential words
            all_files_tokens[file_index] = cut_stopwords(all_files_tokens[file_index])
            # cutting off repeated words
            all_files_tokens[file_index] = unique_words(all_files_tokens[file_index])
            # adding words to our dictionary
            vocabulary += all_files_tokens[file_index]
# cutting off repeated words in final version of dictionary
vocabulary = unique_words(vocabulary)
# starting to form a table to export - filling first line with words from a dictionary
table_to_csv = [vocabulary]

# adding lines-vectors representing words contained in files
for file_tokens in all_files_tokens:
    table_to_csv.append(vectorize(file_tokens))

df = pd.DataFrame(table_to_csv)
df.to_csv(r"/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Data_representation/anwser.csv", sep=',', index=False, header=False)
print(df)
