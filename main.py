import news
from db import top_headlines, all_articles, breaking_headlines_db
from summarizer import gemini_summary, extract_article
from bias_classifier import gemini_biased_classifier

def summary():
    print("What do you want to summarise?\n"
          "1. Top Headlines\n"
          "2. Detailed Article\n"
          "3. Breaking Headline\n")
    choice = input("Enter your choice: ")

    collection = None

    if choice == "1":
        collection = top_headlines
    elif choice == "2":
        collection = all_articles
    elif choice == "3":
        collection = breaking_headlines_db
    else:
        print("Invalid Choice.")
        return  # Important: prevents error if invalid choice

    docs = list(collection.find({}))
    if not docs:
        print("No articles found")
        return

    print("\nAvailable Articles:")
    for i, doc in enumerate(docs, start=1):
        title = doc.get("title", "No Title")
        url = doc.get("url", "No URL")
        print(f"{i}. {title}\n{url}\n")

    try:
        choice = int(input("Enter the article number to summarize: ")) - 1

        if choice < 0 or choice >= len(docs):
            raise IndexError("Invalid article number.")
        url = docs[choice].get("url")
        if not url:
            raise ValueError("No URL found for the selected article.")
        print("Article is getting downloaded")
        content = extract_article(url)
        print("Article is getting summarised")
        summary = gemini_summary(content)
        print("\n--- SUMMARY ---\n")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")

def bias():
    print("What do you want to test for biasness?\n"
          "1. Top Headlines\n"
          "2. Detailed Article\n"
          "3. Breaking Headline\n")
    pick = int(input("Enter your choice: "))

    collection = None

    if pick == 1:
     collection = top_headlines
    elif pick == 2:
     collection = all_articles
    elif pick == 3:
     collection = breaking_headlines_db
    else:
     print("Invalid choice")

    docs = list(collection.find({}))
    if not docs:
        print("No article found")

    print("All available articles: ")
    for i, doc in enumerate(docs, start=1):
        title = doc.get("title", "No Title")
        url = doc.get("url", "No Url")
        print(f"{i}. {title}\n{url}\n")

    try:
        choice = int(input("Enter the article number to test for biasness: ")) - 1
        if choice < 0 or choice >= len(docs):
            raise IndexError("Invalid article number.")
        url = docs[choice].get("url")
        if not url:
            raise ValueError("No URL found for the selected article.")
        print("Article is getting downloaded")
        content = extract_article(url)
        print("Article is getting tested for biasness")
        reports = gemini_biased_classifier(content)
        print("\n--- TEST RESULTS ---\n")
        print(reports)
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("Welcome to News CLI")
        print("Press 1 to get top headlines: ")
        print("Press 2 to get detailed article: ")
        print("Press 3 to get breaking headline: ")
        print("Press 4 to summarise article: ")
        print("Press 5 to use bias classifier")
        print("Press 6 to exit News CLI: ")
        try:
            choice = input("Enter your choice: ")
        except ValueError:
            print("Please enter a valid number.")
            continue
        match choice:
            case "1":
                news.get_top_headlines()
            case "2":
                news.get_everything()
            case "3":
                news.breaking_headlines()
            case "4":
                summary()
            case "5":
                bias()
            case "6":
                exit()
            case _:
                print("Choice not recognized")

if __name__ == '__main__':
    main()
