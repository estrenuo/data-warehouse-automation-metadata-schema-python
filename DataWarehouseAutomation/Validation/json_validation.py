""" Validate the JSON data mapping file against the GenericInterface JSON schema
"""
import argparse
import json
import jsonschema

# Create an ArgumentParser object
parser = argparse.ArgumentParser(
description="Validate JSON data against JSON schema")

# Add command line arguments for the JSON schema and data
parser.add_argument("schema_file", help="Path to the JSON schema")
parser.add_argument("json_file", help="Path to the JSON data")

# Parse the command line arguments
args = parser.parse_args()

# Read the JSON schema from the specified file
with open(args.schema_file, encoding='utf-8-sig', mode='r') as schema_file:
    schema = json.load(schema_file)

# Read the JSON data from the specified file
with open(args.json_file, encoding='utf-8-sig', mode='r') as json_file:
    data = json.load(json_file)

try:
    # Validate the JSON data against the schema
    jsonschema.validate(data, schema)
    print("JSON data is valid according to the schema.")
except jsonschema.exceptions.ValidationError as e:
    print(f"JSON data is not valid. Details: {e}")
