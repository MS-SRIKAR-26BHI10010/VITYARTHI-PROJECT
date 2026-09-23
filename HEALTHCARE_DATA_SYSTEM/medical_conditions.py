"""Past medical history input and validation."""


def collect_medical_conditions():
    answer = input("Do you have any past medical conditions? (Yes/No): ").strip().lower()
    while answer not in {"yes", "no"}:
        answer = input("Please answer Yes or No: ").strip().lower()

    past_conditions = "None reported"
    if answer == "yes":
        past_conditions = input("Enter your medical conditions: ").strip() or "Not specified"

    return {"has_conditions": answer == "yes", "past_conditions": past_conditions}
