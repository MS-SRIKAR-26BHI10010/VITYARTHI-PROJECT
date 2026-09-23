"""Patient input collection and validation."""


def _prompt_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Please enter a value.")


def _prompt_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value > 0:
                return value
        except ValueError:
            pass
        print("Please enter a positive whole number.")


def collect_patient_details():
    return {
        "name": _prompt_non_empty("Enter your name: "),
        "age": _prompt_positive_int("Enter your age: "),
        "date_of_birth": _prompt_non_empty("Enter your date of birth: "),
        "height": _prompt_non_empty("Enter your height: "),
        "weight": _prompt_positive_int("Enter your weight in kg: "),
    }
