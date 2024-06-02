# 🚀 Excel to CSV Converter 📊

- Made with Flask 🚀

- Solves the problem of having to convert multiple XLSX files into just one long CSV file 📂➡️📜 to have all the content together in one place. 📍

## Overview

This application provides a simple yet powerful interface for converting Excel (.xlsx) files to CSV format. It leverages Flask for web development and OpenPyXL for handling Excel files, making it a robust solution for batch processing.
Features

- **Batch Conversion**: Convert multiple.xlsx files to CSV format in one go.
- **File Upload**: Supports uploading multiple files simultaneously.
- **Output Management**: Generates a single CSV file from all uploaded.xlsx files.
- **Security**: Implements basic security measures such as file type validation.

## Getting Started

To get started with the Excel to CSV Converter API, ensure you have Python installed on your system. Then, clone this repository and navigate to its root directory. Install the required dependencies using pip:

```bash
pip install Flask openpyxl
```

Run the application:

```bash
python app.py
```

## Usage

1. **Upload Files**: Navigate to the application's homepage (http://localhost:5000/). Use the form to upload.xlsx files and specify the desired output CSV file name.
2. **Conversion Process**: Once the files are uploaded, they will be converted to CSV format and saved in the specified location.
3. **Download Output**: After conversion, download the resulting CSV file from the provided link.

## Security Note

The application uses a hardcoded secret key for simplicity. In a production environment, it's crucial to use a secure method for generating and storing the secret key.

## Contributing

Contributions are welcome Feel free to submit pull requests or report issues through the GitHub repository.

🛠️ Developed with care in Barcelona, Spain by **Gero Zayas**.
