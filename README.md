# Image Processing and Cell Counting Project

## Overview
This project is designed to automate the process of subdividing large images, processing them, and performing cell counting on each subdivided section. The primary goal is to facilitate accurate counting with simple to use webtool. 

## Installation

**Prerequisites**

Before you begin, ensure you have Python 3.6 or later installed on your system. This application also requires pip for installing Python packages.

**Steps**

1. **Clone the repository:**
Open a terminal and run the following command to clone the repository.
```bash
git clone https://github.com/liamstamper/cell-counter.git
```

2. **Create a virtual environment:**
Create a virtual environment to manage the project's dependencies separately by running:
```bash
python3 -m venv venv
```

3. **Activate the virtual environment:**
* On Windows, execute:
```bash
.\venv\Scripts\activate
```
* On macOS and Linux, use:
```bash
source venv/bin/activate
```
4. **Install the required packages:**
Install all dependencies listed in `requirements.txt` by running:
```bash
pip install -r requirements.txt
```
5. **Running the application**
To start the flask application, run:
```bash
flask run
```
