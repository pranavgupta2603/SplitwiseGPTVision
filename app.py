import streamlit as st
import pandas as pd
# Import other necessary libraries like those for image processing
from openai import OpenAI
from dotenv import load_dotenv
import os
from PIL import Image
from bill_process import get_bill_details, get_dataframes_using_convo
from workingsplit import *
import numpy as np
st.set_page_config(layout="wide")
load_dotenv()  
client = OpenAI()
uploaded_image = st.file_uploader("Upload Your Bill Image", type=["png", "jpg", "jpeg"])
#st.session_state
members = get_members()
member_names = [member.first_name for member in members]
if uploaded_image is not None:
    # Process the image through the functions
    with open("download.jpg", "wb") as file:
            file.write(uploaded_image.getbuffer())
    image = Image.open(uploaded_image)
    paidby = st.sidebar.radio("Who paid the bill?", member_names)
    idpaidby = members[member_names.index(paidby)].id
    st.sidebar.image(image, caption='Uploaded Image.', width=300)
    if "df" not in st.session_state:
        with st.spinner("Loading..."):
            bill_details = get_bill_details(client)
            #st.write(bill_details)
            df = get_dataframes_using_convo(client, bill_details)
            st.session_state["df"] = df
            
            df.to_csv('bill.csv', index=False)
    else:
        df = st.session_state["df"] 
    st.sidebar.write(df)
    #df= pd.read_csv('bill.csv')
    #cols[0].write(df)
    for item in range(0, len(df)):
        item_name = df.iloc[item]['Item']
        cols = st.columns(len(members)+1)
        for i in range(len(cols)):
            if i == 0:
                cols[i].write(item_name)
            else:
                cols[i].checkbox(members[i-1].first_name, key =str(item)+"_"+str(members[i-1].id))
        st.divider()
    
    
    conf =st.button("Create Split")
    if conf:
        mat = [list() for i in range(len(df))]
        for i in st.session_state:
            try:
                if st.session_state[i] == True:
                    item, user = map(int, i.split("_"))
                    mat[item].append(user)
            except:
                pass
        #st.write(mat)
        for i in range(len(mat)):
            if len(mat[i]) > 1:
                print(mat[i])
                print(df['Price'][i])
                expense = create_split(idpaidby, mat[i], df['Total'][i], df['Item'][i])
                if expense[1] != None:
                    print(expense[1].errors)
                else:
                    st.write("Split created for item", df['Item'][i])
        #st.session_state["lol"] = members[cols.index(i)].first_name
    

