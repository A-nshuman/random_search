# Random Search

A Python script that automates random web searches using Selenium and the Microsoft Edge browser.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction
Random Search is a Python script that uses the Selenium web automation framework to perform random web searches on Bing using the Microsoft Edge browser. It can be used for various purposes, such as testing web search functionalities or generating random search queries for research.

## Prerequisites
Before running this script, make sure you have the following prerequisites installed:
- [Python](https://www.python.org/) (3.x)
- [Selenium](https://selenium-python.readthedocs.io/)
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)

## Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/A-nshuman/random_search.git

2. Install the required Python packages using pip:
   ```bash
   pip install selenium

3. Download the Microsoft Edge WebDriver for your system and place it in the project directory.

4. Modify the `executable_path` in the script to point to the Edge WebDriver executable you downloaded.

## Usage

1. Run the script:
   ```bash
   python random_search.py

2. The script will open the Microsoft Edge browser and perform a series of random web searches using the provided search queries.

3. Customize the number of searches, search queries, and other settings in the script as needed.

## Configuration
You can customize the behavior of the script by adjusting the following variables in the script:

- `search_queries`: List of search queries to choose from.
- `num_searches`: The number of random searches to perform.
