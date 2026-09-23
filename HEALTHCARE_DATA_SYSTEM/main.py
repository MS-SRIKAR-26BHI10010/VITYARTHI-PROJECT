"""Entry point for the healthcare data system."""

from consultation import collect_consultation
from medical_conditions import collect_medical_conditions
from patient_details import collect_patient_details
from payment_method import collect_payment_method


def main():
    patient = collect_patient_details()
    history = collect_medical_conditions()
    payment = collect_payment_method()
    consultation = collect_consultation()

    print("\n" + "=" * 58)
    print("             PATIENT CONSULTATION & TRIAGE NOTE")
    print("=" * 58)
    print(f"PATIENT NAME     : {patient['name']}")
    print(f"AGE / DOB        : {patient['age']} yrs | DOB: {patient['date_of_birth']}")
    print(f"VITALS/METRICS   : Height: {patient['height']} | Weight: {patient['weight']} kg")
    print(f"PAYMENT PROFILE  : {payment.upper()}")
    print("-" * 58)
    print(f"PAST HISTORY     : {history['past_conditions']}")
    print(f"GENETIC PROFILE  : {consultation['genetic_disease']}")
    print(f"PRESENTING SIGNS : {consultation['symptoms']}")
    print("-" * 58)
    print(f"PRELIMINARY NOTE : {consultation['disease']}")
    print(f"RECOMMENDATION   : {consultation['medicine']}")
    print("=" * 58)
    print("DISCLAIMER: This is preliminary decision support, not a diagnosis.")
    print("Seek qualified medical care; call emergency services for acute symptoms.")
    print("=" * 58)


if __name__ == "__main__":
    main()
