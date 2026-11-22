---
title: "Create a data agent grounded in an ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-data-agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-data-agent) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create a data agent grounded in an ontology (preview)

Summarize this article for me

Ontology (preview) integrates with [Fabric data agent](../../data-science/concept-data-agent) to provide a data agent interface that you can use to ask questions in natural language and get answers grounded in the ontology's definitions and bindings.

Important

This feature is in [preview](../../fundamentals/preview).

## Prerequisites

Before you begin, make sure you have:

- A Microsoft Fabric workspace that contains at least one ontology (preview) item, accessible through the OneLake catalog. For more information, see [Create ontology (preview) item](tutorial-1-create-ontology#create-ontology-preview-item).
- Configured the [data agent tenant settings](../../data-science/data-agent-tenant-settings), including Copilot and Azure OpenAI.

Note

Due to a current known issue, data agent doesn't work with an ontology that uses semantic models for binding.

## Create data agent with ontology source

Follow these steps to create a new data agent that connects to your ontology (preview) item.

1. Go to your Fabric workspace. Use the **+ New item** button to create a new **Data agent** item.

   [![Screenshot of creating a new data agent item.](media/how-to-create-data-agent/data-agent-new.png)](media/how-to-create-data-agent/data-agent-new.png#lightbox)

   Tip

   If you don't see the data agent item type, make sure that it's enabled in your tenant as described in the [tutorial prerequisites](tutorial-0-introduction#prerequisites).
2. The agent opens when it's ready. Select **Add a data source**.

   [![Screenshot of adding a source to the data agent.](media/how-to-create-data-agent/add-source.png)](media/how-to-create-data-agent/add-source.png#lightbox)

   Search for your ontology item and select **Add**. Now your ontology is a source for the data agent.

When the agent is ready, the ontology and its entity types are visible in the Explorer.

[![Screenshot of the Retail Ontology Agent.](media/how-to-create-data-agent/data-agent.png)](media/how-to-create-data-agent/data-agent.png#lightbox)

## Provide agent instructions

Note

This step addresses a known issue affecting aggregation in queries.

Next, add a custom instruction to the agent.

1. Select **Agent instructions** from the menu ribbon.
2. At the bottom of the input box, add `Support group by in GQL`. This instruction enables better aggregation across ontology data.

   [![Screenshot of the agent instructions.](media/how-to-create-data-agent/agent-instructions.png)](media/how-to-create-data-agent/agent-instructions.png#lightbox)
3. The agent applies the instruction automatically. Optionally, close the **Agent instructions** tab.

## Query agent with natural language

Next, explore your ontology with natural language questions.

Example prompts:

- *For each store, show any freezers operated by that store that ever had a humidity lower than 46 percent.*
- *What is the top product by revenue across all stores?*

Notice that the responses reference entity types and their relationships, not just raw tables.

[![Screenshot of the result of a query.](media/how-to-create-data-agent/query-result.png)](media/how-to-create-data-agent/query-result.png#lightbox)

Tip

If you see errors that say there's no data while running the example queries, wait a few minutes to give the agent more time to initialize. Then, run the queries again.

## Related content

- [Data agent overview](../../data-science/concept-data-agent)
- [Agent integration options for ontology (preview)](concepts-agent-integration)

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
