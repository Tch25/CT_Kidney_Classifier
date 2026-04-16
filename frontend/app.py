import streamlit as st
#Send HTTP requests to the FastAPI backend
import requests
from PIL import Image
import io

#---Configuration---
st.set_page_config(
    page_title = "Kidney CT Analyzer",
    page_icon = "🩻",
    layout = "wide"
)

#--Style--
st.markdown("""
    <style>
        .centered-title {
            text-align: center;
        }
        .centered-subtitle {
            text-align: center;
            color: #666;
        }
        /* New button styling */
    div.stButton > button {
        background-color: #1E88E5;
        color: white;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        width: 100%;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #1565C0;
        color: white;
    }

    /*background */
    .stApp {
    background: linear-gradient(to bottom, #E8F4F8 0%, #81D4FA 100%);
    }
    /* Make file uploader text bigger */
    .stFileUploader label {
    font-size: 1.8rem !important;
    font-weight: 600 !important;
    }

    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    #URL of the API
    API_URL = st.text_input("API Endpoint:", value="https://ct-kidney-classifier-709689790245.europe-west1.run.app")
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("This tool uses deep learning to analyze kidney CT scans and detect abnormalities.")
    st.markdown("---")
    st.markdown("### 👩‍💻 Made by")
    st.markdown("[Valeria](https://github.com/VMontejo) & [Milka](https://github.com/Tch25)")


#---App header and description---
st.markdown('<h1 class="centered-title">🩻 Kidney CT Scan Analyzer</h1>', unsafe_allow_html=True)
st.markdown('<h4 class="centered-subtitle">AI-powered detection of cysts, tumors, and kidney stones</h4>', unsafe_allow_html=True)

#---file uploader---
uploaded_file = st.file_uploader(
    "Choose a CT image...",
    type = ["jpg", "png", "jpeg"]
)


# --- Display the image and add columns ---
if uploaded_file is not None:
    # Open the image using PIL
    image = Image.open(uploaded_file)

    # Create two columns side by side
    col1, col2 = st.columns(2)

    # Column 1: Show the uploaded image
    with col1:
        st.subheader("📷 Uploaded CT Scan")
        st.image(image, width=400)

    # Column 2: Will show results
    with col2:
        st.subheader("📊 Analysis Results")

        # --- Add the analyze button and API call ---
        if st.button("🔍 Analyze CT Scan"):
            with st.spinner("Analyzing..."):
                # Prepare image for API
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "image/jpeg")}

                # Call the API
                response = requests.post(f"{API_URL}/predict", files=files)

                if response.status_code == 200:
                    result = response.json()
                    pred = result['prediction']
                    confidence = result['confidence']

                    # Show result with color
                    if pred == "Stone":
                        st.error(f"⚠️ **{pred}** detected ({confidence:.1%} confidence)")
                    elif pred == "Tumor":
                        st.error(f"🟠 **{pred}** detected ({confidence:.1%} confidence)")
                    elif pred == "Cyst":
                        st.info(f"📌 **{pred}** detected ({confidence:.1%} confidence)")
                    else:
                        st.success(f"✅ **{pred}** ({confidence:.1%} confidence)")
                    # Show medical recommendation
                    st.markdown("---")
                    st.markdown("### 📋 Clinical Recommendation")

                    if pred == "Stone":
                        st.info("💧 **Recommendation:** Increase fluid intake (2-3L/day). Consult urology if symptomatic.")
                    elif pred == "Tumor":
                        st.warning("🏥 **Recommendation:** Further characterization with contrast-enhanced CT/MRI recommended. Urgent urology consultation advised.")
                    elif pred == "Cyst":
                        st.success("✅ **Recommendation:** Benign finding. Follow-up imaging in 6-12 months.")
                    else:
                        st.success("✅ **Recommendation:** No abnormalities detected. Continue routine monitoring.")

                    # Show AI-generated clinical report
                    if 'report' in result:
                        st.markdown("---")
                        st.markdown("### 📄 AI Clinical Report")
                        st.info(result['report'])
                        st.caption("⚠️ AI-generated. Must be reviewed by a medical professional.")


                else:
                    st.error(f"API Error: {response.status_code}")
