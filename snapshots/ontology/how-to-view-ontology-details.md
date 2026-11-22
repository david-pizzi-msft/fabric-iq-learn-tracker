---
title: "View ontology details in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-view-ontology-details](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-view-ontology-details) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# View ontology details in ontology (preview)

Summarize this article for me

To view and explore your ontology, start with the multiple view formats on the home configuration canvas. To drill down into entity type details, use the *entity type details* view. There, you can configure an entity type and explore its instance data.

Important

This feature is in [preview](../../fundamentals/preview).

## Prerequisites

Before viewing entity type details, make sure you have the following prerequisites:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- An ontology (preview) item with entity types defined. You can inspect and configure entity definitions without binding data. To view populated entity instances, complete [data binding](how-to-bind-data) for the entity type.

## Explore canvas views

The home configuration canvas of ontology contains three views: [full ontology](#full-ontology), [neighborhood](#neighborhood), and [inheritance](#inheritance).

To switch views, select **Full ontology**, **Neighborhood**, or **Inheritance** in the upper-right corner of the canvas.

### Full ontology

The **Full ontology** view of the canvas shows all entity types and relationships present in the ontology. Select an entity type from the **Explorer** to center it in the canvas window.

[![Screenshot of the full ontology canvas view.](media/tutorial-3-preview-ontology/canvas-full-ontology.png)](media/tutorial-3-preview-ontology/canvas-full-ontology.png#lightbox)

### Neighborhood

The **Neighborhood** view of the canvas shows the modeled relationships of an entity type. Select an entity type from the **Explorer** to show it in the canvas along with related entity types.

[![Screenshot of the Neighborhood canvas view.](media/tutorial-3-preview-ontology/canvas-relationship.png)](media/tutorial-3-preview-ontology/canvas-relationship.png#lightbox)

### Inheritance

The **Inheritance** view of the canvas shows the inheritance structure of entity types. Select an entity type from the **Explorer** to show it in the canvas along with its inheritance relationships.

[![Screenshot of the Inheritance canvas view.](media/tutorial-3-preview-ontology/canvas-lineage.png)](media/tutorial-3-preview-ontology/canvas-lineage.png#lightbox)

## View entity type details

Follow these steps to access the entity type details in your ontology (preview) item.

1. In the **Explorer** pane of the Home configuration canvas, select the entity type that you want to view. Select **Entity type > Open details** from the ribbon, or select the open-details icon next to the entity name on the canvas.

   [![Screenshot of opening the experience from the menu ribbon.](media/how-to-view-ontology-details/view-entity-type-details.png)](media/how-to-view-ontology-details/view-entity-type-details.png#lightbox)
2. The entity type details view opens to the **Configure** page. Use the tabs across the top of the page to switch between the **Configure** and **Instances** pages.

   [![Screenshot of the entity type details configure page. The Configure and Instances tabs are highlighted.](media/how-to-view-ontology-details/entity-type-details-tabs.png)](media/how-to-view-ontology-details/entity-type-details-tabs.png#lightbox)

### Configure tab

On the **Configure** page, you can manage properties, data bindings, relationship types, metrics, metadata, and resource links for the entity type.

[![Screenshot of the entity type details configure page.](media/how-to-view-ontology-details/entity-type-details-configure.png)](media/how-to-view-ontology-details/entity-type-details-configure.png#lightbox)

For more information about these features, see the following documents:

- [Add properties](how-to-create-entity-types#add-properties)
- [Bind data](how-to-bind-data)
- [Add relationship types](how-to-create-relationship-types)
- [Use resource links](how-to-use-resource-links)

### Instances tab

In the **Instances** page, you can view the instances associated with the entity type and their static property values.

[![Screenshot of the entity type details instances page.](media/how-to-view-ontology-details/entity-type-details-instances.png)](media/how-to-view-ontology-details/entity-type-details-instances.png#lightbox)

## Troubleshooting

For troubleshooting tips related to the entity type details in ontology (preview), see [Troubleshoot ontology (preview)](resources-troubleshooting).

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
