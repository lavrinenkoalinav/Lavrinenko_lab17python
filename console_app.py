from assistant import Assistant

def main():
    assistant = Assistant()

    print("Консольний асистент. Команди: /add, /list, /search, /exit")

    while True:
        command = input(">>> ").strip()
        
        if command == "/add":
            note = input("Введіть нотатку: ")
            assistant.add_note(note)
            print("✅ Нотатку додано.")
        
        elif command == "/list":
            notes = assistant.list_notes()
            if notes:
                print("\n".join(f"{i+1}. {n}" for i, n in enumerate(notes)))
            else:
                print("⚠️ Немає нотаток.")
        
        elif command == "/search":
            keyword = input("Ключове слово: ")
            results = assistant.search_notes(keyword)
            if results:
                print("\n".join(results))
            else:
                print("🔍 Нічого не знайдено.")
        
        elif command == "/exit":
            print("👋 До побачення!")
            break
        else:
            print("❓ Невідома команда.")

if __name__ == "__main__":
    main()
