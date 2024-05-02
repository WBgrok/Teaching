# Here is some code to validate a user's password:

pw = input("Enter password: ")

# isalpha(), isupper(), islower() and isnumeric() are string methods ( you call them like str.method() )
# that return True if ALL characters of the string are alphabetical/uppercase/lowercase/numeric - respectively
if len(pw) < 8 or pw.isalpha() or pw.isupper() or pw.islower() or pw.isnumeric():
  print("Invalid password")
  print("Your password should be  8+ character, with mix of upper and lower case letters and numbers")

"""
Task:
 - Run the code, and verify it validates the string correctly.
 - Change the code to ask for the password until it passes validation
STRETCH
 - Change the code to ask for the password twice, performing the validation each time.
 - (if validation fails on the second pass, the code should ask for the first one again)
 - further stretch: Can you write this minimising code duplication? (using a subroutine)

"""