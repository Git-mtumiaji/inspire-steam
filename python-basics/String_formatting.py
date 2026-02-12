# Name : Ronnie Muturi
# Date : 12/02/2026
# Sting formatting

# Get string Length
sentence = "I watch anime"

sting_length = len(sentence)

print(f"The length is: {sting_length}")

# splitting a string
sentence_2 = "Mathematics Physics"
split = sentence_2.split(" ")

print(f"the first subject is: ", split[0])

# Make everything CAPS
mpesa_code = "ub12ddsgrt"

capitalized = mpesa_code.upper()

print("New mpesa code: ", capitalized)

#Make everything lower
mpesa_code1 = "UB12DDSGRT"

minimized = mpesa_code1.lower()
print("New mpesa code: ", minimized)

# Replacing charaters in a string

balance = "100Kes"
amount_added = "50Kes"

cleaned_balance = balance.replace("Kes", "")

print("cleaned balance: ", cleaned_balance)

cleaned_amount_added = amount_added.replace("Kes", "")

print("cleaned amount added: ", cleaned_amount_added)

sum_balance = int(cleaned_balance) + int(cleaned_amount_added)
print(f"The new balance is: {sum_balance}Kes")


original_amount = "12Kes"

mpesa_message="CONFIRMED you have received 40Kes from Phillip Mugambi."
split = mpesa_message.split(" ")
received = split[4]

print(f"{mpesa_message}" , received)
print(" " , received)

received_cash =received.replace("Kes", "")
cleaned_balance1 = original_amount.replace("Kes", "")
sum_balance1 = int(cleaned_balance1) + int(received_cash) # converting types > Type casting
print(f"{mpesa_message}Your New account balance is {sum_balance1}Kes")