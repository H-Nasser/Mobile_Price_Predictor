# Mobile Price Prediction using Machine Learning

This project is a machine learning model designed to accurately predict the price of mobile phones based on their features and specifications. By leveraging a real-world dataset, this model provides a practical application of regression analysis to solve a common business problem. The project follows an end-to-end machine learning workflow, from data exploration and preprocessing to model training and evaluation.

**This project was awarded 1st Place (Best Team) out of 40 teams at the GDG on Campus Benha Competition.**

---

## 🚀 Project Overview

The core objective of this project is to build a reliable regression model that can estimate the price of a mobile phone given its attributes. This involves:

1.  **Exploratory Data Analysis (EDA):** Understanding the dataset, visualizing relationships between features, and identifying key factors that influence price.
2.  **Data Preprocessing:** Cleaning the data, handling missing values, and preparing it for model training.
3.  **Model Training:** Implementing and training a machine learning model to learn the patterns between a phone's features and its price.
4.  **Model Evaluation:** Assessing the model's performance using standard regression metrics to determine its accuracy and reliability.

---

## 📈 Key Results & Performance

The final model, a `RandomForestRegressor`, demonstrated excellent predictive power on the test dataset.

* **R-squared Score:** **0.954 (95.4%)**
    * This indicates that the model successfully explains 95.4% of the variance in mobile phone prices, signifying a very strong fit.
* **Mean Absolute Error (MAE):** ~97.45
    * On average, the model's price prediction is off by approximately $97.45.
* **Mean Squared Error (MSE):** ~18600.35

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**
    * **Pandas:** For data manipulation and analysis.
    * **NumPy:** For numerical operations.
    * **Matplotlib & Seaborn:** For data visualization and exploratory data analysis.
    * **Scikit-learn:** For implementing the machine learning model and evaluation metrics.
* **Environment:** Jupyter Notebook

---

## 📂 Dataset

The project utilizes a dataset containing various specifications for a range of mobile phones. The key features include:

* `battery_power`
* `ram`
* `int_memory` (Internal Memory)
* `px_height` & `px_width` (Pixel Resolution)
* `mobile_wt` (Mobile Weight)
* ...and other relevant hardware and software features.

The target variable for prediction is `price_range`.

---

## ⚙️ How to Run This Project

To replicate this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/H-Nasser/Mobile_Price_Predictor.git](https://github.com/H-Nasser/Mobile_Price_Predictor.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Mobile_Price_Predictor
    ```
3.  **Install the required libraries:**
    ```bash
    pip install numpy pandas scikit-learn matplotlib seaborn jupyter
    ```
4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
5.  Open the `.ipynb` file from the Jupyter interface and run the cells sequentially to see the analysis, model training, and evaluation.

