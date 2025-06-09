import os;

try :
    while True :
        A = float(input("💡 What's the first number you'd like to work with?\n → "))
        os.system("cls");

        B = float(input("🔢 Great! Now, what's the second number?\n → "))
        os.system("cls");

        C = int(input("🚀 Ready to crunch some numbers? Pick your operation:\n\n[1] Add ➕\n[2] Subtract ➖\n[3] Multiply ✖️\n[4] Divide ➗\n → "))
        os.system("cls");

        if C == 1:
            result = A + B
        elif C == 2:
            result = A - B
        elif C == 3:
            result = A * B
        elif C == 4:
            result = A / B
        else:
            print('Invalid operation selected!');
            continue;

        print(f"🧮 Your result is → {result}\n");

        D = int(input("🔄 Would you like to continue?\n\n[1] Yes, let's go again! 💪\n[2] No, I'm done for now. 🛑\n → "))

        if D != 1:
            os._exit(0);
        elif D == 1 :
            os.system("cls");
except ValueError :
    print('Invalid input! Please enter numbers and select a valid operation.')