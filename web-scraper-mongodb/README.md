# web-scraper-mongodb

## Project Overview
This project is a web scraper that connects to a local MongoDB server to store input data and output responses from web scraping activities. It utilizes Python libraries for web scraping and MongoDB interactions.

## Directory Structure
```
web-scraper-mongodb
├── src
│   ├── __init__.py
│   ├── scraper.py
│   ├── database.py
│   ├── models
│   │   ├── __init__.py
│   │   └── scrape_result.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── config
│   └── config.py
├── requirements.txt
├── .env
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd web-scraper-mongodb
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration
- Update the `.env` file with your MongoDB connection details.
- Modify `config/config.py` if additional configuration settings are needed.

## Usage
1. Run the scraper:
   ```
   python src/scraper.py
   ```
2. Follow the prompts to input the URL you wish to scrape.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes.

## License
This project is licensed under the MIT License.