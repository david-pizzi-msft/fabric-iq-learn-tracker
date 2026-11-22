---
title: "Create a planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-get-started](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-get-started) · Last updated on **2026-10-01**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create a planning sheet

Summarize this article for me

This article describes how to get started with your first planning sheet inside planning in Fabric.

Note

Planning in Fabric IQ is now available to organizations worldwide as part of the Microsoft Fabric SKU. New billing meters are also introduced and are now available for billing.

## Prerequisites

Before you set up planning sheets, make sure you have the following prerequisites:

- The overall [prerequisites for planning in Fabric](overview-prerequisites), including the required tenant and capacity settings.
- Data in a [Power BI semantic model](../../data-warehouse/semantic-models).

Important

- The connection-based flow for semantic models is deprecated. You can now connect to a semantic model directly by using your signed-in identity without configuring a shared cloud connection.
- Existing artifacts built by using the shared cloud connections auto-switch, and rows appear on the sheet based on the RLS evaluated against the signed-in user.
- Cloud connection owners can delete the old connections.

## Create plan item

1. From your Fabric workspace, select **New item** > **Plan**.

   [![Screenshot of creating a new plan item.](media/planning-how-to-get-started/new-plan-1.png)](media/planning-how-to-get-started/new-plan-1.png#lightbox)
2. On **New Plan**, enter a name for your plan, and then select **Create**.

   ![Screenshot of providing name and location details for a new plan.](media/planning-how-to-get-started/new-plan-2.png)

   Note

   When you create a plan item, you also automatically create a Fabric SQL database in your workspace. This database stores your plan report's metadata.

## Create your planning sheet

1. In your new plan item, you see options to get your data from the semantic model or from Excel, and to create a planning sheet from it. Alternatively, start with a planning sheet and then connect it to data.

   [![Screenshot showing the options to create a new planning sheet.](media/planning-how-to-get-started/create-sheet.png)](media/planning-how-to-get-started/create-sheet.png#lightbox)
2. Select **Planning**, enter a name for the new planning sheet, and then select **Create**.

   [![Screenshot of naming a new planning sheet.](media/planning-how-to-get-started/new-plan-creation-1.png)](media/planning-how-to-get-started/new-plan-creation-1.png#lightbox)

You created a new planning sheet.

[![Screenshot of a new planning sheet.](media/planning-how-to-get-started/new-planning-sheet.png)](media/planning-how-to-get-started/new-planning-sheet.png#lightbox)

## Add the semantic model

Connect your plan item to a semantic model that contains your data, so you can start planning. The result of this step is that your planning sheet has access to data in the semantic model.

Important

The connection-based flow for semantic models is deprecated. You can now connect to a semantic model directly using your signed-in identity without configuring a shared cloud connection.

1. In your new planning sheet, in the **Data** pane, select **Add**.
2. In the **Select Semantic Model** popup, select the textbox to connect to your semantic model.

   [![Screenshot of connecting to a semantic model.](media/planning-how-to-get-started/semantic-model-connection.png)](media/planning-how-to-get-started/semantic-model-connection.png#lightbox)
3. Select the semantic model, and then select **Add**.

   [![Screenshot of choosing a semantic model.](media/planning-how-to-get-started/new-plan-4.png)](media/planning-how-to-get-started/new-plan-4.png#lightbox)
4. Select **Connect** to connect to the selected semantic model.

   [![Screenshot of selecting connect to connect to the semantic model.](media/planning-how-to-get-started/connect-semantic-model.png)](media/planning-how-to-get-started/connect-semantic-model.png#lightbox)
5. The semantic model is connected to your planning sheet. The **Data** pane displays all your loaded data tables, columns, hierarchies, and measures.

   [![Screenshot of connected semantic model and data in data pane.](media/planning-how-to-get-started/connected-semantic-model.png)](media/planning-how-to-get-started/connected-semantic-model.png#lightbox)
6. Assign the data you want to **Rows**, **Columns**, and **Values** fields. Now you have your first planning sheet.

   [![Screenshot of the created planning sheet.](media/planning-how-to-get-started/planning-sheet.png)](media/planning-how-to-get-started/planning-sheet.png#lightbox)

Note

Each **Plan** item is associated with a single semantic model. To connect to a different semantic model, [create a new plan item](#create-plan-item).

You can create multiple plan items within the same billing session. All items you create use the same active billing session, regardless of the number of items or use cases. For more information, see [Billing and usage for Fabric Planning](resources/billing-fabric-plan#faqs).

## Optional: Connect to a database for collaboration

If you want to collaborate with others on this planning sheet, create a database connection for your plan item to store comments and other collaboration details. For more information, see [Create a database connection for collaboration](planning-how-to-create-database-connection).

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
