import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') #Tkagg
import seaborn as sns

def main():
    st.title("Streamlit Forms & Salary Calculator")
    df = pd.read_csv("data/iris.csv")
    df2 = pd.read_csv("data/lang_data.csv")

    # # Method 1
    # fig,ax = plt.subplots()
    # ax.scatter(*np.random.random(size=(2,100)))
    # st.pyplot(fig)

    # # Method 2
    # fig2 = plt.figure()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig2)

    #  # Method 3
    # fig3,ax3 = plt.subplots()
    # df['species'].value_counts().plot(kind='bar')
    # st.pyplot(fig3)
        # alternative For Matplotlib
    fig = plt.figure()
    sns.countplot(data=df,x=df['species'])
    st.pyplot(fig)

    # Bar chart
    chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])
    st.bar_chart(chart_data)

    # Language data
    lang_list = df2.columns.tolist()
    lang_choices = st.multiselect("Choose Language",lang_list,default='Python')
    new_df = df2[lang_choices]
    st.line_chart(new_df)
    st.area_chart(new_df,use_container_width=True )



if __name__ == "__main__":
    main()
