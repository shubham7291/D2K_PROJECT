import pickle
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the trained model
with open('RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

# List of all columns used in the model, including those that were dropped
model_columns = [
    'Customer_Age', 'Dependent_count', 'Months_on_book', 'Total_Relationship_Count',
    'Months_Inactive_12_mon', 'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
    'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt', 'Total_Trans_Ct',
    'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio', 'Gender_M', 'Education_Level_Doctorate',
    'Education_Level_Graduate', 'Education_Level_High School', 'Education_Level_Post-Graduate',
    'Education_Level_Uneducated', 'Education_Level_Unknown', 'Marital_Status_Married',
    'Marital_Status_Single', 'Marital_Status_Unknown', 'Income_Category_$40K - $60K',
    'Income_Category_$60K - $80K', 'Income_Category_$80K - $120K', 'Income_Category_Less than $40K',
    'Income_Category_Unknown', 'Card_Category_Gold', 'Card_Category_Platinum', 'Card_Category_Silver'
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    
    # Convert form data to DataFrame
    df = pd.DataFrame([data])
    
    # Convert categorical variables to dummy variables
    df = pd.get_dummies(df)

    # Ensure all model columns are present, set missing columns to zero
    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[model_columns]
    
    # Make prediction
    prediction = model.predict(df)
    
    # Map the prediction to a custom message
    if prediction[0] == 0:
        message = "Customer will attire the company"
    else:
        message = "Customer will not attire the company"
    
    return jsonify({'prediction': message})

if __name__ == '__main__':
    app.run(debug=True)
