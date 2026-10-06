from sklearn.metrics.pairwise import cosine_similarity
from data_set.questions_answers import QuestionsAnswers
from sklearn.feature_extraction.text import TfidfVectorizer

class DailyDishAgent:

    def __init__(self):
        self.questions_answers = QuestionsAnswers()
        self.questions = self.questions_answers.questions
        self.answers = self.questions_answers.answers
        # Initialize the TF-IDF vectorizer to convert text into numerical vectors
        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            max_features=1000
        )
        self.doc_vectors = self.vectorizer.fit_transform(self.questions_answers.questions)
        
    def answer(self, query, threshold=0.08):
        """return the answer from the user's query"""
        # Convert the user query into a TF-IDF vector
        query_vector = self.vectorizer.transform([query])
        # Calculate cosine similarity between the query vector
        similarities = cosine_similarity(
            query_vector,
            self.doc_vectors
        )[0]
        best_idx = similarities.argmax()
        best_score = similarities[best_idx]
        if best_score >= threshold:
            return self.answers[best_idx]
        else:
            return "I don't have information about that. Please contact us directly."
