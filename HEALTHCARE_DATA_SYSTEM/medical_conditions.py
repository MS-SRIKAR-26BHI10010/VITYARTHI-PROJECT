
past_medical_conditions = input("DO YOU HAVE ANY PAST MEDICAL CONDITIONS (YES OR NO) :")

if past_medical_conditions in ("YES"):
    past_medical_conditions = input("PLEASE ENTER THE PAST CONDITION :")
else:
    past_medical_conditions = "N/A"