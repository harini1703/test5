import pickle
import streamlit as st

# Load the model
pickle_in = open('class.pkl', 'rb')
clf = pickle.load(pickle_in)
