import sys
import datetime
import json
import os

# File to store patient data
DATA_FILE = "patient_data.json"

def get_patient_details():
    """
    Collect basic patient details: name and age.
    """
    patient_details = {}
    print("\nEnter patient details:")
    patient_details["name"] = input("Patient's name: ").strip()  # Patient's name
    try:
        patient_details["age"] = int(input("Patient's age: ").strip())  # Patient's age
    except ValueError:
        print("Invalid input for age. Please enter a valid number.")
        sys.exit(1)
    return patient_details

def get_patient_vitals():
    """
    Collect patient vital signs for trauma triage.
    Ensures accurate input and provides feedback for invalid entries.
    """
    vitals_data = {}
    print("\nPlease enter the following vital signs for trauma triage.\n")
    try:
        vitals_data["temperature"] = float(input("Body temperature (Celsius): ").strip())  # Core body temperature
        vitals_data["heart_rate"] = int(input("Heart rate (beats per minute): ").strip())  # Heart rate
        vitals_data["blood_pressure_sys"] = int(input("Systolic BP (mmHg): ").strip())  # Systolic BP
        vitals_data["blood_pressure_dia"] = int(input("Diastolic BP (mmHg): ").strip())  # Diastolic BP
        vitals_data["oxygen_saturation"] = float(input("Oxygen saturation (%): ").strip())  # O2 saturation
        vitals_data["glasgow_coma_scale"] = int(input("Glasgow Coma Scale score (3-15): ").strip())  # GCS
        vitals_data["respiratory_rate"] = int(input("Respiratory rate (breaths per minute): ").strip())  # Respiratory rate
        vitals_data["recorded_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Timestamp
        print("\nVitals recorded successfully!\n")
        return vitals_data
    except ValueError:
        print("Invalid input. Please ensure all values are numeric.")
        sys.exit(1)

def save_patient_data(patient_details, vitals_data):
    """
    Save patient data to a JSON file.
    If the file exists, append the new entry; otherwise, create a new file.
    """
    patient_record = {**patient_details, **vitals_data}

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)  # Initialize an empty list in the JSON file

    with open(DATA_FILE, "r+") as file:
        data = json.load(file)
        data.append(patient_record)
        file.seek(0)
        json.dump(data, file, indent=4)
    print("Patient data saved to file.\n")

def calculate_shock_index(vitals_data):
    """
    Calculate the Shock Index (SI): Heart Rate / Systolic Blood Pressure.
    """
    return vitals_data["heart_rate"] / vitals_data["blood_pressure_sys"]

def calculate_rts(vitals_data):
    """
    Calculate Revised Trauma Score (RTS) using:
    RTS = (0.9368 * GCS) + (0.7326 * Systolic BP) + (0.2908 * Respiratory Rate)
    """
    return (0.9368 * vitals_data["glasgow_coma_scale"] +
            0.7326 * vitals_data["blood_pressure_sys"] +
            0.2908 * vitals_data["respiratory_rate"])

def evaluate_triage(vitals_data):
    """
    Evaluate patient condition using multiple indicators and assign a triage level.
    """
    feedback = []
    critical = False

    # Evaluate Shock Index
    shock_index = calculate_shock_index(vitals_data)
    if shock_index > 0.9:
        feedback.append(f"Shock Index: {shock_index:.2f} (High). Indicates potential hypovolemic shock.")
        critical = True
    elif 0.7 <= shock_index <= 0.9:
        feedback.append(f"Shock Index: {shock_index:.2f} (Moderate). Requires closer monitoring.")
    else:
        feedback.append(f"Shock Index: {shock_index:.2f} (Low). Stable.")

    # Evaluate Revised Trauma Score
    rts = calculate_rts(vitals_data)
    if rts < 4:
        feedback.append(f"RTS: {rts:.2f}. Critical condition, immediate intervention required.")
        critical = True
    elif rts < 7:
        feedback.append(f"RTS: {rts:.2f}. Moderate condition, monitor closely.")
    else:
        feedback.append(f"RTS: {rts:.2f}. Stable condition.")

    # Glasgow Coma Scale Evaluation
    gcs = vitals_data["glasgow_coma_scale"]
    if gcs <= 8:
        feedback.append("GCS: Severe head injury (critical condition).")
        critical = True
    elif 9 <= gcs <= 12:
        feedback.append("GCS: Moderate head injury. Monitor closely.")
    else:
        feedback.append("GCS: Mild head injury.")

    # Respiratory Rate Evaluation
    rr = vitals_data["respiratory_rate"]
    if rr < 10 or rr > 29:
        feedback.append("Respiratory rate abnormal. Potential respiratory distress.")
        critical = True
    else:
        feedback.append("Respiratory rate is normal.")

    # Oxygen Saturation Evaluation
    o2_sat = vitals_data["oxygen_saturation"]
    if o2_sat < 90:
        feedback.append("Oxygen saturation critically low (<90%). Immediate support needed.")
        critical = True
    elif o2_sat < 95:
        feedback.append("Oxygen saturation slightly low. Monitor closely.")
    else:
        feedback.append("Oxygen saturation normal.")

    # Blood Pressure Evaluation
    sbp = vitals_data["blood_pressure_sys"]
    dbp = vitals_data["blood_pressure_dia"]
    if sbp < 90 or dbp < 60:
        feedback.append("Hypotension detected. Align with medical triage criteria for shock and hypovolemia.")
        critical = True
    elif sbp > 180 or dbp > 120:
        feedback.append("Hypertension crisis (Emergency). Immediate evaluation required.")
        critical = True
    elif sbp > 160 or dbp > 100:
        feedback.append("Hypertension urgency. No immediate damage, but close monitoring needed.")
    else:
        feedback.append("Blood pressure normal.")

    # Heart Rate Evaluation
    hr = vitals_data["heart_rate"]
    if hr < 50 or hr > 100:
        feedback.append("Abnormal heart rate. Possible cardiac distress.")
        critical = True
    else:
        feedback.append("Heart rate normal.")

    # Temperature Evaluation
    temp = vitals_data["temperature"]
    if temp < 35:
        feedback.append("Hypothermia detected. Warm the patient immediately.")
        critical = True
    elif 37.5 <= temp <= 38.4:
        feedback.append("Low-grade fever detected. Monitor for potential infection.")
    elif temp > 38.5:
        feedback.append("Fever detected. Monitor for infection or systemic inflammatory response.")
    else:
        feedback.append("Temperature normal.")

    # Assign triage level
    triage_level = "RED - IMMEDIATE" if critical else "YELLOW - OBSERVATION"
    feedback.append(f"Triage Level: {triage_level}")
    return feedback, triage_level

def display_summary(patient_details, vitals_data, feedback, triage_level):
    """
    Display a summary of vital signs, evaluations, and assigned triage level.
    """
    print("\nTrauma Triage Summary:")
    print("----------------------------------------")
    print(f"Patient Name: {patient_details['name']}")
    print(f"Patient Age: {patient_details['age']} years")
    print(f"Recorded Time: {vitals_data['recorded_time']}")
    print(f"Body Temperature: {vitals_data['temperature']} °C")
    print(f"Heart Rate: {vitals_data['heart_rate']} bpm")
    print(f"Blood Pressure: {vitals_data['blood_pressure_sys']}/{vitals_data['blood_pressure_dia']} mmHg")
    print(f"Respiratory Rate: {vitals_data['respiratory_rate']} breaths/min")
    print(f"Oxygen Saturation: {vitals_data['oxygen_saturation']}%")
    print(f"Glasgow Coma Scale: {vitals_data['glasgow_coma_scale']}")
    print("----------------------------------------")
    print("Triage Feedback:")
    for line in feedback:
        print(f"- {line}")
    print(f"\n**Assigned Triage Level: {triage_level}**")

def main():
    """Run the trauma triage system."""
    print("Welcome to the Trauma Emergency Department Triage System!\n")
    patient_details = get_patient_details()
    vitals_data = get_patient_vitals()
    save_patient_data(patient_details, vitals_data)
    feedback, triage_level = evaluate_triage(vitals_data)
    display_summary(patient_details, vitals_data, feedback, triage_level)

if __name__ == "__main__":
    main()
