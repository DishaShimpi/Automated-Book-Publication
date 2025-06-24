# auto_book_pub/human_loop.py

def human_edit(text):
    print("\nAI-Reviewed Chapter:\n", text[:1000], "...")  # Preview only first 1000 chars
    print("\nDo you want to edit this? (y/n): ", end="")
    choice = input().lower()
    if choice == 'y':
        print("\nEnter your version below. End with an empty line:\n")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        return "\n".join(lines)
    return text
