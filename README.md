# Computer Automation Scripts

A collection of simple Python automation scripts for everyday tasks on my computer.

## Purpose

This repository contains small utility scripts designed to automate repetitive tasks such as:

- File organization and cleanup
- Application launching shortcuts
- System monitoring
- Clipboard utilities
- Other personal automation tasks

## Requirements

- Python 3.8 or higher
- pip (Python package manager)

Some scripts may require additional packages. Install dependencies with:

pip install -r requirements.txt

## Usage

Run any script using Python:

python scripts/script_name.py

Example:

python scripts/file_cleanup.py

## Project Structure

computer-automation/
│
├── scripts/        Main automation scripts
├── utils/          Shared helper functions
├── config/         Configuration files (optional)
├── tests/          Test files (optional)
├── requirements.txt
└── README.md

## Notes

- Do not store sensitive information such as passwords or API keys in the repository
- Use a .env file for environment variables (do not commit it)
- Add new scripts inside the scripts folder
- Place reusable code in the utils folder

## Future Improvements

- Add GUI dashboard for automation tools
- Add task scheduling support
- Improve cross-platform compatibility
- Add logging system for scripts

## License

This project is for personal use and learning purposes
