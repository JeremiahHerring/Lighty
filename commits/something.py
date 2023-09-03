cyber = input("Are you interested in cybersecurity (Y/N): ").lower()

if cyber != 'y' and cyber != 'n':
    print("Please enter a valid response")
    exit()
elif cyber == 'y':
    print("Congratulations, let's get started with your cybersecurity roadmap")
else:
    print("Okay, have a nice day!")
    exit()
