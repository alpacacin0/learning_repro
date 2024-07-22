guitars = ["fender", "gibson", "ibanez", "jackson", "paul reed smith"]

print ("I started with these guitars:")
for guitar in guitars:
    print (f"a {guitar.title()}")

print (f"\nBut I sold the {guitars.pop().title()}")

print ("I now have:")
for guitar in guitars:
    print (f"a {guitar.title()}")

new_guitar = "eastman"

print (f"\nToday, I bought an {new_guitar.title()}")
print (f"\nNow I have these guitars:")

guitars.insert(len(guitars)//2, new_guitar)
for guitar in guitars:
    print (f"a {guitar.title()}")