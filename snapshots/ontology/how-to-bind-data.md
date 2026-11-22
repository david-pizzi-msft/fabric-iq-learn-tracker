---
title: "Data binding in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-bind-data) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Data binding in ontology (preview)

Summarize this article for me

Data binding in ontology (preview) connects the schema of entity types, relationship types, and properties to concrete data sources that drive enterprise operations and analytics.

Important

This feature is in [preview](../../fundamentals/preview).

By using data binding, you can:

- Integrate data into a semantic layer without copying source data
- Enrich entity types with up-to-date contextual information from batch and real-time sources
- Provide a semantic backbone for AI agents and automation to support reasoning, decision-making, and actions across the enterprise

## Prerequisites

Before binding data to your ontology, make sure you have the following prerequisites:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Users can create ontology (preview) items** and **Users can create Fabric items** [enabled on your Fabric tenant](overview-tenant-settings).
- An ontology (preview) item with [entity types](how-to-bind-data) created.
- Data that you prepared according to these guidelines:
  - The data is organized and has gone through any necessary ETL required by your business. It contains all the information required to model it. For more information, see [Core concept: Data binding](overview#data-binding).
  - The data is in Microsoft Fabric. Supported sources include eventhouse, KQL database, lakehouse, mirrored database, semantic model, SQL database, or warehouse.
    - For semantic models, you need both [Read and Build permissions](/en-us/power-bi/connect-data/service-datasets-permissions#what-are-the-semantic-model-permissions) to bind the data to an ontology.

## Add data binding

1. You can start a data binding from either the Home configuration canvas or the **Configure** tab of the entity type details.

   On the Home configuration canvas, select **...** next to an entity type name to open its options menu and select **Bind data**.

   [![Screenshot of starting a data binding from the configuration canvas.](media/how-to-bind-data/bind-data-canvas.png)](media/how-to-bind-data/bind-data-canvas.png#lightbox)

   On the **Configure** page, select **Bind data**. You can also select **Add properties from data** if the entity type has no properties yet.

   [![Screenshot of adding a new data binding to the entity type.](media/how-to-bind-data/bind-data-add.png)](media/how-to-bind-data/bind-data-add.png#lightbox)
2. The **Bind data** page opens. Select the plus (**+**) button next to **Data sources**, and then select **OneLake catalog**.

   [![Screenshot of adding a data source.](media/how-to-bind-data/add-data-source.png)](media/how-to-bind-data/add-data-source.png#lightbox)
3. Select your data source table from the OneLake catalog, and then select **Select**. For a schema-enabled lakehouse, expand the lakehouse, **Schemas**, and the schema that contains your table.

   [![Screenshot of the data source selection.](media/how-to-bind-data/bind-data-select-table.png)](media/how-to-bind-data/bind-data-select-table.png#lightbox)
4. The data source loads.

   [![Screenshot of the data source after it is loaded.](media/how-to-bind-data/data-source-loaded.png)](media/how-to-bind-data/data-source-loaded.png#lightbox)
5. Select **Properties** under **Entity type**. The columns from the source table automatically populate as proposed properties on the **Bind data: Properties** page.

   [![Screenshot of the populated properties.](media/how-to-bind-data/entity-type-properties.png)](media/how-to-bind-data/entity-type-properties.png#lightbox)
6. Add, rename, or delete properties as needed. Property names can match the source column names or be different. To reuse an existing property, select its name from the property name dropdown menu.
7. When you finish configuring properties, select **Create** to save the data binding and return to the **Configure** page.
8. In the **Configure** page, verify the bindings by reviewing the properties in the **Properties** pane and confirming that they're bound to the correct data sources.

   [![Screenshot of the data bindings in the Configure page.](media/how-to-bind-data/bind-data-complete.png)](media/how-to-bind-data/bind-data-complete.png#lightbox)

### Add more data bindings

Follow these steps to add more bindings after the first binding is created.

1. On the **Configure** page, select **Bind data** to reopen the binding configuration.
2. Select the plus (**+**) button next to **Data sources**, and then select **OneLake catalog**. Choose your data table, and then select **Select**. The system adds the new data source as a secondary data source.
3. In **Relationship with primary data source**, select the common column from each table to link the secondary source to the primary source.

   [![Screenshot of defining the data source relationship.](media/how-to-bind-data/bind-data-time-series-relationship.png)](media/how-to-bind-data/bind-data-time-series-relationship.png#lightbox)
4. Select **Properties** to review the proposed properties from the new source alongside the existing properties. Check the property names, source columns, and property types, and make any changes you need.

   [![Screenshot of reviewing properties from primary and secondary data sources before saving.](media/how-to-bind-data/bind-data-time-series-complete.png)](media/how-to-bind-data/bind-data-time-series-complete.png#lightbox)
5. Select **Save**. On the **Configure** page, verify the properties and their data source bindings.

## Edit or delete data binding

To edit or delete data bindings, start on the **Configure** page and select **Bind data**.

[![Screenshot of the manage bindings options.](media/how-to-bind-data/manage-bindings.png)](media/how-to-bind-data/manage-bindings.png#lightbox)

The configuration page reopens, where you can edit binding details or delete binding data sources.

Note

To see updates from upstream data sources, such as new rows, you need to manually refresh the ontology item. For more information, see [refresh the graph model](how-to-use-ontology-graph#refresh-the-graph-model).

## Supported data source types

The following data source types support data binding in ontology (preview):

- Eventhouse
- KQL database
- Lakehouse
- Mirrored database
- Semantic model
- SQL database
- Warehouse

[![Screenshot of the data source types in the OneLake catalog.](media/how-to-bind-data/source-types.png)](media/how-to-bind-data/source-types.png#lightbox)

## Supported property types

The following table lists the supported property types for data that you can bind to properties in ontology (preview).

| Ontology property value type | Supported lakehouse types | Supported eventhouse types |
| --- | --- | --- |
| integer | tinyint, smallint, bigint, integer, long, short | int, long |
| boolean | boolean | bool |
| datetime | datetime, date, timestamp | datetime |
| double | double, decimal, float | decimal, real |
| string | char, decimal(p, s), string, array, binary, binary16, byte, map, object, struct, timestampint64, timestamp\_ntz | dynamic, string, guid, timespan |

The following table shows supported source column value types that you can use for the timestamp selection in a time series binding.

| Ontology configuration | Lakehouse and eventhouse source column value type |
| --- | --- |
| Timestamp | datetime, date, timestamp |

The following table shows supported property types that you can use as the entity type key.

| Ontology configuration | Ontology property value type |
| --- | --- |
| Entity type key | string, integer |

If your data contains other data types, perform ETL to convert the data to one of the supported types before bringing the data to ontology.

---

## Feedback

Was this page helpful?

Yes

No

No

Need help with this topic?

Want to try using Ask Learn to clarify or guide you through this topic?

Ask Learn

Ask Learn

 Suggest a fix?

---

## Additional resources
