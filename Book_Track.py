"""
============================================================
📚 BOOKTRACK
Personal Book Management System

Read. Track. Grow. 🚀
============================================================
"""

from datetime import date
import json


# ============================================================
# 📖 BOOK CLASS
# ============================================================

class Book:

    def __init__(
        self,
        book_id,
        title,
        author,
        genre,
        pages,
        progress,
        rating,
        status,
        created_at=None
    ):
        self.id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.progress = progress
        self.rating = rating
        self.status = status

        if created_at:
            self.created_at = created_at
        else:
            self.created_at = date.today()

    def show_info(self):

        print("-" * 60)
        print(f"🆔 ID: {self.id}")
        print(f"📕 Title: {self.title}")
        print(f"✍️ Author: {self.author}")
        print(f"🏷️ Genre: {self.genre}")
        print(f"📄 Pages: {self.pages}")
        print(f"📊 Progress: {self.progress}%")
        print(f"⭐ Rating: {self.rating}/5")
        print(f"📌 Status: {self.status}")
        print(f"📅 Added: {self.created_at}")
        print("-" * 60)


# ============================================================
# 📚 BOOK STORAGE
# ============================================================

books = []
next_id = 1

FILE_NAME = "books.json"


# ============================================================
# 💾 SAVE BOOKS
# ============================================================

def save_books():

    data = []

    for book in books:

        data.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "pages": book.pages,
            "progress": book.progress,
            "rating": book.rating,
            "status": book.status,
            "created_at": str(book.created_at)
        })

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

    print("💾 Books saved successfully!")


# ============================================================
# 📥 LOAD BOOKS
# ============================================================

def load_books():

    global next_id

    try:

        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        for item in data:

            book = Book(
                item["id"],
                item["title"],
                item["author"],
                item["genre"],
                item["pages"],
                item["progress"],
                item["rating"],
                item["status"],
                item["created_at"]
            )

            books.append(book)

        if books:
            next_id = max(book.id for book in books) + 1

        print(f"📚 {len(books)} book(s) loaded successfully!")

    except FileNotFoundError:

        print("📭 No saved books found. Starting fresh.")

    except json.JSONDecodeError:

        print("⚠️ books.json is empty or corrupted.")
        print("📭 Starting with an empty library.")


# ============================================================
# ➕ ADD BOOK
# ============================================================

def add_book():

    global next_id

    print("\n" + "=" * 60)
    print("➕ ADD NEW BOOK")
    print("=" * 60)

    title = input("📕 Enter book title: ").strip()

    if not title:
        print("❌ Title cannot be empty!")
        return

    author = input("✍️ Enter author: ").strip()

    if not author:
        print("❌ Author cannot be empty!")
        return

    genre = input("🏷️ Enter genre: ").strip()

    if not genre:
        print("❌ Genre cannot be empty!")
        return

    try:

        pages = int(input("📄 Enter number of pages: "))

        if pages <= 0:
            print("❌ Pages must be greater than 0!")
            return

    except ValueError:

        print("❌ Please enter a valid number!")
        return

    try:

        progress = float(
            input("📊 Enter progress (0-100): ")
        )

        if progress < 0 or progress > 100:
            print("❌ Progress must be between 0 and 100!")
            return

    except ValueError:

        print("❌ Please enter a valid number!")
        return

    try:

        rating = float(
            input("⭐ Enter rating (0-5): ")
        )

        if rating < 0 or rating > 5:
            print("❌ Rating must be between 0 and 5!")
            return

    except ValueError:

        print("❌ Please enter a valid number!")
        return

    if progress == 0:
        status = "Not Started"

    elif progress == 100:
        status = "Completed"

    else:
        status = "Reading"

    book = Book(
        next_id,
        title,
        author,
        genre,
        pages,
        progress,
        rating,
        status
    )

    books.append(book)

    save_books()

    print(f"\n✅ '{title}' added successfully!")
    print(f"🆔 Book ID: {next_id}")

    next_id += 1


# ============================================================
# 📚 SHOW ALL BOOKS
# ============================================================

def show_books():

    print("\n" + "=" * 60)
    print("📚 MY BOOKS")
    print("=" * 60)

    if not books:

        print("📭 Your library is empty.")
        return

    for book in books:
        book.show_info()


# ============================================================
# 🔎 SEARCH BOOK
# ============================================================

def search_book():

    print("\n" + "=" * 60)
    print("🔎 SEARCH BOOK")
    print("=" * 60)

    keyword = input(
        "Enter title, author, or genre: "
    ).strip().lower()

    if not keyword:

        print("❌ Search cannot be empty!")
        return

    found = False

    for book in books:

        if (
            keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword in book.genre.lower()
        ):

            book.show_info()
            found = True

    if not found:

        print("❌ No books found.")


# ============================================================
# 📊 UPDATE PROGRESS
# ============================================================

def update_progress():

    print("\n" + "=" * 60)
    print("📊 UPDATE READING PROGRESS")
    print("=" * 60)

    if not books:

        print("📭 No books available.")
        return

    try:

        book_id = int(
            input("🆔 Enter book ID: ")
        )

    except ValueError:

        print("❌ Invalid ID!")
        return

    for book in books:

        if book.id == book_id:

            try:

                progress = float(
                    input("📊 Enter new progress (0-100): ")
                )

                if progress < 0 or progress > 100:

                    print(
                        "❌ Progress must be between 0 and 100!"
                    )

                    return

            except ValueError:

                print("❌ Please enter a valid number!")
                return

            book.progress = progress

            if progress == 0:

                book.status = "Not Started"

            elif progress == 100:

                book.status = "Completed"

            else:

                book.status = "Reading"

            save_books()

            print("✅ Progress updated successfully!")

            return

    print("❌ Book not found.")


# ============================================================
# ⭐ RATE BOOK
# ============================================================

def rate_book():

    print("\n" + "=" * 60)
    print("⭐ RATE BOOK")
    print("=" * 60)

    try:

        book_id = int(
            input("🆔 Enter book ID: ")
        )

    except ValueError:

        print("❌ Invalid ID!")
        return

    for book in books:

        if book.id == book_id:

            try:

                rating = float(
                    input("⭐ Enter new rating (0-5): ")
                )

                if rating < 0 or rating > 5:

                    print(
                        "❌ Rating must be between 0 and 5!"
                    )

                    return

            except ValueError:

                print("❌ Please enter a valid number!")
                return

            book.rating = rating

            save_books()

            print("✅ Rating updated successfully!")

            return

    print("❌ Book not found.")


# ============================================================
# 📌 CHANGE STATUS
# ============================================================

def change_status():

    print("\n" + "=" * 60)
    print("📌 CHANGE BOOK STATUS")
    print("=" * 60)

    try:

        book_id = int(
            input("🆔 Enter book ID: ")
        )

    except ValueError:

        print("❌ Invalid ID!")
        return

    for book in books:

        if book.id == book_id:

            print("\n1. 📕 Not Started")
            print("2. 📖 Reading")
            print("3. ✅ Completed")

            choice = input(
                "\n👉 Choose status: "
            ).strip()

            if choice == "1":

                book.status = "Not Started"

            elif choice == "2":

                book.status = "Reading"

            elif choice == "3":

                book.status = "Completed"

            else:

                print("❌ Invalid choice!")
                return

            save_books()

            print("✅ Status updated successfully!")

            return

    print("❌ Book not found.")


# ============================================================
# 🗑️ DELETE BOOK
# ============================================================

def delete_book():

    print("\n" + "=" * 60)
    print("🗑️ DELETE BOOK")
    print("=" * 60)

    if not books:

        print("📭 No books available.")
        return

    try:

        book_id = int(
            input("🆔 Enter book ID: ")
        )

    except ValueError:

        print("❌ Invalid ID!")
        return

    for book in books:

        if book.id == book_id:

            confirm = input(
                f"⚠️ Delete '{book.title}'? (y/n): "
            ).strip().lower()

            if confirm != "y":

                print("❌ Deletion cancelled.")
                return

            books.remove(book)

            save_books()

            print(
                f"✅ '{book.title}' "
                f"was deleted successfully!"
            )

            return

    print("❌ Book not found.")


# ============================================================
# 📊 STATISTICS
# ============================================================

def show_statistics():

    print("\n" + "=" * 60)
    print("📊 BOOK STATISTICS")
    print("=" * 60)

    if not books:

        print("📭 No books available.")
        return

    total_books = len(books)

    not_started = 0
    reading = 0
    completed = 0

    total_pages = 0
    total_progress = 0

    rated_books = 0
    rating_sum = 0

    genres = {}

    for book in books:

        total_pages += book.pages
        total_progress += book.progress

        if book.status == "Not Started":

            not_started += 1

        elif book.status == "Reading":

            reading += 1

        elif book.status == "Completed":

            completed += 1

        if book.rating > 0:

            rating_sum += book.rating
            rated_books += 1

        if book.genre in genres:

            genres[book.genre] += 1

        else:

            genres[book.genre] = 1

    average_progress = (
        total_progress / total_books
    )

    print(f"📚 Total books: {total_books}")
    print(f"📕 Not Started: {not_started}")
    print(f"📖 Reading: {reading}")
    print(f"✅ Completed: {completed}")
    print(f"📄 Total pages: {total_pages}")
    print(
        f"📊 Average progress: "
        f"{average_progress:.1f}%"
    )

    if rated_books > 0:

        average_rating = (
            rating_sum / rated_books
        )

        print(
            f"⭐ Average rating: "
            f"{average_rating:.1f}/5"
        )

    else:

        print("⭐ Average rating: No ratings yet")

    print("\n🏷️ GENRES")

    for genre, count in genres.items():

        print(f"   • {genre}: {count}")


# ============================================================
# 🏠 MAIN MENU
# ============================================================

def main():

    load_books()

    while True:

        print("\n")

        print(
            "╔══════════════════════════════════════════════════════╗"
        )
        print(
            "║                    📚 BOOKTRACK                      ║"
        )
        print(
            "║          Personal Book Management System             ║"
        )
        print(
            "╠══════════════════════════════════════════════════════╣"
        )
        print(
            "║  1. ➕ Add Book                                      ║"
        )
        print(
            "║  2. 📚 Show All Books                                ║"
        )
        print(
            "║  3. 🔎 Search Book                                   ║"
        )
        print(
            "║  4. 📊 Update Progress                               ║"
        )
        print(
            "║  5. ⭐ Rate Book                                     ║"
        )
        print(
            "║  6. 📌 Change Status                                 ║"
        )
        print(
            "║  7. 🗑️ Delete Book                                   ║"
        )
        print(
            "║  8. 📈 Statistics                                    ║"
        )
        print(
            "║  9. 🚪 Exit                                          ║"
        )
        print(
            "╚══════════════════════════════════════════════════════╝"
        )

        choice = input(
            "\n👉 Choose an option: "
        ).strip()

        if choice == "1":

            add_book()

        elif choice == "2":

            show_books()

        elif choice == "3":

            search_book()

        elif choice == "4":

            update_progress()

        elif choice == "5":

            rate_book()

        elif choice == "6":

            change_status()

        elif choice == "7":

            delete_book()

        elif choice == "8":

            show_statistics()

        elif choice == "9":

            save_books()

            print(
                "\n👋 Thank you for using BookTrack!"
            )

            print(
                "📚 Keep reading and keep growing! 🚀"
            )

            break

        else:

            print(
                "❌ Invalid choice. Please choose 1-9."
            )


# ============================================================
# 🚀 START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()