# VITYARTHI-PROJECT

## Healthcare Data System

A simple Python-based healthcare data collection and preliminary consultation system. The program collects basic patient information, medical history, payment details, genetic conditions, and symptoms, then displays a formatted consultation and triage note.

> **Important:** This project is for educational and preliminary decision-support purposes only. It does not provide a medical diagnosis or replace advice from a qualified healthcare professional.

## Features

- Collects patient details:
  - Name
  - Age
  - Date of birth
  - Height
  - Weight
- Records previous medical conditions
- Records genetic diseases
- Accepts common payment methods:
  - Cash
  - Card
  - Insurance
- Performs a basic rule-based symptom assessment
- Displays a formatted patient consultation and triage note
- Validates several user inputs and asks again when input is invalid

## Technologies Used

- Python 3
- Python standard library
- Command-line interface (CLI)

## Project Structure

```text
VITYARTHI-PROJECT/
├── README.md
└── HEALTHCARE_DATA_SYSTEM/
    ├── main.py
    ├── consultation.py
    ├── medical_conditions.py
    ├── patient_details.py
    └── payment_method.py
```

## Requirements

- Python 3.8 or later
- No external Python packages are required

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/MS-SRIKAR-26BHI10010/VITYARTHI-PROJECT.git
   ```

2. Open the project directory:

   ```bash
   cd VITYARTHI-PROJECT/HEALTHCARE_DATA_SYSTEM
   ```

3. Run the program:

   ```bash
   python main.py
   ```

   On some systems, use:

   ```bash
   python3 main.py
   ```

4. Follow the prompts in the terminal.

## How It Works

The application runs as a sequence of interactive steps:

1. Collects patient details.
2. Collects past medical conditions.
3. Collects the preferred payment method.
4. Collects genetic disease information and symptoms.
5. Matches entered symptoms against predefined rules.
6. Prints a preliminary consultation and triage note.

## Example Symptom Rules

The current prototype includes rules for symptoms such as:

- Chest pain
- Sudden weakness
- Facial drooping
- Shortness of breath
- Fever
- Cough
- Headache and nausea
- Rash and itching
- Burning urination
- Heartburn

These rules are only basic text matches and should not be used to make medical decisions.

## Future Improvements

- Add a graphical or web-based user interface
- Store patient records securely in a database
- Add authentication and role-based access
- Improve symptom and condition matching
- Add automated tests
- Generate downloadable reports
- Add stronger privacy and data-protection controls

## Disclaimer and Privacy Notice

Do not enter real patient information into this educational prototype unless appropriate security, consent, and data-protection measures have been implemented. The output is preliminary information only and must be reviewed by a qualified healthcare professional.

## Author

**MS-SRIKAR-26BHI10010**

## License

A license has not yet been selected for this project. Add a license here when you decide how others may use, modify, and distribute the code.
