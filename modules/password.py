from zxcvbn import zxcvbn
from getpass import getpass
import bcrypt

def check_strength(password):
    result = zxcvbn(password)  # returns an object with properties about the password
    score = result["score"]
    if score == 3:
        response = "Strong enough password: Score of 3"
    elif score == 4:
        response = "Very strong password: Score of 4"
    else:
        feedback = result.get("feedback")
        warning = feedback.get("warning")
        suggestions = feedback.get("suggestions")
        response = "Weak password: Score of " + str(score)  # convert score to string to concatenate
        if warning:                       # only add a warning line if there is one
            response += "\nWarning: " + warning
        response += "\nSuggestions:"
        # suggestions comes back as a list, so loop through it
        for suggestion in suggestions:
            response += " " + suggestion
    return response

def hash_pw(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)   # <-- was bcrypt.hash_pw (no underscore)
    return hashed

def verify_password(pw_attempt, hashed):
    # check if they match
    if bcrypt.checkpw(pw_attempt.encode(), hashed):
        return "Password is correct. Access granted!"
    else:
        return "Password incorrect. Access denied."

if __name__ == "__main__":
    while True:
        password1 = getpass("Enter a password to check strength: ")
        result_text = check_strength(password1)   # run the check once, reuse it
        print(result_text)
        if result_text.startswith("Weak"):
            print("Please choose a stronger password.")
        else:
            break
    hashed_password = hash_pw(password1)
    print("Hashed password: ", hashed_password)
    attempt = getpass("Re-enter password to verify: ")
    print(verify_password(attempt, hashed_password))