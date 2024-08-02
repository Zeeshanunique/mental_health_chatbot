import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

def load_data():
    # Load dataset
    data = pd.read_csv('./IMDB_Dataset.csv')
    data['review'] = data['review'].apply(lambda x: x.lower())  # convert to lowercase
    return data

def train_model(data):
    # Split data into train and test sets
    train_data, _, train_labels, _ = train_test_split(data['review'], data['sentiment'], test_size=0.2, random_state=42)
    
    # Create a text processing and classification pipeline
    model = make_pipeline(CountVectorizer(), MultinomialNB())
    
    # Train the model
    model.fit(train_data, train_labels)
    return model

def save_model(model):
    # Save the model
    joblib.dump(model, './movie_review_classifier.joblib')

def main():
    data = load_data()
    model = train_model(data)
    save_model(model)
    print("Model trained and saved successfully.")

if __name__ == "__main__":
    main()
