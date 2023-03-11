import numpy as np
import os

# assign directory
directory = "/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Assignment 1/files"

# iterate over files in
# that directory
for filename in sorted(os.listdir(directory)):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        with open(f) as f:
            print(filename)
            string = f.read().lower()
            print(string)
            tokens = string.split()
            print(tokens)
            # df = pd.DataFrame(data)
            # df.to_csv(r"/Users/macbookair/Documents/UNIC STUDIES/Machine Learning and Data Mining I/Assignment 1/anwser.csv", index=False, header=True)
            # print(df)

