
genetic_disease = input("DO YOU HAVE ANY GENETIC DISEASE ? (YES/NO): ")

if genetic_disease in ["YES", "Y"]:
    genetic_disease = input("PLEASE ENTER THE GENETIC DISEASE : ")
else:
    genetic_disease = "N/A"

symptoms = input("ENTER THE SYMPTOMS : ")

if "chest pain" in symptoms:
    disease = "Possible Cardiovascular Risk"
    medicine = "Aspirin (Must visit a doctor)"

elif "sudden weakness" in symptoms or "facial drooping" in symptoms or "slurred speech" in symptoms:
    disease = "Acute Ischemic Stroke / Neurological Deficit"
    medicine = "Emergency hospital evaluation (Brain CT Scan neccessary)"

elif "stiff neck" in symptoms and "photophobia" in symptoms:
    disease = "Suspected Acute Meningitis"
    medicine = "Emergency hospital transfer "

elif "burning epigastric pain" in symptoms and "black tarry stools" in symptoms:
    disease = "Peptic Ulcer Disease / Upper GI Bleed"
    medicine = "Intravenous Pantoprazole and urgent endoscopy required"

elif "calf swelling" in symptoms and "unilateral leg pain" in symptoms:
    disease = "Deep Vein Thrombosis "
    medicine = "Low Molecular Weight Heparin (Vascular Ultrasound required)"

elif "itchy blisters" in symptoms or "fluid filled spots" in symptoms or "chickenpox" in symptoms:
    disease = "Chickenpox "
    medicine = "Calamine lotion, Paracetamol, and strict isolation(DO NOT TAKE ASPRIRIN AS A MEDICATION)"

elif "step ladder fever" in symptoms or ("fever" in symptoms and "stomach pain" in symptoms and "headache" in symptoms):
    disease = "Typhoid Fever "
    medicine = "Widal test,Azithromycin (or) Cefixime, and ORS hydration"

elif "pain behind eyes" in symptoms or ("high fever" in symptoms and "severe joint pain" in symptoms and "vomiting" in symptoms):
    disease = "Dengue Fever"
    medicine = "Complete Blood Profile (CBP), Paracetamol, and vigorous oral hydration"

elif "severe joint pain" in symptoms and "swelling" in symptoms and "rash" in symptoms:
    disease = "Chikungunya Viral Fever"
    medicine = "Paracetamol, cold compresses, hydration, and gentle joint mobilization"

elif "shivering" in symptoms or ("high fever" in symptoms and "chills" in symptoms and "sweating" in symptoms):
    disease = "Malaria"
    medicine = "Rapid diagnostic test, Artemisinin combination therapy (ACT)"

elif "yellow skin" in symptoms or "yellow eyes" in symptoms or "dark urine" in symptoms:
    disease = "Jaundice /Hepatitis(Acute)"
    medicine = "Liver Function Tests (LFT), viral hepatitis markers, bed rest, and low-fat diet"

elif "severe right lower stomach pain" in symptoms or "right lower quadrant pain" in symptoms:
    disease = "Appendicitis"
    medicine = "immediate surgical consultation required"

elif "wheezing" in symptoms or "shortness of breath" in symptoms:
    disease = "Asthma Exacerbation / Bronchospasm"
    medicine = " Use of Bronchodilator and Oxygen Therapy"

elif "fever" in symptoms and "cough" in symptoms and "chest pain" in symptoms:
    disease = "Pneumonia"
    medicine = "Chest X-ray, Sputum culture, and Amoxicillin-Clavulanate"

elif "fever" in symptoms and "cough" in symptoms:
    disease = "Viral Infection (Flu / Influenza)"
    medicine = "Paracetamol 500mg, Cough Syrup, and adequate rest"

elif "sore throat" in symptoms and "fever" in symptoms:
    disease = "Pharyngitis / Acute Tonsillitis"
    medicine = "Warm saline gargles, Paracetamol, and Amoxicillin if bacterial"

elif "runny nose" in symptoms or "sneezing" in symptoms:
    disease = "Allergic Rhinitis / Common Cold"
    medicine = "Antihistamine (Cetirizine 10mg) and Saline nasal spray"

elif "productive cough" in symptoms or "phlegm" in symptoms:
    disease = "Acute Bronchitis"
    medicine = "Guaifenesin and steam inhalation"

elif "dry cough" in symptoms and "throat irritation" in symptoms:
    disease = "Upper Respiratory Tract Infection (URTI)"
    medicine = "Dextromethorphan cough syrup and warm hydration"

elif "facial bone pain" in symptoms or "sinus pressure" in symptoms:
    disease = "Acute Sinusitis"
    medicine = "Steam inhalation, saline nasal rinse, and Usage of Oxymetazoline nasal drops (max 3 days)"

elif "intermittent wheezing" in symptoms and "prolonged cough" in symptoms:
    disease = "Chronic Obstructive Pulmonary Disease (COPD)"
    medicine = "Ipratropium Bromide inhaler and Tiotropium"

elif "stomach ache" in symptoms or "vomiting" in symptoms:
    disease = "Gastroenteritis (Food Poisoning)"
    medicine = "Intake of ORS and Ondansetron "

elif "watery diarrhea" in symptoms and "cramps" in symptoms:
    disease = "Acute Watery Diarrhea / Viral Enteritis"
    medicine = "Oral Rehydration Salts (ORS) and Intake of Zinc supplements"

elif "bloody diarrhea" in symptoms or "blood in stool" in symptoms:
    disease = "Dysentery (Amoebic / Bacillary)"
    medicine = "Stool routine examination, Metronidazole or Ciprofloxacin, and hydration"

elif "heartburn" in symptoms or "acid reflux" in symptoms:
    disease = "Gastroesophageal Reflux Disease (GERD)"
    medicine = "Proton Pump Inhibitor (Omeprazole 20mg) and Antacids"

elif "excessive gas" in symptoms or "abdominal bloating" in symptoms:
    disease = "Indigestion"
    medicine = "Simethicone and Alpha-galactosidase enzyme"

elif "constipation" in symptoms or "hard stools" in symptoms:
    disease = "Functional Constipation"
    medicine = "Polyethylene Glycol (Laxative) and Must include high dietary fiber in diet"

elif "painful swallowing" in symptoms or "lump feeling in throat" in symptoms:
    disease = "Esophagitis / Globus Pharyngeus"
    medicine = "Pantoprazole 40mg and Sucralfate oral suspension"

elif "burning urination" in symptoms or "frequent urination" in symptoms:
    disease = "Urinary Tract Infection (UTI)"
    medicine = "Nitrofurantoin or Fosfomycin, and plenty of fluids"

elif "severe unilateral flank pain" in symptoms or "blood in urine" in symptoms:
    disease = "Nephrolithiasis (Kidney Stones)"
    medicine = "Intense analgesia (Ketorolac / Tramadol) and urgent Ultrasound Of Kidney"

elif "headache" in symptoms and "nausea" in symptoms:
    disease = "Migraine"
    medicine = "Ibuprofen 400mg and Anti-nausea medication"

elif "dizziness" in symptoms or "spinning sensation" in symptoms:
    disease = "Vertigo / Vestibular Neuritis"
    medicine = "Betahistine or Meclizine"

elif "sudden palpitations" in symptoms and "anxiety" in symptoms:
    disease = "Panic Attack / Supraventricular Tachycardia"
    medicine = "Vagal maneuvers, ECG evaluation, and clinical observation"

elif "persistent low mood" in symptoms and "anhedonia" in symptoms:
    disease = "Major Depressive Disorder"
    medicine = "Psychiatric evaluation and supportive counseling"

elif "memory impairment" in symptoms and "confusion" in symptoms:
    disease = "Cognitive Decline / Neurological Workup"
    medicine = "Formal neurocognitive workup and brain imaging(MRI)"

elif "severe throbbing facial pain" in symptoms or "jaw pain" in symptoms:
    disease = "Trigeminal Neuralgia / Odontogenic Infection"
    medicine = "Carbamazepine (if neuralgic) or  Must take a Dental consultation if Symptoms still persists"

elif "joint pain" in symptoms and "swelling" in symptoms:
    disease = "Arthritis / Synovitis"
    medicine = "Naproxen and topical NSAID gel"

elif "back pain" in symptoms or "lumbar stiffness" in symptoms:
    disease = "Lumbar Muscle Strain / Spondylosis"
    medicine = "Muscle relaxant (Thiocolchicoside) and Paracetamol"

elif "muscle ache" in symptoms and "fatigue" in symptoms:
    disease = "Viral Myalgia / Generalized Body Ache"
    medicine = "Paracetamol, rest, and intake of oral fluids"

elif "generalized hives" in symptoms or "angioedema" in symptoms:
    disease = "Acute Urticaria (Severe Allergy)"
    medicine = "Fexofenadine 180mg and oral Prednisolone if severe"

elif "rash" in symptoms and "itching" in symptoms:
    disease = "Allergic Reaction / Contact Dermatitis"
    medicine = "Antihistamine (Cetirizine 10mg) and Calamine lotion"

elif "ring-shaped itchy rash" in symptoms:
    disease = "Tinea Corporis (Fungal Infection / Ringworm)"
    medicine = "Topical Clotrimazole or Terbinafine cream"

elif "dry scaly patches" in symptoms or "skin peeling" in symptoms:
    disease = "Eczema / Atopic Dermatitis"
    medicine = "Emollient barrier cream and topical Hydrocortisone"

elif "silvery scales" in symptoms and "extensor plaque" in symptoms:
    disease = "Psoriasis"
    medicine = "Topical Calcipotriol and Clobetasol propionate"

elif "itchy scalp" in symptoms or "flaking" in symptoms:
    disease = "Seborrheic Dermatitis / Dandruff"
    medicine = "Ketoconazole 2% Shampoo"

elif "mouth ulcers" in symptoms or "painful sores in mouth" in symptoms:
    disease = "Aphthous Stomatitis (Canker Sores)"
    medicine = "Triamcinolone acetonide buccal paste and  Intake of Vitamin B-complex Tablets (Can take everyday)"

elif "red eyes" in symptoms or "eye discharge" in symptoms:
    disease = "Conjunctivitis (Pink Eye)"
    medicine = "Antibacterial eye drops (Moxifloxacin) or Lubricant tear drops"

elif "ear pain" in symptoms or "ear discharge" in symptoms:
    disease = "Otitis Media / Otitis Externa (Ear Infection)"
    medicine = "Analgesic ear drops and Amoxicillin-Clavulanate if bacterial"

elif "blurry vision" in symptoms and "excessive thirst" in symptoms:
    disease = "Hyperglycemia / Suspected Diabetes Mellitus"
    medicine = "Blood glucose screening and physician consultation"

elif "hot dry skin" in symptoms or "high body temperature after sun" in symptoms:
    disease = "Heat Stroke / Heat Exhaustion"
    medicine = "Immediate cold water cooling, ice packs, oral hydration, or emergency IV fluids or May even need to be admitted to Hospital"

elif "pale skin" in symptoms and "generalized weakness" in symptoms:
    disease = "Iron Deficiency Anemia"
    medicine = "Ferrous Ascorbate and elemental Iron supplements"

elif "fever" in symptoms or "high temperature" in symptoms or "hot" in symptoms:
    disease = "Pyrexia / Mild Febrile Illness"
    medicine = "Paracetamol 650mg SOS, temperature chart tracking, and oral fluids"

elif "cough" in symptoms:
    disease = "Acute Cough / Bronchial Irritation"
    medicine = "Cough lozenges, warm steam inhalation, and hydration"

elif "headache" in symptoms:
    disease = "Tension Headache"
    medicine = "Paracetamol 500mg, adequate rest, hydration"

elif "pain" in symptoms or "ache" in symptoms:
    disease = "Non-Specific Musculoskeletal Pain"
    medicine = "Oral Paracetamol, warm compress, and proper rest"

else:
    disease = "General Malaise"
    medicine = "Proper Rest, hydration, and standard observation"