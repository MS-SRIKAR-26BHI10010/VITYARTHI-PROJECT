import patient_details
import medical_conditions
import payment_method
import consultation

print("\n" + "=" * 50)
print("       PATIENT CONSULTATION & TRIAGE NOTE        ")
print("=" * 50)
print(f"PATIENT NAME     : {patient_details.name}")
print(f"AGE / DOB        : {patient_details.age} yrs | DOB: {patient_details.date_of_birth}")
print(f"VITALS/METRICS   : Height: {patient_details.height} | Weight: {patient_details.weight} kg")
print(f"PAYMENT PROFILE  : {payment_method.payment.upper()}")
print("-" * 50)
print(f"PAST HISTORY     : {medical_conditions.past_conditions if medical_conditions.medical_conditions == 'Yes' else 'None reported'}")
print(f"GENETIC PROFILE  : {consultation.genetic_disease}")
print(f"PRESENTING SIGNS : {consultation.symptoms}")
print("-" * 50)
print(f"PRESUMPTIVE DX   : {consultation.disease}")
print(f"RECOMMENDED PLAN : {consultation.medicine}")
print("=" * 50)
print("DISCLAIMER: Automated preliminary decision support only.")
print("Immediate physician or EMS escalation required for acute red flags.")
print("=" * 50 + "\n")
