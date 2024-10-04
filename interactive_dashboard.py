import pandas as pd
import streamlit as st

df = pd.read_csv("D:\\github_dataset.csv")
# setting page configuration like Title,and so
st.set_page_config(page_title="GitHub Repository Data",layout="wide")
# ------------------SideBar Section-----------------------
# Adding Title to the sidebar
st.sidebar.header("Filter Github Data")
# getting list of repository name available in file
availableRepository = df["repositories"]
# giving repository name list to the choice selection
repository_name = st.sidebar.selectbox("Filter By Repository",availableRepository,placeholder="Repository Name")
# ------------------Main Section---------------------------
# Main Title of the Page
st.markdown(f'<div style="color:#7d9ed4;font-size:44px;text-align:left">Github Data DashBoard</div>', unsafe_allow_html=True)                         
st.divider()
# fetching record from dataset for the selected Repository
df_selected = df.query("repositories==@repository_name")
# displaying data for the got row set
for index,data in df_selected.iterrows():
    # displaying selected data in two columns[title in one column , detail in another]
    repo_title,repo_detail=st.columns(2)
    with repo_title:
        st.markdown(f'<div style="color:#34568c;font-size:24px;text-align:left">{df_selected["repositories"][index]}</div>', unsafe_allow_html=True)                         
    with repo_detail:
        for index_in_data in data.index[1:]:
            # displaying detail in column format
            variable,value=st.columns(2)
            with variable:
                st.markdown(f'<div style="color:#213e6e;font-size:24px;text-align:right">{index_in_data.capitalize().replace("_"," ")}</div>', unsafe_allow_html=True)
            with value:
                st.markdown(f'<div style="color:#7d9ed4;font-size:24px;text-align:left">{data[index_in_data]}</div>', unsafe_allow_html=True)                         
    # divider to distinguish record/row
    st.divider()





