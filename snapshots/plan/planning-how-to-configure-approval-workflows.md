---
title: "Configure approval workflows"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-configure-approval-workflows](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-configure-approval-workflows) · Last updated on **2026-07-23**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure approval workflows

Summarize this article for me

Approval workflows route planning data updates through one or more approval levels before finalizing changes. They help maintain data integrity by ensuring that updates are reviewed before they're committed to the planning sheet.

When a user updates a data input or forecast value, the approval workflow can automatically:

- Send Microsoft Teams notifications.
- Update task and approval statuses.
- Update related field values.

Approvers can then review the request and either approve or reject it.

You can configure approval workflows in one of the following ways:

- By using [scripts](#configure-approval-workflows-by-using-scripts).
- By using the [Approval Workflow interface](#configure-approval-workflows-without-scripting).

## Configure approval workflows by using scripts

You can create custom approval workflows by writing scripts in the **On Change Formula** section of data input and forecast columns. The scripts run automatically whenever a column value changes.

The following example creates a two-level approval workflow that uses the following columns:

- *Task Status*
- *Manager Approval*
- *Director Approval*
- *Associate Email*
- *Manager Email*
- *Director Email*

[![Screenshot of a planning sheet configured for a script-driven approval workflow with Task Status, Manager Approval, Director Approval, and email fields.](media/planning-how-to-configure-approval-workflows/script-driven-approval-workflow.png)](media/planning-how-to-configure-approval-workflows/script-driven-approval-workflow.png#lightbox)

**Single Select** columns let users select a single value from a predefined list. For more information, see [Single Select columns](planning-how-to-insert-columns/how-to-insert-dropdown-columns).

To create this approval workflow:

1. On the **Planning** tab, select **Insert Column** > **Text**.
2. Create the following text columns:

   - *Associate Email*
   - *Manager Email*
   - *Director Email*

   Enter the appropriate email address in each column.
3. On the **Planning** tab, select **Insert Column** > **List** > **Single Select**.
4. Create a column named *Task Status*.

   Configure the following options:

   - *InProgress*
   - *Submit For Review*
   - *Approved*
   - *Reopened*
5. In the **On Change Formula** editor, enter the following script, and then select **Create**.

   ```
   // Notify the manager when a request is submitted.
   IF(THIS == 'Submit For Review', NOTIFY_USER([Manager Email]), "")

   // Update the manager approval status to Pending.
   IF(THIS == 'Submit For Review', SETVALUE([Manager Approval], 'Pending'), "")
   ```
6. Create a **Single Select** column named *Manager Approval*.

   Configure the following options:

   - *Pending*
   - *Approved*
   - *Rejected*
   - *Reopened*
7. In the **On Change Formula** editor, enter the following script, and then select **Create**.

   ```
   // Notify the director and the submitter when the manager approves the request.
   IF(THIS == 'Approved', NOTIFY_USER([Associate Email]), "")
   IF(THIS == 'Approved', NOTIFY_USER([Director Email]), "")

   // Update the director approval status to Pending.
   IF(THIS == 'Approved', SETVALUE([Director Approval], 'Pending'), "")

   // Notify the associate and reopen the task when the request is rejected.
   IF(THIS == 'Rejected', NOTIFY_USER([Associate Email]), "")
   IF(THIS == 'Rejected', SETVALUE([Task Status], 'Reopened'), "")

   // Notify the associate when the request is reopened.
   IF(THIS == 'Reopened', NOTIFY_USER([Associate Email]), "")
   IF(THIS == 'Reopened', SETVALUE([Task Status], 'Reopened'), "")
   ```
8. Create a **Single Select** column named *Director Approval*.

   Configure the following options:

   - *Pending*
   - *Approved*
   - *Rejected*
   - *Reopened*
9. In the **On Change Formula** editor, enter the following script, and then select **Create**.

   ```
   // If the director approves the request, update the task status and notify the associate and manager.
   IF(THIS == 'Approved', SETVALUE([Task Status], 'Approved'), "")
   IF(THIS == 'Approved', NOTIFY_USER([Associate Email]), "")
   IF(THIS == 'Approved', NOTIFY_USER([Manager Email]), "")

   // If the director rejects the request, reopen the task, reopen the manager approval status, and notify the associate and manager.
   IF(THIS == 'Rejected', SETVALUE([Task Status], 'Reopened'), "")
   IF(THIS == 'Rejected', SETVALUE([Manager Approval], 'Reopened'), "")
   IF(THIS == 'Rejected', NOTIFY_USER([Associate Email]), "")
   IF(THIS == 'Rejected', NOTIFY_USER([Manager Email]), "")
   ```

### How the approval workflow works

After you update a data input value, such as *Actuals*, set **Task Status** to **Submit For Review**. This action triggers the script configured in the **On Change Formula** section and starts the approval workflow.

[![Screenshot of the planning sheet showing the Task Status column configured with an On Change Formula script.](media/planning-how-to-configure-approval-workflows/task-status-submit-for-review.png)](media/planning-how-to-configure-approval-workflows/task-status-submit-for-review.png#lightbox)

The approval status columns also contain **On Change Formula** scripts that run automatically when their values change. The following example shows the script configured for the **Manager Approval** column.

[![Screenshot of the On Change Formula editor for the Manager Approval column.](media/planning-how-to-configure-approval-workflows/manager-approval-on-change-formula.png)](media/planning-how-to-configure-approval-workflows/manager-approval-on-change-formula.png#lightbox)

The workflow uses the following functions:

- **SETVALUE** updates related fields when an approval status changes.
- **NOTIFY\_USER** sends Microsoft Teams notifications to approvers or requesters.

The workflow can automatically:

- Update related approval status fields.
- Notify the next approver in the workflow.
- Reopen tasks when a request is rejected.
- Mark tasks as approved after all approval levels are completed.

The following examples show how the workflow behaves.

#### Submit a request for approval

When a user changes **Task Status** to **Submit For Review**, the **Manager Approval** status is automatically updated to **Pending**.

[![Screenshot showing the Manager Approval status updated to Pending after Task Status is changed to Submit For Review.](media/planning-how-to-configure-approval-workflows/manager-approval-pending.png)](media/planning-how-to-configure-approval-workflows/manager-approval-pending.png#lightbox)

#### Approve a request at the manager level

When the manager approves the request, the **Director Approval** status updates to **Pending**.

[![Screenshot showing the Manager Approval workflow updating the Director Approval status to Pending after the manager approves the request.](media/planning-how-to-configure-approval-workflows/director-approval-pending.png)](media/planning-how-to-configure-approval-workflows/director-approval-pending.png#lightbox)

#### Reject a request at the manager level

When the manager rejects the request, **Task Status** updates to **Reopened**.

[![Screenshot showing the Manager Approval workflow updating Task Status to Reopened after the manager rejects the request.](media/planning-how-to-configure-approval-workflows/task-status-reopened-after-manager-rejection.png)](media/planning-how-to-configure-approval-workflows/task-status-reopened-after-manager-rejection.png#lightbox)

#### Complete the approval workflow

When the final approver approves the request, **Task Status** updates to **Approved**.

[![Screenshot showing the Task Status updated to Approved after the final approval.](media/planning-how-to-configure-approval-workflows/task-status-approved.png)](media/planning-how-to-configure-approval-workflows/task-status-approved.png#lightbox)

#### Reopen a rejected request

If the final approver rejects the request, both the previous approval level and **Task Status** update to **Reopened**.

[![Screenshot showing the approval status and Task Status updated to Reopened after the final rejection.](media/planning-how-to-configure-approval-workflows/reopened-after-final-rejection.png)](media/planning-how-to-configure-approval-workflows/reopened-after-final-rejection.png#lightbox)

Tip

You can customize the approval workflow by modifying the scripts in the **On Change Formula** section.

## Configure approval workflows without scripting

You can also create approval workflows without writing scripts by using the **Approval Workflow** interface.

To open the **Approval Workflow** interface:

1. On the **Model** tab, select **Approval**.

   [![Screenshot showing the Approval command on the Model tab.](media/planning-how-to-configure-approval-workflows/open-approval-workflow.png)](media/planning-how-to-configure-approval-workflows/open-approval-workflow.png#lightbox)
2. The **Approval Workflow** window opens.

   [![Screenshot of the Approval Workflow window.](media/planning-how-to-configure-approval-workflows/approval-workflow-window.png)](media/planning-how-to-configure-approval-workflows/approval-workflow-window.png#lightbox)

### Configure approval levels

The first approval level tracks the overall task status. Additional levels represent the approval stages.

To configure approval levels:

1. Select the edit icon and enter a name for the task status column.

   This step creates a **Single Select** column with predefined values such as *In Progress*, *Submitted*, and *Reopened*.
2. Select the users who can update the task status and receive approval notifications.

   You can:

   - Select users directly from the list.
   - Select **Column** to use email addresses stored in a text column.
3. Select the edit icon and enter a name for the first approval level.

   This step creates a **Single Select** column with predefined values such as *Pending*, *Approved*, *Rejected*, and *Reopened*.
4. Select one or more approvers.
5. Optionally, select **Add** to create additional approval levels.
6. Select **Next**.

   [![Screenshot showing approval levels configured in the Approval Workflow window.](media/planning-how-to-configure-approval-workflows/configure-approval-levels.png)](media/planning-how-to-configure-approval-workflows/configure-approval-levels.png#lightbox)

Note

The **Column** option is available only when the planning sheet contains one or more text columns that store email addresses.

### Configure workflow settings

Configure the following settings before you create the approval workflow.

#### Reset on rejection

Turn on **Reset on Rejection** to reset all previous approval levels to *In Progress* or *Reopened* when the final approver rejects a request.

By default, this option is turned off.

#### Teams notifications

Configure Microsoft Teams notifications for the following users:

- **Approvers** receive notifications when data is submitted for approval.
- **Submitters** receive notifications when an approval decision is made.

By default, Microsoft Teams notifications are turned on.

[![Screenshot of the Approval Workflow settings page showing the Reset on Rejection option and Teams notification settings.](media/planning-how-to-configure-approval-workflows/configure-workflow-settings.png)](media/planning-how-to-configure-approval-workflows/configure-workflow-settings.png#lightbox)

Select **Submit** to create the approval workflow.

## Approval workflow behavior

After you create the approval workflow, the required **Single Select** columns are automatically added to the planning sheet.

### Create workflow columns

When you create the workflow, the planning sheet automatically adds the **Task Status**, **Manager Approval**, and **Director Approval** columns.

[![Screenshot showing the Task Status, Manager Approval, and Director Approval columns added to the planning sheet.](media/planning-how-to-configure-approval-workflows/approval-workflow-columns-created.png)](media/planning-how-to-configure-approval-workflows/approval-workflow-columns-created.png#lightbox)

### Submit a request

After updating a data input value, such as *Actuals*, set **Task Status** to **Submitted**.

The workflow sends a Microsoft Teams notification to the configured manager and updates **Manager Approval** to **Pending**.

[![Screenshot showing the Task Status updated to Submitted and the Manager Approval status updated to Pending.](media/planning-how-to-configure-approval-workflows/request-submitted-manager-pending.png)](media/planning-how-to-configure-approval-workflows/request-submitted-manager-pending.png#lightbox)

### Approve a request at the manager level

When the manager approves the request, the workflow sends a Microsoft Teams notification to the configured director and updates **Director Approval** to **Pending**.

[![Screenshot showing the Approval Workflow interface updating Director Approval to Pending after the manager approves the request.](media/planning-how-to-configure-approval-workflows/director-approval-pending-notification.png)](media/planning-how-to-configure-approval-workflows/director-approval-pending-notification.png#lightbox)

### Reject a request at the manager level

When the manager rejects the request, update **Task Status** to **Reopened**.

[![Screenshot showing the Approval Workflow interface updating Task Status to Reopened after the manager rejects the request.](media/planning-how-to-configure-approval-workflows/task-status-reopened-after-manager-rejection-interface.png)](media/planning-how-to-configure-approval-workflows/task-status-reopened-after-manager-rejection-interface.png#lightbox)

### Complete the approval workflow

If the director approves the request, the workflow is complete.

If the director rejects the request, the workflow updates **Manager Approval** to **Reopened**.

[![Screenshot showing the Manager Approval status updated to Reopened after the director rejects the request.](media/planning-how-to-configure-approval-workflows/director-rejection-manager-reopened.png)](media/planning-how-to-configure-approval-workflows/director-rejection-manager-reopened.png#lightbox)

### Reset approval levels after a rejection

If you enable [Reset on Rejection](#reset-on-rejection), the workflow updates both **Task Status** and **Manager Approval** to **Reopened** when the director rejects the request.

[![Screenshot showing the Task Status and Manager Approval columns updated to Reopened after the Reset on Rejection option is applied.](media/planning-how-to-configure-approval-workflows/reset-on-rejection-results.png)](media/planning-how-to-configure-approval-workflows/reset-on-rejection-results.png#lightbox)

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
