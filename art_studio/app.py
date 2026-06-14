import os
import random
from typing import Optional

from art_studio.generators import (
    build_magic_quote,
    build_mosaic,
    build_spiral,
    build_tree,
    build_wave,
)


class ConsoleArtStudio:
    def __init__(self) -> None:
        self.last_art: Optional[str] = None
        self.quotes = [
            "The best way to predict the future is to create it.",
            "Art is the only way to run away without leaving home.",
            "Every line in the console is a chance to make something new.",
            "The simplest shapes become magic when you believe in them.",
        ]

    def run(self) -> None:
        self.clear_screen()
        print("Welcome to Console Art Studio!\n")
        while True:
            self.print_menu()
            choice = self.prompt_choice("Choose an art mode or 7 to exit", 1, 7)

            if choice == 1:
                self.draw_tree()
            elif choice == 2:
                self.draw_spiral()
            elif choice == 3:
                self.draw_wave()
            elif choice == 4:
                self.draw_mosaic()
            elif choice == 5:
                self.draw_quote()
            elif choice == 6:
                self.save_art()
            else:
                self.exit_program()

    def print_menu(self) -> None:
        print("Menu")
        print("1. Draw a graceful ASCII tree")
        print("2. Create a spiral pattern")
        print("3. Paint a rolling wave")
        print("4. Create a word mosaic")
        print("5. Reveal a magic quote")
        print("6. Save the last art to a file")
        print("7. Exit")

    def prompt_choice(self, prompt: str, minimum: int, maximum: int) -> int:
        while True:
            try:
                raw = input(f"{prompt} [{minimum}-{maximum}]: ").strip()
                value = int(raw)
                if minimum <= value <= maximum:
                    return value
                print(f"Enter a number between {minimum} and {maximum}.")
            except ValueError:
                print("Please enter a valid number.")

    def prompt_text(self, prompt: str, default: str = "") -> str:
        answer = input(f"{prompt}{' [' + default + ']' if default else ''}: ").strip()
        return answer or default

    def clear_screen(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def draw_tree(self) -> None:
        self.clear_screen()
        print("ASCII Tree Generator")
        height = self.prompt_number("Tree height", 6, 20, default=10)
        char = self.prompt_text("Drawing character", "*")[:1] or "*"
        art = build_tree(height, char)
        self.show_art(art)

    def draw_spiral(self) -> None:
        self.clear_screen()
        print("Spiral Pattern Maker")
        size = self.prompt_number("Spiral size", 8, 28, default=16)
        char = self.prompt_text("Drawing character", "#")[:1] or "#"
        art = build_spiral(size, char)
        self.show_art(art)

    def draw_wave(self) -> None:
        self.clear_screen()
        print("Wave Painter")
        width = self.prompt_number("Wave width", 20, 80, default=50)
        amplitude = self.prompt_number("Wave amplitude", 3, 12, default=5)
        char = self.prompt_text("Drawing character", "~")[:1] or "~"
        art = build_wave(width, amplitude, char)
        self.show_art(art)

    def draw_mosaic(self) -> None:
        self.clear_screen()
        print("Word Mosaic Studio")
        phrase = self.prompt_text("Enter a phrase to mosaic", "Hello World")
        width = self.prompt_number("Mosaic width", 20, 60, default=40)
        art = build_mosaic(phrase, width)
        self.show_art(art)

    def draw_quote(self) -> None:
        self.clear_screen()
        print("Magic Quote Generator")
        quote = random.choice(self.quotes)
        art = build_magic_quote(quote)
        self.show_art(art)

    def save_art(self) -> None:
        if not self.last_art:
            print("No art has been generated yet. Create something first.")
            input("Press Enter to return to the menu.")
            self.clear_screen()
            return

        default_name = "console_art.txt"
        filename = self.prompt_text("Filename to save", default_name)
        try:
            with open(filename, "w", encoding="utf-8") as handle:
                handle.write(self.last_art)
            print(f"Saved art to {filename}")
        except OSError as error:
            print(f"Could not save file: {error}")
        input("Press Enter to return to the menu.")
        self.clear_screen()

    def exit_program(self) -> None:
        print("Thank you for creating with Console Art Studio.")
        raise SystemExit(0)

    def show_art(self, art: str) -> None:
        self.last_art = art
        print("\n" + art)
        print("\n---\n")
        input("Press Enter to return to the menu.")
        self.clear_screen()

    def prompt_number(self, prompt: str, minimum: int, maximum: int, default: int) -> int:
        while True:
            response = self.prompt_text(prompt, str(default))
            try:
                number = int(response)
                if minimum <= number <= maximum:
                    return number
                print(f"Enter a number between {minimum} and {maximum}.")
            except ValueError:
                print("Please enter a valid whole number.")
