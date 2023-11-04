import streamlit as st
import time

st.set_page_config(page_title="Portfolio", page_icon=":page_with_curl:", layout="wide")


def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://images.unsplash.com/photo-1510936111840-65e151ad71bb?auto=format&fit=crop&q=80&w=1790&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


set_bg_hack_url()

option = st.sidebar.selectbox('', ('About Me', 'Education and Technical skills', 'Experience and Project', 'Hobbies and Future Plan'))

if option == 'About Me':
    st.subheader('PORTFOLIO')
    st.markdown("<h1 style='text-align: left; font-size: 120px; color: white;'>ABHINAV SINGH</h1>",
                unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Personal Info", "Summary"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.image('rename.jpg', width=300)
        with col2:
            multi = ['Phone number = +91 9795620000', 'EmailID = singhabhinav0110@gmail.com',
                    'LinkedinID =   https://www.linkedin.com/in/abhinav-singh-554933247/',
                    'Github id = https://github.com/AbheenavSingh','Location = Chennai, Tamil Nadu,IN']
            for i in multi:
                st.subheader(i)


    with tab2:
        st.title("Summary")
        st.subheader('I am a second-year BTech student with a passion for App Development.'
                     ' Proficient in JAVA and C++, I am eager to learn & understand new things and collaborate with professionals to contribute in open source projects.')

if option == 'Education and Technical skills':
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    with st.container():
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image('gifpage1.gif', use_column_width=True)
    with st.container():
        st.title('Education')
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            st.image('education.jpg', width=300)
        with col2:
            st.header('B.Tech, Computer Science and Engineering (Graduating 2026)')
            st.text('')
            st.text('')
            st.subheader('SRM Institute of Science and Technology, Chennai, India')
            st.subheader('Specialization in Computing Technology')
            st.subheader(
                'Relevant coursework: Data Structures and Algorithm,OODP,Operating System,System Design,Programming,etc.')
            for i in range(5):
                st.text('')

    with st.container():
        st.markdown('<h1 style="text-align: right;">Technical skills</h1>', unsafe_allow_html=True)
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.7, 0.3])
        with col2:
            st.image('technical.jpg', width=350)
        with col1:
            st.header('Languages:')
            st.subheader('C++,Kotlin, Java.')
            st.text('')
            st.text('')
            st.header('App Development')
            st.subheader('Kotlin,Flutter.')
            st.text('')
            st.text('')
            st.header('Developer Tools:')
            st.subheader('Git, VScode, Android Studio,JDK.')

if option == 'Experience and Project':
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    with st.container():
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image('gifpage0.gif', use_column_width=True)
    with st.container():
        st.title('Experience')
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.3, 0.7])
        with col1:
            st.text('')
            st.text('')
            st.image('experience.jpg', width=300)
        with col2:
            st.header('SRM NEWTON SCHOOL CODING CLUB, Chennai, IN: Technical Member (Oct 2023 – Present)')
            st.subheader('Tried to contribute in some projects in APP Development domain')
            st.text('')
            st.text('')
            st.header('Cherry Network+, Chennai, IN: Member (September 2023 – Present)')
            st.subheader('Tried to contribute in some projects in App Development domain')
            for i in range(5):
                st.text('')

    with st.container():
        st.markdown('<h1 style="text-align: right;">Projects</h1>', unsafe_allow_html=True)
        st.subheader('', divider='rainbow')
        col1, col2 = st.columns([0.7, 0.3])
        with col2:
            for i in range(15):
                st.text('')
            st.image('project.jpg', width=350)
        with col1:
            st.header('Expense Tracker')
            st.subheader('Helps to track Expense')
            st.markdown('https://github.com/AbheenavSingh/Expense-Tracker')
            st.text('')
            st.text('')
            st.header('TO DO LIST')
            st.subheader('BASIC TO DO APP')
            st.markdown('https://github.com/AbheenavSingh/To-Do-List')
            st.text('')
            st.text('')
            st.header('SpaceTonic')
            st.subheader('An BMI Calculator App')
            st.markdown('https://github.com/AbheenavSingh/Spacetonic')
            st.text('')
            st.text('')


if option == 'Hobbies and Future Plan':
    progress_text = "Operation in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)
    with st.container():
        col1, col2, col3 = st.columns([0.2, 0.6, 0.2])
        with col2:
            st.image('gifpage2.gif', use_column_width=True)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

    st.balloons()
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.title('Hobbies & Interest')
        st.subheader('', divider='rainbow')
        st.subheader('Playing Cricket')
        st.subheader('Travelling')
        st.subheader('Singing')
    with col2:
        st.title('Future plans')
        st.subheader('', divider='rainbow')
        st.subheader('Learning DSA in Java')
        st.subheader('Learning Machine Learning')