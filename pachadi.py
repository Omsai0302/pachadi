import streamlit as st

# Title and Introduction
st.title("AMMA Pachadi - Health Advisor & Pickle Customization")
st.write("Welcome to AMMA Pachadi! Let's find the perfect pickle for your health and taste preferences.")

# Collect Customer Health Data and Preferences
st.subheader("Tell us about your health and taste preferences to find the perfect pickle!")
bp = st.radio("Do you have high blood pressure?", ["Yes", "No"])
vitamin_deficiency = st.multiselect("Do you have any vitamin deficiencies?", ["Vitamin K", "Vitamin B12", "Vitamin D", "Iron", "Magnesium", "Calcium"])
dietary_preference = st.radio("Any dietary preferences?", ["Low Salt", "Low Sugar", "No Restrictions"])
health_conditions = st.multiselect("Do you have any of the following conditions?", ["Diabetes", "Heart Disease", "Cholesterol", "Obesity", "Digestive Issues"])

# Customize the Pickle (Ingredient Choices and Preferences)
pickle_type = st.selectbox("Choose a pickle type:", [
    "Gongura Mutton Pachadi", "Gongura Prawns Pachadi", "Fish Pachadi", 
    "Mango Pachadi", "Prawns Pachadi", "Tamarind Pachadi", 
    "Kakkarkayi Pachadi", "Vankayi Pachadi", "Drumstick Pachadi", 
    "Amla Pachadi"
])

# Salt Concentration Slider
salt_concentration = st.slider("Select salt concentration (1-10, where 1 is low, 10 is high):", 1, 10, 5)

# Display Health Benefits Based on Custom Pickle Selection
st.subheader("Health Benefits of Your Custom Pickle")

# Health Conditions and Custom Pickle Logic
if bp == "Yes":
    st.warning("We recommend pickles with **low salt content** like **Tamarind Pachadi** and **Amla Pachadi**, which help maintain healthy blood pressure levels.")

if "Vitamin K" in vitamin_deficiency:
    st.success("Pickles with **Gongura** are rich in Vitamin K, which helps with blood clotting and maintaining healthy bones. Try **Gongura Mutton Pachadi** or **Gongura Prawns Pachadi** to boost your Vitamin K levels!")

if dietary_preference == "Low Salt":
    st.info("For a healthier choice with less salt, consider customizing your pickle with reduced salt. **Tamarind Pachadi**, **Amla Pachadi**, and **Drumstick Pachadi** are great low-salt options that still deliver fantastic taste and health benefits!")

if "Diabetes" in health_conditions:
    st.info("Pickles with **low sugar** are better for managing blood sugar. We recommend **Kakkarkayi Pachadi**, which is high in fiber and helps regulate blood sugar levels naturally!")

if "Heart Disease" in health_conditions:
    st.info("Opt for heart-healthy pickles like **Fish Pachadi** and **Drumstick Pachadi**, which are rich in **Omega-3 fatty acids**, **Vitamin E**, and **fiber**, promoting heart health and reducing inflammation.")

if "Cholesterol" in health_conditions:
    st.info("Pickles that are **low in fat** and high in **fiber** can help manage cholesterol. Try **Vankayi Pachadi** or **Drumstick Pachadi**, which are both rich in **antioxidants** and help promote a healthy heart!")

if "Obesity" in health_conditions:
    st.info("For weight management, pickles with **low calories** like **Tamarind Pachadi** and **Amla Pachadi** are ideal choices. Their natural ingredients help with digestion and detoxification.")

if "Digestive Issues" in health_conditions:
    st.info("Pickles with **antioxidants** and **anti-inflammatory properties** are excellent for digestive health. Try **Gongura Pachadi**, which is known to improve gut health and reduce bloating and indigestion!")

# Display Pickle Health Benefits Based on Type with Vitamins, Nutrients, Health Metrics, and Fermentation Duration (3 months)
if pickle_type == "Fish Pachadi":
    st.write("""
        **Fish Pachadi** is a powerhouse of nutrients! 
        - **Rich in Omega-3 fatty acids**: Great for heart health, reducing inflammation, and boosting brain function.
        - **High in Protein**: Supports muscle growth and repair.
        - **Contains Vitamin D**: Helps improve bone health and strengthens your immune system.
        - **Boosts Mental Health**: Omega-3s are linked to better cognitive function and mood improvement.
        - **Selenium**: Essential for the body's antioxidant defense and thyroid health.
        - **Zinc**: Supports the immune system and helps with wound healing.
        
        **Fermentation Duration**: Typically stays fresh for up to **3 months** when stored properly in a cool, dry place.
    """)
elif pickle_type == "Gongura Mutton Pachadi":
    st.write("""
        **Gongura Mutton Pachadi** combines the goodness of mutton and the tangy flavor of Gongura:
        - **Gongura** is rich in **Vitamin C**, iron, and **folate**, improving blood circulation and immune function.
        - **Mutton** provides high-quality protein, supporting muscle repair and recovery.
        - Gongura also has **antioxidants** that help fight inflammation and oxidative stress, promoting overall wellness.
        - **Supports Heart Health**: Gongura’s natural compounds help in managing cholesterol levels and reducing blood pressure.
        - **Magnesium**: Promotes healthy muscle and nerve function.
        - **Iron**: Supports red blood cell production and prevents anemia.
        
        **Fermentation Duration**: Can be stored for up to **3 months** when kept in proper conditions.
    """)
elif pickle_type == "Tamarind Pachadi":
    st.write("""
        **Tamarind Pachadi** is excellent for digestive health:
        - **Rich in Fiber**: Supports digestion and helps prevent constipation.
        - **Packed with Antioxidants**: Protects the body from free radicals and boosts immunity.
        - **Vitamin C**: Helps improve skin health and strengthens the immune system.
        - **Aids Detoxification**: Tamarind naturally helps the body flush out toxins and promotes healthy liver function.
        - **Potassium**: Regulates blood pressure and supports heart health.
        - **Magnesium**: Supports nerve function and bone health.
        
        **Fermentation Duration**: Stays fresh for **up to 3 months** with proper storage.
    """)
elif pickle_type == "Amla Pachadi":
    st.write("""
        **Amla Pachadi** is a perfect choice for boosting immunity and overall vitality:
        - **High in Vitamin C**: Known for boosting the immune system and reducing the risk of infections.
        - **Rich in Antioxidants**: Amla is loaded with antioxidants, which help fight aging and oxidative stress.
        - **Supports Digestion**: Amla aids in digestion, improves gut health, and promotes a healthy metabolism.
        - **Promotes Hair Growth**: Vitamin C in Amla strengthens hair follicles and promotes hair growth.
        - **Calcium**: Supports bone health and prevents bone-related issues.
        - **Iron**: Helps in the production of red blood cells and boosts energy.
        
        **Fermentation Duration**: Can last for **up to 3 months** if stored correctly.
    """)
elif pickle_type == "Mango Pachadi":
    st.write("""
        **Mango Pachadi** is packed with seasonal goodness:
        - **Rich in Vitamin A**: Great for maintaining healthy skin and improving eyesight.
        - **High in Fiber**: Supports healthy digestion and aids in weight management.
        - **Full of Antioxidants**: Mangoes are rich in antioxidants, which help in detoxification and fight free radicals.
        - **Improves Immunity**: Vitamin C in Mango helps strengthen the immune system.
        - **Potassium**: Supports heart health and regulates blood pressure.
        - **Magnesium**: Helps in energy production and supports muscle function.
        
        **Fermentation Duration**: Typically lasts **up to 3 months** when stored in an airtight container.
    """)

# Display Final Customization Choices
st.subheader("Your Custom Pickle")
st.write(f"Pickle Type: {pickle_type}")
st.write(f"Salt Concentration: {salt_concentration}")
st.write("Enjoy your personalized, health-conscious Pachadi! A perfect blend of taste and wellness.")

