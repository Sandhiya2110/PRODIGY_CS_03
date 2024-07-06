import re

def password_strength_checker(password):
    strength_criteria = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'digits': False,
        'special_characters': False
    }
    
    if len(password) >= 8:
        strength_criteria['length'] = True
    if re.search(r'[A-Z]', password):
        strength_criteria['uppercase'] = True
    if re.search(r'[a-z]', password):
        strength_criteria['lowercase'] = True
    if re.search(r'[0-9]', password):
        strength_criteria['digits'] = True
    if re.search(r'[\W_]', password):
        strength_criteria['special_characters'] = True

    strength_score = sum(strength_criteria.values())
    strength_feedback = f"Password Strength: {strength_score}/5\n"

    if strength_score == 5:
        strength_feedback += "Your password is very strong."
    elif strength_score == 4:
        strength_feedback += "Your password is strong."
    elif strength_score == 3:
        strength_feedback += "Your password is good but could be stronger."
    elif strength_score == 2:
        strength_feedback += "Your password is weak."
    else:
        strength_feedback += "Your password is very weak."

    return strength_feedback, strength_criteria

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    feedback, criteria = password_strength_checker(password)
    print(feedback)
    print("Criteria Met:")
    for criterion, met in criteria.items():
        print(f"{criterion}: {'Yes' if met else 'No'}")
