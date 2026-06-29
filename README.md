# Task-Password-Generator

# 🔐 Task-Password-Generator (Python Tkinter)

A robust and feature-rich *Graphical User Interface (GUI)* Password Generator built with Python's native *Tkinter* library and the standard string and random modules. 

This application allows users to generate customizable, highly secure, and random passwords dynamically based on their preferences.

---

## ✨ Features

- *Custom Length Control:* Users can specify the exact length of the password they want to generate.
- *Advanced Customization Checkboxes:*
  - Include Lowercase letters (a-z)
  - Include Uppercase letters (A-Z)
  - Include Numbers (0-9)
  - Include Symbols/Special Characters (!@#$...)
- *Smart Validation & Error Handling:* - Prevents crashes by validating integer inputs for length.
  - Alerts the user via an explicit error box if no character types are selected or if invalid inputs are entered.
- *Secure Output Field:* The generated password is shown in a custom readonly entry state so users cannot accidentally delete or alter characters while copying.

---

## 🛠️ Code Architecture & Logic Explanation

The logic of this application is divided into robust user input scanning and real-time generation:

### 1. Functional Logic (generate_password())
- *Input Gathering:* Reads the desired character count dynamically from the user entry field.
- *Character Pool Construction:* Uses boolean variables attached to the Tkinter checkboxes. If checked, it appends the respective character set using constants like string.ascii_lowercase, string.digits, etc.
- *Randomization Processing:* It utilizes a secure random.choice() iterator grouped inside a comprehension loop running exactly length times to compile the final stream.
- *State Swapping:* Temporarily shifts the output state to normal to clear the field and insert the new password, then immediatelylocks it back to readonly.

