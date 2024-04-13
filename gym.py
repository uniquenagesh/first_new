import streamlit as st

def main():
    st.markdown(
        """
        <style>
        .navbar {
            overflow: hidden;
            background-color: #333;
        }

        .navbar a {
            float: right;
            display: block;
            color: #f2f2f2;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
            font-size: 17px;
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        </style>
        <div class="navbar">
            <a href="#home">Home</a>
            <a href="#about">About</a>
            <a href="#contact">Contact Us</a>
            <a href="#support">Support</a>
            <a href="#signin">Sign In</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .title {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("Gym Membership Form")

    # Get user input for personal details
    st.header("Personal Details")
    first_name = st.text_input("First Name")
    middle_name = st.text_input("Middle Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth")
    address = st.text_input('Address')
    age = st.number_input("Age", min_value=18, max_value=100)
    gender = st.selectbox("Gender", options=["Male", "Female", "Other"])
    personal_training = st.checkbox('Do you want personal training?')

    # Get user input for contact details
    st.header("Contact Details")
    email = st.text_input("Email")
    phone = st.text_input("Phone")

    # Emergency Contact
    st.header("Emergency Contact")
    emergency_name = st.text_input("Emergency Contact Name")
    relationship = st.text_input("Relationship")
    emergency_phone = st.text_input("Emergency Contact Phone")

    # Get user input for membership type
    st.header("Membership Type")
    membership_type = st.radio("Select Membership Type", options=["Monthly", "Quarterly", "Yearly"])
    package = st.radio("Choose Membership Package", ["Basic", "Standard", "Premium"])

    # Get user input for fitness goals
    st.header("Fitness Goals")
    fitness_goals = st.text_area("What are your fitness goals?")

    # Get user input for medical conditions
    st.header("Medical Conditions")
    medical_conditions = st.text_area("Do you have any medical conditions? If yes, please specify.")

    # Health Information
    st.header("Health Information")
    allergies = st.text_area("Allergies (if any)")
    medications = st.text_area("Medications (if any)")
    recent_injuries = st.text_area("Recent Injuries or Surgeries")

    # Terms and Conditions
    st.header("Terms and Conditions")
    st.write("""
                       1. You must be at least 18 years old to join our gym.
                       2. Membership fees are non-refundable.
                       3. Any damages caused to gym property will be the responsibility of the member.
                       4. Our gym reserves the right to terminate membership for violation of gym rules or misconduct.
                       """)
    terms_accepted = st.checkbox("I agree to the Terms and Conditions")

    # Display submit button
    if st.button("Submit"):
        st.success("Form submitted successfully!")
        # Save form data to a file or database
        save_data(first_name, middle_name, last_name, dob, address, age, gender, personal_training, email, phone,
                  emergency_name, relationship, emergency_phone, membership_type, package, fitness_goals, medical_conditions,
                   allergies, medications, recent_injuries)

def save_data(first_name, middle_name, last_name, dob, address, age, gender, persnoal_training, email, phone,
              emergency_name, relationship, emergency_phone , membership_type, package, fitness_goals, medical_conditions,
              allergies, medications, recent_injuries):

    # Save form data to a file or database
    with open("gym_admission_data.txt", "a") as f:
        f.write(f"First Name: {first_name}\n")
        f.write(f"Middle_Name: {middle_name}\n")
        f.write(f"Last Name: {last_name}\n")
        f.write(f"Date_of_Birth: {dob}\n")
        f.write(f"Address: {address}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Gender: {gender}\n")
        f.write(f"Persnoal Training: {persnoal_training}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Phone: {phone}\n")
        f.write(f"Emergency_Name: {emergency_name}\n")
        f.write(f"Relationship: {relationship}\n")
        f.write(f"Emergency_Phone: {emergency_phone}\n")
        f.write(f"Membership Type: {membership_type}\n")
        f.write(f"Package: {package}\n")
        f.write(f"Fitness Goals: {fitness_goals}\n")
        f.write(f"Medical Conditions: {medical_conditions}\n")
        f.write(f"Allergies: {allergies}\n")
        f.write(f"Medications: {medications}\n")
        f.write(f"Recent_Injuries: {recent_injuries}\n\n")

if __name__ == "__main__":
    main()