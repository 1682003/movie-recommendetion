                PANDAS 

1 data ko smjhna h to pd.columns se saare columns pta krlo or unhe copy krdo gpt pe

2 data me null check krlo , jyada hee null h unhe mt lo, apan ne 25 me se 6 column liye hai 
3 jb bhi data m change kro inplace=true krdo , jisse original data m change ho, naki koi naya data bane
   df.dropna(inplace=True)  #means har wo row delete krdo jisme ek bhi value none h
   df = df.reset_index(drop = True)   #[delete krne se indices bigad jaati hai like 1,3,6 unhe wapis 0,1,2 krne k liye kra]
   indices = pd.Series(df.index,index = df['title']).drop_duplicates()   #indices banaye h, jo dict ki keys ki trh work krenge


                  NLP

#Punctuation → symbols that separate/mark text. , inko remove krna hota hai nlp me(taaki)
  #stopwards - the,of,is,are etc [movie recomend me unncesary noise hai jo hum hata denge]
  #lematizers- runing or run is same, taaki dono ko alag consider na kare

import pickle- #This cell packages/saves the results of your expensive preprocessing
and ML work so your final application can load them directly instead of rebuilding everything every time.



                 SK-LEARN

1. TfidfVectorizer , #converts words into nums , example "action'=0.2
2. cosine similarity
"""Movie A → [0.2, 0.5, 0.1, 0.8, ...] 
Movie B → [0.3, 0.4, 0.1, 0.7, ...]
i.e. CS is 0.91  """

it is working on cos value, similar hai to cos(0^) mtlb 1, different hain to cos(90^) mtlb 0
jisse hum similarity score pta kr rhe hein


3. tfidf = TfidfVectorizer(max_features=50000,ngram_range=(1,2),stop_words='english')
"""tags the unhe vector m kr convert kr diya, 45,447 rows m each row ka vector bngea jisme each ki size 50000 hogi,
i.e. matrix shape is [45,477 * 50000]
"""

4. (tfidf_matrix[idx], tfidf_matrix)  #ek movie ki matrix ko all movie ki matirx se comapre kra


            




             BASIC QUESTION AND ANSWER
1.jaha smj na aaye keh de google kr liya tha
2. summary - MOVIE DATASET- Data Cleaning - Select useful columns - NLP Processing - Combine movie information -
            TF-IDF -   Every movie → numbers -  Cosine Similarity -  Find movies most similar to users movie -
            Recommendation-   FastAPI -  Web/API application


         
