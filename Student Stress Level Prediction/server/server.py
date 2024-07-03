from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_stress_level', methods=['POST'])
def predict_stress_level():
    # features1 = [20, 0, 11, 2, 1, 2, 4, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3, 3, 2, 1]
    try:
        features = [
            request.form.get('self_esteem', type=int),
            request.form.get('mental_health_history', type=int),
            request.form.get('depression', type=int),
            request.form.get('headache', type=int),
            request.form.get('blood_pressure', type=int),
            request.form.get('sleep_quality', type=int),
            request.form.get('breathing_problem', type=int),
            request.form.get('noise_level', type=int),
            request.form.get('living_conditions', type=int),
            request.form.get('safety', type=int),
            request.form.get('basic_needs', type=int),
            request.form.get('academic_performance', type=int),
            request.form.get('study_load', type=int),
            request.form.get('teacher_student_relationship', type=int),
            request.form.get('future_career_concerns', type=int),
            request.form.get('social_support', type=int),
            request.form.get('peer_pressure', type=int),
            request.form.get('extracurricular_activities', type=int),
            request.form.get('bullying', type=int),
            request.form.get('stress_level', type=int)
        ]

        response = jsonify({
            'anxiety_level': util.predict_stress(features).tolist()
        })

        response.headers.add('Access-Control-Allow-Origin', '*')

        return response
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server for Stress Level Prediction")
    util.load_saved_artifacts()
    app.run()