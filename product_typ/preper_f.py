import pandas as pd
from bs4 import BeautifulSoup
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

class PreperData:
    def __init__(self, data):
        self.data = data
        self.model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

    def preper_data(self):
        drop_columns = ["review_date_creation", "review_date_last_update", "username", "URL", "review_title"]
        self.data = self.data.drop(columns=drop_columns)
        self.data = self.data.dropna(subset=["review_content"])
        
        # Filtrer les critiques trop courtes ou sans sens {jai utiliser le AI pour ce filtrer}
        self.data = self.data[self.data["review_content"].str.len() > 20]
        
        
        self.data["review_embedding"] = None
        return self.data
    # POUR CETTE FONTION JAI BEIN UTILISER AI POUR FAIRE LE CLEANING
    def clean_special_character(self, text):
        if not isinstance(text, str):
            return ""
        html_pattern = re.compile(r'<[^>]+>')
        if html_pattern.search(text):
            return BeautifulSoup(text, "html.parser").get_text(separator=" ")
        else:

            text = re.sub(r'\n+', ' ', text)
            text = re.sub(r'\s+', ' ', text)
            return text.strip()

    def transform_data(self):
        self.data["review_embedding"] = self.data["review_content"].apply(lambda x: self.model.encode(x))
        return self.data

    def transform_input_cretique(self, input_cretique):
        return self.model.encode(input_cretique)
    
    def find_top_5_similar_reviews(self, input_cretique, similarity_threshold=0.6):
        input_cretique_embedding = self.transform_input_cretique(input_cretique)
        similarities = []
        for i, embedding in enumerate(self.data["review_embedding"]):
            similarity = cosine_similarity([input_cretique_embedding], [embedding])[0][0]
            similarities.append((i, similarity))
        self.similarities = similarities
        
        filtered_similarities = [(i, score) for i, score in similarities if score > similarity_threshold]
        
        if not filtered_similarities:
            print(f"Aucune critique trouvée avec une similarité > {similarity_threshold}")
            filtered_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]
        
        top_5 = sorted(filtered_similarities, key=lambda x: x[1], reverse=True)[:5]
        results = []
        for i, score in top_5:
            results.append({
            "index": i,
            "similarity": score,
            "review": self.data.iloc[i]["review_content"]
        })
        return pd.DataFrame(results)
