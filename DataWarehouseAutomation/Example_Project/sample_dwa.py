"""
Sample project that uses a DataWarehouseAutomation JSON input and Jinja2 template
"""
import argparse
import json
from jinja2 import Environment, FileSystemLoader
import data_warehouse_automation
from jinja_filters import JinjaFilters

def main():
    """ Process JSON data and apply Jinja2 template
    """
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(
        description="Process JSON data and apply Jinja2 template")

    # Add command line arguments for the JSON file and Jinja2 template file
    parser.add_argument("json_file", help="Path to the JSON file")
    parser.add_argument(
        "template_file", help="Path to the Jinja2 template file")

    # Parse the command line arguments
    args = parser.parse_args()

    # Read the JSON data from the specified file
    with open(args.json_file, encoding='utf-8-sig', mode='r') as json_file:
        json_data = json.load(json_file)

    # Process the JSON data using your existing code
    dwa = data_warehouse_automation.data_warehouse_automation_from_dict(
        json_data)

    # Load the Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    env.filters['wrap'] = JinjaFilters.wrap
    env.trim_blocks = True
    env.lstrip_blocks = True
    template = env.get_template(args.template_file)

    # Render the template with the data
    rendered_output = template.render(
        data_object_mappings=dwa.data_object_mappings)

    # You can print the rendered output or save it to a file
    print(rendered_output)


if __name__ == "__main__":
    main()
