---
title: "Agent integration options for ontology (preview) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/concepts-agent-integration](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/concepts-agent-integration) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Agent integration options for ontology (preview) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

An ontology (preview) item gives AI agents a governed, shared understanding of your business, including key entity types, relationships, definitions, rules, and source mappings. When an agent uses an ontology as context, it produces responses that are more grounded, explainable, and consistent across systems instead of relying only on raw data or prompts. This article explains how agents consume ontology context and helps you choose the right agent for your scenario.

Important

This feature is in [preview](../../../fundamentals/preview).

## How agents use ontology as a source

AI agents help you move from static analysis to interactive, goal-oriented workflows by understanding natural language, planning steps, calling tools, and taking action on your behalf. When agents use an ontology as context, they gain a governed understanding of the business instead of a table-by-table view of raw data.

Grounding an agent in an ontology provides several benefits:

- **Business meaning**: The agent reasons over entity types (such as *Store*, *Product*, or *Freezer*) and their relationships, not just raw tables and columns.
- **Consistency**: Every agent that shares the ontology uses the same definitions, rules, and metrics, so answers stay consistent across teams and tools.
- **Governance**: The ontology carries data bindings, provenance, and access controls, so agents respect the same governed model as the rest of Fabric IQ.
- **Explainability**: Responses reference well-defined concepts and relationships, which makes answers easier to trust and validate.

Connect an ontology to several agents. The following agents currently support ontology as a source:

- [Fabric operations agent](#fabric-operations-agent)
- [Fabric data agent](#fabric-data-agent)
- [Foundry IQ agent](#foundry-iq-agent)
- [Copilot Studio agent](#copilot-studio-agent)
- [Custom agents with ontology MCP server](#custom-agents-with-ontology-mcp-server)

## Choose an agent

Use the following table to compare the agents that ontology supports and decide which one fits your scenario.

| Agent | Primary experience | Best for | Audience |
| --- | --- | --- | --- |
| **Fabric operations agent** | Continuous monitoring with recommended actions | Real-time monitoring, alerting, and automated actions against business goals | Operations teams |
| **Fabric data agent** | Conversational Q&A inside Fabric | Interactive analytics over governed Fabric data with ontology context | Data analysts and business users |
| **Foundry IQ agent** | Custom developer agent with tool calling | Advanced, customizable agents that integrate with enterprise systems | Developers |
| **Copilot Studio agent** | Low-code conversational agent | Business-friendly agents and workflow automation without heavy coding | Business makers and low-code developers |
| **Custom agents with ontology MCP server** | Any MCP-compatible AI client or custom agent | Connecting external or custom AI systems and tools to ontology through the Model Context Protocol (MCP) | Developers |

## Supported agent descriptions

### Fabric operations agent

A [Fabric operations agent](../../../real-time-intelligence/operations-agent) continuously monitors your ontology, surfaces insights against your business goals, and monitors your business signalsâall grounded in the ontology's entity types and relationships. Each operations agent is a dedicated Fabric item designed for a specific business process. You configure the agent with instructions and rules in natural language, and it can notify you in Microsoft Teams or take configured actions when it detects a condition that matches your goals.

Use Fabric operations agent with ontology when you want continuous, real-time monitoring of ontology data and automated recommendations or actions, rather than interactive question-and-answer.

For details about setting up a Fabric operations agent with ontology as source, see [Create an operations agent grounded in an ontology](../how-to-create-operations-agent).

### Fabric data agent

A [Fabric data agent](../../../data-science/concept-data-agent) lets you build a conversational Q&A system over governed enterprise data in Fabric. You create the agent directly in Fabric and add your ontology as a data source, so users can ask business questions in natural language and receive answers grounded in the ontology's definitions and bindings. Ontology context adds richer business meaning, relationships, and consistency to the agent's responses.

Use Fabric data agent with ontology when you want an interactive analytics experience inside Fabric, and you want a straightforward path to connect ontology alongside other Fabric data sources.

For details about setting up a Fabric data agent with ontology as source, see [Ontology tutorial part 4: Consume ontology from agents](../tutorial-4-create-data-agent).

### Foundry IQ agent

A [Microsoft Foundry](/en-us/azure/foundry/what-is-foundry) agent helps developers build advanced, customizable agents that can reason over ontology context, call tools, and integrate with enterprise systems. Foundry IQ exposes the ontology as a reusable knowledge source and knowledge base that the agent queries at runtime, which gives the agent a semantically rich, governed view of your Fabric data as a single source of truth.

Use Foundry IQ agent with ontology when you're a developer who needs full customization, tool calling, and integration with enterprise systems beyond Fabric.

For details about setting up a Foundry IQ agent with ontology as a source, see [Build a Foundry IQ agent grounded in an ontology](../how-to-create-agent-foundry-iq).

### Copilot Studio agent

A [Copilot Studio](/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio) agent lets business analysts, developers, and domain experts create conversational agents without extensive coding. You connect the ontology through the Fabric IQ MCP tool, so the agent understands your organization's data structure and business context and can answer business questions or automate workflows.

Use Copilot Studio agent with ontology when you want a low-code path for business and makers to build conversational agents grounded in ontology.

For details about setting up a Copilot Studio agent with ontology as source, see [Build a Copilot Studio agent grounded in an ontology](../how-to-create-agent-copilot-studio).

### Custom agents with ontology MCP server

An ontology can function as a Model Context Protocol (MCP) server, exposing an API so external AI systems and custom agents can discover and interact with it through MCP. This capability extends those systems beyond their own data and reasoning by grounding them in the ontology's entity types, relationships, and definitions. You integrate ontology into custom AI workflows by connecting any MCP-compatible client.

Use custom agents with the ontology MCP server when you want to connect your own MCP-compatible client or custom-built agent to ontology, rather than a prebuilt Fabric, Foundry, or Copilot Studio agent.

For details about consuming ontology through the Model Context Protocol, see [Consume ontology (preview) as an MCP server](../how-to-use-ontology-mcp-server).

## Related content

- [What is ontology (preview)?](overview)
- [Ontology tutorial part 4: Consume ontology from agents](../tutorial-4-create-data-agent)
- [Create an operations agent grounded in an ontology](../how-to-create-operations-agent)
- [Build a Foundry IQ agent grounded in an ontology](../how-to-create-agent-foundry-iq)
- [Build a Copilot Studio agent grounded in an ontology](../how-to-create-agent-copilot-studio)
- [Consume ontology (preview) as an MCP server](../how-to-use-ontology-mcp-server)

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
