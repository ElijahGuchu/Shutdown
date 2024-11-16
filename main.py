def shutdown():
    
    # Ask user for input
    user_input = input("Do you want to shut down? (yes/no): ").strip()

    # Check conditions based on input
    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("Abort shut down.")
    else:
        print("Sorry, invalid input.")

# Call the shutdown function to execute it
shutdown()