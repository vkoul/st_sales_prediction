# Imports
import streamlit as st
import pandas as pd
import pickle

# setting the basic configuration of the web app. This is shown in the Tab
st.set_page_config(page_title = "Sales Prediction" 
                    ,page_icon = ":bar_chart:" 
                    )


# Opening intro text
st.write("# Predict Sales✨")

st.write("### Determine the scenario 🎛️:")

# Price of the product
price = st.slider('Price of the product?💲', min_value=3, max_value=15, value=7, step=1)

# Advertisment budget
ads = st.slider('What is the Adv budget?💰', min_value=35, max_value=65, value=50, step = 2)


# Promotions
promo = st.slider('What is the promotional budget?💰', min_value=35, max_value=65, value=45, step = 2)


# Creating the dataframe to run predictions on
row = [price, ads, promo]
columns = ['dollar_price', 'advertisment', 'promotions']

mktg_scenario = pd.DataFrame(dict(zip(columns, row)), index=[0])

# Show the table?
# st.table(mktg_scenario)

# Now predicting!
if st.button(label="Click to predict unit sales"):

    # Load the model
    loaded_model = pickle.load(open('lm_model_prediction.sav','rb'))
    
    # Make predictions (and get out pred probabilities)
    pred = loaded_model.predict(mktg_scenario)[0]
    
    st.write(f"Predicted Unit Sales📊: {pred:,.0f} units ")

