genetic_disease = input("Do you have any genetic disease ? (Yes/No):")

if genetic_disease == "Yes":
    genetic_disease = input("Please Enter your genetic disease :")
else:
    genetic_disease = "None"

if "diabetes" in genetic_disease:
    disease = "Diabetes Mellitus Management"
    medicine = "Insulin therapy review and blood sugar monitoring kit"
    
elif "sickle cell" in genetic_disease:
    disease = "Sickle Cell Anemia"
    medicine = "Folic acid, pain management plan, and Hematology Referral"
    
elif "cystic fibrosis" in genetic_disease:
    disease = "Cystic Fibrosis"
    medicine = "Pancreatic enzyme supplements and Pulmonology Referral"

symptoms = input("Enter your symptoms (e.g., fever, cough, headache): ")

if "fever" in symptoms or "cough" in symptoms:
    disease = "Viral Infection (Flu)"
    medicine = "Paracetamol 500mg and Cough Syrup"

elif "wheezing" in symptoms or "shortness of breath" in symptoms:
    disease = "Asthma Exacerbation / Bronchospasm"
    medicine = "Bronchodilator (Salbutamol) and Oxygen Therapy"

elif "headache" in symptoms and "nausea" in symptoms:
    disease = "Migraine"
    medicine = "Ibuprofen 400mg and Anti-nausea medication"

elif "rash" in symptoms and "itching" in symptoms:
    disease = "Allergic Reaction"
    medicine = "Antihistamine (Cetirizine 10mg)"

elif "stomach ache" in symptoms or "vomiting" in symptoms:
    disease = "Gastroenteritis (Food Poisoning)"
    medicine = "Oral Rehydration Salts (ORS) and anti-emetics"

elif "chest pain" in symptoms:
    disease = "Possible Cardiovascular Risk"
    medicine = "Aspirin (Seek immediate hospital care)"

elif "sore throat" in symptoms and "fever" in symptoms:
    disease = "Pharyngitis / Tonsillitis"
    medicine = "Amoxicillin (if bacterial) or Paracetamol with warm saline gargles"

elif "runny nose" in symptoms or "sneezing" in symptoms:
    disease = "Allergic Rhinitis / Common Cold"
    medicine = "Antihistamine (Cetirizine 10mg) and Saline nasal spray"

elif "burning urination" in symptoms or "frequent urination" in symptoms:
    disease = "Urinary Tract Infection (UTI)"
    medicine = "Nitrofurantoin or Fosfomycin, and increased fluid intake"

elif "joint pain" in symptoms and "swelling" in symptoms:
    disease = "Arthritis / Synovitis"
    medicine = "Naproxen and topical NSAID gel"

elif "heartburn" in symptoms or "acid reflux" in symptoms:
    disease = "Gastroesophageal Reflux Disease (GERD)"
    medicine = "Proton Pump Inhibitor (Omeprazole 20mg) and Antacids"

elif "dizziness" in symptoms or "spinning sensation" in symptoms:
    disease = "Vertigo / Vestibular Neuritis"
    medicine = "Betahistine or Meclizine"

elif "dry cough" in symptoms and "throat irritation" in symptoms:
    disease = "Upper Respiratory Tract Infection (URTI)"
    medicine = "Dextromethorphan cough syrup and warm hydration"

elif "productive cough" in symptoms or "phlegm" in symptoms:
    disease = "Bronchitis"
    medicine = "Guaifenesin (Expectorant) and steam inhalation"

elif "high fever" in symptoms and "chills" in symptoms:
    disease = "Acute Febrile Illness / Malaria Evaluation"
    medicine = "Paracetamol 650mg and urgent diagnostic blood smear/NS1 antigen test"

elif "watery diarrhea" in symptoms and "cramps" in symptoms:
    disease = "Acute Watery Diarrhea / Viral Enteritis"
    medicine = "Oral Rehydration Salts (ORS) and Zinc supplementation"

elif "constipation" in symptoms or "hard stools" in symptoms:
    disease = "Functional Constipation"
    medicine = "Polyethylene Glycol (Laxative) and high dietary fiber"

elif "red eyes" in symptoms or "eye discharge" in symptoms:
    disease = "Conjunctivitis"
    medicine = "Antibacterial eye drops (Moxifloxacin) or Lubricant tear drops"

elif "ear pain" in symptoms or "ear discharge" in symptoms:
    disease = "Otitis Media / Otitis Externa"
    medicine = "Analgesic ear drops and Amoxicillin-Clavulanate if bacterial"

elif "back pain" in symptoms or "lumbar stiffness" in symptoms:
    disease = "Lumbar Muscle Strain / Spondylosis"
    medicine = "Muscle relaxant (Thiocolchicoside) and Paracetamol"

elif "muscle ache" in symptoms and "fatigue" in symptoms:
    disease = "Viral Myalgia / Influenza"
    medicine = "Paracetamol, rest, and oral fluids"

elif "mouth ulcers" in symptoms or "painful sores in mouth" in symptoms:
    disease = "Aphthous Stomatitis"
    medicine = "Triamcinolone acetonide buccal paste and Vitamin B-complex"

elif "itchy scalp" in symptoms or "flaking" in symptoms:
    disease = "Seborrheic Dermatitis / Dandruff"
    medicine = "Ketoconazole 2 percent shampoo"

elif "blurry vision" in symptoms and "excessive thirst" in symptoms:
    disease = "Hyperglycemia / Suspected Diabetes Mellitus"
    medicine = "Blood glucose screening and physician consultation (Insulin / Metformin evaluation)"

elif "sudden weakness" in symptoms or "facial drooping" in symptoms:
    disease = "Acute Ischemic Stroke / Neurological Deficit"
    medicine = "Emergency hospital evaluation immediately (CT brain protocol)"

elif "tremors" in symptoms and "heat intolerance" in symptoms:
    disease = "Hyperthyroidism"
    medicine = "Thyroid profile evaluation (Anti-thyroid medication under endocrinologist)"

elif "cold intolerance" in symptoms and "weight gain" in symptoms:
    disease = "Hypothyroidism"
    medicine = "Levothyroxine (guided by TSH levels)"

elif "swollen lymph nodes" in symptoms and "night sweats" in symptoms:
    disease = "Lymphadenitis / Systemic Infection"
    medicine = "Clinical evaluation, CBC, and targeted broad-spectrum antibiotic if bacterial"

elif "severe unilateral flank pain" in symptoms or "blood in urine" in symptoms:
    disease = "Nephrolithiasis (Kidney Stones)"
    medicine = "Intense analgesia (Ketorolac / Tramadol) and urgent Ultrasound KUB"

elif "intermittent wheezing" in symptoms and "prolonged cough" in symptoms:
    disease = "Chronic Obstructive Pulmonary Disease (COPD)"
    medicine = "Ipratropium Bromide inhaler and Tiotropium"

elif "pale skin" in symptoms and "generalized weakness" in symptoms:
    disease = "Iron Deficiency Anemia"
    medicine = "Ferrous Ascorbate and elemental Iron supplements"

elif "dry scaly patches" in symptoms or "skin peeling" in symptoms:
    disease = "Eczema / Atopic Dermatitis"
    medicine = "Emollient barrier cream and topical Hydrocortisone"

elif "silvery scales" in symptoms and "extensor plaque" in symptoms:
    disease = "Psoriasis"
    medicine = "Topical Calcipotriol and Clobetasol propionate"

elif "facial bone pain" in symptoms and "nasal congestion" in symptoms:
    disease = "Acute Rhinosinusitis"
    medicine = "Nasal decongestant (Oxymetazoline for max 3 days) and steam inhalation"

elif "burning epigastric pain" in symptoms and "black tarry stools" in symptoms:
    disease = "Peptic Ulcer Disease / Upper GI Bleed"
    medicine = "Intravenous Pantoprazole and urgent endoscopy"

elif "painful swallowing" in symptoms or "lump feeling in throat" in symptoms:
    disease = "Esophagitis / Globus Pharyngeus"
    medicine = "Pantoprazole 40mg and sucralfate oral suspension"

elif "ring-shaped itchy rash" in symptoms:
    disease = "Tinea Corporis (Fungal Infection)"
    medicine = "Topical Clotrimazole or Terbinafine cream"

elif "sudden palpitations" in symptoms and "anxiety" in symptoms:
    disease = "Panic Attack / Supraventricular Tachycardia"
    medicine = "Vagal maneuvers, ECG evaluation, and Propranolol/Lorazepam under guidance"

elif "calf swelling" in symptoms and "unilateral leg pain" in symptoms:
    disease = "Deep Vein Thrombosis (DVT)"
    medicine = "Low Molecular Weight Heparin (Immediate vascular ultrasound)"

elif "itching around anus" in symptoms and "nocturnal restlessness" in symptoms:
    disease = "Enterobiasis (Pinworm Infestation)"
    medicine = "Mebendazole or Albendazole 400mg single dose"

elif "excessive gas" in symptoms or "abdominal bloating" in symptoms:
    disease = "Functional Dyspepsia / Aerophagia"
    medicine = "Simethicone and Alpha-galactosidase enzyme"

elif "painful fluid-filled blisters" in symptoms and "dermatomal rash" in symptoms:
    disease = "Herpes Zoster (Shingles)"
    medicine = "Valacyclovir 1000mg and Pregabalin for neuropathic pain"

elif "generalized hives" in symptoms or "angioedema" in symptoms:
    disease = "Acute Urticaria"
    medicine = "Fexofenadine 180mg and oral Prednisolone if severe"

elif "persistent low mood" in symptoms and "anhedonia" in symptoms:
    disease = "Major Depressive Disorder"
    medicine = "Psychiatric evaluation and SSRI (e.g., Escitalopram 10mg)"

elif "memory impairment" in symptoms and "confusion" in symptoms:
    disease = "Cognitive Decline / Dementia evaluation"
    medicine = "Cholinesterase inhibitors (Donepezil) and formal neurocognitive workup"

elif "severe throbbing facial pain" in symptoms or "jaw pain" in symptoms:
    disease = "Trigeminal Neuralgia / Odontogenic Abscess"
    medicine = "Carbamazepine (if neuralgic) or Dental drainage and antibiotic"

else:
    disease = "General Malaise"
    medicine = "Rest, hydration, and standard observation"
