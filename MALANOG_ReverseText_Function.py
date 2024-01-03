def main():
    user_input = input("Enter a string: ")
    
    # Check if input is a number or not
    
    # If input is a number:
    if user_input.isdigit() == True:
        print("Error reported! Enter text only.")

        # Loop back to main() [prompt for string input again]
        main()
    
    # If input is a string:
    else:
        
        # Reverse it
        print(f"Output: {reverse(user_input)}")
        
def reverse(user_input):

   reverse = ""

   for letter in user_input:
       
       reverse = letter + reverse

   return reverse

main()