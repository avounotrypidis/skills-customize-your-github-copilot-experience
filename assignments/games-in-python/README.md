# 📘 Assignment: Hangman (Games in Python)

## 🎯 Objective

Build a playable Hangman game in Python to practice string manipulation, control flow, and user I/O.

## 📝 Tasks

### 🛠️ Core: Hangman Game

#### Description
Implement a command-line Hangman game that selects a secret word and lets the player guess letters until they either guess the word or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a secret word from a predefined list (or `words.txt` if provided).
- Display the word progress using underscores for unknown letters (e.g. `_ a _ _ m a n`).
- Accept single-letter guesses (case-insensitive) and ignore repeated guesses.
- Track and display remaining attempts and incorrect guesses.
- End when the word is fully guessed (win) or attempts are exhausted (lose), showing a final message and the correct word.
- Provide clear input prompts and basic validation for user input.


### 🛠️ Optional: Enhancements

#### Description
Add extra features to improve gameplay and user experience.

#### Requirements (optional)

- Load words from an external file and support different difficulty levels.
- Display simple ASCII-art hangman states for wrong guesses.
- Add a replay option and a simple high-score or attempts-record.
- Provide a hint system that reveals a letter or gives a clue.

## Starter Files

- [starter-code.py](assignments/games-in-python/starter-code.py) — a minimal starter implementation to build from.

## How to run

From the repository root, run:

```bash
python3 assignments/games-in-python/starter-code.py
```

## Learning outcomes

- Practice working with strings, lists, and control flow in Python.
- Implement user input validation and simple game loops.
- Apply basic file I/O if loading words from a file.

# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
