> **_NOTE:_**  the formal [Data Warehouse Automation Schema documentation](https://data-solution-automation-engine.github.io/data-warehouse-automation-metadata-schema/) is now available on Github pages.

> **_NOTE:_** this is a fork of the original project using Python and Jinja2 templates. 
---

# Generation Metadata Schema for Data Warehouse Automation

#### Intent

To provide a collaborative space to discuss an exchange format concerning ETL generation metadata, supporting Data Warehouse Automation. This adapter should contain all metadata necessary to generate the transformation logic for a Data Warehouse solution.

_This fork of the [original project](https://github.com/data-solution-automation-engine/data-warehouse-automation-metadata-schema) is using Python instead of C# and Jinja2 instead of HandleBars_.

#### Links / structure

The following directories have been set up:

* Generic interface, containing the Json schema definition (only from version 2.0 onwards in this fork). 
* Class Library (DataWarehouseAutomation) containing the object model for deserialisation, as well as various utility classes such as validation of files against the Json schema definition.
* Code examples (examples_jinja), containing Python examples using the generic interface for various purposes.
