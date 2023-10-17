# Web Scraper API Documentation

## Introduction

The API is designed to scrape the content of the following website: [https://wsa-test.vercel.app](https://wsa-test.vercel.app).

## API Endpoint:

- **Endpoint:** http://127.0.0.1:5000.

- **HTTP Method:** POST

**Description:** The API allows you to scrape content from the mentioned webpage by providing a valid URL.If an invalid URLis provide, a proper error message will be displayed. The information returned by this API is in JSON format.

## API Set up

Before running the Web Scraper API, make sure you have the following prerequisites installed:

- [Python](https://docs.python.org/3/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [npm](https://www.npmjs.com)
- [Tailwind CSS](https://tailwindcss.com)

To run the Web Scraper API, run the following command: `python -u main.py`.

## API Folder structure

- `node_module`, `package-lock.json`, `package.json`, `tailwind.config.js` are Tailwind CSS related files.
- **src** directory contains the Python files.
- **templtes** directory contains the HTML files.
- **static** directory contains the other front-end files.
