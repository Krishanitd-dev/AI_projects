import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from ai_service import generate_summary
from prompts import SHORT_SUMMARY, BULLET_SUMMARY, EXECUTIVE_SUMMARY, DETAILED_SUMMARY, EXPLAINED_SIMPLY

load_dotenv()

def choose_prompt(choice):
    """Return the selected prompt."""

    if choice == "1":
        return SHORT_SUMMARY
    elif choice == "2":
        return BULLET_SUMMARY
    elif choice == "3":
        return DETAILED_SUMMARY
    elif choice == "4":
        return EXECUTIVE_SUMMARY
    elif choice == "5":
        return EXPLAINED_SIMPLY
    elif choice == "6":
        print("Exit")
        sys.exit()
    else:
        print("invalid choice.")
        sys.exit() 



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
    print("3. Detailed Summary")
    print("4. Executive Summary")
    print("5. Explained Simply")
    print("6. Exit")
    


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