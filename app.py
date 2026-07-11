import os
from dotenv import load_dotenv
from openai import OpenAI
from prompts import SHORT_SUMMARY, BULLET_SUMMARY, EXECUTIVE_SUMMARY, AGE10_SUMMARY

load_dotenv()
client = OpenAI(
    api_key=os.getenv("AI_API_KEY")
    )
def choose_prompt(choice):
    """Return the selected prompt."""

    if choice == "1":
        return SHORT_SUMMARY
    elif choice == "2":
        return BULLET_SUMMARY
    elif choice == "3":
        return EXECUTIVE_SUMMARY
    elif choice == "4":
        return AGE10_SUMMARY
    else:
        return SHORT_SUMMARY


def generate_summary(prompt,text):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )

    return response.output_text

def save_summary(summary):

    os.makedirs("summaries", exist_ok=True)

    with open("summaries/output.txt", "w", encoding="utf-8") as file:
        file.write(summary)

def main():
    print("=" * 40)
    print("AI TEXT SUMMARIZER")
    print("=" * 40)

    print("\nChoose summary style")
    print("1. Short Summary")
    print("2. Bullet Points")
    print("3. Executive Summary")
    print("4. Explain Like I'm 10")


    choice=input("\nChoice: ")
    text = input("Paste text to summarize:\n")
    
    if not text.strip():
        print("Please provide some text to summarize.")
        return
    
    prompt = choose_prompt(choice)

   
      
    try:
        print("\nGenerating summary...")
        summary = generate_summary(prompt, text)

        save_summary(summary)

        print("\nSummary request saved successfully.")
        print("Saved to: summaries/output.txt")
        print("\nSummary:\n")

        print(summary)

    except Exception as ex:
        if "insufficient_quota" in str(ex):
            print("API quota exceeded. Please check billing.")

        elif "invalid_api_key" in str(ex):
            print("Invalid API key.")
        else:
            print(f"Error: {ex}")


if __name__ == "__main__":
    main()