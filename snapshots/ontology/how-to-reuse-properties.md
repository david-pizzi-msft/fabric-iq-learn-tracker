---
title: "Reuse shared properties in ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-reuse-properties](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-reuse-properties) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Reuse shared properties in ontology (preview)

Summarize this article for me

As an ontology grows, you might need the same property definition across unrelated entity types. The **ontology (preview)** item provides [shared properties](#about-shared-properties), which you define once and add to any entity type by reference.

Shared properties reduce duplication across the ontology and help teams keep common definitions and metadata consistent.

Important

This feature is in [preview](../../fundamentals/preview).

## About shared properties

A *shared property* is a property that's a first-class, top-level construct in the ontology. It carries full metadata, including its data type, description, and semantic-enrichment fields. Any entity type can include a shared property by reference, rather than by copy. Instead of redefining `CreatedBy`, `CreatedOn`, or `Owner` on every entity type that needs them, shared properties let you define each once and reference it wherever it applies.

Shared property names are unique within an ontology.

## Create a shared property

To create a shared property:

1. On the **Home** tab, select **Manage** > **Shared properties**.

   [![Screenshot of Shared properties in the Manage menu.](media/how-to-reuse-properties/shared-properties.png)](media/how-to-reuse-properties/shared-properties.png#lightbox)
2. Select **New** or, if the list is empty, **New shared property**. Enter the property details, and select **Add**.
3. The property is visible on the **Shared properties** page.

   After you add the property to entity types, you can see all the entity types that use this property in the **Linked ontology elements** column.

   [![Screenshot of the shared property and entity types that use it.](media/how-to-reuse-properties/shared-properties-populated.png)](media/how-to-reuse-properties/shared-properties-populated.png#lightbox)

## Reference and bind a shared property

To add a shared property to an entity type:

1. Open the **Configure** tab for the entity.
2. Select **Add shared property**.

   [![Screenshot of adding an existing property.](media/how-to-reuse-properties/add-existing-property.png)](media/how-to-reuse-properties/add-existing-property.png#lightbox)
3. Select shared properties to add to the entity and select **Add**.

   [![Screenshot of choosing the existing property to add.](media/how-to-reuse-properties/add-existing-property-details.png)](media/how-to-reuse-properties/add-existing-property-details.png#lightbox)
4. The property is now available on the entity type.

When you bind data to a shared property on an entity, binding is local to that entity. The shared property itself stays unbound and available for other entity types to reference and bind independently.

### Override metadata locally

You can override a referenced property's [metadata](how-to-add-metadata) (such as its description or key-value pairs) on a specific entity type. The override:

- Applies only to that entity type and leaves the shared property unchanged elsewhere.
- Appears with a provenance badge that makes the override visible.
- Reverts in one action back to the shared property's current value.

If the shared property's value changes while an override is in place, the override persists, and the new value applies to every other referencing entity type that hasn't overridden the same field.

### Remove a shared property reference

When you remove a shared property reference from an entity type, the outcome depends on whether local state exists:

- **Soft detach** keeps the property on the entity type as a local property, preserving its binding, any metadata override, and any relationship endpoint that uses it. Its provenance changes to local.
- **Full delete** removes the property from the entity type and clears the local binding and override.

If the entity type holds no local binding, override, or relationship endpoint against the reference, removing it is a direct action with no choice to make.

## Delete a shared property

When you choose to delete the shared property itself, the ontology shows an impact analysis that lists every affected entity type and categorizes each impact as a data binding, a relationship that uses the property, or a metadata override.

[![Screenshot of deleting a shared property.](media/how-to-reuse-properties/delete-property.png)](media/how-to-reuse-properties/delete-property.png#lightbox)

After you confirm, the ontology removes the central shared property record. The ontology soft-detaches each impacted entity type, which keeps a local copy of the property along with its binding, relationship endpoint, and overridden metadata, so you don't lose any local work. Entity types that only referenced the property, with no local state, lose the reference.

## View property sources

Because a property on an entity type can come from several places, the **Configure** page indicates where each property comes from, and you can filter by property source:

- **Local** â defined directly on this entity type.
- **Inherited** â inherited from a base entity type.
- **Shared** â composed from a shared property.

[![Screenshot of filterable property sources.](media/how-to-reuse-properties/property-sources.png)](media/how-to-reuse-properties/property-sources.png#lightbox)

## Related content

- [Model with inheritance in ontology (preview)](how-to-use-inheritance)
- [What is ontology (preview)?](overview)
- [Agent integration options for ontology (preview)](concepts-agent-integration)
- [Microsoft Fabric terminology](../../fundamentals/fabric-terminology)

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
