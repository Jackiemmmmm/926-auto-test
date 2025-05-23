# Pytest-BDD and Playwright Login Automation Test Example

This example project shows how to use Pytest-BDD and Playwright to create behavior-driven development (BDD) style automation tests.

## Features

- Use Gherkin syntax to write test scenarios
- Use Playwright to automate web browser interactions
- Implement Page Object Model design pattern
- Support data-driven testing (through scenario outline)
- Clear test step definition

## Project structure

```terminal
.
├── README.md
├── conftest.py # Pytest configuration file
├── features
│ └── login.feature # Test scenario in Gherkin format
├── pages
│ │── login_page_playwright.py # Login page playwright
│ └── login_page_selenium.py # Login page selenium
├── pyproject.toml # Project configuration and dependencies
└── step_defs
  │── test_login_playwright.py # Step definition playwright implementation
  └── test_login_selenium.py # Step definition selenium implementation
```

## Installation

### Make sure you have Python 3.8 or higher installed in your environment

### Create and activate a virtual environment

```command
python -m venv .venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

### Install dependencies

```command
pip install -r requirements.txt 
```

### Install Playwright/Selenium Browser

```command
playwright install
```

You also need to download the Chrome browser and ChromeDriver:

Visit Chrome for Testing
Download Chrome and ChromeDriver that match your operating system
Unzip the files to the `chrome` folder of the project

```command
https://googlechromelabs.github.io/chrome-for-testing/
```

## Run tests

Execute all tests:

```command
pytest -s
```

Run tests and show verbose output:

```command
pytest -v
```

Run in headless mode (suitable for CI environments):

```command
pytest --headless
```

## Test scenarios

This example contains the following test scenarios:

1. Login with valid credentials

## Extensions

You can extend this project in the following ways:

1. Add more scenarios (e.g. password reset, remember me feature, etc.)

2. Add test reports (e.g. using pytest-html)
3. Integrate into CI/CD process
4. Add more page objects and functional tests
