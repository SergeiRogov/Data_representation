import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

sentence_1 = "This is a good job.I will not miss it for anything"
sentence_2 = "This is not good at all"
sentence_3 = "This is damn ass good"

CountVec = CountVectorizer(ngram_range=(1, 1),  # to use bigrams ngram_range=(2,2)
                           stop_words='english')
# transform
Count_data = CountVec.fit_transform([sentence_1, sentence_2, sentence_3])

# create dataframe
cv_dataframe = pd.DataFrame(Count_data.toarray(), columns=CountVec.get_feature_names_out())
print(cv_dataframe)
