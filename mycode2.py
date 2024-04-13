import streamlit as st

name=st.text_input("Enter your name : ")
fnme=st.text_input("Enter your father name: ")
adr=st.text_area("Enter your text : ")
classdata=st.selectbox("Enter your class : ",(1,2,3,4,5,6))
button=st.button("Done")
if button:
    st.markdown(F""" 
                
    name:{name}
    
    father name:{fnme}
    
    address:{adr} 
    
    class:{classdata}
    
    """)


