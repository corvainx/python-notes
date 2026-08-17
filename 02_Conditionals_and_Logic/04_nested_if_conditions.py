# Lesson 04: Nested Conditional Statements

is_student = True
has_coupon = True
gpa = 3.9

if is_student:
    print("Student identified.")
    if gpa >= 3.5:
        print("Qualifies for Dean's Honor Roll!")
        if has_coupon:
            print("Eligible for maximum 50% discount.")
        else:
            print("Eligible for standard 25% student discount.")
    else:
        print("Eligible for standard 15% student discount.")
else:
    print("Regular customer pricing applies.")
