import json
import tiktoken


def process_chat_data(
    input_file,
    output_file,
    first_old,
    first_new,
    second_old,
    second_new,
    low_limit,
    high_limit,
):
    """
    This script processes a Telegram chat export (in JSON format), removing non-text messages and emojis,
    and replacing participant names with initials. It also filters out messages that are too short or too long.
    The processed chat data is written to a new file.

    Args:
        input_file (str): Path to the input JSON file.
        output_file (str): Path to the output file.
        first_old (str): Original name of the first user to be replaced.
        first_new (str): New name of the first user.
        second_old (str): Original name of the second user to be replaced.
        second_new (str): New name of the second user.
        low_limit (int): Minimum length of messages to include.
        high_limit (int): Maximum length of messages to include.
    """

    # Get the encoding for token counting
    encoding = tiktoken.get_encoding("cl100k_base")

    lines = 0
    chars = 0
    newline = 0
    all_messages = []

    # Load the data from the JSON Telegram chat export
    with open(input_file, "r") as f:
        data = json.load(f)
        messages = data["messages"]

    # Iterate over each message in the chat
    for message in messages:
        # Skip certain messages based on your conditions
        if (
            message.get("text_entities")
            and "forwarded_from" not in message
            and message["text_entities"][0]["type"] == "plain"
        ):
            text = message["text"]
            while text.count("\n") > 0:
                newline += 1
                text = text.replace("\n", " ")
            if low_limit <= len(text) <= high_limit:
                sender = message["from"]
                lines += 1
                if sender == first_old:
                    sender = first_new
                elif sender == second_old:
                    sender = second_new
                # Add the message to the list
                all_messages.append(f"{sender}:{text}\n")

    # Check the token count
    file = "".join(all_messages)
    tokens = len(encoding.encode(file))

    # Write the messages to a new file
    with open(output_file, "w") as f:
        f.write(file)

    chars = len(file)

    # Print the number of lines created
    print(f"Messages: {lines}. \nCharacters: {chars}. \nOpenAI tokens: {tokens}.")


if __name__ == "__main__":
    # Define the input and output file paths
    input_file_path = "chat_data.json"
    output_file_path = "processed_chat_data.txt"

    # Define the character limits for messages
    char_low_limit = 100
    char_high_limit = 1000

    # Define the old and new names for the chat participants
    first_old_name = "User1"
    first_new_name = "1"
    second_old_name = "User2"
    second_new_name = "2"

    # Call the function to process the chat data
    process_chat_data(
        input_file_path,
        output_file_path,
        first_old_name,
        first_new_name,
        second_old_name,
        second_new_name,
        char_low_limit,
        char_high_limit,
    )
