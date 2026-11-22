---
title: "Ontology (preview) tutorial part 4: Use the ontology agent"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-4-use-agent](https://learn.microsoft.com/en-us/fabric/iq/ontology/tutorial-4-use-agent) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Ontology (preview) tutorial part 4: Use the ontology agent

Summarize this article for me

In this tutorial step, use the ontology agent to ask questions in natural language and get answers grounded in the ontology's definitions and bindings.

Important

This feature is in [preview](../../fundamentals/preview).

## Get started with ontology agent

The [ontology agent (preview)](how-to-use-ontology-agent) is an AI-powered Copilot that helps you build and operate ontologies over the data in your Microsoft Fabric workspace by using a chat interface and natural language.

To access the ontology agent, select **Ontology agent** from the top ribbon in the home canvas. The agent opens in a pane on the right side of the screen.

[![Screenshot of opening the ontology agent from the ribbon.](media/tutorial-4-use-agent/open-agent.png)](media/tutorial-4-use-agent/open-agent.png#lightbox)

The agent opens in **Plan** mode by default. In Plan mode, the agent can query and explore the ontology, but it doesn't make any changes.

## Ask questions in natural language

Interact with the ontology agent to ask questions about the scenario in natural language.

Enter the following question in the ontology agent text box and send it: *Which frozen products are stocked at Tier 1 stores in the West?*

The agent reasons for a short time and then provides an answer from your ontology:

[![Screenshot of the agent listing three items in answer to the question.](media/tutorial-4-use-agent/answer.png)](media/tutorial-4-use-agent/answer.png#lightbox)

Explore the ontology further with the following queries, or create some of your own:

- Which of those inventory positions are below safety stock?
- Which affected stores had a qualifying refrigeration-temperature exception?
- What inbound shipments are expected for the affected products and stores?
- What is the on-shelf availability of frozen products for each store?
- Which of these stores have low on-shelf availability?
- Which of these stores have declining gross margin this month?
- Which of these stores have declining gross margin?

### Answer scenario question

Use the agent to answer the major question of the Lakeshore Retail scenario: *Which high-priority stores in the West have frozen products below safety stock, a recent refrigeration-temperature exception, and on-shelf availability below target? For each store, show the next inbound shipment and its expected arrival.*

The agent considers your ontology and queries your data sources, then provides an answer to the question.

[![Screenshot of the agent listing two stores with columns containing the requested information.](media/tutorial-4-use-agent/answer-main-scenario.png)](media/tutorial-4-use-agent/answer-main-scenario.png#lightbox)

## Next steps

In this step, you explored your ontology by using natural language queries to answer business questions with the ontology agent.

Next, continue to the [tutorial conclusion](tutorial-5-conclusion).

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
