# Name : Ronnie Muturi
# Date : 12/02/2026
# Assignment

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