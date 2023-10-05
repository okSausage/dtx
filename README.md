# ETL Script

This script performs an ETL (Extract, Transform, Load) process on a CSV file using a YAML configuration file for mappings.

## Prerequisites

- Python 3.x
- Required Python packages (specified in `requirements.txt`)

## Installation

1. Clone the repository.
2. Install the required packages by running the following command:
    `pip install -r requirements.txt`
## Usage

Run the script with the following command:

Optional arguments:

- `--mappings MAPPINGS` (default: `mappings.yaml`): Path to the YAML configuration file for mappings.
- `--source SOURCE` (default: `EXAMPLE-source.csv`): Path to the source CSV file.
- `--output OUTPUT` (default: `output.csv`): Path to the output CSV file.

## Configuration

The mappings for the ETL process are specified in a YAML configuration file. By default, the script expects the file to be named `mappings.yaml`. Make sure to update this file according to your specific mappings.

## License

This project is licensed under the [MIT License](LICENSE).