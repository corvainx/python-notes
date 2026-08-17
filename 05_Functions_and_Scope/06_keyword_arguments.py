# Lesson 06: Keyword Arguments
# Keyword arguments explicitly state parameter names, allowing arbitrary call order.

def generate_user_profile(username, email, plan="Free", verified=False):
    print(f"Profile: @{username} | Email: {email} | Plan: {plan} | Verified: {verified}")

# Specifying keyword arguments out of order
generate_user_profile(
    email="dexter@example.com",
    username="dexter_m",
    verified=True,
    plan="Pro"
)
