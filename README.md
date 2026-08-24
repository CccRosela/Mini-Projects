# Mini-Projects
A variety of mini-projects for practice. Please find a small description of each mini-project below.

1. Address_Verifier
    - Name + email <br>→ check if the email contains `:` or `@` → print a colored valid/invalid message → welcome the user if valid.
    - Email Regex Validation <br>→ validate email format using `regex` → check for `word@word.extension` pattern → support optional subdomains (e.g. `univie.ac.at`) → match against common domain extensions → case-insensitive matching.
    - IP Address Validation <br>→ check IP against a regex pattern → verify each segment is `0–255` (with special case `0.0.0.0`).
    - Email Regex Validation Test <br>→ Testing different email inputs with `pytest` to check if the desired output is consistent with what was envisioned when writing the code.

2. Array_Search
    - Array searching <br>→ given an array of numbers and a target value → find `two unique numbers` whose sum equals the target → return their indices in ascending order → return `"Target not found"` if no matching pair exists.

3. Bank_Account
    - Account Management <br>→ user enters their name → match against a list of accounts → display current balance → loop for `deposit and withdrawal amounts` → validate input → update and display balance.

4. Emoji_Text
    - Text Editing <br>→ replace {red}, {blue} → terminal colors → replace text emojis (e.g: `:)`,`:D`) with real emojis.

5. Food_Chain
    - List/Array Processing <br>→ given an array of `[predator, prey]` pairs → identify apex predator  → follow the food chain own to the bottom of the chain → return the chain as an array of strings.

6. Fruit_Info
    - Website Scraping and dataframe creation/selection <br>→ `scrape fruit nutrition data` from a Website → organize data into a `pandas Dataframe` → allow user to select a fruit and view specific nutrition facts.

7. Goodbye
    - Text Formatting <br>→ user enters multiple names until they type exit → display a `formatted goodbye message`, depending on how many names the user entered.

8. Guess_Game
    - Random number generation <br>→ user chooses a level (maximum number) → computer generates a random number → user guesses the number → provides higher/lower hints for incorrect guesses → continue until the correct number is guessed (says how many times the user guessed) or the user types exit.

9. Math_10_Quiz
    - Random math quiz <br>→ generate `10 random addition, subtraction, or multiplication problems` → user enters an answer for each → keep track of correct answers → display the final score.

10. Math_Expression
    - Calculation <br>→ split user input into number/operator/number → perform `+`, `-`, `*`, or `/`.

11. Meal_Time
    - Time Variant <br>→ time input from user→ convert `HH:MM` into decimal hours → check if it’s breakfast, lunch, or dinner time.

12. OOP_Classes
    - Object-Oriented Programming <br>→ define `classes` and `instance attributes` → create `methods` for validation, calculations, and formatting → model concepts such as vehicles, users, rectangles, lights, students, stock, notes, and employees → `inheritance` with full-time and part-time employees.

13. TextFonts
    - tansforms text via fonts in package `pyfiglet`.

14. Vending_Machine
    - Product selection <br>→ user chooses a `product number` → enter payment → check if the amount is enough → confirm the purchase or calculate remaining amount/change.


## Other Ideas waiting to be implemented: U6
    # bitcoin - get API bitcoin value (maybe other funds as well, commodities [gold], derivatives, to be implemented... {depends on complexity, might require a repository by itself...}), user types in how much they want to purchase, adds it to their 'wallet'
    # unit tests ---> test output of past made projects
    # implement a few File I/O's (on past projects)
    # etc...
