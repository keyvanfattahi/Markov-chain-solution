import streamlit as st
import numpy as np
import pandas as pd

# Set page background
page_bg = 'https://www.freecodecamp.org/news/content/images/2022/01/alexander-sinn-KgLtFCgfC28-unsplash.jpg'
page_bg_style = f"""
    <style>
    .stApp {{
        background-image: url({page_bg});
        background-size: cover;
    }}
    </style>
"""
st.markdown(page_bg_style, unsafe_allow_html=True)

# Set page alignment
header_style = """
    <style>
    

    .css-1629p8f h1, .css-1629p8f h2, .css-1629p8f h3, .css-1629p8f h4, .css-1629p8f h5, .css-1629p8f h6, .css-1629p8f span {
        color: floralwhite;
        scroll-margin-top: 2rem;
        font-size: 50px;
        
    }

     .row-widget ,.stButton{
        
        width: 100% !important;
        text-align: center ; !important
        padding-top: 20px;  !important
    } 
    
    .css-1a32fsj ,.e19lei0e0{
        text-align: center;
    }


    .header {
        font-size: 40px !important;
        
        direction: rtl !important;
        margin-bottom: 50px !important;
    }
    .block-container{
        background-color: rgb(17 61 101 / 75%);
        
    }

    .css-1629p8f h1, .css-1629p8f h2, .css-1629p8f h3, .css-1629p8f h4, .css-1629p8f h5, .css-1629p8f h6, .css-1629p8f span {
        color: floralwhite;

    }

    .css-16idsys p {
        word-break: break-word;
        margin-bottom: 0px;
        font-size: 17px;
        color: darksalmon;
        font-weight: bold;
    }

    .css-5rimss p {
        word-break: break-word;
        color: #ffffff;
        font-weight: bold;
        font-size: 20px;
    }

    [type=button]:not(:disabled), [type=reset]:not(:disabled), [type=submit]:not(:disabled), button:not(:disabled) {
        //cursor: pointer;
        //width: 100%;
        color: #ffffff;
        background: #ff0606;
    }

    .css-1vbkxwb p {
        word-break: break-word;
        margin-bottom: 0px;
        font-size: 18px;
    }

    </style>
"""
st.markdown(header_style, unsafe_allow_html=True)

st.title("Markov chain solution project")

# Get the dimension of the matrix
n = st.number_input("Enter the number of rows and columns of the matrix:", min_value=1, step=1)

# Create form to get input for the matrix
form = st.form(key='my-form')
matrix = []
with form:
    st.write("Enter the matrix values:")
    for i in range(n):
        row = []
        for j in range(n):
            value = st.number_input(f"Enter the value of row {i+1}, column {j+1}:", key=f"matrix[{i}][{j}]", step=0.1)
            row.append(value)
        matrix.append(row)

submit_button = form.form_submit_button(label='calculate')

# If the submit button is clicked
if submit_button:
    count = 0
    previous_result = None
    # List to store the results of each step
    result_list = []
    # Add the initial matrix to the list of results
    result_list.append(pd.DataFrame(matrix, dtype=float))


    def is_matrix_close(matrix1, matrix2, decimal=4):
        """
        Check if two matrices are close enough (up to a certain number of decimal places).
        """
        return np.allclose(matrix1, matrix2, rtol=0, atol=10 ** (-decimal))


    while True:
        # Convert the matrix to a NumPy array
        matrix = np.array(matrix, dtype=float)
        # Multiply the matrix by itself
        result_matrix = np.dot(matrix, matrix)
        # Increment the counter
        count += 1
        # Check if the result is the same as the previous result
        if previous_result is not None and is_matrix_close(result_matrix, previous_result, decimal=4):
            break
        else:
            previous_result = matrix
            matrix = result_matrix
            # Add the current matrix to the list of results
            result_list.append(pd.DataFrame(matrix, dtype=float))
            pd.options.display.float_format = "{:.4f}".format

            
    # Display the results
    st.write("Steps of the Markov chain:")
    for i, result in enumerate(result_list):
        st.write(f"Level {i}:")
        st.dataframe(result.style.format("{:.4f}"))
    st.write("Response matrix:")
    st.dataframe(pd.DataFrame(matrix).style.format("{:.4f}"))
    
    if (count - 2) % 2 == 0:
        st.write(f"Markov chain for the matrix entered in exponentiation $P^{{{(count - 2) ** 2}}} $  It was resolved.")
    else:
        st.write(f"Markov chain for the matrix entered in exponentiation $P^{{{(count - 2) ** 2-1}}} $ It was resolved.")


st.write("<br>"*5, unsafe_allow_html=True)
st.write("Developer: Keyvan FattahiRishakan")

    