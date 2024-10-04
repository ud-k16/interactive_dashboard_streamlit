import pandas as pd
import streamlit as st

df = pd.read_csv("D:\\github_dataset.csv")
# setting page configuration like Title,and so
st.set_page_config(page_title="GitHub Repository Data",layout="wide")
# Adding Title to the sidebar
st.sidebar.header("Filter Github Data")
# getting list of repository name available in file
availableRepository = df["repositories"]
# giving repository name list to the choice selection
repository_name = st.sidebar.selectbox("Filter By Repository",availableRepository,placeholder="Repository Name")
# Main Title of the Page
st.title(" Github DashBoard")
st.divider()
# fetching record from dataset for the selected Repository
df_selected = df.query("repositories==@repository_name")
# displaying data for the got row set
for index,data in df_selected.iterrows():
    #displaying selected data in two columns
    repo_title,repo_detail=st.columns(2)
    with repo_title:
        st.header(df_selected["repositories"][index])
    with repo_detail:
        for index_in_data in data.index[1:]:
            variable,value=st.columns(2)
            with variable:
                st.markdown(f'<div style="color:#213e6e;font-size:24px;text-align:right">{index_in_data.capitalize().replace("_"," ")}</div>', unsafe_allow_html=True)
            with value:
                st.markdown(f'<div style="color:#7d9ed4;font-size:24px;text-align:left">{data[index_in_data]}</div>', unsafe_allow_html=True)                         
    st.divider()





