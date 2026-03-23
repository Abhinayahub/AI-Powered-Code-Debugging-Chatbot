def suggest_fix(error_message, language, user_code=""):
    error_message = error_message.lower()
    suggestions = []

    if "❌" in error_message:
        if language == "Python":
            if "expected an indented block" in error_message:
                suggestions.append("🛠 Make sure code blocks are properly indented.")
            if "syntaxerror" in error_message:
                suggestions.append("🛠 Check for missing colons or parentheses.")
            if "nameerror" in error_message:
                suggestions.append("🛠 Make sure all variables/functions are defined.")
            if "typeerror" in error_message:
                suggestions.append("🛠 Avoid mixing incompatible data types.")
            if "indexerror" in error_message:
                suggestions.append("🛠 You're accessing a list index that doesn't exist.")
            if "zerodivisionerror" in error_message:
                suggestions.append("🛠 You tried to divide by zero.")
            if "modulenotfounderror" in error_message:
                suggestions.append("🛠 Install the required module using pip.")
            if "attributeerror" in error_message:
                suggestions.append("🛠 You're trying to access an attribute that doesn't exist.")
            if "invalid literal for int()" in error_message:
                suggestions.append("🛠 Your input couldn't be converted to an integer.")

        elif language == "Java":
            if "incompatible types" in error_message:
                suggestions.append("🛠 You're assigning a value of the wrong type (e.g., assigning String to int).")
            if "cannot find symbol" in error_message:
                suggestions.append("🛠 Check if all variables, methods, or classes are properly declared and spelled correctly.")
            if "';' expected" in error_message:
                suggestions.append("🛠 You might be missing a semicolon at the end of a statement.")
            if "unexpected type" in error_message:
                suggestions.append("🛠 You probably used = instead of == for comparison.")
            if "class, interface, or enum expected" in error_message:
                suggestions.append("🛠 Make sure your code is wrapped inside a valid class.")
            if "illegal start of expression" in error_message:
                suggestions.append("🛠 You might be missing curly braces or misplacing statements.")

        elif language == "JavaScript":
            if "referenceerror" in error_message:
                suggestions.append("🛠 You're using a variable that hasn't been declared.")
            if "syntaxerror" in error_message:
                suggestions.append("🛠 Check for missing brackets, quotes, or other syntax issues.")
            if "typeerror" in error_message:
                suggestions.append("🛠 You're trying to access a property or method of undefined or null.")
            if "unexpected token" in error_message:
                suggestions.append("🛠 Check your code for typos, misplaced commas, or brackets.")
            if "is not defined" in error_message:
                suggestions.append("🛠 Declare all variables before using them.")

    else:
        # General suggestions
        if language == "Python":
            if "input(" in user_code:
                suggestions.append("🛠 Consider wrapping input() with try/except to handle invalid entries.")
            if "int(" in user_code:
                suggestions.append("🛠 Ensure user inputs are valid numbers before converting to int.")
            if "%" in user_code:
                suggestions.append("🛠 % gives remainder — useful for checking even/odd.")
            if "==" in user_code:
                suggestions.append("🛠 Use == for value comparison, not is.")
            if "print(" not in user_code:
                suggestions.append("ℹ Use print() to show output.")

        elif language == "Java":
            if "System.out.println" not in user_code:
                suggestions.append("ℹ Use System.out.println() to print output.")
            if "class" not in user_code:
                suggestions.append("ℹ Java code must be inside a class (e.g., public class Main).")

        elif language == "JavaScript":
            if "console.log" not in user_code:
                suggestions.append("ℹ Use console.log() to display output.")
            if "function" in user_code and "return" not in user_code:
                suggestions.append("ℹ Functions should return values or perform side effects.")

    if not suggestions:
        suggestions.append("✅ No suggestions. Your code looks good!")

    return suggestions
