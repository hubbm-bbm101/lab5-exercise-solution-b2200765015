def email_controller(email):
    if "." in email and "@" in email:
        return "It is an email."
    else:
        return "It is not an email."

email1=input("Enter your email: ")
print(email_controller(email1))