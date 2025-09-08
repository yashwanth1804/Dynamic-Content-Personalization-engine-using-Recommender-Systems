import pandas as pd
from content_library import BANKING_CONTENT

class BankingRecommender:
    def __init__(self):
        self.content_library = BANKING_CONTENT
        self.processed_data = None
    
    def load_processed_data(self, filepath='data/processed_data.csv'):
        #Load the preprocessed customer data
        self.processed_data = pd.read_csv(filepath)
    
    def predict_segment(self, age, job, education='unknown'):
        #Simple rule-based segment prediction for new users
        if age < 30:
            return 0  # Young
        elif age < 50:
            return 1  # Middle-aged
        elif age < 65:
            return 2  # Senior
        else:
            return 3  # Premium
    
    def get_recommendations(self, user_profile):
       #Get personalized recommendations based on user profile
        segment = user_profile.get('segment', 0)
        
        if segment not in self.content_library:
            segment = 0  # Default to young segment
        
        recommendations = self.content_library[segment].copy()
        recommendations['confidence_score'] = self.calculate_confidence(user_profile, segment)
        
        return recommendations
    
    def calculate_confidence(self, user_profile, segment):
        #Simple confidence score based on profile match
        base_confidence = 0.75
        
        # Adjust confidence based on age match
        age = user_profile.get('age', 25)
        expected_age_ranges = {0: (18, 30), 1: (30, 50), 2: (50, 65), 3: (65, 100)}
        
        if segment in expected_age_ranges:
            min_age, max_age = expected_age_ranges[segment]
            if min_age <= age <= max_age:
                base_confidence += 0.15
        
        return round(min(base_confidence, 1.0), 2)
    
    def get_similar_customers(self, user_segment, limit=5):
        #Find similar customers from processed data
        if self.processed_data is None:
            return []
        
        similar_customers = self.processed_data[
            self.processed_data['customer_segment'] == user_segment
        ].head(limit)
        
        return similar_customers[['age', 'job', 'education']].to_dict('records')

# Test the recommender
if __name__ == "__main__":
    recommender = BankingRecommender()
    recommender.load_processed_data()
    
    # Test recommendation
    test_user = {'age': 28, 'job': 'technician', 'segment': 0}
    recommendations = recommender.get_recommendations(test_user)
    
    print(f"Recommendations for {recommendations['segment_name']}:")
    for product in recommendations['products']:
        print(f"- {product['name']}: {product['description']}")
