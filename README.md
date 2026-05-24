# NewsAppUsingPython

A Django-based news aggregator that pulls headlines from multiple technology sources and displays them in a simple web interface.

## Features

- Homepage with news from TechRadar, TechCrunch, Wired, Engadget, The Next Web, and The Verge
- Dedicated pages for each source
- Responsive templates for displaying article title, description, image, and source link

## Requirements

The project uses:

- Django
- newsapi-python
- python-dotenv

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Environment variables

Create a `.env` file in the project root and add your News API key:

```env
NEWSAPI_KEY=your_newsapi_key_here
```

The app loads this key automatically when Django starts.

## Setup

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Create a `.env` file with your `NEWSAPI_KEY`.
5. Run the development server.

```bash
python manage.py migrate
python manage.py runserver
```

## Notes

- The News API key is no longer hardcoded in the application code.
- No code execution was performed while updating this project.

## Project Structure

- `News/` – Django project settings and URL configuration
- `NewsApp/` – app logic and views
- `templates/` – HTML templates for the site
- `static/` – static assets
