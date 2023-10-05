import argparse
import yaml
from etl import ETL

def load_yaml_config(yaml_config_file):
    """
    Load the YAML configuration file.

    Args:
        yaml_config_file (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed YAML configuration.
    """
    with open(yaml_config_file, 'r') as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def main():
    parser = argparse.ArgumentParser(description="ETL Script")

    parser.add_argument("--mappings", default="EXAMPLE-mappings.yaml", help="YAML configuration file for mappings")
    parser.add_argument("--source", default="EXAMPLE-source.csv", help="Source CSV file")
    parser.add_argument("--output", default="output.csv", help="Output CSV file")

    args = parser.parse_args()

    config = load_yaml_config(args.mappings)

    etl = ETL()
    etl.csv(args.source, args.output, config)

if __name__ == "__main__":
    main()