from flask import Flask, render_template, jsonify, request
import pandas as pd
import pickle
import joblib

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Flask(__name__)
# dataset = pd.read_csv('./dataset/dataset.csv')
# dataset.to_html('dataset.html')

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/dataset")
def dataset():
    return render_template('dataset.html')

@app.route("/visualization")
def visualization():
    return render_template('visualization.html')

@app.route("/prediction")
def prediction():
    return render_template('prediction.html')

@app.route("/produk")
def produk():
    return render_template('produk.html')

@app.route("/cluster1")
def c1():
    return render_template('cluster1.html')

@app.route("/cluster2")
def c2():
    return render_template('cluster2.html')

@app.route("/cluster3")
def c3():
    return render_template('cluster3.html')

@app.route("/sales")
def sales():
    return render_template('sales.html')


# @app.route("/result", methods=['POST','GET'])
# def result():
#     if request.method == 'POST':
#         input = request.form
#         prediksi = model.predict([[
#             int(input['person_income']), int(input['loan_amnt']), int(input['loan_percent_income']),
#             int(input['loan_int_rate']), int(input['person_emp_length'])
#         ]])[0]
#     return render_template('result.html', data = input, pred = prediksi)

# if __name__ == "__main__":
#     model = joblib.load('Joblib')
#     app.run(debug=True)
if __name__=="__main__":
    app.run(debug=True)