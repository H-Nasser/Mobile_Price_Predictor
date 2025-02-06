import streamlit as st
import pandas as pd
import joblib
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Scope Mobile Price Prediction", 
    page_icon="👨‍💻", 
)

def load_resources():   
    scaler = joblib.load(r'D:\Projects\alooo\Project\model\workspace\scaler.pkl')
    
    model = joblib.load(r'D:\Projects\alooo\Project\model\workspace\rf_model.pkl')
    
    return scaler, model

def main():
    st.title('Scope Mobile Price Prediction👨🏻‍💻')
    st.info('Easy Application For Mobile Price Prediction')


    scaler, model = load_resources()

    input_data = {}
    
    input_data['Sale'] = st.number_input('Sale', min_value=0, value=10)
    input_data['resoloution'] = st.number_input('resoloution', min_value=0.0, value=10.0)
    input_data['ppi'] = st.number_input('ppi', min_value=0, value=100)
    input_data['cpu core'] = st.number_input('cpu core', min_value=0, value=100)
    input_data['cpu freq'] = st.number_input('cpu freq', min_value=0.0, value=10.0, step=0.1)
    input_data['internal mem'] = st.number_input('internal mem', min_value=0.0, value=10.0)
    input_data['ram'] = st.number_input('ram', min_value=0.0, value=10.0)
    input_data['RearCam'] = st.number_input('RearCam', min_value=0, value=100)
    input_data['Front_Cam'] = st.number_input('Front_Cam', min_value=0, value=100)
    input_data['battery'] = st.number_input('battery', min_value=0, value=100)


    input_df = pd.DataFrame([input_data])
    
    
    if st.button('Predict Price'):
        input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)
        prediction = model.predict(input_df)
        st.success(f'Predicted Mobile Price: {prediction[0]:.2f}')

        

if __name__ == '__main__':
    main()  