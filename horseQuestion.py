"""
'Am I A Horse' Flowchart program
http://mentalfloss.com/sites/default/legacy/blogs/wp-content/uploads/2010/05/345horse.jpg
"""

HORSE_MSG = "You're not a horse"

is_horse = input("Are you a horse?\nYES or NO or MAYBE?").upper()
while is_horse == "YES" or is_horse == "NO" or is_horse == "MAYBE":
    if is_horse == "NO":
        print(HORSE_MSG)
    elif is_horse == "YES" or is_horse == "MAYBE":
        leg_amount = input("How many legs do you walk on?\nTWO or FOUR?").upper()
        if leg_amount == "TWO":
            print(HORSE_MSG)
        elif leg_amount == "FOUR":
            really_boolean = input("Really?\nYES or NO").upper()
            if really_boolean == "YES" or really_boolean == "NO":
                read_and_write = input("Can you read or write?\nYES or NO").upper()
                if read_and_write == "YES":
                    print(HORSE_MSG)
                elif read_and_write == "NO":
                    print("Liar; you're reading this...")
                    print(HORSE_MSG)
                else:
                    print("Invalid entry")
            else:
                print("Invalid entry")
        else:
            print("Invalid entry")
    else:
        print("Invalid entry")
