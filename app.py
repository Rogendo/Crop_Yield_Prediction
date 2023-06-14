import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_extras.card import card
import pandas as pd
from ydata_profiling import ProfileReport
import time

############## page settings ##############
st.set_page_config(page_title="Loan Prediction",
                #    page_icon="chart",
                   layout="wide",
                   page_icon="random",
                   initial_sidebar_state='expanded',
                   menu_items={
                       'Get Help':'mailto:chuckyjucky1963@gmail.com',
                        'report a bug':'mailto:chuckyjucky1963@gmail.com',
                        "About":"This is website is created by Peter Rogendo for a Loan Prediction model and Data Analysis",
    })

############## sidebar menu ################

st.sidebar.title("Loan Prediction",anchor="middle")
st.sidebar.markdown("---")
with st.sidebar:
    menu = option_menu(
        menu_icon="cast",
        menu_title="Menu",
        options=["Home","Data","Analysis","About","Contact us"],
        icons=["house","database-gear","graph-up","info-circle","envelope"],
        default_index=0,
    )
if menu == "Home":
    st.title("Loan Prediction webapp")
    card1,card2,card3=st.columns(3)
    with card1:
        card(
        title="Streamlit Loan Prediction",
        text="Explore more on Loan prediction model and datasets",
        image="3.png",
        url="#", 

    )
    with card2:
        card(
        title="Prediction",
        text="Explore more on Loan prediction model and datasets",
        image="linktoanimage.com",
        url="#", 
    )
    with card3:
        card(
        title="Loan ",
        text="Explore more on Loan prediction model and datasets",
        image="1-.png.jpg",
        url="#", 
    )
    
    ########### load pre-trained model ############
    pickle_in=open("classifier.pkl","rb")
    classifier=pickle.load(pickle_in)
    
    @st.cache_data
    # define function for prediction
    def prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History):
        # Pre-processing user input
        if Gender == "Male":
            Gender = 0
        else:
            Gender = 1

        if Married == "Unmarried":
            Married = 0
        else:
            Married = 1

        if Credit_History == "Unclear Debts":
            Credit_History = 0
        else:
            Credit_History = 1
        LoanAmount = LoanAmount / 1000

        # Making predictions
        prediction = classifier.predict(
            [[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])

        if prediction == 0:
            pred = 'Rejected'
        else:
            pred = 'Approved'
        return pred
    def main():
        
        # following lines create boxes in which user can enter data required to make prediction
        Gender = st.selectbox('Gender', ("Male", "Female"))
        Married = st.selectbox('Marital Status', ("Unmarried", "Married"))
        ApplicantIncome = st.number_input("Applicants monthly income")
        LoanAmount = st.number_input("Total loan amount")
        Credit_History = st.selectbox('Credit_History', ("Unclear Debts", "No Unclear Debts"))
        result = ""

        # when 'Predict' is clicked, make the prediction and store it
        if st.button("Predict"):
            result = prediction(Gender, Married, ApplicantIncome, LoanAmount, Credit_History)
            st.success('Your loan is {}'.format(result))
            # print(LoanAmount)

    if __name__ == '__main__':
        main()
# loading the dataset
df=pd.read_csv("train_ctrUa4K.csv")
if menu == "Data":
    st.title("Dataset Used")
    colored_header(
        label="Dataset",
        description="more info on the data",
        color_name="red-70",        
    )
    
    st.dataframe(df.head())
    # generating a profiling report

    profile=ProfileReport(df,title="Loan Prediction Profile Report")
    # profile.to_file("profilereport.html")
    # df.describe(include="all")
      
    
    a1,a2,a3=st.columns(3)
    with a1:
        
    
        st.markdown("---")
        st.markdown("---")
    with a2:
        
    
        st.markdown("---")
        st.text(df.describe())
        st.markdown("---")
    with a3:
        
    
        st.markdown("---")
        # st.text(df.columns)
        st.markdown("---")
    # save profiling report in a html/pdf format, then when a person
    # clicks to view profiling report, they are redirected to the page
    
    # download profile report
    col1,col2=st.columns(2)
    
    with col1:
        with open("profilereport.html", "rb") as file:
            btn = st.download_button(
                
                label="Download Profile Report",
                data=file,
                file_name="profilereport.pdf",
                mime="profilereport/html"
            )

    
    
    # download dataset button
    @st.cache_data
    def convert_df(df_frame):
        return df_frame.to_csv().encode('utf-8')

    csv=convert_df(df)
    with col2:
        st.download_button(
            label="Download Dataset as CSV",
            data=csv,
            file_name="data.csv",
            mime='train_ctrUa4K/csv',
        
        )
    

if menu == "Analysis":
    st.title("Analysis")
    colored_header(
        label="",
        description="",
        color_name="red-70"
    )
    ############ data preprocessing and cleaning ###########
    # df['Gender']= df['Gender'].map({'Male':0, 'Female':1})
    # df['Married']=df['Married'].map({'No':0, 'Yes':1})
    # df['Loan_Status']= df['Loan_Status'].map({'N':0, 'Y':1})
    
    st.dataframe(df.head(4))
    ######### checking and removing null values ##########
        
    df.isnull().sum()
    df= df.dropna()
    
    ########### sidebar filterigng ##########
    st.markdown("---")
    st.header("filter data to show")
    st.markdown("---")
    f1,f2,f3=st.columns(3)
    
    Gender=f1.multiselect(
        "Select gender :",
        options=df['Gender'],
        default=df["Gender"].unique()
        
    )
    Married=f2.multiselect(
        "Marriage status :",
        options=df["Married"],
        default=df["Married"].unique()
    )
    
    
    Credit_History=f3.multiselect(
        "Credit History (0=unclear debts,1=clear debts) :",
        options=df["Credit_History"],
        default=df["Credit_History"].unique()
    )
    f4,f5,f6=st.columns(3)
    
    Education=f4.multiselect(
        "Education level :",
        options=df["Education"],
        default=df["Education"].unique()
    )
    Self_Employed=f5.multiselect(
        "Self employed :",
        options=df["Self_Employed"],
        default=df["Self_Employed"].unique()
    )
    Property_Area=f6.multiselect(
        "Property area :",
        options=df["Property_Area"],
        default=df["Property_Area"].unique()
    )
    # activity spinner
   
    with st.spinner("...loading"):
            time.sleep(4)

    df_selection=df.query(
        # "year == @year & month ==@month"
        "Gender == @Gender & Married == @Married & Credit_History ==@Credit_History & Education == @Education & Self_Employed == @Self_Employed & Property_Area== @Property_Area"
    )
    st.dataframe(df_selection)
    ########### charts ##########
    st.title(":bar_chart: Charts Analysis")
    colored_header(
        label="",
        description="",  
        color_name="violet-70",
        )
    df_selection['Gender']= df_selection['Gender'].map({'Male':0, 'Female':1})
    df_selection['Married']=df_selection['Married'].map({'No':0, 'Yes':1})
    df_selection['Loan_Status']= df_selection['Loan_Status'].map({'N':0, 'Y':1})
    
    st.subheader("Gender against the Married  (0=Male,1=Female)")
    st.bar_chart(df_selection,x="Gender",y="Married")
    
    st.subheader("Education against the Credit_History")
    st.bar_chart(df_selection,x="Education",y="Credit_History")
    
    st.area_chart(df_selection,y="ApplicantIncome")
    st.line_chart(df_selection,y="ApplicantIncome")
    
    
    

# ############# Buy me A Coffee ##############

# button(username="link to payment",
#        floating=False,
#        width=250)
    
#     ##########    # 
    
    
if menu == "About":
    st.title("About Page")

if menu == "Contact us":
    st.title("Get in touch")
    contact_form = """
    <form action="https://formsubmit.co/peterrogendo1999@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


    local_css("style.css")