import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

list_of_texts = []
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
            string = f.read()
            list_of_texts.append(string)

CountVec = CountVectorizer(ngram_range=(1, 1),  # to use bigrams ngram_range=(2,2)
                           stop_words='english')
# transform
Count_data = CountVec.fit_transform(list_of_texts)

# create dataframe
cv_dataframe = pd.DataFrame(Count_data.toarray(), columns=CountVec.get_feature_names_out())
cv_dataframe.to_csv(r"/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Data_representation/anwser_scikit.csv", sep=';', index=False, header=True)
print(cv_dataframe)



