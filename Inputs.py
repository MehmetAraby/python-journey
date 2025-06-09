import os  # OS
import re  # Regex
import time  # Time

# Step 1: Get the API secret key from user
SecretKey = input('\033[94;1m🔑 Enter your API secret key → \033[0m')

# Step 2: Validate format (UUID)
if not re.match(r'^[a-fA-F0-9]{8}-([a-fA-F0-9]{4}-){3}[a-fA-F0-9]{12}$', SecretKey):
    print('\033[91;1m❌ Invalid API key format. Please enter a valid UUID.\033[0m')
    os._exit(0)

# Step 3: Get two-factor code from user
TwoFactor = input('\033[31;1;3m🔑 Enter your Two-Factor authentication key → \033[0m')

# Step 4: Verifying...
print("\n\033[92;1m🔓 Verifying Key...\033[0m")
time.sleep(1.5)

# Step 5: Sample users
users = [
    {
        'SecretKey': '84eee433-feff-46cb-a516-1b38f59d2aad',
        'TwoFactor': '100233',
        'DisplayNickname': 'Kadence Ailill'
    },
    {
        'SecretKey': '123e4567-e89b-12d3-a456-426614174000',
        'TwoFactor': '589665',
        'DisplayNickname': 'Abdul Hamid Hunfrid'
    }
]

found = False
for user in users:
    if user['SecretKey'] == SecretKey and user['TwoFactor'] == TwoFactor:
        print(f"\033[96;1m✅ Access Granted! Welcome {user['DisplayNickname']}, Agent 🎯\033[0m\n")
        found = True
        break

if not found:
    print("\033[91;1m❌ Access Denied! Please enter a valid license key.\033[0m")
