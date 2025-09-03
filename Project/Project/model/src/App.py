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
    # Get the absolute path to the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the full paths to the scaler and model files
    scaler_path = os.path.join(script_dir, '..', 'workspace', 'scaler.pkl')
    model_path = os.path.join(script_dir, '..', 'workspace', 'rf_model.pkl')

    # Load the scaler and model
    scaler = joblib.load(scaler_path)
    model = joblib.load(model_path)

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
