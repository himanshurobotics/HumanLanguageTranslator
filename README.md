https://github.com/terraspin/HumanLanguageTranslator

# Human Language Translator

In this Python project, I've made a windows application to translate the Natural Human Language from one language to another language.

Modules I've used in this project with their use,
  - pip is required to install required libraries/modules
  - Googletrans python module for Google Translate API
  - TextBlob python module to process Natural Human Language
  - Tkinter GUI toolkit for GUI
  - PyInstaller to convert the Python script to executable (.exe) file.

# Features!

  - Auto detect the language of the input text which you want to translate
  - You can translate even the Natural Human Language not just only some words or phrases
  - Convert the text in 107 different languages
  - Easy to use with simple GUI
  - Portable by converting to executable file but system should have internet connection.

# Installation

This program requires Python installed in PC.

#### Install the dependencies

1. pip
    pip is a Python standard module, so it comes preinstalled with Python Setup.

2. Tkinter
    Tkinter is a Python standard library, so it comes preinstalled with Python Setup.
    ```
    Click on the checkbox of tcl/tk and IDLE while installing Python from setup in windows
    ```
3. Google Translate API
    Run the below command in the Terminal in Linux/Mac or CCMD/Powershell in Windows
    ```
    pip install googletrans
    ```
4. TextBlob module
    Run the below command in the Terminal in Linux/Mac or CCMD/Powershell in Windows
    ```
    pip install textblob
    ```
5. PyInstaller module
    Run the below command in the Terminal in Linux/Mac or CCMD/Powershell in Windows
    ```
    pip install pyinstaller
    ```

#### Usage (internet should be connected to the system)
From Python Script
Just run the `HumanLanguageTranslator.py` in your favourite Python enabled IDE. 
##### or
Create your own executable file by following the below method,
1. Open Terminal in Linux/Mac or CMD/Powershell in Windows.
2. Run the below command,
    ```
    pyinstaller -F \Path\to\the\script\HumanLanguageTranslator.py
    ```
3. This will create a `HumanLanguageTranslator.exe` file inside the `dist` folder in the current working directly, which can be used anytime.
