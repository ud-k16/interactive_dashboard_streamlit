import pandas as pd
import streamlit as st

# reading csv file
df = pd.read_csv("D:\\github_dataset.csv")
# setting page configuration like Title,and so
st.set_page_config(page_title="GitHub Repository Data",layout="wide")

# ------------------Adding custom CSS--------------
# Function to read the CSS file
def load_css(file_name):
    with open(file_name) as f:
        return f.read()

# Load CSS and inject it
css = load_css('styles.css')
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# ------------------function definition-------------
def display_repo_info(data):
    repo_data_html = '<div class="flex-container">'
    for index_in_data in data.index[1:]:
        repo_data_html += f"""<div class="flex-item">
            <p>{index_in_data.capitalize().replace("_"," ")}</p>
            <p>{data[index_in_data]}</p>
        </div>"""
    repo_data_html += '</div>'  
    return repo_data_html

def data_set_on_range_count(range_selected,column_name="stars_count"):
    range_selected = range_selected.split("-")
    range_selected = [int(range_selected[0]),int(range_selected[1])]
    df_selected_min = df.query( f"{column_name}>=@range_selected[0]"  ) 
    return df_selected_min.query( f"{column_name}<=@range_selected[1]"  )

# ------------------SideBar Section-----------------------
# Adding Title to the sidebar
st.sidebar.header("Filter Github Data")

# getting list of repository name available in file
availableRepository = df["repositories"]
# common range option
range_option = ["0-10","11-50","51-100","101-1000"]
# language option
language_option = ["Python","JavaScript","TypeScript","Java","C++","Swift","Rust","Dart","Smarty"]


# giving repository name list to the choice selection
repository_name = st.sidebar.selectbox("Filter By Repository",availableRepository,placeholder="Repository Name")
# selection by Language
language_selected = st.sidebar.selectbox("Filter By Language",language_option,placeholder=" Select Language")
# range selection by star count
star_range_selected = st.sidebar.selectbox("Filter By Star's Given",range_option,placeholder="Star Rating Range")
# range selection by fork count
fork_range_selected = st.sidebar.selectbox("Filter By Fork's Count",range_option,placeholder="Fork Range")
# range selection by pull request count
pull_range_selected = st.sidebar.selectbox("Filter By Pull Request's Count",range_option,placeholder="Pull Request Range")
# range selection by issue count
issue_range_selected = st.sidebar.selectbox("Filter By Issues's Count",range_option,placeholder="Issues Range")
# range selection by contributor count
contributor_range_selected = st.sidebar.selectbox("Filter By Contributor's Count",range_option,placeholder="Contributor Range")


# ------------------Main Section---------------------------
# Main Title of the Page
st.markdown(f'<div class="page-title">Github Data DashBoard</div>', unsafe_allow_html=True)                         
st.divider()
# fetching record from dataset for the selected Repository

df_selected =data_set_on_range_count(star_range_selected)

# dividing main section into two column
repo_name_section,detail_section = st.columns(2)

# displaying data for the got row set
for index,data in df_selected.iterrows():
    with repo_name_section:
        if st.button(f'{df_selected["repositories"][index]}',key=index): 
                with detail_section:
                    st.markdown(display_repo_info(data), unsafe_allow_html=True)        
    # divider to distinguish record/row
    st.divider()





