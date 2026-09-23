"""Payment method input and validation."""

VALID_PAYMENT_METHODS = {"cash", "card", "insurance"}


def collect_payment_method():
    while True:
        payment = input("Enter your payment method (Cash, Card, Insurance): ").strip().lower()
        if payment in VALID_PAYMENT_METHODS:
            return payment
        print("Please choose Cash, Card, or Insurance.")
