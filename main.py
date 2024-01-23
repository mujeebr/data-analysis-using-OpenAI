# import streamlit as st
# import pandas as pd
# import pandasai
# from pandasai.llm import OpenAI
# import os
# from pandasai import SmartDataframe
# from matplotlib import pyplot as plt
# import warnings
# st.set_option('deprecation.showPyplotGlobalUse', False)

# # Filter all warnings
# warnings.filterwarnings("ignore")
# # fig, ax = plt.subplots()


# import os
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# st.image("Odinschool.jpg")

# st.title("Odinschool's Data Analysis App")
# st.subheader("Created by Mujeeb")
# file=st.file_uploader("Upload a CSV for data analysis")
# if file is not None:
    

#     df=pd.read_csv(file)
#     st.write(df.head(5))


#     query=st.text_area("What do you want to know from the csv file?")  

    
#     llm = OpenAI(api_token=os.getenv("API_KEY"))
#     df=SmartDataframe(df,config={"llm":llm})
#     if st.button("Fetch"):
#         if query:
#             with st.spinner("Fetching info"):
#                 st.write(df.chat(query))


#         else:
#             st.warning("please enter your query")

        
# st.pyplot()

import streamlit as st
import pandas as pd
from pandasai.llm import OpenAI
from pandasai import SmartDataframe
import os
from dotenv import load_dotenv
from matplotlib import pyplot as plt
import warnings
st.set_option('deprecation.showPyplotGlobalUse', False)

# Load environment variables from .env
load_dotenv()

st.image("Odinschool.jpg")

st.title("Odinschool's Data Analysis App")
st.subheader("Created by Mujeeb")
file = st.file_uploader("Upload a CSV or Excel file for data analysis", type=["csv", "xlsx", "xls"])

if file is not None:
    # Check file extension
    file_extension = os.path.splitext(file.name)[1].lower()

    if file_extension == ".csv":
        df = pd.read_csv(file)
    elif file_extension in [".xlsx", ".xls"]:
        df = pd.read_excel(file)
    else:
        st.error(f"Unsupported file format: {file_extension}")
        st.stop()

    st.write(df.head(5))

    query = st.text_area("What do you want to know from the file?")

    llm = OpenAI(api_token=os.getenv("API_KEY"))
    df_smart = SmartDataframe(df, config={"llm": llm})

    if st.button("Fetch"):
        
        if query:
            
            with st.spinner("Fetching info"):
                st.write(df_smart.chat(query))
                
#                 

        else:
            st.warning("Please enter your query")

st.pyplot()

