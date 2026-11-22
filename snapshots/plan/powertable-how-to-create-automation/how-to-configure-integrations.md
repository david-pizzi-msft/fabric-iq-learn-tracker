---
title: "Integrations in automation"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-configure-integrations](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-configure-integrations) · Last updated on **2026-10-26**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Integrations in automation

Summarize this article for me

Learn how to use the PowerTable sync integration feature to bring in updated data from Power BI semantic model.

The **PowerTable** and **Power BI** integration lets you synchronize data from a Power BI semantic model so you can work with the latest analytical data in PowerTable.

This integration is a one-way sync from the semantic model into PowerTable, so changes made in PowerTable can't be synced back to the semantic model that you're syncing with.
To learn more, see [FAQs on connecting PowerTable to a semantic model](../powertable-how-to-connect-semantic-model#faq).

## Refresh semantic model

When you create a PowerTable sheet using a Power BI semantic model as the source, you can refresh the source (semantic model) so the table data is up to date.

To learn more, see [Refresh semantic model](../powertable-how-to-connect-semantic-model#refresh-semantic-model).

## Sync the semantic model in an automation

You can also synchronize the semantic model as part of an automation workflow to ensure that subsequent actions use the latest available data.

The following steps explain how to synchronize with the semantic model through the automation workflow.

1. In your automation workflow, select **Add Action**.
2. Select **Power BI** > **Sync semantic model**.
3. Add any subsequent actions required for your workflow.

The **Sync semantic model** action runs whenever the automation executes, allowing subsequent actions to work with the latest synchronized data.

[![Screenshot of an automation workflow with Add Action selected and the Power BI integration menu showing the Sync semantic model option.](../media/powertable-how-to-create-automation/how-to-add-integration-automation/sync-semantic-model.png)](../media/powertable-how-to-create-automation/how-to-add-integration-automation/sync-semantic-model.png#lightbox)

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
