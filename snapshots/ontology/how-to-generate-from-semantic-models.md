---
title: "Generate an ontology (preview) from semantic models"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-generate-from-semantic-models](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-generate-from-semantic-models) · Last updated on **2026-11-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Generate an ontology (preview) from semantic models

Summarize this article for me

A [semantic model](../../data-warehouse/semantic-models) in Fabric is a logical description of a domain, like a business. Semantic models hold information about your data and the relationships among that data. One way to create an ontology (preview) is to generate it directly from a semantic model. You can also pull data into a single ontology (preview) from more than one semantic model.

Important

This feature is in [preview](../../fundamentals/preview).

Note

You need both Read and Build [permissions](/en-us/power-bi/connect-data/service-datasets-permissions#what-are-the-semantic-model-permissions) on the semantic models to generate an ontology from a semantic model and query the semantic models using ontology.

## Process overview

Ontology generation automatically creates the following elements:

- A new **ontology item (preview)** in your Fabric workspace, with a name that you choose.
- **Entity types** in the ontology that match the tables in your semantic model.
- **Properties** on each entity type based on the columns in your tables, and **data bindings** that link your data rows to these properties.
- **Relationship types** between entity types that follow relationships defined in the semantic model.
- **Metrics** on entity types based on DAX measures in the semantic model. For more information, see [Use metrics in ontology (preview)](how-to-use-metrics).

After generating an ontology, complete these actions manually:

- Bind **time series data** to entity types. Ontology generation doesn't create properties for time series data automatically.
- Review **entity type keys** and add any that are missing, especially for multi-key scenarios.
- Bind **relationship types** to data.
- Rename entity types or relationships to friendly names as needed.
- Review the entire ontology to make sure entity types, their properties and data bindings, metrics, and relationships are complete.

### Adding multiple semantic models

You can source data for a single ontology from more than one semantic model by using the [ontology agent](how-to-use-ontology-agent). When you use the ontology agent in an existing ontology and ask it to include another semantic model, the agent reads the new model, reconciles overlapping concepts like shared customer or order tables, and binds everything into one connected ontology. Combining semantic models is useful when the data for a domainâsuch as a full customer 360 viewâspans separate models for retention, sales, support, and returns.

By generating an ontology from multiple semantic models, you can:

- Bring related concepts that live in separate semantic models into one ontology.
- Let the agent normalize duplicate entities and create relationships that span models.
- Query across the combined domain, including relationships that no single source model captures on its own.

Note

Currently, you can add a second semantic model to an existing ontology only through the ontology agent.

## Prerequisites

Before you add semantic models to an ontology, ensure you have:

- A [Fabric workspace](../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../enterprise/licenses#capacity).
- **Users can create ontology (preview) items** and **Users can create Fabric items** [enabled on your Fabric tenant](overview-tenant-settings).
- One or more related [semantic models](../../data-warehouse/semantic-models) in your workspace that represent parts of the same business domain (for example, `SalesReport` and `InventoryReport`).
  - Both Read and Build [permissions](/en-us/power-bi/connect-data/service-datasets-permissions#what-are-the-semantic-model-permissions) on the semantic model(s). This is required to generate an ontology from the semantic models and query the semantic models using ontology.
- Basic familiarity with the [ontology agent](how-to-use-ontology-agent).

## Create the ontology item

To generate an ontology from a semantic model, select **Generate Ontology** from the semantic model ribbon. This button is available whether or not the semantic model is open. If you don't see the **Generate Ontology** option, it might be hidden in the **...** action menu.

[![Screenshot of Generate ontology button in the ribbon of a closed semantic model.](media/how-to-generate-from-semantic-models/generate-ontology-closed.png)](media/how-to-generate-from-semantic-models/generate-ontology-closed.png#lightbox)

[![Screenshot of Generate ontology button in the ribbon of an open semantic model.](media/how-to-generate-from-semantic-models/generate-ontology-open.png)](media/how-to-generate-from-semantic-models/generate-ontology-open.png#lightbox)

Note

You can also create an empty ontology item from scratch and use the ontology agent to add semantic model data afterwards.

Enter the new ontology details when prompted and select **Create**.

After you create the ontology, review it and confirm it contains the entity types that you expect.

[![Screenshot of the new ontology with entities.](media/how-to-generate-from-semantic-models/ontology-generated.png)](media/how-to-generate-from-semantic-models/ontology-generated.png#lightbox)

Open each entity type to view its details. Confirm that the entity type includes all information from the semantic model, including **Properties**, **Relationships**, and **Metrics**.

[![Screenshot of entity type details in the new ontology.](media/how-to-generate-from-semantic-models/ontology-generated-details.png)](media/how-to-generate-from-semantic-models/ontology-generated-details.png#lightbox)

## Add more semantic models with the ontology agent

Add one or more semantic models to an existing ontology by using the ontology agent.

1. With the ontology open, select **Home** > **Ontology agent** and set the agent to **Act**.

   [![Screenshot of opening the ontology agent in Act mode.](media/how-to-generate-from-semantic-models/agent-act-mode.png)](media/how-to-generate-from-semantic-models/agent-act-mode.png#lightbox)
2. Prompt the agent to include additional semantic models that your Fabric account has access to. Here's an example query:

   ```
   Use the SalesReport and InventoryReport semantic models in this workspace.
   Keep Sales and Locations bound to SalesReport. Use InventoryReport for
   Products and InventoryPositions, including its measures. Preserve the
   existing entity types and relationships, reconcile overlapping tables,
   and don't create duplicate entities. Apply the changes and summarize
   the entity types, relationships, and measure bindings.
   ```
3. Submit the query and let the agent process the request. The agent summarizes what it did and exposes its reasoning steps, including how it resolved conflicts between overlapping tables in the multiple models.

   [![Screenshot of the ontology agent summary and reasoning steps after combining multiple semantic models.](media/how-to-generate-from-semantic-models/agent-summary.png)](media/how-to-generate-from-semantic-models/agent-summary.png#lightbox)
4. Confirm that the expected objects from all semantic models are present in the ontology, with no unintended duplicates.

## Test and query the ontology

After you build the ontology with semantic model data, use the agent to validate it and run queries across all source models.

1. In the chat pane, select **Test the ontology** if the suggestion is available. Otherwise, ask the agent to generate representative questions and answer them by querying the bound data.

   [![Screenshot of an ontology test request and generated DAX questions and answers.](media/how-to-generate-from-semantic-models/test-after.png)](media/how-to-generate-from-semantic-models/test-after.png#lightbox)

   Review the generated queries and their results. In this example, the agent tests questions about Net Sales, Gross Margin %, products, stores, and inventory statuses.

   [![Screenshot of the agent's sample product, store, and inventory-status results.](media/how-to-generate-from-semantic-models/test-before.png)](media/how-to-generate-from-semantic-models/test-before.png#lightbox)

   If a result is blank or a query fails, verify the source data and bindings before relying on the answer.
2. Ask your own question in plain language to query across the combined models. For example, ask *Show sales by store alongside current inventory positions*, where sales data comes from one semantic model and inventory data comes from another.

   The agent uses the relationships between sales, locations, products, and inventory positions to answer the question, even though the data originates in separate semantic models.

Note

You need both Read and Build [permissions](/en-us/power-bi/connect-data/service-datasets-permissions#what-are-the-semantic-model-permissions) on the semantic models to generate an ontology from a semantic model and query the semantic models using ontology.

## Related content

- [Use the ontology agent (preview) in Fabric](how-to-use-ontology-agent)

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
