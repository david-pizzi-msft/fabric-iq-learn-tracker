---
title: "Resource links in ontology (preview) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-use-resource-links](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-use-resource-links) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Resource links in ontology (preview) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

In ontology (preview), *resource links* let you associate resources with an entity type. Currently, the only supported type of resource is [Power BI reports](/en-us/power-bi/create-reports/).

Important

This feature is in [preview](../../../fundamentals/preview).

Linking reports provides essential provenance, context, and discoverability for insights tied to a business concept. By linking reports directly to an entity type, you can:

- Quickly access relevant analytics without searching across workspaces
- Maintain consistent context between data, ontology, and reporting

## Prerequisites

Before adding resource links, ensure you have the following prerequisites:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- An ontology (preview) item with [entity types](how-to-create-entity-types) defined.
- A Power BI report containing insights relevant to an entity type, and permission to view the report. If you don't have view permission for a report, you can still add it as a link, but it appears as *Report unavailable* when viewed in the list.

## Add a resource link

To add a link to an existing Power BI report on an entity type, follow these steps.

1. In the Home contextual canvas, select the entity type in the **Explorer** pane. Select **View Entity Type details** from the ribbon.

   [![Screenshot of selecting View Entity Type details from the canvas.](media/how-to-use-resource-links/view-entity-type-details.png)](media/how-to-use-resource-links/view-entity-type-details.png#lightbox)

   The entity type details view opens to the **Configure** tab.
2. The **Resources** section displays any linked resources. Select **Add** to add a new resource link.

   [![Screenshot of the Resources section and the Add button.](media/how-to-use-resource-links/add-resources.png)](media/how-to-use-resource-links/add-resources.png#lightbox)
3. Fabric opens your OneLake catalog of resources. Choose the Power BI report you want to link to the entity type, and select **Add**.
4. Verify that the report appears in the **Resources** section.

   [![Screenshot of a resource inside the Resources section.](media/how-to-use-resource-links/resources-entry.png)](media/how-to-use-resource-links/resources-entry.png#lightbox)

## View resource links

You can view resources linked to an entity type from the following locations.

### Configure tab

The list of resources linked to an entity type is visible in the **Configure** tab of the entity type details, in the **Resources** section.

[![Screenshot of a resource inside the Resources section of the Configure tab.](media/how-to-use-resource-links/resources-entry.png)](media/how-to-use-resource-links/resources-entry.png#lightbox)

### Overview tab

You can display linked resources in a tile on the **Overview** tab of the entity type details. An entity type can have only one **Resource links** tile at a time.

[![Screenshot of the Resource links tile on the Overview tab.](media/how-to-use-resource-links/resource-links-tile.png)](media/how-to-use-resource-links/resource-links-tile.png#lightbox)

You can open the resources directly from the tile by selecting their names. Reports open inside Fabric in a new tab.

#### Manage the Resource links tile

If the entity type overview doesn't have a **Resource links** tile, you can add one manually.

1. In the entity type overview, select **Add tile** > **Resource links**.

   [![Screenshot of adding a Resource links tile.](media/how-to-use-resource-links/add-tile.png)](media/how-to-use-resource-links/add-tile.png#lightbox)
2. Preview the links that appear on the tile and select **Create**.

   ![Screenshot of confirming the Resource links tile.](media/how-to-use-resource-links/add-tile-2.png)

You might see these messages on the tile creation step:

- If a tile already exists, you see this message: *A Resource links tile already exists on this overview*.

  ![Screenshot of the message when a Resource links tile already exists.](media/how-to-use-resource-links/tile-already-exists.png)
- If the entity type has no linked resources, you see this message: *No links to display*, with a link to the entity type configuration.

  ![Screenshot of the empty link tile configuration.](media/how-to-use-resource-links/no-links-tile.png)

  If you add the tile anyway, the tile stays empty in the overview.

  [![Screenshot of the empty link tile in the entity type overview.](media/how-to-use-resource-links/no-links-tile-2.png)](media/how-to-use-resource-links/no-links-tile-2.png#lightbox)

## Delete a resource link

Note

Deleting a resource link in ontology doesn't delete the report from the Power BI workspace.

To remove a linked resource from an entity type:

1. Start in the **Configure** tab of the entity type details.
2. In the **Resources** section, select the trash icon next to the link you want to delete.

   [![Screenshot of the trash icon next to a linked resource.](media/how-to-use-resource-links/delete.png)](media/how-to-use-resource-links/delete.png#lightbox)
3. Select **Delete** when prompted to confirm the deletion.

To remove linked resources from the **Overview** tab, remove the entire Resource links tile. (You can't keep the tile while deleting individual links from it.)

1. Expand the **...** options on the **Resource links** tile and select **Delete**.

   [![Screenshot of deleting the Resource links tile from the entity type overview.](media/how-to-use-resource-links/delete-tile.png)](media/how-to-use-resource-links/delete-tile.png#lightbox)
2. Select **Delete** to confirm the deletion when prompted.

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
