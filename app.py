import pickle 
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_extras.card import card
import pandas as pd
from ydata_profiling import ProfileReport
import time


############## page settings ##############
st.set_page_config(page_title="Crop Yield Prediction",
                #    page_icon="chart",
                   layout="wide",
                   page_icon="random",
                   initial_sidebar_state='expanded',
                   menu_items={
                       'Get Help':'mailto:chuckyjucky1963@gmail.com',
                        'report a bug':'mailto:chuckyjucky1963@gmail.com',
                        "About":"This crop prediction website is created by Peter Rogendo for a Loan Prediction model and Data Analysis",
    })
# loading the pre-trained model
pickle_in = open('RandomForest.pkl', 'rb')
classifier = pickle.load(pickle_in)

# loading the dataset
df=pd.read_csv('Crop_recommendation.csv')


############## sidebar menu ################

st.sidebar.title("Crop yield Prediction",anchor="middle")
st.sidebar.markdown("---")
with st.sidebar:
    menu = option_menu(
        menu_icon="cast",
        menu_title="Menu",
        options=["Prediction","Data","Analysis","About","Contact us"],
        icons=["house","database-gear","graph-up","info-circle","envelope"],
        default_index=0,
    )

if menu == "Prediction":
    st.title("Crop Yield Prediction webapp")
    # loading the pre-trained model
    pickle_in = open('RandomForest.pkl', 'rb')  
    classifier = pickle.load(pickle_in)
    


    @st.cache_data()
    # defining the function which will make the prediction using the data which the user inputs
    def recommendation(N,P,K, temperature,humidity, ph, rainfall):
        
        
        N=N
        P=P
        K=K
        temperature=temperature
        humidity=humidity
        ph=ph
        rainfall=rainfall

        # Make recommendations
        recommendation = classifier.predict([[N, P, K, temperature, humidity, ph, rainfall]])
        if recommendation == 0:
            
            reco = "apple"
        elif recommendation==1:
            reco='banana'
        elif recommendation == 2:
            reco = "blackgram"
        elif recommendation == 3:
            reco = "chickpea"
        elif recommendation == 4:
            reco = "coconut"
        elif recommendation == 5:
            reco = "coffee"
        elif recommendation == 6:
            reco = "cotton"

        elif recommendation == 7:
            reco = "grapes"
        elif recommendation == 8:
            reco = "jute"
        elif recommendation[0] == 9:
            reco = "kidneybeans"
        elif recommendation == 10:
            reco = "lentil"
        elif recommendation == 11:
            reco = "maize"
        elif recommendation == 12:
            reco = "mango"
        elif recommendation == 13:
            reco = "mothbeans"
        elif recommendation == 14:
            reco = "mungbean"
        elif recommendation == 15:
            reco = "muskmelon"
        elif recommendation == 16:
            reco = "orange"
        elif recommendation == 17:
            reco = "papaya"
        elif recommendation == 18:
            reco = "pigeonpeas"
        elif recommendation == 19:
            reco = "pomegranate"
        elif recommendation == 20:
            reco = "rice"
        elif recommendation == 21:
            reco = "watermelon"
        else:
            reco='failed to recommend'
        return reco
                    
    # this is the main function in which we define our webpage
    def main():
        # front end elements of the web page
       
        # following lines create boxes in which user can enter data required to make prediction
        N=st.number_input('Nitrogen')
        P=st.number_input('Phosphorus')
        K=st.number_input('Potassium')
        temperature=st.number_input('temperature')   
        humidity=st.number_input('humidity')
        ph=st.number_input('ph')
        rainfall=st.number_input('rainfall')
        
        result=""
        print(result)
        # when 'recommend' is clicked, make the recommendation and store it
        if st.button("Recommend"):
            result = recommendation(N,P,K, temperature,humidity, ph, rainfall)
            
            
            st.success('Your Recomended product  {}'.format(result))
            print(result)
    if __name__ == '__main__':
        main()
        
if menu=="Data":
    st.title("Dataset Used")
    colored_header(
        label="Dataset",
        description="more info on the data",
        color_name="red-70",        
    )
    
    st.dataframe(df.head())
    # generating a profiling report

    profile=ProfileReport(df,title="Crop yield Profile Report")
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
            file_name="Crop_recommendation.csv",
            mime='Crop_recommendation/csv',
        
        )
    

if menu == "Analysis":
    st.title("Analysis")
    colored_header(
        label="",
        description="",
        color_name="red-70"
    )
    ############ data preprocessing and cleaning ###########
    # df['label']=df['label'].map({'apple':0,'banana':1, 'blackgram':2,'chickpea':3,'coconut':4,'coffee':5,'cotton':6,'grapes':7,'jute':8,'kidneybeans':9,'lentil':10,'maize':11,'mango':12,'mothbeans':13,'mungbean':14,'muskmelon':15,'orange':16,'papaya':17,'pigeonpeas':18,'pomegranate':19,'rice':20,'watermelon':21})
    st.dataframe(df.head(4))
    ######### checking and removing null values ##########
        
    df.isnull().sum()
    df= df.dropna()
    
    ########### sidebar filterigng ##########
    st.markdown("---")
    st.header("filter data to show")
    st.markdown("---")
    f1,f2,f3=st.columns(3)
    
    column_start=1
    column_end=5
    
    Nitrogen=f1.slider(
        "..columns",
        
        column_start,column_end
        )
    selecteddata= df.iloc[:,Nitrogen -1]
    sorteddata=selecteddata.sort_values()
    
    
    # activity spinner
   
    with st.spinner("...loading"):
            time.sleep(4)

    # st.table(sorteddata)
    st.markdown("---")
    st.title("....Not yet complete")

# ############# Buy me A Coffee ##############

# button(username="link to payment",
#        floating=False,
#        width=250)
    
#     ##########    # 
    
    
if menu == "About":
    st.title("About Page")
    st.markdown("---")
    st.markdown("""
            This is a crop yield recommendation tool that helps farmers,
            both small scale and large scale, and gardeners know what is 
            best to grow in their area. This is useful since it helps farmers
            avoid loses such as low yield etc. To be recommended what to grow,
            the user has to input the values of their land's Nitrogen content, 
            Phosphorus content, Temperature, Humidity, Soil pH, rainfall etc""")

    
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
