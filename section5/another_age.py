rajeev=float(input("Enter the age of Rajeev: "))
riya=float(input("Enter the age of Riya: "))
banni=float(input("Enter the age of Banni: "))
if rajeev>riya and rajeev>banni:
    print("Rajeev is oldest")
elif riya>rajeev and riya>banni:
    print("Riya is oldest")
elif banni>rajeev and banni>riya:
    print("Banni is oldest")