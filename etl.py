import csv
import json

class ETL:
    def csv(self, source_file, destination_file, config):
        """
        Perform ETL (Extract, Transform, Load) on the source file.

        Args:
            source_file (str): Path to the source CSV file.
            destination_file (str): Path to the destination CSV file.
            config (dict): Configuration mapping for source and destination columns.
        """
        try:
            with open(source_file, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                rows_to_write = []
                for row in csv_reader:
                    row_data = {}
                    for source_column, column_mapping in config.items():
                        dest_column = column_mapping['mapping']
                        if source_column in row:
                            row_data[dest_column] = row[source_column]
                    rows_to_write.append(row_data)

        except FileNotFoundError:
            print(f"Source file '{source_file}' not found.")
            return

        try:
            with open(destination_file, 'w', newline='') as csv_file:
                fieldnames = list(rows_to_write[0].keys())
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(rows_to_write)

        except Exception as e:
            print(f"An error occurred during file operations: {str(e)}")
            return

        print(f"ETL process completed by ETL.csv class/method.")
        print(f"Source file: {source_file}")
        print(f"Destination file: {destination_file}")
        print(f"Mappings file:")
        print(json.dumps(config, indent=4))