---
title: "Rules in ontology (preview) (with Fabric Activator) - Old experience"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-use-rules](https://learn.microsoft.com/en-us/fabric/iq/ontology/old-experience/how-to-use-rules) · Last updated on **2026-09-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Rules in ontology (preview) (with Fabric Activator) - Old experience

Summarize this article for me

Important

This article is about the **old experience** of ontology (preview). You can't create ontology items with the old experience anymore through the ontology interface in Fabric. It's still possible to create instances of the old experience using the ontology APIs and CI/CD.

Use this documentation only if you're maintaining an existing old experience item. Otherwise, see the [ontology (preview) new experience documentation](../overview).

The old experience of ontology retires on Jan 31, 2027.

The *rules* feature of ontology (preview) lets you automate and manage event-driven alerts directly within your entity types. By using the integrated capabilities of [Fabric Activator](../../../real-time-intelligence/data-activator/activator-introduction), you can achieve real-time monitoring and response for your business entities. This feature allows you to define alerts that monitor properties across every instance of an entity type, to ensure comprehensive, ongoing oversight.

Important

This feature is in [preview](../../../fundamentals/preview).

Rules transform ontologies from static information models to operationalized ones. The ontology becomes capable of automatically initiating business processes through alerts and automated actions, all within a seamless and context-aware environment. This feature helps you unlock automation capabilities without needing to switch between tools or write custom code, to streamline workflows and enhance efficiency.

Note

Rules in ontology (preview) rely on Fabric Activator and are subject to Fabric Activator costs. For more information about Fabric Activator pricing, see [Understand Activator capacity consumption, usage reporting, and billing](../../../real-time-intelligence/data-activator/activator-capacity-usage).

## Prerequisites

Before defining rules, ensure you have the following prerequisites:

- A [Fabric workspace](../../../fundamentals/create-workspaces) with a Microsoft Fabric-enabled [capacity](../../../enterprise/licenses#capacity).
- **Ontology item (preview)** enabled on your tenant.
- An ontology (preview) item with [data binding](how-to-bind-data) completed for at least one time series property.

## Key concepts

Rules use the following ontology (preview) concepts. For definitions of these terms, see the [Ontology (preview) glossary](../resources-glossary).

- *Entity type*
- *Rule*
- *[Fabric Activator](../../../real-time-intelligence/data-activator/activator-introduction)*

## Create a rule

1. Open the rules configuration from the Home configuration canvas or from the entity type details.

   To open rules from the configuration canvas, select **...** next to an entity type name to open its options menu. Hover over **Manage rules**, and then select **Add rule**.

   [![Screenshot of Manage rules from the Home configuration canvas.](media/how-to-use-rules/add-rules-canvas.png)](media/how-to-use-rules/add-rules-canvas.png#lightbox)

   To open rules from the entity type details view (any tab), select **Manage rules** > **Add rule**.

   [![Screenshot of View rules from the entity type details Configuration tab.](media/how-to-use-rules/add-rules-preview.png)](media/how-to-use-rules/add-rules-preview.png#lightbox)
2. The **Add rule** panel opens and displays the rule configuration options.

   [![Screenshot of Add rule panel.](media/how-to-use-rules/add-rule.png)](media/how-to-use-rules/add-rule.png#lightbox)
3. Configure the rule, including **Details**, **Monitor**, **Conditions**, **Actions**, and **Save location**.

   While configuring, keep the following notes in mind:

   - Ontology-authored rules support temporal conditions (for example, thresholds exceeded over a time window) and aggregations through the Fabric Activator condition configuration. The conditions evaluate per entity instance. For more information about using these fields, see [Create a rule in Fabric Activator](../../../real-time-intelligence/data-activator/activator-create-activators).
   - By default, ontology rules are saved to a new Fabric Activator item. If you want to choose an existing Fabric Activator item instead, select it manually from the **Save location** step. Consider saving all rules for an ontology to the same workspace and Fabric Activator item.

     ![Screenshot of changing the save location.](media/how-to-use-rules/save-location.png)
4. When you're finished configuring, select **Create**.
5. The rule is now visible in the **Rules** panel. To start or stop the rule, toggle the switch next to the rule name.

   [![Screenshot of the option to disable a rule.](media/how-to-use-rules/completed-rule.png)](media/how-to-use-rules/completed-rule.png#lightbox)

## View and edit a rule

You can reopen the **Rules** panel at any time by selecting **View rules** from any of the **Manage rules** dialogs described in [Create a rule](#create-a-rule).

In the **Rules** pane, you can:

- Change which Fabric Activator item stores ontology rules by selecting **Edit** next to the Activator name.

  ![Screenshot of editing the overall activator instance used for ontology rules.](media/how-to-use-rules/edit-activator-overall.png)
- Manage the rule by selecting **...** next to the rule name to open its options menu. From here, you can **Edit** the rule, **Delete** the rule, or **Open in Activator**. Opening a rule in Fabric Activator lets you make more edits to the rule and analyze its conditions and actions. For more information, see [Create a rule in Fabric Activator](../../../real-time-intelligence/data-activator/activator-create-activators).

  ![Screenshot of the options for a rule.](media/how-to-use-rules/rule-options.png)

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
