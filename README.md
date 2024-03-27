# Russian Word Parser

This Python application parses a website containing a Russian word dictionary. The parsed words are filtered based on the starting letters specified in the `parse.py` file, where the letters are stored in an array called `letters`. 

Additionally, in the `main.py` file, consonant letters are assigned to digits from 0 to 9. Then, for numbers from 10 to 100, the program searches for words in the downloaded dictionary that contain only the encoded consonant letters and no other consonant code letters.

Based on the output, you can build a personal dictionary, which is essential for some memorisation techniques.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)

## Setup

1. Clone this repository to your local machine.
2. Install the dependencies using the command `pip install -r requirements.txt`.


## Usage

1. Open `parse.py` and specify the starting letters for the words you want to parse by adding them to the `letters` array.

2. Run the `parse.py` script to parse the website and retrieve the words:
    
    ```bash
    python parse.py
    ```

3. Open `main.py` and ensure that consonant letters are properly assigned to digits from 0 to 9.

4. Run the `main.py` script to filter words according to the specified encoding:

    ```bash
    python main.py
    ```
