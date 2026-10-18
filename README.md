Python Web Explorer 🔎

A simple website analysis tool built with Python and Tkinter.

Web Explorer allows users to enter a website URL, fetch its HTML content, and inspect useful information about the page through a graphical user interface.

✨ Features

* Enter a website URL through a GUI.
* Fetch website content using HTTP requests.
* Display the final URL and HTTP status code.
* Extract the page title.
* Find headings (h1, h2, and h3).
* Extract links and their text.
* Optionally inspect the HTML source code.
* Run website requests in a background thread to keep the interface responsive.
* Handle request errors and display results in the GUI.

🛠️ Technologies

* Python — application logic.
* Tkinter — graphical user interface.
* Requests — HTTP requests.
* BeautifulSoup — HTML parsing.
* Threading — background tasks.
* window.after() — safely schedule GUI updates from the main thread.

📦 Requirements

* Python 3.10 or newer recommended.
* requests
* beautifulsoup4

Tkinter is included with many Python installations.

🚀 Installation

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Install the required packages:

python -m pip install requests beautifulsoup4

4. Run the application:

python web_explorer.py

📖 What I Learned

While building this project, I practised:

* Creating a GUI with Tkinter.
* Sending HTTP requests and handling responses.
* Parsing HTML with BeautifulSoup.
* Working with lists, loops, and string formatting.
* Running tasks in background threads.
* Using window.after() to schedule GUI updates.
* Handling exceptions and displaying error messages.
* Organizing a Python project into functions.

🎯 Future Improvements

* Validate URLs more thoroughly.
* Improve HTML source viewing and line limits.
* Add a progress indicator.
* Support exporting analysis results to a text file.
* Improve the layout and user experience.

👩‍💻 Author

Created as a personal learning project while exploring Python, GUI development, web requests, HTML parsing, and threading.
