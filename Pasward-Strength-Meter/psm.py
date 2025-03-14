
import streamlit as st
import re

# ... (rest of the code remains the same)

def check_password_strength(password):
    score = 0
    feedback = {}

    if len(password) >= 8:
        score += 1
    else:
        feedback["length"] = "Password must be at least 8 characters long."

    if re.search(r'[A-Z]', password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback["case"] = "Password must contain both uppercase and lowercase letters."

    if re.search(r'\d', password):
        score += 1
    else:
        feedback["digit"] = "Password must contain at least one digit."

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback["special"] = "Password must contain at least one special character."

    return score, feedback

def render_feedback(feedback):
    with st.expander("Improve your password"):
        for key, value in feedback.items():
            st.write(value)

def main():
    st.title("🔐 Password Strength Meter")
    st.write("Enter your password to check its security levels.🔍")

    password = st.text_input("Enter Password:", type="password", help="Ensure your password is strong.")

    if st.button("Check Password strength"):
        if password:
            score, feedback = check_password_strength(password)
            if score == 4:
                st.success("✔️ Strong Password - Your password is secure.")
            elif score == 3:
                st.info("❌ Moderate Password - Improve security by adding more characters.")
            else:
                st.error("❌Weak Password - Follow the suggestions below to strengthen it")
                render_feedback(feedback)
        else:
            st.warning("❌ Please enter your password!")

if __name__ == "__main__":
    main()