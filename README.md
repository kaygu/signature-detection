# Signature Detection

This use-case project is provided by *Business & Decision*. In this project, we have to devlop an AI model to detect and locate a signature in a document

**Success criterias:**  
*...*

----------

## Project Guidelines

- Repository: `signature-detection`
- Type of Challenge: `Use-case`
- Duration: `2 weeks`
- Deadline: `22/10/2021`
- Team Challenge : `Solo`

----------

## Data

The dataset provided for this project contains a train set of documents associated with XML files containing informations about Signatures positions. And a test folder containing documents <u>without</u> XML files

----------

## Prerequisites

- **Python 3.8+**

## Installation

```bash
git clone git@github.com:kaygu/signature-detection.git 
cd signature-detection
pip install -r requirements.txt 
```

## Usage

```bash
python main.py
```

## Docker

Build

```bash
docker build -t signature_detection:latest .
```

Run

```bash
docker run -p 8501:8501 signature_detection:latest
```

## Contributors

- [Camille De Neef](https://github.com/kaygu)
