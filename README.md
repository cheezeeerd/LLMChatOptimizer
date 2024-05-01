#### Overview
This Python script is designed to efficiently process Telegram chat data for analysis with Large Language Models (LLMs) like GPT or Gemini. It filters and transforms chat exports into a cleaner, more concise format that focuses strictly on textual communication, optimizing both processing time and cost.

#### Features
- **Remove Non-Text Messages:** Filters out any messages that do not contain text.
- **Emoji Removal:** Strips emojis from text messages to reduce noise.
- **Name Anonymization:** Replaces names of participants with initials to preserve privacy and reduce token usage.
- **Message Filtering:** Excludes messages shorter than 10 characters or longer than 500 characters.
- **Token Count:** Uses the `tiktoken` library to count the number of tokens to ensure compatibility with LLM's context window.

#### Requirements
- Python 3.x
- `json` library (standard in Python)
- `tiktoken` library
  - Install via pip:
  ```bash
  pip install tiktoken
  ```

#### Usage
1. Prepare your Telegram chat data in JSON format by using the Telegram export feature.
2. Place the `chat_data.json` file in the same directory as the script, or modify the `input_file_path` in the script to match your file location.
3. Run the script:
   ```bash
   python optimizer.py
   ```
4. The processed chat data will be saved in `processed_chat_data.txt`.

#### Configuration
Modify the following parameters in the script as needed:
- `input_file_path`: Path to the input JSON chat data file.
- `output_file_path`: Path to where the cleaned chat data should be written.
- `char_low_limit` and `char_high_limit`: Set the minimum and maximum message lengths.
- `first_old_name`, `first_new_name`, `second_old_name`, `second_new_name`: Configure names to replace in the chat data for anonymity.

#### Output
The output file will contain:
- Processed chat messages formatted as "Initial:Message".
- Messages between the configured character limits and free of emojis.
- A terminal output summarizing the number of messages, total characters, and total token count.

#### Example
Before Processing:
```
User1: Hello! 😊
User2: Hey! How are you doing today?
User1: I'm fine, thanks for asking! 👍😉
```
After Processing:
```
1: Hello!
2: Hey! How are you doing today?
1: I'm fine, thanks for asking!
```
Terminal Output:
```
Messages: 3.
Characters: xyz.
OpenAI tokens: abc.
```
Where `xyz` and `abc` would be the specific counts from the processing.

#### Support
For issues or questions, submit a pull request or an issue on this GitHub repository.
