---
title: "Add semantic enrichment with metadata - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-add-semantic-enrichment](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-add-semantic-enrichment) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Add semantic enrichment with metadata - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

Semantic enrichment lets you add structured metadata to ontology objects, including descriptions, synonyms, and custom key-value attributes. By enriching your ontology with semantic metadata, you improve discoverability, provide context for AI agents, and ensure consistent understanding across your organization.

Important

This feature is in [preview](../../../fundamentals/preview).

Semantic enrichment helps AI agents and downstream systems better understand your data by providing:

- **Descriptions** that explain the purpose and meaning of entity types, properties, and relationship types
- **Synonyms** that capture alternative names and terms for entity types
- **Additional metadata** that captures domain-specific attributes as key-value pairs

This metadata improves agent answer correctness, especially for prompts that depend on contextual information like units of measurement, sensitivity levels, or business definitions.

## Prerequisites

Before you add semantic enrichment to your ontology, make sure you have:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** [enabled on your Fabric tenant](../overview-tenant-settings#users-can-create-ontology-preview-items).
- An ontology (preview) item that has [entity types](how-to-create-entity-types) or [relationship types](how-to-create-relationship-types).
- Understanding of [core ontology concepts](overview#core-concepts-defining-an-ontology).

## Key concepts

Semantic enrichment uses the following ontology (preview) concepts. For definitions of these terms, see the [Ontology (preview) glossary](../resources-glossary).

- *Entity type*
- *Property*
- *Relationship type*

## Add metadata to entity types

Entity types support descriptions, synonyms, and additional metadata key-value pairs. Follow these steps to add semantic enrichment to entity types.

1. In the **Explorer** pane of the Home configuration canvas, select the entity type to enrich. Select **View Entity Type details** from the top ribbon.
2. In the **Metadata** section, select the **Edit** button to open the metadata configuration.

   [![Screenshot of adding metadata attributes to an entity type.](media/how-to-add-semantic-enrichment/add-metadata-entity.png)](media/how-to-add-semantic-enrichment/add-metadata-entity.png#lightbox)
3. Add a **Description** to explain what the entity type represents. The description helps users and agents understand the purpose and meaning of the entity type.
4. To add **Synonyms**, enter alternative names or terms that refer to the same entity type. Synonyms improve discoverability and help agents understand different ways users might reference the entity.
5. To add **Additional metadata**, enter key-value pairs for domain-specific metadata, such as:

   - Units of measurement (example: `Unit of measurement: cm`)
   - Sensitivity classification (example: `Sensitivity: Confidential`)
   - Business owner information (example: `Business owner: Elaheh Mansouri`)
   - Data quality indicators (example: `Data quality: Incomplete`)

   Important

   Additional metadata keys must be unique within each entity type. You can't use duplicate key names.
6. Select **Update** to apply your metadata changes.

## Add metadata to properties

Properties support descriptions and additional metadata key-value pairs, but not synonyms. Follow these steps to add semantic enrichment to properties.

1. From the **Configure** tab of the entity type details, open the [data binding configuration](how-to-bind-data) for an entity type.
2. In the **Properties** section, select the **Tag** icon next to the property you want to enrich.

   [![Screenshot of adding metadata to properties.](media/how-to-add-semantic-enrichment/add-metadata-properties.png)](media/how-to-add-semantic-enrichment/add-metadata-properties.png#lightbox)

   [![Screenshot showing property metadata configuration.](media/how-to-add-semantic-enrichment/add-metadata-properties-2.png)](media/how-to-add-semantic-enrichment/add-metadata-properties-2.png#lightbox)
3. Add a **Description** that explains what the property represents and how to interpret it.
4. To add **Additional metadata**, enter key-value pairs.

   Important

   Additional metadata keys must be unique within each property. You can't use duplicate key names on the same property.
5. Select **Update** to apply your changes.

## Add metadata to relationship types

Relationship types support descriptions and additional metadata key-value pairs, but not synonyms. Follow these steps to add semantic enrichment to relationship types.

1. From the **Configure** tab of the entity type details, open the [relationship type configuration](how-to-create-relationship-types#create-relationship-type).
2. In the **Metadata** section, select **Edit** to open the metadata configuration.
3. Add a **Description** that explains the nature of the relationship and when it applies.
4. To add **Additional metadata**, enter key-value pairs.

   Important

   Additional metadata keys must be unique within each relationship type. You can't reuse the same key name.
5. Select **Update** to apply your metadata changes.

## Edit or delete metadata attributes

You can modify or remove metadata attributes from entity types, properties, and relationship types.

1. Select the ontology object (entity type, property, or relationship type) that contains the metadata you want to change.
2. In the **Metadata** section, locate the metadata attribute you want to modify.

   [![Screenshot of editing metadata attributes.](media/how-to-add-semantic-enrichment/edit-metadata.png)](media/how-to-add-semantic-enrichment/edit-metadata.png#lightbox)
3. Edit the metadata as needed and select **Update**.

## Best practices for semantic enrichment

Follow these best practices to maximize the value of semantic enrichment:

### Write clear descriptions

- Start descriptions with what the entity type, property, or relationship represents.
- Include the business context and purpose.
- Mention key characteristics or constraints.
- Keep descriptions concise but informative (one to three sentences).

### Use effective synonyms

- Include common abbreviations and acronyms.
- Add industry-specific terminology.
- Consider regional variations in terminology.
- Include both formal and informal terms that users might search for.

### Design meaningful key-value pairs for extra metadata

- Use consistent key naming conventions across your ontology.
- Document your key-value extra metadata standards for your team.
- Consider how agents and downstream systems consume the attributes.

### Optimize for agent performance

Note

Data agent doesn't use the semantic enrichment fields.

- Add unit information for numeric properties, such as `unit: celsius` or `unit: USD`.
- Include sensitivity classifications for properties that contain personal or sensitive data.
- Provide context about valid ranges or formats.
- Use descriptions that explain relationships between entities.

### Maintain metadata over time

- Review and update descriptions when business logic changes.
- Add synonyms as new terminology emerges in your organization.
- Remove outdated extra metadata key-value pairs.

## Limitations and considerations

- **Data agent limitation**: Data agent doesn't use the semantic enrichment fields.
- **Duplicate keys**: Each entity type, property, and relationship type must have unique keys for additional metadata. If you add duplicate keys, you get an error.
- **Synonyms**: Only entity types support synonyms. Properties and relationship types don't support synonyms.

## Related content

- [Create entity types](how-to-create-entity-types)
- [Create relationship types](how-to-create-relationship-types)
- [Data binding in ontology](how-to-bind-data)

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
