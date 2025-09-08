from flask import Flask, render_template, request, jsonify 
from recommender import BankingRecommender  
from content_library import BANKING_CONTENT
import json

app = Flask(__name__)
recommender = BankingRecommender()
recommender.load_processed_data()

@app.route('/')
def home():
    #Homepage with user input form
    return render_template('index.html')

@app.route('/get_recommendations', methods=['POST'])
def get_recommendations():
    try:
        # Get user input
        age = int(request.form.get('age', 25))
        job = request.form.get('job', 'unknown')
        education = request.form.get('education', 'unknown')
        
        # Predict user segment
        segment = recommender.predict_segment(age, job, education)
        
        # Create user profile
        user_profile = {
            'age': age,
            'job': job,
            'education': education,
            'segment': segment
        }
        
        # Get recommendations
        recommendations = recommender.get_recommendations(user_profile)
        similar_customers = recommender.get_similar_customers(segment)
        
        return render_template('recommendations.html', 
                             recommendations=recommendations,
                             user_profile=user_profile,
                             similar_customers=similar_customers)
    
    except Exception as e:
        return render_template('error.html', error=str(e))

@app.route('/api/recommendations', methods=['POST'])
def api_recommendations():
    #API endpoint for recommendations (JSON response)
    try:
        data = request.get_json()
        age = data.get('age', 25)
        job = data.get('job', 'unknown')
        
        segment = recommender.predict_segment(age, job)
        user_profile = {'age': age, 'job': job, 'segment': segment}
        recommendations = recommender.get_recommendations(user_profile)
        
        return jsonify({
            'status': 'success',
            'user_profile': user_profile,
            'recommendations': recommendations
        })
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)