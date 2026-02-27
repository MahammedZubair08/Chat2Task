def parse_command(message: str):
    if not message.lower().startswith("bot"):
        raise ValueError("Invalid command prefix.")

    message = message[3:].strip()

    if message.startswith("create file"):
        filename = message.replace("create file", "").strip()
        return {
            "action": "create_file",
            "filename": filename
        }

    elif message.startswith("send email"):
        # Example format:
        # bot send email to xyz@gmail.com subject Hello body Test
        parts = message.split(" ")
        try:
            to_index = parts.index("to") + 1
            subject_index = parts.index("subject") + 1
            body_index = parts.index("body") + 1
        except ValueError:
            raise ValueError("Invalid email format.")

        return {
            "action": "send_email",
            "to": parts[to_index],
            "subject": parts[subject_index],
            "body": " ".join(parts[body_index:])
        }

    else:
        raise ValueError("Unknown command.")