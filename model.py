import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel , cosine_similarity, cosine_distances
movies_data=pd.read_csv("Nlp with images.csv")
indexed = pd.Series(data= movies_data.index ,index=movies_data["Movie Title"])
tfidf = TfidfVectorizer()
def movies(name,n=10):
    try:
        matrixs = tfidf.fit_transform(movies_data["genre"])
        simalar=linear_kernel(matrixs[indexed[name]],matrixs)
        movies_data["similar"] = simalar[0]
        ans=movies_data.sort_values(by="similar",ascending=False)
        result=[]
        for i in range(0,n):
            res={}
            res["Movies"]=ans["Movie Title"][i]
            res["Rating"]=ans["Ratinng"][i]
            res["Genere"]=ans["genre"][i]
            res["Image"]=ans["img"][i]
            result.append(res)
        return result
    except:
        return 0
