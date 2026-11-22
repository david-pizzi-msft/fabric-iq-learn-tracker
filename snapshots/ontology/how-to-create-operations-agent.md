---
title: "Create an operations agent grounded in an ontology (preview)"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-operations-agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/how-to-create-operations-agent) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create an operations agent grounded in an ontology (preview)

Summarize this article for me

Ontology (preview) integrates with [operations agent](../../real-time-intelligence/operations-agent) to continuously monitor your ontology, surface insights against your business goals, and recommend actionsâall grounded in the ontology's entity types and relationships.

Important

This feature is in [preview](../../fundamentals/preview).

## Prerequisites

Before you begin, make sure you have:

- A Microsoft Fabric workspace that contains at least one ontology (preview) item, accessible through the OneLake catalog. For more information, see [Create ontology (preview) item](tutorial-1-create-ontology#create-ontology-preview-item).
- The [operations agent prerequisites](../../real-time-intelligence/operations-agent#prerequisites), including the Microsoft Teams account and tenant settings for operations agent, Microsoft Copilot, and Azure OpenAI.

Note

Due to a current known issue, operations agent doesn't work with an ontology that uses semantic models for binding.

## Create operations agent with ontology source

Follow these steps to create a new operations agent that monitors an ontology (preview) item. For full details on each setup field, see [Create an operations agent](../../real-time-intelligence/operations-agent#create-an-operations-agent).

1. In your Fabric workspace, select **+ New item** and create a new **Operations agent** item.
2. On the **Agent setup** page, fill in the following fields:

   - **Agent instructions**: Add guidance for the agent's behavior. For example, *Monitor the freezer temperature and keep the temperature below 20.*
   - **Knowledge**: Select **Add data** and choose your ontology item.
   - **Actions** (optional): Define one or more actions the agent can recommend, such as *NotifyStoreOperations* with parameters like *StoreId* and *FreezerId*. If you add an action, configure it as described in [Configure an operations agent](../../real-time-intelligence/operations-agent-actions).
3. **Save** the agent.
4. Select **Generate playbook**. Review the concepts and rules in the playbook and confirm they reference the expected ontology entity types (such as *Store*, *Product*, and *Freezer*) and properties.
5. Select **Start** in the toolbar to start the agent.

[![Screenshot of the operations agent setup page with ontology as the knowledge source.](media/how-to-create-operations-agent/operations-agent.png)](media/how-to-create-operations-agent/operations-agent.png#lightbox)

## Receive notifications in Teams

Install the **Fabric Operations Agent** Teams app so the agent can contact you when it detects matching conditions in your ontology data. For more information, see [Receive messages from an operations agent](../../real-time-intelligence/operations-agent-actions#receive-messages-from-an-operations-agent).

When a recommendation arrives, review the context (which references ontology entity types, not raw tables), adjust any action parameters if needed, then select **Yes** to approve or **No** to reject.

## Related content

- [Operations agent overview](../../real-time-intelligence/operations-agent)
- [Operations agent limitations](../../real-time-intelligence/operations-agent-limitations)
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
