import os

def execute_command(data: dict):
    action = data.get("action")

    if action == "create_file":
        filename = data.get("filename")
        with open(filename, "w") as f:
            f.write("Created by Chat2Task")
        return f"File '{filename}' created successfully."

    elif action == "send_email":
        # Placeholder for now
        return f"Email prepared for {data.get('to')} (email logic not added yet)."

    else:
        return "No valid action executed."