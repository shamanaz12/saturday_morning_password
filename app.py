import streamlit as st
import string
import secrets

# Function to check password strength
def check_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)

    score = sum([has_upper, has_lower, has_digit, has_special]) + (length >= 8)

    if length < 8:
        return "❌ Weak", "🔴 Too short! Use at least 8 characters."
    elif score == 2:
        return "⚠️ Medium", "🟠 Add special characters & numbers for better security."
    elif score >= 4:
        return "✅ Strong", "🟢 Good! Your password is strong."
    else:
        return "❌ Weak", "🔴 Mix uppercase, lowercase, numbers & symbols."

# Function to generate a strong password
def generate_password(length=12):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    return password

# Streamlit App UI
st.title("🔐 Password Strength Checker & Generator")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    st.subheader(f"Strength: {strength}")
    st.write(feedback)

# Password Generator Section
st.subheader("🔑 Generate a Strong Password")
length = st.slider("Select Password Length", min_value=8, max_value=32, value=12)
if st.button("Generate Password"):
    new_password = generate_password(length)
    st.code(new_password, language="bash")
