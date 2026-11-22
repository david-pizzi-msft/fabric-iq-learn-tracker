---
title: "Get started with Fabric IQ"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/get-started-with-fabric-iq](https://learn.microsoft.com/en-us/fabric/iq/get-started-with-fabric-iq) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Get started with Fabric IQ

Summarize this article for me

Fabric IQ is the part of Microsoft IQ that provides context on business entities and data. It elevates your data into the language of your businessâconcepts like *Customer*, *Shipment*, and *Asset*âso that people and AI agents can reason and act in business terms. Fabric IQ delivers this context through three layers: unified data in OneLake, business intelligence from Power BI semantic models, and operational intelligence from ontologies.

The IQ (preview) workload in Fabric provides a suite of items across these layers for analyzing, consuming, and operationalizing business context.

Fabric IQ isn't a single tool. It's a set of related capabilities you combine based on what you want to do. This article points you to the right starting point. For the full concept and the relationships between capabilities, see [What is Fabric IQ?](overview)

## Find your starting point

Find the job that matches your scenario, and then follow the entry article for that Fabric IQ capability.

| I want to... | Use this capability | Start here |
| --- | --- | --- |
| Define a shared business vocabularyâentities, relationships, and rulesâand ground AI agents in it | Ontology (preview) | [What is ontology?](ontology/overview) |
| Build curated analytics with trusted measures, hierarchies, and key performance indicators (KPIs) | Power BI semantic model | [Power BI semantic models in Fabric](../data-warehouse/semantic-models) |
| Plan, forecast, and report collaboratively in one no-code experience | Planning | [What is planning in Fabric?](plan/overview) |
| Query connected data with nodes, edges, and traversals for impact and dependency analysis | Graph | [Graph in Microsoft Fabric overview](../graph/overview) |
| Give users natural-language Q&A over a specific data domain | Data agent | [Fabric data agent concepts](../data-science/concept-data-agent) |
| Monitor live data, detect anomalies, and take governed action | Operations agent | [Create and configure operations agents](../real-time-intelligence/operations-agent) |
| Ask questions about your Power BI data inside Microsoft 365 Copilot Chat or Cowork | Integrations | [Fabric IQ in Microsoft 365 Copilot Chat](connectors/microsoft-365-copilot-overview) |

## Try an end-to-end tutorial

If you'd rather learn by building, follow a guided tutorial that walks through a complete scenario from setup to cleanup.

- **[Ontology tutorial](ontology/tutorial-0-introduction)** - Build your first ontology for a fictional retail company. You create entity types and relationships, bind streaming and static data, and explore the ontology using a built-in graph and ontology agent questions in natural language. This tutorial is the best starting point for the operational intelligence layer.
- **[Graph tutorial](../graph/tutorial-introduction)** - Load sample data, model nodes and edges, and query a graph with the query builder and Graph Query Language (GQL).
- **[Data agent tutorial](../data-science/data-agent-end-to-end-tutorial)** - Build a Fabric data agent that reasons over lakehouse data, both interactively and programmatically.

## Check tenant settings

Some Fabric IQ capabilities require a Fabric administrator to enable tenant settings before you begin. If you plan to use ontology (preview), review [Ontology required tenant settings](ontology/overview-tenant-settings). For data agent, see [Configure Fabric data agent tenant settings](../data-science/data-agent-tenant-settings).

## Related content

- [What is Fabric IQ?](overview)
- [What is ontology?](ontology/overview)
- [What is planning in Fabric?](plan/overview)
- [Graph in Microsoft Fabric overview](../graph/overview)
- [Fabric data agent concepts](../data-science/concept-data-agent)
- [Create and configure operations agents](../real-time-intelligence/operations-agent)
- [Power BI semantic models in Microsoft Fabric](../data-warehouse/semantic-models)
- [Fabric IQ in Microsoft 365 Copilot Chat](connectors/microsoft-365-copilot-overview)

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
