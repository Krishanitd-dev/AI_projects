import os
import sys
from dotenv import load_dotenv
from ai.service import generate_summary, translate_summary
from datetime import datetime
from prompts import SHORT_SUMMARY, BULLET_SUMMARY, EXECUTIVE_SUMMARY, DETAILED_SUMMARY, EXPLAINED_SIMPLY, TRANSLATE_FRENCH, TRANSLATE_JAPANESE, TRANSLATE_SPANISH

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



def save_summary(summary, prefix="output"):

    os.makedirs("summaries", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"summaries/{prefix}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(summary)
    return filename

def main():
    print("=" * 40)
    print("AI Text Summarizer")
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
        original_chars = len(text)
        summary_chars = len(summary)
        compression = (original_chars - summary_chars) / original_chars * 100

        filename = save_summary(summary)

        print("\nSummary saved successfully.")
        print(f"Saved to: {filename}")
        print("\nSummary:\n")

        print(summary)

        print("\nSummary Statistics:")
        print("-" * 25)
        print(f"original characters: {original_chars:,}")
        print(f"summary characters : {summary_chars:,}")
        print(f"compression : {compression:.1f}%")
        
        print("\nTranslate Summary?")
        print("1. English")
        print("2. Spanish")
        print("3. French")
        print("4. Japanese")
        print("5. Skip")

        language = input("\nChoice: ")

        translated = None

        if language == "1":
            translated = summary
        elif language == "2":
            translated = translate_summary(TRANSLATE_SPANISH, summary)
        elif language == "3":
            translated = translate_summary(TRANSLATE_FRENCH, summary)
        elif language == "4":
            translated = translate_summary(TRANSLATE_JAPANESE, summary)
        elif language == "5":
            print("translation skipped.")
            
        else:
            print("invalid choice.")

        if translated:
            print("\n========= Translated Summary =========\n")
            print(translated)
            print("=======================")
            translated_filename = save_summary(translated, "translation")
            print(f"\nTranslated summary saved to: {translated_filename}")


    except Exception as ex:
        error = str(ex).lower()
        if "connection" in error:
            print("Network error.")
        
        elif"insufficient_quota" in error:
            print("API quota exceeded. Please check billing.")

        elif "invalid_api_key" in error:
            print("Invalid API key.")
        
        elif "invalid_request_error" in error:
            print("Invalide_Request.")
        else:
            print(f" UnexpectedError: {ex}")


if __name__ == "__main__":
    main()