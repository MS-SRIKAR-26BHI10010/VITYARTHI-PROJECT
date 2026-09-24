#VITYARTHI-PROJECT
Healthcare Data System
A simple Python-based healthcare data collection and preliminary consultation system. The program collects basic patient information, medical history, payment details, genetic conditions, and symptoms, then displays a formatted consultation and triagee notes.

#Features
Collects patient details:
Name:
Age:
Date of birth:
Height:
Weight:
Records previous medical conditions:
Records genetic diseases:
Accepts common payment methods(Cash , Card ,Insurance):

Performs a basic rule-based symptom assessment
Displays a formatted patient consultation and triage note
Validates several user inputs and asks again when input is invalid

#Technologies Used
Python 
Python standard library
Command-line interface (CLI)

#Project Structure
VITYARTHI-PROJECT/
├── README.md
└── HEALTHCARE_DATA_SYSTEM/
    ├── main.py
    ├── consultation.py
    ├── medical_conditions.py
    ├── patient_details.py
    └── payment_method.py
Requirements
Python 3.8 or later
No external Python packages are required
How to Run
Clone this repository:

git clone https://github.com/MS-SRIKAR-26BHI10010/VITYARTHI-PROJECT.git
Open the project directory:

cd VITYARTHI-PROJECT/HEALTHCARE_DATA_SYSTEM
Run the program:

python main.py
On some systems, use:

python3 main.py
Follow the prompts in the terminal.

How It Works
The application runs as a sequence of interactive steps:

Collects patient details.
Collects past medical conditions.
Collects the preferred payment method.
Collects genetic disease information and symptoms.
Matches entered symptoms against predefined rules.
Prints a preliminary consultation and triage note.
Example Symptom Rules
The current prototype includes rules for symptoms such as:

Chest pain
Sudden weakness
Facial drooping
Shortness of breath
Fever
Cough
Headache and nausea
Rash and itching
Burning urination
Heartburn
These rules are only basic text matches and should not be used to make medical decisions.

Future Improvements
Add a graphical or web-based user interface
Store patient records securely in a database
Add authentication and role-based access
Improve symptom and condition matching
Add automated tests
Generate downloadable reports
Add stronger privacy and data-protection controls
Disclaimer and Privacy Notice
Do not enter real patient information into this educational prototype unless appropriate security, consent, and data-protection measures have been implemented. The output is preliminary information only and must be reviewed by a qualified healthcare professional.

Author
MS-SRIKAR-26BHI10010

License
A license has not yet been selected for this project. Add a license here when you decide how others may use, modify, and distribute the code.
