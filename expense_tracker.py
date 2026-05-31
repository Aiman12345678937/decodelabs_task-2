def expense_tracker():
    print("=== EXPENSE TRACKER STARTED ===")
    print("Enter expenses (type 'quit' to stop)\n")

    # STATE INITIALIZATION (The Memory)
    total = 0

    while True:
        user_input = input("Enter expense: ")

        # KILL SWITCH (Sentinel Value)
        if user_input.lower() == "quit":
            break

        # DEFENSIVE CODING (Type Safety)
        try:
            expense = int(user_input)
        except ValueError:
            print("Invalid Data! Please enter a number.")
            continue

        # ACCUMULATOR PATTERN (Core Logic)
        total += expense
        print(f"Added: {expense} | Current Total: {total}")

    # OUTPUT PHASE (Final State)
    print("\n=== SESSION CLOSED ===")
    print(f"FINAL TOTAL SPENT: {total}")


# RUN PROGRAM
expense_tracker()