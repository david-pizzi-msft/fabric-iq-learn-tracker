---
title: "Data binding in ontology (preview) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-bind-data](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-bind-data) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Data binding in ontology (preview) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

Data binding in ontology (preview) connects the schema of entity types, relationship types, and properties to concrete data sources that drive enterprise operations and analytics.

Important

This feature is in [preview](../../../fundamentals/preview).

By using data binding, you can:

- Integrate data into a semantic layer without copying source data
- Enrich entity types with up-to-date contextual information from batch and real-time sources
- Provide a semantic backbone for AI agents and automation to support reasoning, decision-making, and actions across the enterprise

## Prerequisites

Before binding data to your ontology, ensure you have the following prerequisites:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** [enabled on your Fabric tenant](../overview-tenant-settings#users-can-create-ontology-preview-items).
- An ontology (preview) item with [entity types](how-to-bind-data) created.
- Data that you prepared according to these guidelines:
  - The data is organized, and you completed any necessary ETL required by your business.
  - The data contains all required information for it to be modeled. For more information, see [Core concept: Data binding](overview#data-binding).
  - The data is in Microsoft Fabricâstatic data in [OneLake](../../../onelake/onelake-overview), time series data in OneLake or an [eventhouse](../../../real-time-intelligence/eventhouse).
  - Time series data is in *columnar* format, meaning it's represented in a table with a row for each timestamped observation. Columns contain time stamps and property values (like temperature or pressure).
  - Lakehouse tables conform to ontology (preview)'s data binding [limitations](#limitations-and-troubleshooting): They're **managed** and don't have column mapping enabled.

## Key concepts

Data binding uses the following ontology (preview) concepts. For definitions of these terms, see the [Ontology (preview) glossary](../resources-glossary).

- *Entity type*
- *Entity type key*
- *Entity instance*
- *Property*

## Add static data

First, bind static data to entity types in your ontology (preview) item. This non-time series binding defines the unique entity type instances.

1. You can start a data binding from either the Home configuration canvas or the **Configure** tab of the entity type details.

   On the Home configuration canvas, select **...** next to an entity type name to open its options menu and select **Bind data**.

   [![Screenshot of starting a data binding from the configuration canvas.](media/how-to-bind-data/bind-data-canvas.png)](media/how-to-bind-data/bind-data-canvas.png#lightbox)

   On the **Configure** page, select **Manage property bindings** > **Add binding and properties**, or **Add properties from data** in the **Properties** section if the entity type has no properties yet.

   [![Screenshot of adding a new data binding to the entity type.](media/how-to-bind-data/bind-data-add.png)](media/how-to-bind-data/bind-data-add.png#lightbox)
2. On the binding page, select **Add data binding** and choose the type of OneLake data source that contains the data for the entity.

   ![Screenshot of the data binding page and data source selection.](media/how-to-bind-data/bind-data-add-data-binding.png)
3. Choose your data source and table from the OneLake catalog.

   [![Screenshot of the data source selection.](media/how-to-bind-data/bind-data-select-table.png)](media/how-to-bind-data/bind-data-select-table.png#lightbox)
4. Fields from the source table populate the data binding configuration. Observe the sections of the configuration page:

   - **Entity type key**: Identifies the field (or fields) that can be used to uniquely identify each record of ingested data.
   - **Binding selection**: Identifies the source table that holds the data for the binding.
   - **Entity type key mapping**: Identifies the column(s) in the source data table that map to the entity type key property. You can select string and integer columns from your source data as the entity type key. Together, the columns you select uniquely identify a record.
   - **Properties**: Lists the columns from the source data and corresponding properties on the entity type. The **Source column** side populates automatically with the columns from the table, and the **Property name** side lists their corresponding property names on the entity type within ontology.

   [![Screenshot of the configuration.](media/how-to-bind-data/bind-data-configuration.png)](media/how-to-bind-data/bind-data-configuration.png#lightbox)
5. In the **Properties** section, add, rename, or delete properties as needed. Property names can match the source column names or be different. If you have existing properties defined on the entity type, you can select their names from the dropdown menu.

   Custom property names must be 1â26 characters, contain only alphanumeric characters, hyphens, and underscores, and start and end with an alphanumeric character. Property names must be unique across all entity types.
6. Select **Define entity type key** at the top of the configuration. Select the property or set of properties that uniquely identifies each record in your data and **Save**.

   [![Screenshot of adding an entity type key.](media/how-to-bind-data/bind-data-key.png)](media/how-to-bind-data/bind-data-key.png#lightbox)
7. Select **Save** to save your static data binding. You see a confirmation message indicating that the entity type was updated successfully.
8. From here, you can continue on to [add a time series binding](#add-time-series-data-after-binding-static-data) on this page, or you can close the binding page by selecting **Cancel**. Closing the binding page returns you to the **Configure** page.
9. In the **Configure** page, verify the bindings by reviewing the properties in the **Properties** pane and confirming that they're bound to the correct data sources.

   [![Screenshot of the data bindings in the Configure page.](media/how-to-bind-data/bind-data-complete.png)](media/how-to-bind-data/bind-data-complete.png#lightbox)
10. Optionally, select a property modeled on your entity type to use as the **display name property**. This step provides a friendly name for entity instances in downstream experiences.

    [![Screenshot of the option to choose a property as a display name.](media/how-to-bind-data/display-name.png)](media/how-to-bind-data/display-name.png#lightbox)

## Add time series data (after binding static data)

Next, bind time series data to entity types in your ontology (preview) item.

Important

Before you bind time series data to an entity type, ensure your static data binding is complete. The entity type must have at least one property with static data bound to it that you can use as the key to contextualize your time series data. This static data must exactly match a column in your time series data.

1. In the **Configure** page, expand **Manage property bindings** and select **Add binding and properties** again to reopen the binding configuration.

   Tip

   Although this article shows adding static and time series data in separate visits to the configuration page, you could also bind all the data in the first visit to this configuration page, as long as you complete the static binding before the time series one.
2. On the binding page, select **Add data binding** and choose the type of OneLake data source that contains the time series data for the entity. Choose your data source and table from the OneLake catalog and select **Add**.
3. A **Timeseries data** section appears in the configuration. Select the source data **Timestamp column** that contains the timestamp values.

   [![Screenshot of selecting the timestamp column.](media/how-to-bind-data/bind-data-time-series-configure.png)](media/how-to-bind-data/bind-data-time-series-configure.png#lightbox)
4. In the **Properties** section, add, rename, or delete properties as needed.
5. **Save** the data binding. Confirm that the entity type updated successfully, then select **Cancel** to close the configuration options.
6. Back in the **Configure** page, verify the new properties and their binding to the data source.

   [![Screenshot of all the data bindings in the Configure page.](media/how-to-bind-data/bind-data-time-series-complete.png)](media/how-to-bind-data/bind-data-time-series-complete.png#lightbox)

## Edit or delete data binding

To edit or delete data bindings, start in the **Configure** page. Select **Manage property bindings** > **Manage bindings**.

[![Screenshot of the manage bindings options.](media/how-to-bind-data/manage-bindings.png)](media/how-to-bind-data/manage-bindings.png#lightbox)

The configuration page reopens, where you can edit binding details or delete binding data sources.

Note

To see updates in upstream data sources, such as new rows, manually refresh the ontology item. For more information, see [refresh the graph model](how-to-view-entity-type-details#refresh-the-graph-model).

## Supported property types

The following table lists the supported property types for data that you can bind to properties in ontology (preview).

| Ontology property value type | Supported Lakehouse types | Supported Eventhouse types |
| --- | --- | --- |
| integer | tinyint, smallint, bigint, integer, long, short | int, long |
| boolean | boolean | bool |
| datetime | datetime, date, timestamp | datetime |
| double | double, decimal, float | decimal, real |
| string | char, decimal(p, s), string, array, binary, binary16, byte, map, object, struct, timestampint64, timestamp\_ntz | dynamic, string, guid, timespan |

The following table shows supported source column value types that you can use for the timestamp selection in a time series binding.

| Ontology configuration | Lakehouse and Eventhouse source column value type |
| --- | --- |
| Timestamp | datetime, date, timestamp |

The following table shows supported property types that you can use as the entity type key.

| Ontology configuration | Ontology property value type |
| --- | --- |
| Entity type key | string, integer |

If your data contains other data types, perform ETL to convert the data to one of the supported types before bringing the data to ontology.

## Limitations and troubleshooting

Data binding has the following limitations:

- Ontology only supports **managed** lakehouse tables (located in the same OneLake directory as the lakehouse), not **external** tables that show in the lakehouse but reside in a different location.
- Changing the lakehouse table name after mappings are created might cause problems accessing data in the entity type details.
- The ontology graph doesn't support delta tables with column mapping enabled. Column mapping can be enabled manually, or is enabled automatically on lakehouse tables where column names have certain special characters, including `,`, `;`, `{}`, `()`, `\n`, `\t`, `=`, and space. It also happens automatically on the delta tables that store data for import mode semantic model tables.
- Each entity type supports one **static** data binding. You can't combine static data from multiple sources for a single entity type.
  - You must use OneLake-backed sources for static data.
  - Entity types **do** support bindings from multiple **time series** sources. You can bind time series data from both eventhouse and lakehouse sources.

### Troubleshooting

For troubleshooting tips related to data binding, see [Troubleshoot ontology (preview)](../resources-troubleshooting#troubleshoot-data-binding).

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
