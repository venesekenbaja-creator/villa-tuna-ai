print("Welcome to Villa Tuna AI")
print("1. Rooms")
print("2. Prices")
print("3. Book Now")
print("")
choice = input("What do you want? Type 1, 2 or 3: ")

if choice == "1":
    print("We have: Deluxe Room, Family Room, Tuna View Room")
elif choice == "2":
    print("Prices start at P2,500 per night")
elif choice == "3":
    name = input("What is your name? ")
    print("Thank you", name, "! We will message you to confirm your booking.")
else:
    print("Please type 1, 2 or 3 only")
