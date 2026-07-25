# Password Strength Checker in Python

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    length_ok = len(password) >= 8
    
    score = sum([has_upper, has_lower, has_digit, length_ok])
    
    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Moderate"
    else: