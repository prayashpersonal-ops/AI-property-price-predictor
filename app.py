import pandas as pd
import pickle
from flask import Flask, render_template, request

app=Flask(__name__)

with open("model.pkl", "rb") as f:
    model=pickle.load(f)
    
# homepage

@app.route('/')
def home():
    return render_template("index.html")

# prediction route

@app.route('/predict',methods=['POST'])
def predict():
    area=int(request.form['area'])
    bedrooms=int(request.form['bedrooms'])
    bathrooms=int(request.form['bathrooms'])
    age=int(request.form['age'])
    
    data = pd.DataFrame(
        [[area, bedrooms, bathrooms, age]],
        columns=["area", "bedrooms", "bathrooms", "age"]
    )

    prediction= model.predict(data)
    
    return render_template(
        "index.html",
        prediction_text=f"Predicted Price: ₹{prediction[0]}"
    )
app.run(debug=True)


