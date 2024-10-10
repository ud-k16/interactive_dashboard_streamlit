import pandas as pd
import streamlit as st

# reading csv file
df = pd.read_csv("github_dataset.csv")
# Initialization of a state for selected data set
if 'df_selected' not in st.session_state:
    st.session_state['df_selected'] = df   

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

def data_set_on_range_count(range_selected,column_name="stars_count",data_set=df):
    range_selected = range_selected.split("-")
    range_selected = [int(range_selected[0]),int(range_selected[1])]
    df_selected_min = data_set.query( f"{column_name}>=@range_selected[0]"  ) 
    st.session_state['df_selected'] = df_selected_min.query( f"{column_name}<=@range_selected[1]"  )

def data_set_on_language():
    if(st.session_state['language']!=None):
        if(st.session_state['language']!="Other"):
            st.session_state['df_selected']= df.query("language==@st.session_state['language']")
        else:
            st.session_state['df_selected']= df
    else: 
        st.session_state['df_selected']= df

def data_set_on_repo_name():
    if(st.session_state['repo']!=None):
        st.session_state['df_selected']= df.query("repositories==@st.session_state['repo']")
    else : 
        st.session_state['df_selected']= df
   

def filter_data_set(column_name):
    # fetching latest dataset result
    data = st.session_state['df_selected'] 
    # choosing respective range 
    match column_name:
        case 'stars_count':
            range = st.session_state['stars'] 
        case 'forks_count':
             range = st.session_state['forks'] 
        case 'issues_count':
             range = st.session_state['issues']
        case 'pull_requests':
             range = st.session_state['pulls']
        case 'contributors':
             range = st.session_state['contributors']

    # printing out selected filter for log  
    print(column_name,range)
    # filtering data on given range/ no filter when range is none
    if (range != None):
        data_set_on_range_count(range_selected=range,column_name=column_name,data_set=data)
    # else:
    #     reset_filter()
   

def reset_filter():
    st.session_state['df_selected'] = df
    st.session_state['repo'] = None
    st.session_state['language'] = None
    st.session_state['stars'] = None
    st.session_state['forks'] = None
    st.session_state['pulls'] = None
    st.session_state['issues'] = None
    st.session_state['contributors'] = None
   
# ------------------SideBar Section-----------------------
# Adding Title to the sidebar
st.sidebar.header("Filter Github Data")

# getting list of repository name available in file
availableRepository = df["repositories"]
# common range option
range_option = ["0-10","11-50","51-100","101-1000"]
# language option
language_option = ["Python","JavaScript","TypeScript","Java","C++","Swift","Rust","Dart","Smarty","Other"]


# reset button
st.sidebar.button("Reset",on_click=reset_filter)
# giving repository name list to the choice selection
st.sidebar.selectbox("Filter By Repository",availableRepository,placeholder="Repository Name",index=None,on_change=data_set_on_repo_name,key="repo")
# selection by Language
st.sidebar.selectbox("Filter By Language",language_option,placeholder=" Select Language",index=None,on_change=data_set_on_language,key="language")
# range selection by star count
st.sidebar.selectbox("Filter By Star's Given",range_option,placeholder="Star Rating Range",index=None,on_change=filter_data_set,args=("stars_count",),key="stars")
# range selection by fork count
st.sidebar.selectbox("Filter By Fork's Count",range_option,placeholder="Fork Range",index=None,on_change=filter_data_set,args=("forks_count",),key="forks")
# range selection by pull request count
st.sidebar.selectbox("Filter By Pull Request's Count",range_option,placeholder="Pull Request Range",index=None,on_change=filter_data_set,args=("pull_requests",),key="pulls")
# range selection by issue count
st.sidebar.selectbox("Filter By Issues's Count",range_option,placeholder="Issues Range",index=None,on_change=filter_data_set,args=("issues_count",),key="issues")
# range selection by contributor count
st.sidebar.selectbox("Filter By Contributor's Count",range_option,placeholder="Contributor Range",index=None,on_change=filter_data_set,args=("contributors",),key="contributors")


# ------------------Main Section---------------------------
# Main Title of the Page
st.markdown(f'<div class="page-title">Github Data DashBoard</div>', unsafe_allow_html=True)                         
st.divider()


# dividing main section into two column
# repo_name_section,detail_section = st.columns(2)
# data set to be displayed
df_selected = st.session_state['df_selected']
print(df_selected)
# displaying data for the got row set
for index,data in df_selected.iterrows():
    with st.popover(f'{df_selected["repositories"][index]}',use_container_width=True):
    # if st.button(f'{df_selected["repositories"][index]}',key=index):
         st.markdown(display_repo_info(data), unsafe_allow_html=True)        
    # divider to distinguish record/row
    st.divider()





