import streamlit as st
import pandas as pd
import pandasai
from pandasai.llm import OpenAI
import os
from pandasai import SmartDataframe

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

st.image("/Users/shaikmujeeburrahman/Downloads/Odinschool.jpg")

st.title("Odinschool's Data Analysis App")
st.subheader("Created by Mujeeb")
file=st.file_uploader("Upload a CSV for data analysis")
if file is not None:
    df=pd.read_csv(file)
    st.write(df.head(5))


    query=st.text_area("What do you want to know from the csv file?")  

    
    llm = OpenAI(api_token=os.getenv("API_KEY"))
    df=SmartDataframe(df,config={"llm":llm})
    if st.button("Fetch"):
        if query:
            with st.spinner("Fecthing info"):
                st.write(df.chat(query))

        else:
            st.warning("please enter your query")

