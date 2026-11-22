---
title: "Relationship types in ontology (preview) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-create-relationship-types](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-create-relationship-types) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Relationship types in ontology (preview) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

Relationships allow organizations to model, manage, and govern semantic connections between business entities. Clearly defined relationships help organizations turn complex connections into actionable insights and decisions with the following benefits:

- Semantic clarity: Explicitly defined relationships (such as *owns*, *located at*, *supplies*, or *monitored by*) allow organizations to represent not only what entities exist, but how they interact.
- Analytics: Ontologies that are enriched with relationships offer contextualized insights.

Important

This feature is in [preview](../../../fundamentals/preview).

## Prerequisites

Before adding relationship types to your ontology, make sure you have the following prerequisites:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** [enabled on your Fabric tenant](../overview-tenant-settings#users-can-create-ontology-preview-items).
- An ontology (preview) item with [entity types](how-to-create-entity-types) created.
- Relationship source data that meets these guidelines:
  - The data is in [OneLake](../../../onelake/onelake-overview).
  - The source data contains keys for both the source and target entity type.

## Key concepts

Relationship types use the following ontology (preview) concepts. For definitions of these terms, see the [Ontology (preview) glossary](../resources-glossary).

- *Entity type*
- *Relationship type*
- *Relationship instance*

## Create relationship type

The first step in adding a relationship in your ontology (preview) item is creating a relationship type. Then, bind data to the relationship type to create relationship instances.

For example, suppose you want to define a relationship between the entity types *Truck* and *Driver*, and your data contains a table called *Truck data* with columns `TruckId`, `Site`, `TruckName`, and `DriverId`. You might start by defining a relationship type called *drives* from the *Driver* entity type to the *Truck* entity type. Then, create a data binding based on the *Truck data* table, using the columns `TruckId` and `DriverId` to define relationship instances for that relationship type. The result is that your *drives* relationship type has instances to represent each combination of `TruckId` and `DriverId` in your data.

Follow these steps to create a relationship type and bind data to it:

1. In the Home configuration canvas, there are multiple ways to create a relationship type. Select **Add relationship** from the top ribbon, select **... > Add relationship** next to the name of an entity type in the **Explorer**, or select **... > Add relationship type** on an entity type card in the main canvas.

   [![Screenshot of the Add relationship buttons.](media/how-to-create-relationship-types/add-relationship-1.png)](media/how-to-create-relationship-types/add-relationship-1.png#lightbox)
2. The **Add new relationship** window appears. Enter the **Relationship type name**, the **Origin entity type**, and the **Target entity type**. Select **Create**.

   ![Screenshot of the Add new relationship options.](media/how-to-create-relationship-types/add-relationship-2.png)

   Note

   Due to a known issue affecting duplicate relationship names, ensure relationship names are unique.
3. The relationship type is created and appears in the configuration canvas. Select it on the canvas to open the relationship details configuration.

   [![Screenshot of the created relationship on the canvas.](media/how-to-create-relationship-types/add-relationship-3.png)](media/how-to-create-relationship-types/add-relationship-3.png#lightbox)
4. Observe the sections of the configuration page:

   - **Origin entity type**: Lists details of the origin entity.
   - **Relationship type**: Sets details of the relationship type.
   - **Target entity type**: Lists details of the target entity.

   [![Screenshot of the relationship type configuration.](media/how-to-create-relationship-types/add-relationship-sections.png)](media/how-to-create-relationship-types/add-relationship-sections.png#lightbox)
5. In the middle panel, enter the relationship type details.

   1. **Mapping table**: Expand **Browse available sources** and choose the table in the source data that can link the two entity types together. This table should contain identifying information for both entity types within each row (such as columns for a store ID and a freezer ID).
   2. **Matched ...** (origin entity type): This setting specifies the column in the relationship source data table whose values match the key property defined on the origin entity type. The name might match or it might be different.
   3. **Matched ...** (target entity type): This setting specifies the column in the relationship source data table whose values match the key property defined on the target entity type. The name might match or it might be different.
6. **Save** the relationship type. Confirm that the relationship type updated successfully, and then select **Cancel** to close the configuration options.
7. You see the **Configure** page for the entity, where the updated relationship is visible in the **Relationships** section.

   [![Screenshot of the relationship type on the configuration page.](media/how-to-create-relationship-types/add-relationship-finished.png)](media/how-to-create-relationship-types/add-relationship-finished.png#lightbox)

## Edit or delete relationship type

To edit or delete a relationship type, reopen its configuration page by selecting the relationship type in the canvas view (visible in both the Home configuration canvas and the **Relationships** section of the **Configure** page). On the **Configure** page, you can also select **Manage relationships > {relationship type name}**.

[![Screenshot of reopening the relationship configuration.](media/how-to-create-relationship-types/open-relationship.png)](media/how-to-create-relationship-types/open-relationship.png#lightbox)

On this page, edit the relationship type configuration or delete the relationship type.

[![Screenshot of editing/deleting a relationship type.](media/how-to-create-relationship-types/delete-relationship.png)](media/how-to-create-relationship-types/delete-relationship.png#lightbox)

Note

To see updates in upstream data sources, such as new rows, manually refresh the ontology item. For more information, see [refresh the graph model](how-to-view-entity-type-details#refresh-the-graph-model).

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
