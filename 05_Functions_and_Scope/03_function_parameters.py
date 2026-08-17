# Lesson 03: Function Parameters and Data Transformation

def format_full_name(first: str, last: str) -> str:
    """Capitalizes and concatenates first and last name."""
    clean_first = first.strip().capitalize()
    clean_last = last.strip().capitalize()
    return f"{clean_first} {clean_last}"

full_name = format_full_name("dexter", "morgan")
print(f"Formatted Name: {full_name}")
