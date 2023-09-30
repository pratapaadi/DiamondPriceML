# Diamond Price Prediction Project

## Overview

This project aims to predict the prices of diamonds based on various attributes such as carat weight, cut, color, clarity, depth, and table using Python libraries and Jupyter Notebook. Diamond price prediction is a common task in the jewelry industry, and accurate predictions can assist in pricing diamonds competitively.

The project leverages machine learning techniques to build a predictive model using a dataset of diamond attributes and corresponding prices. The code is implemented in a Jupyter Notebook for ease of analysis and visualization.

## Prerequisites

Before running the Jupyter Notebook, make sure you have the following libraries and tools installed:

- Python (3.x)
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

You can install these libraries using the following command:

```bash
pip install jupyter pandas numpy matplotlib seaborn scikit-learn
```

## Dataset

The dataset used for this project is included in the repository as `diamonds.csv`. It contains the following columns:

- `carat`: Carat weight of the diamond (numeric)
- `cut`: Quality of the cut (categorical: Fair, Good, Very Good, Premium, Ideal)
- `color`: Diamond color, from J (worst) to D (best) (categorical)
- `clarity`: A measurement of how clear the diamond is, from I1 (worst) to IF (best) (categorical)
- `depth`: Total depth percentage, calculated as `(z / mean(x, y)) = 2 * z / (x + y)` (numeric)
- `table`: Width of the top of the diamond relative to the widest point (numeric)
- `price`: Price of the diamond (numeric)

## Usage

1. Clone the repository to your local machine:

```bash
git clone https://github.com/pratapaadi/DiamondPriceML.git
cd diamond-price-prediction
```

2. Launch Jupyter Notebook:

```bash
jupyter notebook
```

3. Open the `EDA.ipynb`and 'modelTraining.ipynb' notebook and follow the instructions within for data preprocessing, model training, evaluation, and prediction.

## Data Preprocessing

- Data Cleaning: Handle missing values (if any) and remove duplicates.
- Encoding: Convert categorical variables like 'cut', 'color', and 'clarity' into numerical format using one-hot encoding or label encoding.
- Feature Scaling: Scale the numeric features to ensure they have similar ranges.

## Model Building

- Train and evaluate machine learning models such as Linear Regression, Random Forest, or XGBoost.
- Use cross-validation to assess model performance and select the best model.

## Evaluation

- Evaluate the models using appropriate metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).
- Visualize the model's performance using plots and graphs.

## Predictions

- Make predictions on new data or use the trained model to predict diamond prices.
- Interpret the results and make pricing recommendations based on the model's predictions.

## Conclusion

This Diamond Price Prediction project demonstrates the use of Python libraries and Jupyter Notebook for building a predictive model to estimate diamond prices based on various attributes. By following the steps outlined in the notebook, you can learn about data preprocessing, model training, evaluation, and making predictions. Feel free to customize and extend this project to suit your specific needs or dataset.

If you have any questions or feedback, please feel free to contact the project owner at [pratap.aditya2712@gmail.com](mailto:pratap.aditya2712@gmail.com).

Happy predicting! 🚀
