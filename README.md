# Diamond Price Predictor

## 📌 Project Description
The **Diamond Price Predictor** is a web-based application built using **Python** and **Flask** that allows users to predict the price of a diamond based on various input features such as carat, cut, color, clarity, and more. The environment for this project is created using **Anaconda**, ensuring a smooth and efficient execution of dependencies and packages.

Users can enter diamond attributes in a web form, and the application will return the predicted price using a trained machine learning model.

## 🛠️ Tech Stack
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **Machine Learning Model:**  Ridge Regression (Scikit-learn)
- **Environment:** Anaconda
- **Database (if used):** Pandas (CSV-based data storage)

---

## ⚙️ Installation & Setup

### 1️⃣ Prerequisites
Make sure you have the following installed:
- [Anaconda](https://www.anaconda.com/download)
- Python (comes with Anaconda)
- Git (optional, for cloning the repository)

### 2️⃣ Setup Virtual Environment
Use **Anaconda** to create and activate a virtual environment for the project:
```bash
conda create --name diamond_price_env python=3.8
conda activate diamond_price_env
```

### 3️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/diamond-price-predictor.git
cd diamond-price-predictor
```

### 4️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
> If `requirements.txt` is not available, manually install the required libraries:
```bash
pip install flask pandas scikit-learn numpy matplotlib seaborn
```

### 5️⃣ Run the Application
```bash
python app.py
```

### 6️⃣ Open in Browser
Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the web application.

---

## 🚀 Features
- **User-friendly Interface**: A form where users can input diamond details.
- **Machine Learning Model**: Uses a trained model to predict prices.
- **Flask-based API**: Handles user input and returns predictions.
- **Real-time Predictions**: Displays the predicted price instantly.

---

## 🗃️ Project Structure
```
📂 diamond-price-predictor
│── app.py                # Flask Application Entry Point
│── templates
│   ├── index.html        # Main Webpage with Form
│   ├── form.html       # Page to Display Prediction
│── static
│   ├── style.css         # CSS File for Styling 
│── data
│   ├── gemstones.csv     # Dataset used for Training
│── src
│   ├── components        # Core ML Components
│   │   ├── data_ingestion.py       # Data Collection & Storage
│   │   ├── data_transformation.py  # Data Preprocessing & Cleaning
│   │   ├── model_trainer.py        # Model Training & Saving
│   ├── pipelines         # ML Pipelines
│   │   ├── training_pipeline.py    # Full Model Training Pipeline
│   │   ├── prediction_pipeline.py  # Prediction Pipeline
│── artifact              # Stores Model & Preprocessor Files
│   ├── model.pkl         # Trained Model File
│   ├── preprocessor.pkl  # Data Preprocessor File
│   ├── raw_data.csv      # Raw Dataset
│   ├── processed_data.csv # Processed Dataset
│── requirements.txt      # Dependencies
│── README.md             # Project Documentation
```

---

## 🎯 Usage Guide
1. Open the application in a browser.
2. Fill in the diamond details (Carat, Cut, Color, Clarity, etc.).
3. Click the "Predict" button.
4. View the predicted price of the diamond.

---

## 🛠️ Model Training (Optional)
If you want to retrain the model:
1. Load `gemstones.csv` dataset.
2. Preprocess the data using Pandas.
3. Train a regression model using Scikit-learn.
4. Save the trained model using `pickle`.
5. Replace `model.pkl` in the `artifact` folder.

---

## 📌 Future Enhancements
- Deploy on **Heroku** or **AWS**.
- Improve UI with **React.js**.
- Add **database storage** for predictions.
- Implement **authentication & user profiles**.

---

## 📜 License
This project is **open-source** and free to use.

---

### 🔗 Connect with Me
📧 Email: [pratap.aditya2712@gmail.com](mailto:pratap.aditya2712@gmail.com)  
🐙 GitHub: [github.com/pratapaadi](https://github.com/pratapaadi/pratapaadi)  
💼 LinkedIn: [linkedin.com/aditya-pratap-singh](https://www.linkedin.com/in/aditya-pratap-singh-6a35aa22b/)

---

> **Happy Predicting! 🚀**

