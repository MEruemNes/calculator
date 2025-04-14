import streamlit as st

st.title("🧮 Marks Calculator")

st.subheader("Grammar Quizzes")
grm1 = st.number_input("Grammar 1", min_value=0,max_value=100)
grm2 = st.number_input("Grammar 2", min_value=0,max_value=100)
grm3 = st.number_input("Grammar 3", min_value=0,max_value=100)

st.subheader("Writing Quizzes")
wrt1 = st.number_input("Writing 1", min_value=0,max_value=100)
wrt2 = st.number_input("Writing 2", min_value=0,max_value=100)
wrt3 = st.number_input("Writing 3", min_value=0,max_value=100)

st.subheader("Other Quizzes")
dbt = st.number_input("Debate", min_value=0,max_value=100)
prj = st.number_input("Project", min_value=0,max_value=100)
ohmw = st.number_input("Online Homework", min_value=0,max_value=100)
mid = st.number_input("Midterm", min_value=0,max_value=100)
final = st.number_input("EMT", min_value=0,max_value=100, help="If the grade is not available yet, you can leave it blank.")

if st.button("Calculate"):
    result = (((grm1 + grm2 + grm3)/3)*0.1) + (((wrt1 + wrt2 + wrt3)/3)*0.1) + (dbt*0.05) + (prj*0.1) + (ohmw*0.05) + (mid*0.2)
    resultforfinal = ((60-result)*2.5)
    st.success(f"Your Score: {round(result, 2)}")
    st.success(f"Required Marks(Only for EMT): {round(resultforfinal,3)}")

    if result >= 50:
        st.info("YOU ARE SUPERMAN 💪")
    elif result >= 40:
        st.warning("YOU SHOULD STUDY A BIT 📚")
    elif result >= 30:
        st.warning("YOU HAVE TO STUDY MORE ⚠️")
    else:
        st.error("YOU SHOULD GET LUCKY 🤞")
        
        st.markdown("___")
    st.markdown("**Developed by Enes**")