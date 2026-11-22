def greet(name: str) -> str:
    return f"Hello, {name}! Your VS Code project is successfully connected to GitHub."


if __name__ == "__main__":
    user_name = input("Enter your name: ").strip() or "Developer"
    print(greet(user_name))