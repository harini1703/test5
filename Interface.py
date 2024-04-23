import pickle
import streamlit as st

# Load the model
pickle_in = open('class.pkl', 'rb')
clf = pickle.load(pickle_in)
st.title("Windy Predict")
b=st.selectbox("SELECT THE WIND DIRECTION:",('Calm','NNW','NE','NW','WNW','NNE','ENE','N','Variable','E','SE','W','SW','S','ESE','SSE','WSW'))
if b=='Calm':
  b=0
elif b=='NNW':
  b=34
elif b=='NE':
  a=5
elif b=='NW':
  b=32
elif b=='WNW':
  b=29
elif b=='NNE':
  b=2
elif b=='ENE':
  b=7 
elif b=='N':
  b=36
elif b=='Variable':
  b=99
elif b=='E':
  b=9
elif b=='SE':
  b=14
elif b=='W':
  b=27
elif b=='SW':
  b=23
elif b=='S':
  b=18
elif b=='ESE':
  b=11
elif b=='SSE':
  b=16
else:
  a=25

def predict_class(features):
    prediction = clf.predict([features])
    return prediction[0]
  

if st.button("Predict"):
    features = [b]
    prediction = predict_class(features)
    st.write(f"The predicted wind speed is: {prediction}")
  
  



