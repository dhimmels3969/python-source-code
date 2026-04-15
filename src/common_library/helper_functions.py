

def get_positive_int_from_user(prompt):
    incomplete = True
    final_result = None
    while incomplete:
        user_number = input(prompt)
        try:
            user_number = int(user_number)
            if user_number > 0:
                incomplete = False
                final_result = user_number
            else:
                print("Number must be greater than 0. Please try again.")

        except ValueError:
            print("Previous value was invalid. Enter a number.")
    return final_result