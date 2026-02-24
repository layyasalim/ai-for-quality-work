My definition of good code is:

- It is easy to read and understand.
- Use descriptive variable and function names.
- Bias against try / except blocks. Use them only when necessary.
- Add docstrings / type hints / comments (where appropriate) to clarify the code.
- Bias for using Python 3.13 onwards features, such as pattern matching, dataclasses, libraries and type annotations.
- Bias towards using guard clauses to reduce nesting and improve readability.
- Ensure functions are small and focused on a single task.To allow for easier testing and maintenance.
- Always return one type of value from a function, rather than multiple types. This helps to avoid confusion and makes the code easier to understand.
- Use OOP where possible
- All functions should have comprehensive error handling to ensure that the code is robust and can handle unexpected situations gracefully.
- Bias against list comprehensions. Only use for very simple cases where it enhances readability.