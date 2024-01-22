name = input("Please enter your name: ")
print(f"\nHello,{name}!")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"Hello, {name}!")


def greet_user():
    """显示简单的问候语"""
    print("Hello!")


greet_user()
