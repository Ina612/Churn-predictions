from fastapi import FastAPI
import uvicorn
import pickle
from encodings import encodings

app = FastAPI()
pickle_in = open('/model/best_model.pkl', 'rb')
classifier = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Welcome to churn prediction'}

@app.post('/predict')
def predict_churn(data:encodings):
    data = data.dict()
    support_calls = data['Support Calls']
    total_spend = data['Total Spend']
    usage_frequency = data['Usage Frequency']
    tenure = data['Tenure']
    payment_delay = data['Payment Delay']
    prediction = classifier.predict([[support_calls, total_spend, usage_frequency, tenure, payment_delay]])
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)