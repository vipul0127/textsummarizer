Here's the revised README file for your Text Summarizer project:

---

# Text Summarizer Web Application

## Overview

The **Text Summarizer Web Application** is a user-friendly web-based tool that allows users to input a block of text and receive a concise summary in return. Built using Python and Flask, this application leverages natural language processing (NLP) techniques to extract the most relevant information from the text. This tool is useful for quickly understanding lengthy articles, documents, or any large text data.

## Features

- **Text Input**: Users can paste text directly into the input field on the web interface.
- **Text Summarization**: The app generates a summary by extracting the most relevant sentences from the input text.
- **Simple Interface**: The web app has a clean and easy-to-use interface built using HTML and Flask.
- **Efficient Processing**: The summarization is performed efficiently, even for longer texts.

## Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **NLP Library**: spaCy for text processing
- **Data Handling**: pandas, collections (Counter)

## Web UI![image](https://github.com/user-attachments/assets/fe46938f-d114-4b0d-8b14-824074c4a25b)


1. **Open the web application** in your preferred browser.
2. **Input your text** into the provided text box.
3. **Click the "Summarize" button** to generate a summary of the provided text.
4. **View the summary** displayed on the screen below the input box.

## File Structure

- `app.py`: Main Flask application file that handles routing and logic.
- `templates/`: Contains HTML files for the web interface.
  - `index.html`: Main page of the web application.
- `static/`: Contains CSS and other static files for styling.
- `requirements.txt`: Lists all the Python libraries required to run the application.

## Example

Input:

```
Created by artist/writer Rob Liefeld and writer Fabian Nicieza, Deadpool made his first appearance on the pages of The New Mutants #98 cover-dated Feb. 1991.
```

Output:

```
Deadpool made his first appearance in The New Mutants #98 in 1991.
```

## Future Enhancements

- Add support for file uploads (PDF, DOCX, etc.) for text summarization.
- Implement additional NLP techniques for more refined summaries.
- Add multilingual support for text summarization.

## Contributing

Feel free to submit a pull request or report issues. Contributions are welcome to improve this project!

## Acknowledgments

- Inspired by various NLP projects and the need for quick text summarization tools.
- Libraries used: spaCy, Flask, pandas.
