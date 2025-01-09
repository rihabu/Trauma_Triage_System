# Trauma Emergency Department Triage System

#### Video Demo: https://youtu.be/j5uJ5oNUutU?si=6jqm2B7dh4YPHx48

#### Description:
The **Trauma Emergency Department Triage System** is a Python-based application designed to assist medical professionals in making fast and accurate triage decisions for trauma patients based on their vital signs.
This system calculates critical health indicators, such as the **Shock Index** and **Revised Trauma Score (RTS)**, to help assess the severity of trauma and guide emergency response.

### **Medical Context:**
In an emergency department, quick and accurate triage is essential for prioritizing care, particularly in trauma situations where resources may be limited.
The system leverages vital signs to assess the patient's condition and provide recommendations that help clinicians decide on the urgency of intervention.

The following medical metrics are used in the triage process:

- **Shock Index (SI)**: This index is the ratio of heart rate to systolic blood pressure and is used to assess the risk of hypovolemic shock, a life-threatening condition that can result from severe blood loss.
  - **SI > 0.9**: High risk (suggests hypovolemic shock or hemodynamic instability).
  - **SI between 0.7 and 0.9**: Moderate risk (requires closer monitoring).
  - **SI < 0.7**: Low risk (generally stable condition).

- **Revised Trauma Score (RTS)**: This score is calculated based on the **Glasgow Coma Scale (GCS)**, **Systolic Blood Pressure (SBP)**, and **Respiratory Rate (RR)**. It is used to assess the severity of trauma and predict mortality risk:
  - **Higher RTS values** suggest a better prognosis, indicating stable or mild conditions.
  - **Lower RTS values** are associated with critical trauma and a higher risk of mortality.

- **Glasgow Coma Scale (GCS)**: The GCS assesses a patient's level of consciousness based on eye, verbal, and motor responses. A score between 3 and 15 helps clinicians determine the severity of brain injury:
  - **GCS < 8**: Severe head injury, potentially requiring immediate intervention.
  - **GCS 9-12**: Moderate head injury, close monitoring needed.
  - **GCS > 12**: Mild head injury, non-critical.

The system also evaluates other indicators such as oxygen saturation, respiratory rate, blood pressure, and body temperature to provide a comprehensive triage level (e.g., **RED - IMMEDIATE** for critical patients or **YELLOW - OBSERVATION** for stable patients).

### **Key Features:**

- **Vital Signs Collection**: Collects vital signs such as body temperature, heart rate, blood pressure, oxygen saturation, Glasgow Coma Scale (GCS), and respiratory rate from the user.
- **Shock Index (SI) Calculation**: Determines the potential for shock based on heart rate and systolic blood pressure.
- **Revised Trauma Score (RTS)**: Calculates a score to evaluate the severity of trauma based on key parameters (GCS, SBP, and RR).
- **Triage Level Assignment**: Based on the vital signs and calculated scores, the system classifies the patient’s condition and provides a recommended triage level: **RED (Immediate)**, **YELLOW (Observation)**, or **GREEN (Stable)**.
- **Medical Feedback**: Offers diagnostic feedback based on vital sign readings, alerting clinicians to potential issues like hypotension, abnormal heart rate, or low oxygen saturation.

### **Usage:**
1. The user is prompted to enter critical vital signs such as heart rate, blood pressure, and respiratory rate.
2. The system calculates the **Shock Index** and **Revised Trauma Score**.
3. Feedback is provided based on these calculations, offering insights on the patient's condition.
4. The system assigns a **triage level** (e.g., **RED**, **YELLOW**, or **GREEN**) based on the overall assessment.

### **Potential Applications:**
- **Emergency Departments**: This system can help prioritize care based on the severity of trauma, especially during mass casualty incidents or limited resource scenarios.
- **Pre-hospital Care**: First responders can use the system to quickly assess the patient's condition and make decisions on transport and treatment.
- **Clinical Decision Support**: Healthcare providers can use this tool as part of their decision-making process to evaluate patients in real time and ensure they receive the right level of care.
