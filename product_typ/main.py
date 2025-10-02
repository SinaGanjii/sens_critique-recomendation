from preper_f import PreperData
import pandas as pd

def main():
    print("=== Système de Recommandation de Films ===")
    print("Choisissez le film:")
    print("1. Fight Club")
    print("2. Interstellar")
    
    while True:
        movie_choice = input("Votre choix (1 ou 2): ").strip()
        if movie_choice == "1":
            movie_name = "Fight Club"
            dataset_file = "fightclub_critiques.csv"
            break
        elif movie_choice == "2":
            movie_name = "Interstellar"
            dataset_file = "interstellar_critique.csv"
            break
        else:
            print("Veuillez choisir 1 ou 2.")
    
    print(f"\nChargement des critiques pour {movie_name}...")
    
    data = pd.read_csv(dataset_file, encoding="utf-8")
    preper_data = PreperData(data)
    preper_data.preper_data()
    preper_data.data["review_content"] = preper_data.data["review_content"].apply(preper_data.clean_special_character)

    preper_data.transform_data()
    
    print(f"Système de recommandation prêt pour {movie_name}!\n")
    print("Options disponibles:")
    print("- Entrez votre critique pour analyser")
    print("- Tapez 'switch' pour changer de film")
    print("- Tapez 'exit' pour quitter\n")
    
    while True:
        user_input = input(f"Entrez votre critique pour {movie_name}: ").strip()
        
        if user_input.lower() == 'exit':
            print("Au revoir!")
            break
        
        if user_input.lower() == 'switch':
            print("\nRetour au menu de sélection de film...")
            main()
            break
        
        if not user_input:
            print("Veuillez entrer une critique valide.")
            continue
        
        try:
            print(f"\nRecherche de critiques similaires à: '{user_input}'")
            # la on peut manuelement modifier les elment quon veutm je veut mettre ST sur 0,6, et senti sur 0,6 
            similar_reviews = preper_data.find_top_5_similar_reviews(user_input, similarity_threshold=0.6, sentiment_label_match=True, sentiment_score_threshold=0.6)
            
            print(f"\nSentiment de votre critique: {similar_reviews.iloc[0]['input_sentiment']} (score: {similar_reviews.iloc[0]['input_sentiment_score']:.3f})")
            print("\nTop 5 critiques similaires:")
            for idx, row in similar_reviews.iterrows():
                print(f"Score de similarité: {row['similarity']:.3f}")
                print(f"Sentiment: {row['sentiment_label']} (score: {row['sentiment_score']:.3f})")
                print(f"Critique: {row['review']}")
                
        except Exception as e:
            print(f"Erreur lors de la recherche: {e}")
        
        print()

if __name__ == "__main__":
    main()
