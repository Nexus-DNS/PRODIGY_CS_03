def check_password_strength(password):
  """
  This function checks the strength of a password based on various criteria.

  Args:
      password: The password string to be evaluated.

  Returns:
      A string indicating the strength of the password and feedback for improvement.
  """

  # Define minimum length requirement
  min_length = 8

  # Check for character types using string methods
  has_uppercase = any(char.isupper() for char in password)
  has_lowercase = any(char.islower() for char in password)
  has_number = any(char.isdigit() for char in password)
  has_special_char = any(char in "!@#$%^&*()_+-=[]{};':\",./<>?|\\" for char in password)

  # Calculate score based on criteria met
  score = 0
  if len(password) >= min_length:
    score += 2
  if has_uppercase:
    score += 1
  if has_lowercase:
    score += 1
  if has_number:
    score += 1
  if has_special_char:
    score += 1

  # Ensure score stays within valid range (0-5)
  score = min(max(score, 0), 5)

  # Provide feedback based on the adjusted score
  feedback = {
    0: "Very Weak! This password can be cracked easily. Please consider using at least "
       f"{min_length} characters, including uppercase letters, lowercase letters, numbers, "
       "and special characters.",
    1: "Very Weak! This password can be cracked easily. Please consider using at least "
       f"{min_length} characters, including uppercase letters, lowercase letters, numbers, "
       "and special characters.",
    2: "Weak. Consider adding more variety to your password. Use a mix of uppercase, "
       "lowercase letters, numbers, and special characters.",
    3: "Moderate. This password is getting stronger. Aim for at least "
       f"{min_length} characters with a mix of character types.",
    4: "Strong! This is a good password.",
    5: "Strong! This is a very strong password."
  }

  return feedback.get(score)

# Get user input
password = input("Enter your password: ")

# Check password strength and provide feedback
strength_feedback = check_password_strength(password)
print(strength_feedback)
