def check_eligibility():
    try:
        # Vecums
        age = int(input("Ievadi savu vecumu: "))

        if age < 0:
            print("Ievadi vecumu virs 0.")
            return

        # Balsošana
        if age >= 18:
            print("- Drīkst balsot.")
        else:
            print("- Nedrīkst balsot.")
            

        # Autovadītāja apliecība
        if age >= 18:
            print("- Atļauts iegūt autovadītāja apliecību.")
        else:
            print("- Pārāk jauns, lai iegūtu autovadītāja apliecību.")
        
   # Auto īre
        if age >= 21:
            print("- Atļauts īrēt automašīnu.")
        else:
            print("- Pārāk jauns, lai īrētu automašīnu.")
             # Studenta atlaide
        if (16 <= age <= 26):
            print("- Ir studenta atlaide.")
                # Saņemt senioru atlaidi
        if age >= 65:
            print("- Var saņemt senioru atlaidi.")
        

    except ValueError:
        print("Kļuda! Lūdzu ievadi vecumu ciparos!")

# Run the function
check_eligibility()
