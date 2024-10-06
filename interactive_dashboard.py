import pandas as pd
import streamlit as st

df = pd.read_csv("D:\\github_dataset.csv")
# setting page configuration like Title,and so
st.set_page_config(page_title="GitHub Repository Data",layout="wide")
# ------------------SideBar Section-----------------------
# Adding custom CSS
st.markdown(
    """
    <style>
    .stSelectbox {
        border: 2px solid #4CAF50; /* Green border */
        border-radius: 5px; /* Rounded corners */
        background-color: #f0f0f0; /* Light grey background */
        color: #333; /* Text color */
        padding: 10px; /* Padding */
        font-size: 16px; /* Font size */
        transition: background-color 0.3s ease; /* Transition effect */
    }

    .stSelectbox:hover {
        background-color: #e0e0e0; /* Darker grey on hover */
    }

    .page-title {
    color:#7d9ed4;
    font-size:44px;
    text-align:left
    }

    .repo-title {
    color:#34568c;
    font-size:24px;
    text-align:left
    }

    .flex-container {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
      background-color: #e0e0e0;
    }

    .flex-item {
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 20px;
        width: 200px; /* Set a fixed width */
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Adding Title to the sidebar
st.sidebar.header("Filter Github Data")
# getting list of repository name available in file
availableRepository = df["repositories"]
# giving repository name list to the choice selection
repository_name = st.sidebar.selectbox("Filter By Repository",availableRepository,placeholder="Repository Name")
# ------------------Main Section---------------------------
# Main Title of the Page
st.markdown(f'<div class="page-title">Github Data DashBoard</div>', unsafe_allow_html=True)                         
st.divider()
# fetching record from dataset for the selected Repository
df_selected = df.query("repositories==@repository_name")
# displaying data for the got row set
for index,data in df_selected.iterrows():
    st.markdown(f'<div class="repo-title">{df_selected["repositories"][index]}</div>', unsafe_allow_html=True)                             # HTML for displaying data
    flex_items_html = '<div class="flex-container">'
    for index_in_data in data.index[1:]:
        flex_items_html += f"""<div class="flex-item">
            <h3>{index_in_data.capitalize().replace("_"," ")}</h3>
            <p>{data[index_in_data]}</p>
        </div>"""
    flex_items_html += '</div>'       
    st.markdown(flex_items_html, unsafe_allow_html=True)        
    # divider to distinguish record/row
    st.divider()





