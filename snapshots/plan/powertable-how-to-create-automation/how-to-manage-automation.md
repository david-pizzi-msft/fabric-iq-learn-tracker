---
title: "Manage automations"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-manage-automation](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-create-automation/how-to-manage-automation) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Manage automations

Summarize this article for me

This article explains how to manage automation workflows you created in PowerTable.

## Manage workflows

You can create multiple automation workflows for a table. To view the workflows that you created, select **Setup** > **Automations**. The following screen opens.

[![Screenshot of the Automations list showing two workflows with the enable/disable toggle and More options highlighted.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/manage-automations.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/manage-automations.png#lightbox)

- **Enable or disable a workflow:** Use the toggle to enable or disable a workflow.
- **Duplicate a workflow:** Select **More options** (**...**), and then select **Duplicate** to create a copy of a workflow. Modify the copied workflow as needed instead of creating one from scratch.
- **Delete a workflow:** Select **More options** (**...**), and then select **Delete** to permanently remove a workflow. You must disable a workflow before you can delete it.
- **Search**: Use the search box to find a specific automation flow by name.

## View run history

Use the **Run History** pane to monitor workflow executions and review the status of each run. You can see the users who initiated the automations, when they initiated them, the duration and time of automation, and whether it succeeded or failed.

Failed automations trigger Microsoft Teams notifications for the user who initiated the automation.

Open the required automation workflow and select **Run History**.

[![Screenshot of the Get Order automation with the Run History pane open, listing eight runs with Job ID, Started At, Status, Duration, and Details.](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/view-run-history.png)](../media/powertable-how-to-create-automation/how-to-configure-automation-workflows/view-run-history.png#lightbox)

The pane lists all workflow runs along with details such as:

| Column | Description |
| --- | --- |
| **Job ID** | Unique identifier for the workflow run. |
| **Started At** | Date and time when the workflow started. |
| **Status** | Current execution status, such as **Success** or **Failed**. |
| **Duration** | Total time taken to complete the workflow run. |
| **Started By** | User who triggered the workflow. |
| **Details** | Select **View Details** to view the full execution details for the workflow run. |

You can also use the following options:

- **Retry**: Failed runs display a **Retry** option. Select it to rerun the workflow after resolving the issue.
- **Refresh**: Use **Refresh** to refresh the run history and display the status of latest workflow runs.

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
