import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# 1. Upload the PDF
print("--- Step 4: Initializing Chat with Persistent Memory ---")
file_path = "data.pdf"
uploaded_file = client.files.upload(file=file_path)

# Wait for processing
while uploaded_file.state == "PROCESSING":
    print(".", end="", flush=True)
    time.sleep(2)
    uploaded_file = client.files.get(name=uploaded_file.name)

# 2. Create a Formal Chat Session
# This 'chat' object automatically stores the history of the conversation
chat = client.chats.create(model="gemini-flash-latest")

print("\n🚀 System Ready! You can now chat with your PDF.")
print("Type 'exit' to stop the session.\n")

while True:
    user_query = input("You: ")
    
    if user_query.lower() == "exit":
        print("Closing chat. Goodbye!")
        break

    # We send the file AND the query in the message to provide the context
    # Gemini handles the 'memory' for all following turns automatically
    response = chat.send_message(message=[uploaded_file, user_query])
    
    print(f"\nAI: {response.text}\n")