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

   .stApp {
        background-color: #98e2c6; 
    }

    .stSidebar{
        background-color: #98e2c6; 
    }

   .stSelectbox {
        background-color: #545c52;
        border-radius: 5px;
        padding: 10px;
    }
    
    .st-cu {
        border: 2px solid #98e2c6;
      }

    .st-emotion-cache-jkfxgf {
        color:#98e2c6;
    }

    .page-title {
        color:#545c52;
        font-size:44px;
        text-align:left
    }

    .repo-title {
        color:#f8f2eb;
        font-size:64px;
        text-align:center
    }

    .flex-container {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        justify-content:space-evenly;
        column-gap:26px;
        row-gap:20px;
        padding:20px 0 0 0;
    #   background-color: #e0e0e0;
    }

    .flex-item {
        background-color: #545c52;
        border: 1px solid #ccc;
        border-radius: 5px;
        padding: 20px;
        width: 250px; 
        box-shadow: 10px 2px 5px #f8f2eb;
        color:#98e2c6
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
# get repository by star count
star_count_option = ["0-10","11-50","51-100","101-1000"]
star_range_selected = st.sidebar.selectbox("Filter By Star's Given",star_count_option,placeholder="Star Rating Range")
star_range_selected = star_range_selected.split("-")
star_range_selected = [int(star_range_selected[0]),int(star_range_selected[1])]

# ------------------Main Section---------------------------
# Main Title of the Page
st.markdown(f'<div class="page-title">Github Data DashBoard</div>', unsafe_allow_html=True)                         
st.divider()
# fetching record from dataset for the selected Repository
df_selected = df.query( "stars_count>=@star_range_selected[0]"  )

def display_repo_info(data):
    repo_data_html = '<div class="flex-container">'
    for index_in_data in data.index[1:]:
        repo_data_html += f"""<div class="flex-item">
            <p>{index_in_data.capitalize().replace("_"," ")}</p>
            <p>{data[index_in_data]}</p>
        </div>"""
    repo_data_html += '</div>'  
    return repo_data_html

# displaying data for the got row set
for index,data in df_selected.iterrows():
    st.markdown(f'<div class="repo-title">{df_selected["repositories"][index]}</div>', unsafe_allow_html=True)    # HTML for displaying data
    st.markdown(display_repo_info(data), unsafe_allow_html=True)        
    # divider to distinguish record/row
    st.divider()





