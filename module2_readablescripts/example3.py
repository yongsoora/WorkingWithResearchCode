# Check if password is strong enough

# length is over 8
# has number
# has special digit


def is_password_strong(password):

    if type(password) == str:
        if len(password) > 8:
            if contains_both_letters_and_numbers(password):
                if has_special_character(password):
                    return True
                else:
                    return False
            else:
                    return False
        else:
                return False
    else:
        return "password variable is not a string"
