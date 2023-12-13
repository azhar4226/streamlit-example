import streamlit as st

def find_largest_number(num1, num2, num3):
    numbers = [num1, num2, num3]
    largest_number = max(numbers)
    return largest_number

def main():
    st.title("Find the Largest Number App")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest Number"):
        result = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
