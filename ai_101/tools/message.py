from openai.types.chat.chat_completion import ChatCompletionMessage

def print_messages(messages):
    for message in messages:
        if isinstance(message, dict):
            role = message['role']
            content = message['content']
            print(f"{role.capitalize()}: {content}\n")
        elif isinstance(message, ChatCompletionMessage):
            print(f"{message.role.capitalize()}: {message.content}\n")
