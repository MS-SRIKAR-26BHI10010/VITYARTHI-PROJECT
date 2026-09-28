payment_method = input("ENTER THE PAYMENT METHOD (CASH/CARD/INSURANCE) :")

if payment_method in ("CASH", "CARD", "INSURANCE"):
    print("Valid input")
else:
    print("Invalid payment method selected")
    