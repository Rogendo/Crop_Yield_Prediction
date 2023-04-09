import pickle 
import streamlit as st


st.set_page_config(page_title="Crop Yield Prediction",layout="wide", initial_sidebar_state="expanded")

# st.set_page_config(page_title="Career Recommender", page_icon="static/img/icon4.png",layout="wide", initial_sidebar_state="expanded")
st.title(" Recommender")
# Load custom CSS
# def load_css(file_name):
#     with open(file_name) as f:
        
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# load_css('static/style.css')


# loading the pre-trained model
pickle_in = open('RandomForest.pkl', 'rb')
classifier = pickle.load(pickle_in)

@st.cache()
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
     elif recommendation == 9:
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
    html_temp = """ 
    <body style="background-color:#d7ebf8;">
    <div style="background-color:#F8D7DA;padding:10px;border-radius:10px">
    <h1 style="color:#721c24;text-align:center;"> Recommendation WebAPP</h1> 
    </div> 
    </body>
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    
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
