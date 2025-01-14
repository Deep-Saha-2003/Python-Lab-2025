# Q11. A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is  input  through  the  keyboard  in  hundreds, find the  total number  of  currency  notes  of  each denomination the cashier will have to give to the withdrawer. 

def calculate_notes(amount_in_hundreds):
    # Convert the input amount in hundreds to the actual amount in currency
    total_amount = amount_in_hundreds * 100
    
    # Calculate the number of 100 denomination notes
    notes_100 = total_amount // 100
    remaining_amount = total_amount % 100
    
    # Calculate the number of 50 denomination notes from the remaining amount
    notes_50 = remaining_amount // 50
    remaining_amount = remaining_amount % 50
    
    # Calculate the number of 10 denomination notes from the remaining amount
    notes_10 = remaining_amount // 10
    remaining_amount = remaining_amount % 10
    
    # Print the result (note that the remaining amount should be zero)
    print(f"100 denomination notes: {int(notes_100)}")
    print(f"50 denomination notes: {int(notes_50)}")
    print(f"10 denomination notes: {int(notes_10)}")

# Get the amount in hundreds from the user (it can be a whole number or float)
amount_in_hundreds = float(input("Enter the amount to withdraw in hundreds (e.g., 8.5 for 850): "))

# Call the function to calculate the notes
calculate_notes(amount_in_hundreds)