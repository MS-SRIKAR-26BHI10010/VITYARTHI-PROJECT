# HEALTHCARE DATA SYSTEM 
## Problem Statement
During first clinical visits, collecting and matching patient information like demographic details, physical measurements, medical history, presenting symptoms, and billing preferences usually relies on manual data entry. This increases administrative work, raises the risk of overlooking important background factors such as previous illnesses or genetic susceptibilities, and delays the preparation of initial consultation summaries for attending doctors. And it's even hard to store as a hard copy. 

## Scope of the Project
- Patient Data Collection: Asking for patient personal identification, demographic records, and biometric measurements (height and weight).
- Clinical History & Genetic History: Recording pre-existing medical conditions, genetic disease profiles, and active symptoms the patient is facing.
- Consultation report: Associating symptoms with preliminary disease assessments and suggested medications.
- Billing: Asking for preferred patient payment methods.
- Command-line interface (CLI) Consultation Report: Consolidating modular data into a structured, readable consultation summary complete with a clinical safety disclaimer.

## Target Users
- Clinic Desk Staff: To quickly record basic demographics, biometric metrics, and billing preferences during patient registration.
​- Outpatient Clinic Physicians & Medical Assistants: To review compact patient intakes, active symptoms, medical history, and primary consultation summaries at a glance.
​- Health Informatics Students & Developers: To explore and test modular Python programming structures for organizing clinical workflows and patient reports.

## High-Level Features
- System Architecture: Separate dedicated Python modules for handling different functions required for the project, which are as follows:
   - patient_details.py: Stores patient name, age, date of birth, height, and weight.
   - medical_conditions.py: Records previous and pre-existing medical background.
   - consultation.py: Manages genetic profiles, active symptoms, preliminary disease classifications, and medicine recommendations.
   - payment_method.py: Stores the patient's selected payment method.
- Unified Report Generation (main.py): Central report generation by importing all modular data components and formatting them into a clean, segmented consultation report.
- Integrated Clinical Safety Disclaimer: Automatically appends standard medical liability and emergency escalation disclaimers to remind users that output is non-diagnostic.
# CREATED BY :- SAI SRIKAR MAMIDANNA (26BHI10010)
# THANK YOU 
