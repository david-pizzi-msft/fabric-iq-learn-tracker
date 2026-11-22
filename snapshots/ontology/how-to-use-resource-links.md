---
title: "Link external resources in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-resource-links](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-use-resource-links) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Link external resources in ontology (preview)

Summarize this article for me

In ontology (preview), *resource links* let you associate Fabric items, such as [Power BI reports](/en-us/power-bi/create-reports) and semantic models, with an entity type. Resource links can also reference compatible item-reference variables.

Important

This feature is in [preview](../../fundamentals/preview).

Linking resources provides provenance, context, and discoverability for insights tied to a business concept. By linking resources directly to an entity type, you can:

- Quickly access relevant analytics without searching across workspaces
- Maintain consistent context between data, ontology, and reporting

A resource link is a reference, not a [data binding](how-to-bind-data). Adding a link doesn't import the linked item's data or grant permission to access it. Access to the linked item is controlled separately by that item's permissions.

## Prerequisites

Before adding resource links, make sure you have the following prerequisites:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- An ontology (preview) item with [entity types](how-to-create-entity-types) defined.
- A Fabric item relevant to an entity type, and permission to access that item. A linked item might be unavailable if you don't have access to it.

## Add a resource link

To add a link to an existing Fabric item on an entity type, follow these steps.

1. In the Home configuration canvas, select the entity type in the **Explorer** pane. Select **Entity type > Open details** from the ribbon.

   [![Screenshot of selecting Open details from the Entity type ribbon.](media/how-to-use-resource-links/view-entity-type-details.png)](media/how-to-use-resource-links/view-entity-type-details.png#lightbox)

   The entity type details view opens to the **Configure** tab.
2. Scroll down to the **Resources** section, which shows any linked resources. Select **Manage resources** > **Add Fabric item** to add a new resource link.

   [![Screenshot of Add Fabric item in the Manage resources menu.](media/how-to-use-resource-links/add-resources.png)](media/how-to-use-resource-links/add-resources.png#lightbox)
3. Fabric opens your OneLake catalog of resources. Choose the Fabric item you want to link to the entity type, and select **Add**.
4. Verify that the item appears in the **Resources** section.

   [![Screenshot of a resource inside the Resources section.](media/how-to-use-resource-links/resources-entry-crop.png)](media/how-to-use-resource-links/resources-entry-crop.png#lightbox)

## View resource links

View resources linked to an entity type from the **Configure** tab.

The list of resources linked to an entity type is visible in the **Configure** tab of the entity type details, in the **Resources** section.

[![Screenshot of a resource inside the Resources section of the Configure tab.](media/how-to-use-resource-links/resources-entry.png)](media/how-to-use-resource-links/resources-entry.png#lightbox)

## Delete a resource link

Note

Deleting a resource link in ontology does **not** delete the actual linked item from the workspace.

To remove a linked resource from an entity type:

1. Start in the **Configure** tab of the entity type details.
2. In the **Resources** section, hover over the link to reveal the trash icon. Select the icon.

   [![Screenshot of the trash icon next to a linked resource.](media/how-to-use-resource-links/delete.png)](media/how-to-use-resource-links/delete.png#lightbox)
3. Select **Delete** when prompted to confirm the deletion.

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
