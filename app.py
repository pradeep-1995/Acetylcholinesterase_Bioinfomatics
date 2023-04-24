import numpy as np
import pandas as pd
import streamlit as st
import subprocess
import os



# Molecular_descriptor_calculator
#FP_list = ['PubChem']

def desc_calculation():
    bashCommand = "java -Xms2G -Xmx2G -Djava.awt.headless=true -jar ./PaDEL-Descriptor/PaDEL-Descriptor.jar -removesalt -standardizenitro -fingerprints -descriptortypes ./PaDEL-Descriptor/E:\PRADEEP\python\git\Bioinformatics Project - Drug Discovery\PaDEL-Descriptor\PubchemFingerprinter.xml -dir ./ -file descriptors_output.csv"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    os.remove('molecule.smi')



# Sidebar
with st.sidebar.header('1. Upload CSV Data'):
    upload_file = st.sidebar.file_uploader('Upload your input file',type=['txt'])

    st.sidebar.markdown("""
[Example input file](https://raw.githubusercontent.com/dataprofessor/bioactivity-prediction-app/main/example_acetylcholinesterase.txt)
""")
if st.sidebar.button('Predict'):

# Loading Dataset
    load_data = pd.read_table(upload_file,sep=' ',header=None)
    load_data.to_csv('molecule.smi', sep = '\t', header = False, index = False)

    st.header('Original Input Dataset :')
    #st.write(load_data)
    st.table(load_data)
    #st.dataframe(load_data)

# Calculated the descriptor and display table
    # Create a dropdown menu to select the fingerprint type
    #fingerprint = st.selectbox("Select fingerprint type", FP_list)
    with st.spinner('Calculating Descriptor....'):
        desc_calculation()
    descriptors = pd.read_csv('descriptors_output.csv')
    st.write(descriptors)

    
else:   
    st.info('Upload input data in the sidebar to start!')