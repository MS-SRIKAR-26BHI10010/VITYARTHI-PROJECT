
import patient_details
import medical_conditions
import consultation
import payment_method

print("PATIENT CONSULTATION REPORT")
print("=" * 58)
print(f"PATIENT NAME     : {patient_details.name}")
print(f"AGE / DOB        : {patient_details.age} yrs | DOB: {patient_details.date_of_birth}")
print(f"METRICS   : Height: {patient_details.height} | Weight: {patient_details.weight} kg")
print(f"PAYMENT PROFILE  : {payment_method.payment_method}")
print("-" * 58)
print(f"PAST HISTORY     : {medical_conditions.past_medical_conditions}")
print(f"GENETIC PROFILE  : {consultation.genetic_disease}")
print(f"PRESENTING SIGNS : {consultation.symptoms}")
print("-" * 58)
print(f"PRELIMINARY NOTE : {consultation.disease}")
print(f"RECOMMENDATION   : {consultation.medicine}")
print("=" * 58)
print("DISCLAIMER: This is a preliminary decision support, not a diagnosis report.")
print("Seek a qualified medical doctor; call emergency services for any  acute symptoms.")
print("=" * 58)

