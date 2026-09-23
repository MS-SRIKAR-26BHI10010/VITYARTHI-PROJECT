"""Rule-based preliminary symptom assessment; not a medical diagnosis."""

GENETIC_GUIDANCE = {
    "diabetes": ("Diabetes Mellitus Management", "Insulin therapy review and blood sugar monitoring kit"),
    "sickle cell": ("Sickle Cell Anemia", "Folic acid, pain management plan, and Hematology Referral"),
    "cystic fibrosis": ("Cystic Fibrosis", "Pancreatic enzyme supplements and Pulmonology Referral"),
}

SYMPTOM_RULES = [
    (("sudden weakness",), "Possible Stroke", "Call emergency services immediately"),
    (("facial drooping",), "Possible Stroke", "Call emergency services immediately"),
    (("chest pain",), "Possible Cardiovascular Risk", "Seek immediate emergency medical care"),
    (("shortness of breath",), "Breathing Emergency", "Seek urgent medical care"),
    (("calf swelling", "unilateral leg pain"), "Possible Deep Vein Thrombosis", "Seek urgent medical evaluation"),
    (("fever",), "Viral Infection (Flu)", "Rest, fluids, and qualified medical advice"),
    (("cough",), "Respiratory Infection", "Rest, fluids, and qualified medical advice"),
    (("headache", "nausea"), "Migraine", "Arrange clinical evaluation and appropriate treatment"),
    (("rash", "itching"), "Allergic Reaction", "Seek medical advice; emergency care for breathing difficulty"),
    (("vomiting",), "Gastroenteritis", "Hydration and clinical advice if persistent or severe"),
    (("burning urination",), "Possible Urinary Tract Infection", "Arrange clinical evaluation"),
    (("frequent urination",), "Possible Urinary Tract Infection", "Arrange clinical evaluation"),
    (("heartburn",), "Possible GERD", "Arrange clinical evaluation and dietary review"),
    (("acid reflux",), "Possible GERD", "Arrange clinical evaluation and dietary review"),
    (("dizziness",), "Possible Vertigo", "Avoid driving until assessed by a professional"),
    (("generalized hives",), "Acute Urticaria", "Seek medical advice; emergency care for breathing difficulty"),
    (("angioedema",), "Possible Severe Allergic Reaction", "Seek emergency medical care immediately"),
    (("persistent low mood", "anhedonia"), "Possible Depression", "Arrange a mental-health professional evaluation"),
    (("memory impairment", "confusion"), "Cognitive Decline Evaluation", "Arrange clinical evaluation"),
]


def collect_consultation():
    answer = input("Do you have any genetic disease? (Yes/No): ").strip().lower()
    while answer not in {"yes", "no"}:
        answer = input("Please answer Yes or No: ").strip().lower()
    genetic_disease = "None reported"
    if answer == "yes":
        genetic_disease = input("Please enter your genetic disease: ").strip() or "Not specified"

    symptoms = input("Enter your symptoms: ").strip().lower() or "not specified"
    disease, medicine = "General Malaise", "Rest, hydration, observation, and professional medical advice"
    for terms, candidate, recommendation in SYMPTOM_RULES:
        if all(term in symptoms for term in terms):
            disease, medicine = candidate, recommendation
            break
    else:
        for term, guidance in GENETIC_GUIDANCE.items():
            if term in genetic_disease.lower():
                disease, medicine = guidance
                break
    return {"genetic_disease": genetic_disease, "symptoms": symptoms, "disease": disease, "medicine": medicine}
