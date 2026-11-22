---
title: "Entity type creation in ontology (preview) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-create-entity-types](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-create-entity-types) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Entity type creation in ontology (preview) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

*Entity types* represent real-world concepts such as *Truck*, *Sensor*, or *Customer*. They define standard names, descriptions, identifiers, and properties to ensure consistency across data sources and tools. By modeling your domain with entity types, you eliminate inconsistent column-level definitions and create a shared semantic layer that powers downstream experiences like analytics and AI agents. You can create entity types manually or import them from existing business logic in [semantic models](../../../data-warehouse/semantic-models).

Important

This feature is in [preview](../../../fundamentals/preview).

## Prerequisites

Before creating entity types, ensure you have the following prerequisites:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** [enabled on your Fabric tenant](../overview-tenant-settings#users-can-create-ontology-preview-items).
- An ontology (preview) item.
- Understanding of [core ontology concepts](overview#core-concepts-defining-an-ontology).
- Understanding of the data binding process from [Data binding](how-to-bind-data).

## Key concepts

Entity types use the following ontology (preview) concepts. For definitions of these terms, see the [Ontology (preview) glossary](../resources-glossary).

- *Entity type*
- *Entity type key*
- *Entity instance*
- *Property*
- *Data binding*

## Create an entity type

Follow these steps to create entity types in your ontology (preview) item.

1. From the Home configuration canvas, select **Add entity type** from the top ribbon or the center of the canvas.

   [![Screenshot of adding entity type.](media/how-to-create-entity-types/add-entity-type.png)](media/how-to-create-entity-types/add-entity-type.png#lightbox)
2. Enter a name for your entity type, and select **Add Entity Type**.

   Note

   Entity type names must be 1â26 characters, contain only alphanumeric characters, hyphens, and underscores, and start and end with an alphanumeric character.
3. The configuration canvas displays your new entity type.

   ![Screenshot of the new entity type on the canvas.](media/how-to-create-entity-types/new-entity-type.png)

### Add properties

This section shows how to create properties on entity types without binding data to them (the properties remain unbound until you add data bindings for them later). You can also add properties while binding data in a single operation, which is described in [Data binding](how-to-bind-data).

1. Select the entity type name in the **Explorer** and select **View entity type details** from the top ribbon.

   [![Screenshot of the View Entity Type details button.](media/how-to-create-entity-types/view-entity-type-details.png)](media/how-to-create-entity-types/view-entity-type-details.png#lightbox)
2. The **Configure** page opens. This page surfaces important information about the entity type, including its properties and data bindings. Expand **Manage property bindings** and select **Add properties**.

   [![Screenshot of adding properties to the entity type.](media/how-to-create-entity-types/add-properties-1.png)](media/how-to-create-entity-types/add-properties-1.png#lightbox)
3. Add a name and property type for each property, or choose *Define at binding* to [model untyped properties](#modeling-untyped-properties) without specifying a data type upfront. Select **Save** to view the saved properties in the Properties pane.

   [![Screenshot of configuring the listed property details.](media/how-to-create-entity-types/add-properties-2.png)](media/how-to-create-entity-types/add-properties-2.png#lightbox)

   Note

   Property names can only be duplicated across entities for properties of the same type. For example, you can't have one entity type with a string `ID` property and another entity type with an integer `ID` property, but you can have two entity types that both have a string `ID` property.
4. The properties are added to the **Configure** page, unbound to any data source.

   [![Screenshot of the new unbound properties on the entity type.](media/how-to-create-entity-types/add-properties-3.png)](media/how-to-create-entity-types/add-properties-3.png#lightbox)
5. Optionally, select a property to use as the **display name property** for instances of this entity type in downstream experiences.

   [![Screenshot of the option to choose a property as a display name.](media/how-to-create-entity-types/choose-display-name.png)](media/how-to-create-entity-types/choose-display-name.png#lightbox)
6. To make the entity type operational, [bind data](how-to-bind-data) to it.

## Edit or delete an entity type

To delete an entity type from your ontology (preview) item, go to the **Home** configuration canvas. Next to the entity type name in the **Explorer**, select **...** > **Delete entity type**.

[![Screenshot of deleting an entity type.](media/how-to-create-entity-types/delete-entity-type.png)](media/how-to-create-entity-types/delete-entity-type.png#lightbox)

To edit details of the entity type, select **View Entity type details** from the top ribbon to open the **Configure** page.

From this page, you can add, rename, and delete properties, and rename or delete the entity type itself.

[![Screenshot of editing entity type details.](media/how-to-create-entity-types/edit-entity-type.png)](media/how-to-create-entity-types/edit-entity-type.png#lightbox)

Deleting a property removes it from the entity everywhere it's configured, including the entity type key and [relationship type configurations](how-to-create-relationship-types).

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

## Modeling untyped properties

Entity types in ontology (preview) support creating properties without specifying a data type upfront. This capability enables conceptual modeling workflows where you define business concepts and their meanings before making technical decisions about data types. When you're ready to bind data to these properties, you determine the data type.

Untyped properties are useful when:

- You're modeling business concepts before identifying source systems or data structures.
- You want to separate conceptual modeling (what the business means) from physical modeling (how data is structured).

An untyped property is always unbound. Once you bind data to an untyped property, it becomes both typed and bound in a single operation.

Note

Untyped properties don't appear in query results, data previews, or downstream experiences (such as graph in Fabric, SQL analytics endpoint, or KQL) until you assign a data type through binding. However, the API includes untyped properties in the entity type definition, so programmatic consumers can discover and reference them before binding.

### Create untyped property

To create a property without specifying a data type, choose *Define at binding* as the **Property type** when defining the property.

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
