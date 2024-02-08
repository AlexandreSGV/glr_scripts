# GLR Scripts for Automated Searches

## About

This repository hosts a collection of Python scripts designed to automate the search process for Grey Literature Reviews (GLR). Utilizing the Google search engine, these scripts enable automated literature gathering by running predefined search strings in both Google's general search and across specific target websites.

## Features

- **Automated Searches**: Execute search queries automatically on Google.
- **Targeted Website Searches**: Direct searches to specific websites to find relevant literature.
- **Results Export**: Collect and export search results into a structured CSV format for easy analysis.

## Getting Started

### Prerequisites

- Python 3.x
- BeautifulSoup4
- requests
- googlesearch-python

### Installation

1. Clone the repository:
  ```bash
   git clone https://github.com/AlexandreSGV/glr_scripts.git
  ´´´
2. Install the required Python packages:
  ```bash
   pip install -r requirements.txt
  ´´´

### Usage

1. Edit `search_strings` and `search_websites` in `main.py` to define your search queries and target websites.
2. Run the script:
```bash
   python main.py
  ´´´

3. Check `search_results.csv` for your results.

## Contributing

We welcome contributions to improve these scripts further. Please feel free to fork the repository, make your changes, and submit a pull request.

## Author

- **Alexandre Strapação Guedes Vianna**
- Email: strapacao@gmail.com
- Website: [alexandrevianna.net](http://alexandrevianna.net)
- Related Paper: [A Grey Literature Review on Data Stream Processing applications testing](https://www.sciencedirect.com/science/article/abs/pii/S0164121223001395)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
