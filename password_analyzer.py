import re
import random
import string

def analyze_password(password):
    """
    Evaluates the strength of a user-entered password based on length, 
    complexity (uppercase, lowercase, numbers, special chars), and uniqueness.
    """
    score = 0
    feedback = []

    # 1. Check Length
    length = len(password)
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password is too short (Minimum 8 characters recommended, 12+ is ideal).")

    # 2. Check Complexity
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numerical digits (0-9).")

    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (e.g., !, @, #, $).")

    # 3. Check Uniqueness (Basic entropy / variety of characters used)
    unique_chars = len(set(password))
    if length > 0 and (unique_chars / length) < 0.5:
        feedback.append("Password has too many repeating characters. Increase variety.")
        score = max(0, score - 1) # Penalize slightly for lack of uniqueness

    # Determine Rating
    if score >= 5:
        rating = "STRONG 💪"
    elif score >= 3:
        rating = "MEDIUM ⚠️"
    else:
        rating = "WEAK ❌"

    return rating, score, feedback


def generate_alternatives(password):
    """
    Suggests stronger variations of the entered password.
    """
    suggestions = []
    
    # Alternative 1: Appending a strong suffix
    special_suffix = "".join(random.choices(string.punctuation, k=2))
    num_suffix = "".join(random.choices(string.digits, k=2))
    suggestions.append(f"{password.capitalize()}{num_suffix}{special_suffix}")
    
    # Alternative 2: A completely random strong passphrase fallback
    words = ["Cyber", "Secure", "Shield", "Vault", "Matrix", "Quantum", "Fortress"]
    random_word = random.choice(words)
    random_nums = "".join(random.choices(string.digits, k=3))
    random_spec = random.choice(string.punctuation)
    suggestions.append(f"{random_word}{random_nums}{random_spec}")

    return suggestions


def main():
    print("=" * 45)
    print("      🔒 PASSWORD STRENGTH ANALYZER 🔒      ")
    print("=" * 45)
    
    # Simulating a database to prevent reuse of old passwords (Optional Feature)
    simulated_db = ["Password123!", "Admin@2025", "Welcome#1"]
    
    user_password = input("Enter a password to test: ").strip()
    
    if not user_password:
        print("Password cannot be empty!")
        return

    # Check against database (Optional feature implementation)
    if user_password in simulated_db:
        print("\n[ALERT] This password has been used previously. Please choose a completely unique password!")
        rating, score, feedback = "REUSED / UNSAFE ❌", 0, ["Do not reuse old passwords."]
    else:
        rating, score, feedback = analyze_password(user_password)

    # Display Results
    print(f"\nResults for: {user_password}")
    print(f"Overall Strength: {rating} (Score: {score}/6)")
    
    if feedback:
        print("\nSuggestions to Improve:")
        for tip in feedback:
            print(f" - {tip}")
            
    # Provide stronger alternatives
    print("\nStronger Alternatives for You:")
    alternatives = generate_alternatives(user_password)
    for alt in alternatives:
        print(f" 👉 {alt}")
    print("=" * 45)

if __name__ == "__main__":
    main()
      
