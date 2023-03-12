import numpy as np
import pprint
import pandas as pd
import os
import re


words_to_cut = {'to', 'is', 'a', 'the', 'of', 'as', 'and'}
vocabulary = []
all_files_tokens = []


def unique_words(sequence):
    seen = set()
    return [x for x in sequence if not (x in seen or seen.add(x))]


def cut_stopwords(sequence):
    return [word for word in sequence if not (word in words_to_cut)]


def vectorize(tokens):
    vect = []
    for word in vocabulary:
        vect.append(1 if word in tokens else 0)
    return vect


# assign directory
directory = "/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Data_representation/files"

files_in_directory = filter(lambda c: c[0] != '.', os.listdir(directory))
# iterate over files in
# that directory
for file_index, filename in enumerate(sorted(files_in_directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f) as f:
            string = f.read().lower()
            all_files_tokens.extend([re.findall(r"\w+|[^.,!?;:'*`~@=(){}\w\s]", string, re.UNICODE)])
            all_files_tokens[file_index] = cut_stopwords(all_files_tokens[file_index])
            all_files_tokens[file_index] = unique_words(all_files_tokens[file_index])
            vocabulary += all_files_tokens[file_index]
vocabulary = unique_words(vocabulary)
pprint.pprint(vocabulary)

table_to_csv = [vocabulary]

for file_tokens in all_files_tokens:
    table_to_csv.append(vectorize(file_tokens))

df = pd.DataFrame(table_to_csv)

df.to_csv(r"/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Data_representation/anwser.csv", sep=';', index=False, header=False)

print(df)
