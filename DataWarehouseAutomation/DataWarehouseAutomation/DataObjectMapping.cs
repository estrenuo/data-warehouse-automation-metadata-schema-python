﻿namespace DataWarehouseAutomation;

/// <summary>
/// The mapping between a source and target data set / table / file.
/// 
/// The DataObjectMapping is the element that defines an individual source-to-target mapping / ETL process. It is a mapping between a source and target object - referred to as DataObjects.
/// The DataObject is in fact a reusable definition in the Json schema.
///
/// This definition is used twice in the DataObjectMapping: as the *SourceDataObject* and as the *TargetDataObject* - both instances of the DataObject class / type.
///
/// The other key component of a DataObjectMapping is the* DataItemMapping*, which describes the column-to-column(or transformation-to-column).
/// The SourceDataObject, TargetDataObject and DataItemMapping are the mandatory components of a DataObjectMapping.There are many other attributes that can be set, and there are mandatory items within the DataObjects and DataItems.These are all described in the Json schema.
/// </summary>
public class DataObjectMapping : IMetadata
{
    #region Properties
    /// <summary>
    /// An optional unique identifier for the Data Object mapping.
    /// </summary>
    [JsonPropertyName("id")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public string? Id { get; set; }

    /// <summary>
    /// The name of the Data Object Mapping. Ideally an unique name that identifies the individual mapping.
    /// </summary>
    [JsonPropertyName("name")]
    [JsonIgnore(Condition = JsonIgnoreCondition.Never)]
    public string Name { get; set; } = "NewDataMappingName";

    /// <summary>
    /// Free-form and optional classification for the mapping for use in data logistics generation logic (evaluation).
    /// </summary>
    [JsonPropertyName("classifications")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public List<DataClassification>? Classifications { get; set; }

    /// <summary>
    /// The source object(s) of the mapping. This can either be an object or a query.
    /// Potentially multiple source objects can be mapped to a single target object.
    /// </summary>
    [JsonPropertyName("sourceDataObjects")]
    public List<IDataObject> SourceDataObjects { get; set; } = new();

    /// <summary>
    /// The target object of the mapping. This is always a Data Object type.
    /// </summary>
    [JsonPropertyName("targetDataObject")]
    public DataObject TargetDataObject { get; set; } = new() { Name = "NewTargetDataObject" };

    /// <summary>
    /// The collection of associated data object for purposes other than source-target relationship.
    /// For example for lookups, merge joins, lineage etc.
    /// </summary>
    [JsonPropertyName("relatedDataObjects")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public List<DataObject>? RelatedDataObjects { get; set; }

    /// <summary>
    /// The collection of individual attribute (column or query) mappings.
    /// </summary>
    [JsonPropertyName("dataItemMappings")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public List<DataItemMapping>? DataItemMappings { get; set; }

    /// <summary>
    /// The definition of the Business Key(s) for the Data Object Mapping.
    /// </summary>
    [JsonPropertyName("businessKeyDefinitions")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public List<BusinessKeyDefinition>? BusinessKeyDefinitions { get; set; }

    /// <summary>
    /// Any filtering that needs to be applied to the source-to-target mapping.
    /// </summary>
    [JsonPropertyName("filterCriterion")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public string? FilterCriterion { get; set; }

    /// <summary>
    /// An indicator (boolean) which can capture enabling / disabling of (the usage of) an individual source-to-target mapping.
    /// </summary>
    [JsonPropertyName("enabled")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public bool? Enabled { get; set; }

    /// <summary>
    /// The collection of extension Key/Value pairs.
    /// </summary>
    [JsonPropertyName("extensions")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public List<Extension>? Extensions { get; set; }

    /// <summary>
    /// Free-format notes on the Data Object Mapping.
    /// </summary>
    [JsonPropertyName("notes")]
    [JsonIgnore(Condition = JsonIgnoreCondition.WhenWritingDefault)]
    public string? Notes { get; set; }
    #endregion

    #region Methods
    /// <summary>
    /// Use this method to assert if two Data Object Mappings are the same, based on their Ids.
    /// </summary>
    /// <param name="obj"></param>
    /// <returns>True if the Data Object Mappings are the same, based on their Ids</returns>
    public override bool Equals(object? obj)
    {
        var other = obj as DataObjectMapping;
        return other?.Id == Id;
    }

    /// <summary>
    /// Override to get a hash value that represents the identifier.
    /// </summary>
    /// <returns>A 32-bit signed integer hash code</returns>
    public override int GetHashCode() => (Id?.GetHashCode()) ?? 0;

    /// <summary>
    /// String override so that the object returns its value ('Name').
    /// When an instance of this class is passed to a method that expects a string, the ToString() method will be called implicitly to convert the object to a string, and the value of the "Name" property will be returned.
    /// </summary>
    /// <returns>The Name</returns>
    public override string ToString()
    {
        return Name;
    }
    #endregion
}