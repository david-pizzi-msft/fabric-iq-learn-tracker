---
title: "Create entity types in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-entity-types](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-entity-types) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create entity types in ontology (preview)

Summarize this article for me

*Entity types* represent real-world concepts such as *Truck*, *Sensor*, or *Customer*. They define standard names, descriptions, identifiers, and properties to ensure consistency across data sources and tools. By modeling your domain with entity types, you eliminate inconsistent column-level definitions and create a shared semantic layer that powers downstream experiences like analytics and AI agents. You can create entity types manually or import them from existing business logic in [semantic models](../../data-warehouse/semantic-models).

Important

This feature is in [preview](../../fundamentals/preview).

## Prerequisites

Before creating entity types, make sure you have the following prerequisites:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Users can create ontology (preview) items** and **Users can create Fabric items** [enabled on your Fabric tenant](overview-tenant-settings).
- An ontology (preview) item.
- Understanding of [core ontology concepts](overview#core-concepts).
- Understanding of the data binding process from [Data binding](how-to-bind-data).

## Create an entity type

Follow these steps to create entity types in your ontology (preview) item.

1. On the **Home** tab of the top ribbon, select **+ Add** > **Entity type**.

   [![Screenshot of the Entity type option in the Home ribbon's Add menu.](media/how-to-create-entity-types/add-entity-type.png)](media/how-to-create-entity-types/add-entity-type.png#lightbox)
2. Enter an **Entity type name**, such as *Freezer*, and select **Add**.
3. The configuration canvas shows your new entity type.

   [![Screenshot of the new entity type on the canvas.](media/how-to-create-entity-types/new-entity-type.png)](media/how-to-create-entity-types/new-entity-type.png#lightbox)

### Add properties

This section shows how to create properties on entity types without binding data to them (the properties remain unbound until you add data bindings for them later). You can also add properties while binding data in a single operation, as described in [Data binding](how-to-bind-data).

1. Select the entity type name in the **Explorer**, and then select **Entity type > Open details** from the ribbon. You can also open the entity type details by selecting the open-details icon next to the entity name on the canvas.

   [![Screenshot of the Open details button on the Entity type ribbon.](media/how-to-create-entity-types/view-entity-type-details.png)](media/how-to-create-entity-types/view-entity-type-details.png#lightbox)
2. The **Configure** page opens. This page surfaces important information about the entity type, including its properties and data bindings. Select **Create property**.

   [![Screenshot of adding properties to the entity type.](media/how-to-create-entity-types/add-properties.png)](media/how-to-create-entity-types/add-properties.png#lightbox)
3. Enter a **Name** and select a **Data type** for the first property. Select **Add** to add another property row. For example, add `FreezerId` and `FreezerName` with **String** data types. You can also choose **Unknown** to [model untyped properties](#modeling-untyped-properties) without specifying a data type upfront.

   To reuse an existing [shared property](how-to-reuse-properties#about-shared-properties), select **Add shared property** on the **Configure** page instead.

   [![Screenshot of configuring the listed property details.](media/how-to-create-entity-types/add-properties-details.png)](media/how-to-create-entity-types/add-properties-details.png#lightbox)
4. Select **Create**. The properties appear on the **Configure** page, unbound to any data source.

   [![Screenshot of the new unbound properties on the entity type.](media/how-to-create-entity-types/add-properties-done.png)](media/how-to-create-entity-types/add-properties-done.png#lightbox)
5. To make the entity type operational, [bind data](how-to-bind-data) to it.

## Edit or delete an entity type

To delete an entity type from your ontology (preview) item, go to the **Home** configuration canvas. Next to the entity type name in the **Explorer**, select **... > Delete**, and then confirm with **Delete entity type**.

[![Screenshot of deleting an entity type.](media/how-to-create-entity-types/delete-entity-type.png)](media/how-to-create-entity-types/delete-entity-type.png#lightbox)

To edit details of the entity type, select it and then select **Entity type > Open details** from the ribbon to open the **Configure** page.

On this page, you can add, rename, and delete properties. To rename or delete the entity type itself, select **...** in the upper-right corner of the page, and then select **Rename** or **Delete**.

[![Screenshot of editing entity type details.](media/how-to-create-entity-types/edit-entity-type.png)](media/how-to-create-entity-types/edit-entity-type.png#lightbox)

Deleting a property removes it from the entity everywhere it's configured, including the entity type key and [relationship type configurations](how-to-create-relationship-types).

Note

To see updates from upstream data sources, such as new rows, you need to manually refresh the ontology item. For more information, see [refresh the graph model](how-to-use-ontology-graph#refresh-the-graph-model).

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

## Modeling untyped properties

Entity types in ontology (preview) support creating properties without specifying a data type upfront. This capability supports conceptual modeling workflows where you define business concepts and their meanings before making technical decisions about data types. The data type is determined later when you're ready to bind data to these properties.

Untyped properties are useful when:

- You're modeling business concepts before identifying source systems or data structures.
- You want to separate conceptual modeling (what the business means) from physical modeling (how data is structured).

An untyped property is always unbound. Once you bind data to an untyped property, it becomes both typed and bound in a single operation.

Note

Untyped properties don't appear in query results, data previews, or downstream experiences (such as graph in Fabric, SQL analytics endpoint, or KQL) until you assign a data type through binding. However, the API includes untyped properties in the entity type definition, so programmatic consumers can discover and reference them before binding.

### Create untyped property

To create a property without specifying a data type, select **Unknown** as the **Data type** when defining the property.

[![Screenshot of creating an untyped property.](media/how-to-create-entity-types/untyped-property.png)](media/how-to-create-entity-types/untyped-property.png#lightbox)

### Assign a data type by binding data

When you're ready to assign a data type to an untyped property, [bind a source column to it](how-to-bind-data). The source column's native data type becomes the property's data type.

After binding, the property becomes operational and appears in query results, previews, and downstream experiences.

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
