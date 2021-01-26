import streamlit as st 

def main():
	"""Deploying Streamlit App In Docker"""

	st.title("Streamlit App")
	st.header("Deploying Streamlit in Docker")


	activities = ["EDAL","Plot"]

	choices = st.sidebar.selectbox('Select Activities',activities)

	if choices == 'EDAL':
		st.subheader("EDA")

	elif choices == 'Plot':
		st.subheader("Visualization")


if __name__ == '__main__':
	main()
