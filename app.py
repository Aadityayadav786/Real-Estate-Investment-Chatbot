import streamlit as st
from crew import Crew
from agents import property_researcher, property_analyst
from tasks import generate_tasks  # function that creates tasks dynamically
from crew import run_crew_for_city
st.set_page_config(page_title="Retail Property Investment AI", layout="wide")

st.title("🏙️ Retail Property Investment AI")
st.write("Enter a city to analyze retail property investment opportunities.")

city_name = st.text_input("Enter city name", "Bhopal")

if st.button("🔍 Run Property Investment Analysis"):
    if not city_name.strip():
        st.warning("Please enter a valid city name.")
    else:
        with st.spinner(f"Running agents for {city_name}..."):
            try:
                # Dynamically create tasks for the selected city
                property_research_task, property_analysis_task = generate_tasks(city_name)

                # Create and run Crew instance
                crew = Crew(
                    agents=[property_researcher, property_analyst],
                    tasks=[property_research_task, property_analysis_task],
                    verbose=True
                )

                task_output = run_crew_for_city(city_name)

                st.success("✅ Task completed successfully!")
                st.subheader("Agent Output")

                # Display output as markdown for better formatting
                st.markdown(task_output, unsafe_allow_html=False)

            except Exception as e:
                st.error(f"❌ Error: {e}")
