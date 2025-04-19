# import streamlit as st

# def convertor(conversion_value: float, unit_from: str, unit_to :str): #Arguments(taking value)


# #     # 1 kilometer = 1000 meters
# #     #1 meter = 0.001 kilometer
# #     # 1 kilogram = 1000 grams
# #     #1 gram = 0.001 kilogram

#     if unit_from == "kilometers" and unit_to == "meters":
#         return conversion_value * 1000
#     elif unit_from == "meters" and unit_to == "kilometers":
#         return conversion_value*0.001
#     elif unit_from == "kilograms" and unit_to == "grams":
#         return conversion_value*1000
#     elif unit_from == "grams" and unit_to == "kilograms":
#         return conversion_value*0.001
#     else:
#         return "Conversion Is not Supported"



# def unit_convertor():
#     st.title("UNIT CONVERTER")
#     st.write("Welcome to Unit Convertor")
#     conversion_value = st.number_input("Enter Your Value for Conversion:")
#     unit_from = st.text_input("Enter the Type you want to convert from (e.g meters, kilometers, grams, kilograms, ):")
#     unit_to = st.text_input("Enter the Type you want to convert in to (e.g meters, kilometers, grams, kilograms, ):")

#     # print("Value= ",conversion_value)
#     # print("Unit From = ",unit_from)
#     # print("Unit To = ",unit_to)

#     if st.button("convert"):
#         result = convertor(conversion_value, unit_from, unit_to)
#         st.write("Converted value is",result)

# unit_convertor()
import streamlit as st

def convertor(conversion_value: float, unit_from: str, unit_to: str):
    # Unit conversion logic
    if unit_from == "kilometers" and unit_to == "meters":
        return conversion_value * 1000
    elif unit_from == "meters" and unit_to == "kilometers":
        return conversion_value * 0.001
    elif unit_from == "kilograms" and unit_to == "grams":
        return conversion_value * 1000
    elif unit_from == "grams" and unit_to == "kilograms":
        return conversion_value * 0.001
    else:
        return "Conversion is not supported"

def unit_convertor():
    st.title("UNIT CONVERTER")
    st.write("Welcome to Unit Converter")

    conversion_value = st.number_input("Enter Your Value for Conversion:")
    unit_from = st.text_input("Convert from (e.g., meters, kilometers, grams, kilograms):")
    unit_to = st.text_input("Convert to (e.g., meters, kilometers, grams, kilograms):")

    if st.button("Convert"):
        result = convertor(conversion_value, unit_from.strip().lower(), unit_to.strip().lower())
        st.write("Converted value is:", result)

# Call the function
unit_convertor()
