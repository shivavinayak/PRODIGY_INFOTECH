import re 
def password_strength(password):
    


    length_score = len(password) >= 8
    uppercase_score = bool(re.search(r'[A-Z]', password))
    lowercase_score = bool(re.search(r'[a-z]', password))
    number_score = bool(re.search(r'[0-9]', password))
    special_character_score = bool(re.search(r'[!@#$%^&*()-_=+\|{};:/?.>]', password))

    total_score = length_score + uppercase_score + lowercase_score + number_score + special_character_score

    if total_score == 5:
        return "Strong Password"
    elif total_score >= 3:
        return "Good Password"
    else:
        return "Weak Password"
    
    
password = input("Enter your password: ")
strength = password_strength(password)
print(f"password strength: {strength}")