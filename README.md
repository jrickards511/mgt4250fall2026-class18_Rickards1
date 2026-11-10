# MGT 4250 Fall 2026 - Class 18

This repository contains a Streamlit dashboard for exploring and visualizing retail sales data from a Superstore dataset. The project was created for a class assignment and focuses on reporting key business metrics such as sales, profit, and profit margin across regions and product categories.

## Project Overview

The app loads a sample Excel workbook and presents:

- A preview of the dataset
- U.S. state-level profit margin analysis
- Category-level profit margin comparisons
- Sales treemap by category and sub-category
- State filtering controls for interactive exploration

## Files in This Repository

- `class17.py` – main Streamlit application
- `requirements.txt` – Python dependencies
- `sample_-_superstore (2).xls` – sample Superstore dataset
- `README.md` – project documentation

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- OpenPyXL
- xlrd

## Setup

1. Clone the repository.
2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# or
.venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
streamlit run class17.py
```

## Notes

- The application reads the Excel file from the repository root.
- The dashboard is designed for a wide layout and includes interactive visualizations for better data exploration.
- The dataset is a sample retail dataset used for classroom analysis and dashboard design.

## License

This project is intended for academic use and does not include a formal license unless otherwise specified by the course or instructor.
