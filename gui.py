import streamlit as st
from book_views import LibraryManager

book_instance = LibraryManager()       #Creating object

tab1 , tab2 = st.tabs(["ADD", "VIEW"])

with tab1:
    st.header("Add New Books")
    name = st.text_input("Enter Donor Name")
    blood_group = st.selectbox("Select Blood Group", ["A+","B+", "O+", "AB+", "A-", "B-", "O-", "AB-"])
    phone = st.text_input("Enter Donor Contact Number")
    city = st.text_input("Enter City")
    last_donation = st.text_input("Enter last donation")
    if st.button("Add New Donor"):
        book_instance.post(name=name, blood_group=blood_group,phone=phone, city=city, last_donation=last_donation)
        st.success("New Donor Added Successfully...!")
with tab2:
    st.header("View Donor Details")
    records = book_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Donor Details Found...!")