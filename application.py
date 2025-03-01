from flask import Flask,render_template,request,jsonify
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline
app=Flask(__name__)

@app.route('/')
def home():
 return render_template('index.html')

@app.route('/form')
def form_page():
    return render_template('form.html')

@app.route('/predict',methods=['POST'])
def predict_datapoint():
        try:
                data=CustomData(
                carat=float(request.form['carat']),
                depth = float(request.form['depth']),
                table = float(request.form['table']),
                x = float(request.form['x']),
                y = float(request.form['y']),
                z = float(request.form['z']),
                cut = request.form['cut'],
                color= request.form['color'],
                clarity = request.form['clarity']
                )
                final_new_data=data.get_data_as_dataframe()
                predict_pipeline=PredictPipeline()
                pred=predict_pipeline.predict(final_new_data)

                results=round(pred[0],2)
                return render_template('form.html',final_result=f"{results}")
        except KeyError as e:
            return render_template('form.html', 
                         final_result=f"Missing required field: {e}")
        except ValueError as e:
            return render_template('form.html',
                         final_result=f"Invalid format: {e}")
        except Exception as e:
            return render_template('form.html',
                         final_result=f"Prediction Error: {str(e)}")

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True) 

