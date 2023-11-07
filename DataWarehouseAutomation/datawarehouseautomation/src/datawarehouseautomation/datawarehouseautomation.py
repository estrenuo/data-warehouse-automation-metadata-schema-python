"""Here a description of the Data Warehouse Automation module is needed"""
from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast

T = TypeVar("T")

def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x

def from_none(x: Any) -> Any:
    assert x is None
    return x

def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False

def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]

def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()

def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x

def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x

@dataclass
class Extension:
    """Free-format key/value pair that can be used for additional context."""
    # The Key in a Key/Value pair
    key: str
    # Any additional information
    description: Optional[str] = None
    # Optional unique identifier for an extension
    id: Optional[str] = None
    # The Value in a Key/Value pair
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Extension':
        assert isinstance(obj, dict)
        key = from_str(obj.get("key"))
        description = from_union([from_str, from_none], obj.get("description"))
        id = from_union([from_none, from_str], obj.get("id"))
        value = from_union([from_str, from_none], obj.get("value"))
        return Extension(key, description, id, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["key"] = from_str(self.key)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        if self.value is not None:
            result["value"] = from_union([from_str, from_none], self.value)
        return result

@dataclass
class DataClassification:
    """Classification for the source-to-target mapping (free form), used to add various tags and
    notes if required.
    """
    # A free-form name that adds documentation / classification to an object
    classification: str
    # An optional unique identifier for the classification, for sorting or identification purposes
    id: Optional[str] = None
    # Any additional information to be added to the classification
    notes: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataClassification':
        assert isinstance(obj, dict)
        classification = from_str(obj.get("classification"))
        id = from_union([from_none, from_str], obj.get("id"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        return DataClassification(classification, id, notes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["classification"] = from_str(self.classification)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        if self.notes is not None:
            result["notes"] = from_union([from_str, from_none], self.notes)
        return result

@dataclass
class DataConnectionClass:
    """Classification for the Data Item Query."""
    classifications: Optional[List[DataClassification]] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """An optional identifier."""
    id: Optional[str] = None
    """A connection token, key or string"""
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataConnectionClass':
        assert isinstance(obj, dict)
        classifications = from_union([from_none,
                            lambda x: from_list(DataClassification.from_dict,
                            x)],obj.get("classifications"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)],
                                obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        name = from_union([from_none, from_str], obj.get("name"))
        return DataConnectionClass(classifications, description, extensions, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        result["name"] = from_union([from_none, from_str], self.name)
        return result

@dataclass
class TargetDataItemElement:
    """The generic definition of a column. A column, attribute or item in a dataObject
    
    The target item of the mapping.
    """
    """Unique name which identifies the column / attribute."""
    name: str
    """Optional. Length of the item in case it is text."""
    character_length: Optional[int] = None
    """Classification for the dataObject (free form)."""
    classifications: Optional[List[DataClassification]] = None
    """The data object of the data item, which may be required when the data item is used in a
    data item mapping context.
    """
    data_object: Optional['DataObjectClass'] = None
    """Data type of the Data Item."""
    data_type: Optional[str] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """An optional identifier."""
    id: Optional[str] = None
    """Boolean value indicating if the item is a Primary Key."""
    is_primary_key: Optional[bool] = None
    """The number of digits in a numeric value (number)."""
    numeric_precision: Optional[int] = None
    """The number of digits to the right of the decimal point."""
    numeric_scale: Optional[int] = None
    """Optional. The position of items in the data object."""
    ordinal_position: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TargetDataItemElement':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        character_length = from_union([from_none, from_int], obj.get("characterLength"))
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        data_object = from_union([DataObjectClass.from_dict, from_none], obj.get("dataObject"))
        data_type = from_union([from_none, from_str], obj.get("dataType"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        is_primary_key = from_union([from_none, from_bool], obj.get("isPrimaryKey"))
        numeric_precision = from_union([from_none, from_int], obj.get("numericPrecision"))
        numeric_scale = from_union([from_none, from_int], obj.get("numericScale"))
        ordinal_position = from_union([from_none, from_int], obj.get("ordinalPosition"))
        return TargetDataItemElement(name, character_length, classifications,
                                    data_object, data_type, description, extensions,
                                    id, is_primary_key, numeric_precision, numeric_scale,
                                    ordinal_position)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        if self.character_length is not None:
            result["characterLength"] = from_union([from_none, from_int], self.character_length)
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.data_object is not None:
            result["dataObject"] = from_union([lambda x: to_class(DataObjectClass, x), from_none], self.data_object)
        if self.data_type is not None:
            result["dataType"] = from_union([from_none, from_str], self.data_type)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        if self.is_primary_key is not None:
            result["isPrimaryKey"] = from_union([from_none, from_bool], self.is_primary_key)
        if self.numeric_precision is not None:
            result["numericPrecision"] = from_union([from_none, from_int], self.numeric_precision)
        if self.numeric_scale is not None:
            result["numericScale"] = from_union([from_none, from_int], self.numeric_scale)
        if self.ordinal_position is not None:
            result["ordinalPosition"] = from_union([from_none, from_int], self.ordinal_position)
        return result

@dataclass
class DataObjectClass:
    """The data object of the data item, which may be required when the data item is used in a
    data item mapping context.
    
    The generic table of file definition. Any kind of entity, i.e. data set, query, object,
    file or table.
    
    The target object of the mapping. This is always a Data Object type.
    """
    """Mandatory unique name of the file/table."""
    name: str
    """Classification for the Data Object (free form)."""
    classifications: Optional[List[DataClassification]] = None
    """Data Connection"""
    data_connection: Optional[DataConnectionClass] = None
    """Collection of dataItems for a table or file. Elements that define the dat set."""
    data_items: Optional[List[TargetDataItemElement]] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """Optional unique identifier for a file/table."""
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataObjectClass':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        data_connection = from_union([from_none, DataConnectionClass.from_dict], obj.get("dataConnection"))
        data_items = from_union([from_none, lambda x: from_list(TargetDataItemElement.from_dict, x)], obj.get("dataItems"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        return DataObjectClass(name, classifications, data_connection, data_items, description, extensions, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.data_connection is not None:
            result["dataConnection"] = from_union([from_none, lambda x: to_class(DataConnectionClass, x)], self.data_connection)
        if self.data_items is not None:
            result["dataItems"] = from_union([from_none, lambda x: from_list(lambda x: to_class(TargetDataItemElement, x), x)], self.data_items)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        return result

@dataclass
class TheIndividualValueQueryOrAttributeWithinADataObject:
    """The generic definition of a column. A column, attribute or item in a dataObject
    
    The target item of the mapping.
    
    A concise piece of transformation or logic at Data Item level e.g. a query which can act
    as a source for a dataItem.
    """
    """Optional. Length of the item in case it is text."""
    character_length: Optional[int] = None
    """Classification for the dataObject (free form).
    
    Classification for the Data Item Query.
    """
    classifications: Optional[List[DataClassification]] = None
    """The data object of the data item, which may be required when the data item is used in a
    data item mapping context.
    """
    data_object: Optional[DataObjectClass] = None
    """Data type of the Data Item."""
    data_type: Optional[str] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """An optional identifier.
    
    Optional unique identifier for a Data Item Query.
    """
    id: Optional[str] = None
    """Boolean value indicating if the item is a Primary Key."""
    is_primary_key: Optional[bool] = None
    """Unique name which identifies the column / attribute.
    
    An optional name for the query
    """
    name: Optional[str] = None
    """The number of digits in a numeric value (number)."""
    numeric_precision: Optional[int] = None
    """The number of digits to the right of the decimal point."""
    numeric_scale: Optional[int] = None
    """Optional. The position of items in the data object.
    
    Optional. The position in the data object.
    """
    ordinal_position: Optional[int] = None
    """The code that constitutes the query."""
    query_code: Optional[str] = None
    """The language that the code was written in (e.g. SQL)."""
    query_language: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TheIndividualValueQueryOrAttributeWithinADataObject':
        assert isinstance(obj, dict)
        character_length = from_union([from_none, from_int], obj.get("characterLength"))
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        data_object = from_union([DataObjectClass.from_dict, from_none], obj.get("dataObject"))
        data_type = from_union([from_none, from_str], obj.get("dataType"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        is_primary_key = from_union([from_none, from_bool], obj.get("isPrimaryKey"))
        name = from_union([from_str, from_none], obj.get("name"))
        numeric_precision = from_union([from_none, from_int], obj.get("numericPrecision"))
        numeric_scale = from_union([from_none, from_int], obj.get("numericScale"))
        ordinal_position = from_union([from_none, from_int], obj.get("ordinalPosition"))
        query_code = from_union([from_str, from_none], obj.get("queryCode"))
        query_language = from_union([from_str, from_none], obj.get("queryLanguage"))
        return TheIndividualValueQueryOrAttributeWithinADataObject(character_length, classifications, data_object, data_type, description, extensions, id, is_primary_key, name, numeric_precision, numeric_scale, ordinal_position, query_code, query_language)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.character_length is not None:
            result["characterLength"] = from_union([from_none, from_int], self.character_length)
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.data_object is not None:
            result["dataObject"] = from_union([lambda x: to_class(DataObjectClass, x), from_none], self.data_object)
        if self.data_type is not None:
            result["dataType"] = from_union([from_none, from_str], self.data_type)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        if self.is_primary_key is not None:
            result["isPrimaryKey"] = from_union([from_none, from_bool], self.is_primary_key)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.numeric_precision is not None:
            result["numericPrecision"] = from_union([from_none, from_int], self.numeric_precision)
        if self.numeric_scale is not None:
            result["numericScale"] = from_union([from_none, from_int], self.numeric_scale)
        if self.ordinal_position is not None:
            result["ordinalPosition"] = from_union([from_none, from_int], self.ordinal_position)
        if self.query_code is not None:
            result["queryCode"] = from_union([from_str, from_none], self.query_code)
        if self.query_language is not None:
            result["queryLanguage"] = from_union([from_str, from_none], self.query_language)
        return result

@dataclass
class TheIndividualMappingsBetweenDataItems:
    """A mapping between a source and a target columns or attributes"""
    """The target item of the mapping."""
    target_data_item: TargetDataItemElement
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """An optional identifier."""
    id: Optional[str] = None
    """The source item of the mapping. This can either be an column or a query."""
    source_data_items: Optional[List[TheIndividualValueQueryOrAttributeWithinADataObject]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TheIndividualMappingsBetweenDataItems':
        assert isinstance(obj, dict)
        target_data_item = TargetDataItemElement.from_dict(obj.get("targetDataItem"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        source_data_items = from_union([from_none, lambda x: from_list(TheIndividualValueQueryOrAttributeWithinADataObject.from_dict, x)], obj.get("sourceDataItems"))
        return TheIndividualMappingsBetweenDataItems(target_data_item, extensions, id, source_data_items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["targetDataItem"] = to_class(TargetDataItemElement, self.target_data_item)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        result["sourceDataItems"] = from_union([from_none, lambda x: from_list(lambda x: to_class(TheIndividualValueQueryOrAttributeWithinADataObject, x), x)], self.source_data_items)
        return result

@dataclass
class TheDefinitionOfTheBusinessKey:
    """The generic definition of business key."""
    business_key_component_mapping: Any
    """Items that define the Business Key e.g. the collection of columns for a Business Key."""
    business_key_component_mappings: Optional[List[TheIndividualMappingsBetweenDataItems]] = None
    """Classification for the dataObject (free form)."""
    classification: Optional[List[DataClassification]] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """An optional identifier."""
    id: Optional[str] = None
    """An optional label for the end result e.g. the target business key attribute."""
    surrogate_key: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TheDefinitionOfTheBusinessKey':
        assert isinstance(obj, dict)
        business_key_component_mapping = obj.get("businessKeyComponentMapping")
        business_key_component_mappings = from_union([lambda x: from_list(TheIndividualMappingsBetweenDataItems.from_dict, x), from_none], obj.get("businessKeyComponentMappings"))
        classification = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classification"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        surrogate_key = from_union([from_none, from_str], obj.get("surrogateKey"))
        return TheDefinitionOfTheBusinessKey(business_key_component_mapping, business_key_component_mappings, classification, description, extensions, id, surrogate_key)

    def to_dict(self) -> dict:
        result: dict = {}
        result["businessKeyComponentMapping"] = self.business_key_component_mapping
        if self.business_key_component_mappings is not None:
            result["businessKeyComponentMappings"] = from_union([lambda x: from_list(lambda x: to_class(TheIndividualMappingsBetweenDataItems, x), x), from_none], self.business_key_component_mappings)
        if self.classification is not None:
            result["classification"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classification)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        if self.surrogate_key is not None:
            result["surrogateKey"] = from_union([from_none, from_str], self.surrogate_key)
        return result

@dataclass
class TargetDataObjectElement:
    """The data object of the data item, which may be required when the data item is used in a
    data item mapping context.
    
    The generic table of file definition. Any kind of entity, i.e. data set, query, object,
    file or table.
    
    The target object of the mapping. This is always a Data Object type.
    """
    """Mandatory unique name of the file/table."""
    name: str
    """Classification for the Data Object (free form)."""
    classifications: Optional[List[DataClassification]] = None
    """Data Connection"""
    data_connection: Optional[DataConnectionClass] = None
    """Collection of dataItems for a table or file. Elements that define the dat set."""
    data_items: Optional[List[TargetDataItemElement]] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """Optional unique identifier for a file/table."""
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TargetDataObjectElement':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        data_connection = from_union([from_none, DataConnectionClass.from_dict], obj.get("dataConnection"))
        data_items = from_union([from_none, lambda x: from_list(TargetDataItemElement.from_dict, x)], obj.get("dataItems"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        return TargetDataObjectElement(name, classifications, data_connection, data_items, description, extensions, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.data_connection is not None:
            result["dataConnection"] = from_union([from_none, lambda x: to_class(DataConnectionClass, x)], self.data_connection)
        if self.data_items is not None:
            result["dataItems"] = from_union([from_none, lambda x: from_list(lambda x: to_class(TargetDataItemElement, x), x)], self.data_items)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        return result

@dataclass
class SourceDataObjectDataConnection:
    """Classification for the Data Item Query."""
    classifications: Optional[List[DataClassification]] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """An optional identifier."""
    id: Optional[str] = None
    """A connection token, key or string"""
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SourceDataObjectDataConnection':
        assert isinstance(obj, dict)
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        name = from_union([from_none, from_str], obj.get("name"))
        return SourceDataObjectDataConnection(classifications, description, extensions, id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        result["name"] = from_union([from_none, from_str], self.name)
        return result

@dataclass
class DataObject:
    """The data object of the data item, which may be required when the data item is used in a
    data item mapping context.
    
    The generic table of file definition. Any kind of entity, i.e. data set, query, object,
    file or table.
    
    The target object of the mapping. This is always a Data Object type.
    
    A concise piece of transformation or logic at Data Object level e.g. a query which can
    act as a source in a Data Object Mapping.
    """
    """Classification for the Data Object (free form).
    
    Classification for the Data Item Query.
    """
    classifications: Optional[List[DataClassification]] = None
    """Data Connection"""
    data_connection: Optional[SourceDataObjectDataConnection] = None
    """Collection of dataItems for a table or file. Elements that define the dat set."""
    data_items: Optional[List[TargetDataItemElement]] = None
    """Any additional information."""
    description: Optional[str] = None
    """Key/Value pair extension object."""
    extensions: Optional[List[Extension]] = None
    """Optional unique identifier for a file/table.
    
    Optional unique identifier for a Data Object Query
    """
    id: Optional[str] = None
    """Mandatory unique name of the file/table.
    
    An optional name for the query
    """
    name: Optional[str] = None
    """The code that constitutes the query."""
    query_code: Optional[str] = None
    """The language that the code was written in (e.g. SQL)."""
    query_language: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataObject':
        assert isinstance(obj, dict)
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        data_connection = from_union([from_none, SourceDataObjectDataConnection.from_dict], obj.get("dataConnection"))
        data_items = from_union([from_none, lambda x: from_list(TargetDataItemElement.from_dict, x)], obj.get("dataItems"))
        description = from_union([from_str, from_none], obj.get("description"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        id = from_union([from_none, from_str], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        query_code = from_union([from_str, from_none], obj.get("queryCode"))
        query_language = from_union([from_str, from_none], obj.get("queryLanguage"))
        return DataObject(classifications, data_connection, data_items, description, extensions, id, name, query_code, query_language)

    def to_dict(self) -> dict:
        result: dict = {}
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.data_connection is not None:
            result["dataConnection"] = from_union([from_none, lambda x: to_class(SourceDataObjectDataConnection, x)], self.data_connection)
        if self.data_items is not None:
            result["dataItems"] = from_union([from_none, lambda x: from_list(lambda x: to_class(TargetDataItemElement, x), x)], self.data_items)
        if self.description is not None:
            result["description"] = from_union([from_str, from_none], self.description)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.query_code is not None:
            result["queryCode"] = from_union([from_str, from_none], self.query_code)
        if self.query_language is not None:
            result["queryLanguage"] = from_union([from_str, from_none], self.query_language)
        return result

@dataclass
class DataObjectMapping:
    """The list (array) of source-to-target mappings between Data Objects. This is the top-level
    object that contains one or more data object mappings.
    
    An individual mapping between a source data object and a target data object.
    """
    """The target object of the mapping. This is always a Data Object type."""
    target_data_object: TargetDataObjectElement
    """The definition of the Business Key(s) for the Data Object Mapping."""
    business_key_definitions: Optional[List[TheDefinitionOfTheBusinessKey]] = None
    """Classification for the Data Object Mapping."""
    classifications: Optional[List[DataClassification]] = None
    """The collection of individual attribute (column or query) mappings."""
    data_item_mappings: Optional[List[TheIndividualMappingsBetweenDataItems]] = None
    """An indicator (boolean) which can capture enabling / disabling of (the usage of) an
    individual source-to-target mapping.
    """
    enabled: Optional[bool] = None
    """The collection of extension Key/Value pairs."""
    extensions: Optional[List[Extension]] = None
    """Any filtering that needs to be applied to the Data Object Mapping."""
    filter_criterion: Optional[str] = None
    """An optional unique identifier for a Data Object Mapping."""
    id: Optional[str] = None
    """Unique name which identifies the mapping."""
    name: Optional[str] = None
    """Any additional information to be added to the Data Object Mapping."""
    notes: Optional[str] = None
    """The collection of associated data object for purposes other than source-target
    relationship. For example for lookups, merge joins, lineage.
    """
    related_data_objects: Optional[List[TargetDataObjectElement]] = None
    """The source object of the mapping. This can either be an object or a query."""
    source_data_objects: Optional[List[DataObject]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataObjectMapping':
        assert isinstance(obj, dict)
        target_data_object = TargetDataObjectElement.from_dict(obj.get("targetDataObject"))
        business_key_definitions = from_union([from_none, lambda x: from_list(TheDefinitionOfTheBusinessKey.from_dict, x)], obj.get("businessKeyDefinitions"))
        classifications = from_union([from_none, lambda x: from_list(DataClassification.from_dict, x)], obj.get("classifications"))
        data_item_mappings = from_union([lambda x: from_list(TheIndividualMappingsBetweenDataItems.from_dict, x), from_none], obj.get("dataItemMappings"))
        enabled = from_union([from_none, from_bool], obj.get("enabled"))
        extensions = from_union([from_none, lambda x: from_list(Extension.from_dict, x)], obj.get("extensions"))
        filter_criterion = from_union([from_none, from_str], obj.get("filterCriterion"))
        id = from_union([from_none, from_str], obj.get("id"))
        name = from_union([from_none, from_str], obj.get("name"))
        notes = from_union([from_str, from_none], obj.get("notes"))
        related_data_objects = from_union([from_none, lambda x: from_list(TargetDataObjectElement.from_dict, x)], obj.get("relatedDataObjects"))
        source_data_objects = from_union([from_none, lambda x: from_list(DataObject.from_dict, x)], obj.get("sourceDataObjects"))
        return DataObjectMapping(target_data_object, business_key_definitions, classifications, data_item_mappings, enabled, extensions, filter_criterion, id, name, notes, related_data_objects, source_data_objects)

    def to_dict(self) -> dict:
        result: dict = {}
        result["targetDataObject"] = to_class(TargetDataObjectElement, self.target_data_object)
        if self.business_key_definitions is not None:
            result["businessKeyDefinitions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(TheDefinitionOfTheBusinessKey, x), x)], self.business_key_definitions)
        if self.classifications is not None:
            result["classifications"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataClassification, x), x)], self.classifications)
        if self.data_item_mappings is not None:
            result["dataItemMappings"] = from_union([lambda x: from_list(lambda x: to_class(TheIndividualMappingsBetweenDataItems, x), x), from_none], self.data_item_mappings)
        if self.enabled is not None:
            result["enabled"] = from_union([from_none, from_bool], self.enabled)
        if self.extensions is not None:
            result["extensions"] = from_union([from_none, lambda x: from_list(lambda x: to_class(Extension, x), x)], self.extensions)
        if self.filter_criterion is not None:
            result["filterCriterion"] = from_union([from_none, from_str], self.filter_criterion)
        if self.id is not None:
            result["id"] = from_union([from_none, from_str], self.id)
        result["name"] = from_union([from_none, from_str], self.name)
        if self.notes is not None:
            result["notes"] = from_union([from_str, from_none], self.notes)
        if self.related_data_objects is not None:
            result["relatedDataObjects"] = from_union([from_none, lambda x: from_list(lambda x: to_class(TargetDataObjectElement, x), x)], self.related_data_objects)
        result["sourceDataObjects"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataObject, x), x)], self.source_data_objects)
        return result

@dataclass
class DataWarehouseAutomation:
    """Standardized format for the required metadata to generate data logistics (ETL) and object
    creation (DDL) for Data Solutions such as a Data Warehouse or Data Lake. The intent is to
    separate / decouple how individual software stores Data Warehouse Automation metadata and
    how this metadata can be exposed to other components, technologies and solutions for data
    processing and data structure generation.
    """
    data_object_mappings: Optional[List[DataObjectMapping]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DataWarehouseAutomation':
        assert isinstance(obj, dict)
        data_object_mappings = from_union([from_none, lambda x: from_list(DataObjectMapping.from_dict, x)], obj.get("dataObjectMappings"))
        return DataWarehouseAutomation(data_object_mappings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dataObjectMappings"] = from_union([from_none, lambda x: from_list(lambda x: to_class(DataObjectMapping, x), x)], self.data_object_mappings)
        return result

def data_warehouse_automation_from_dict(s: Any) -> DataWarehouseAutomation:
    return DataWarehouseAutomation.from_dict(s)

def data_warehouse_automation_to_dict(x: DataWarehouseAutomation) -> Any:
    return to_class(DataWarehouseAutomation, x)
