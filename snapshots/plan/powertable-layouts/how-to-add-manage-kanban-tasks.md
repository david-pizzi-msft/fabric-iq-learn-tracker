---
title: "Add and manage tasks in Kanban layout"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-add-manage-kanban-tasks](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-add-manage-kanban-tasks) · Last updated on **2026-10-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Add and manage tasks in Kanban layout

Summarize this article for me

This article explains how to add and manage tasks within the Kanban layout.

Important

- After you add, edit, duplicate, delete, or move tasks between stacks, select **Save to Database** to save your changes to the database.
- Use **Discard Changes** if you want to discard all the changes you made.
- Select **Preview Changes** to preview all changes you made. You can select the ones you want to discard and save the remaining to the database.

## View tasks

Each Kanban card displays the task title and the assigned user. Cards are organized into stacks based on the selected **Stack by** field.

[![Screenshot of the Kanban board with task cards in Backlog, In Progress, Review, Done, and To Do stacks.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/view-tasks.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/view-tasks.png#lightbox)

You can:

- Scroll vertically to view more tasks within a stack.
- Select **Load More Tasks** to add more stacks to the display for your viewing.
- See the number of tasks in each stack from the count displayed next to the stack header.
- Scroll horizontally to view more Kanban stacks or workflow stages.

  [![Screenshot of the Kanban board with the Load More Tasks button highlighted below the task stacks.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/load-more-tasks.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/load-more-tasks.png#lightbox)

## Add a task

To add a new task:

1. Select **Add Task** on the toolbar. The form editor opens.

   [![Screenshot of the PowerTable toolbar with Add Task highlighted above a Kanban board grouped by Status.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/add-task.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/add-task.png#lightbox)
2. Enter the task details in the form editor.

   [![Screenshot of the PowerTable Record Details form editor with new task details entered and the Apply button highlighted.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/add-task-details.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/add-task-details.png#lightbox)
3. Select **Apply**. The new task is added to the appropriate Kanban stack based on the entered **Stage**.
4. Select **Save to Database** to update the database table.

Alternatively, select the **+** icon on the required stage stack to add a new task in that stack.

[![Screenshot of PowerTable Kanban board with the plus icons highlighted on the In Progress and Review stacks for adding a new task.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/select-plus-button.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/select-plus-button.png#lightbox)

Note

Use [**Customize Form**](../powertable-how-to-generate-forms#customize-form) in the form editor to customize the form.

## Edit a task

To edit a task, follow these steps:

1. Select the vertical ellipsis on the task card you want to edit, and then select **Edit**. The form editor opens.

   [![Screenshot of a Kanban task card menu with Edit highlighted and the Record Details form editor open for the task.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/edit-task.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/edit-task.png#lightbox)
2. Update the required fields in the form editor.
3. Select **Apply** to save the changes.
4. Select **Save to Database** to update the changes in the database table.

Tip

You can also open the **Form Editor** for a task card by selecting anywhere on the card and then starting to edit the task details.

## View history

View the audit trail of changes made to a specific task by using the **History** tab.

To view task history:

1. Select a task in the Kanban layout.
2. In the **Record Details** side panel, select the **History** tab. The following image shows the **History** tab for a recently added task, displaying the changes recorded for the task.

   [![Screenshot of the Kanban layout with a selected task and the History tab highlighted in the Record Details panel.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/history-tab.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/history-tab.png#lightbox)
3. The **History** tab displays operations performed on the task record, including:

   - The task that you inserted or modified.
   - The field that you modified.
   - The previous and updated values.
   - The user who made the change.
   - The date and time of the change.

   The following image shows the updates made to an existing task along with all these details.

   [![Screenshot of Record Details History tab listing T-1008 updates: Progress changed from 0 to 10 and Status from Backlog to In Progress.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/history-details.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/history-details.png#lightbox)
4. Use the **History** tab to review task updates and track changes throughout the task lifecycle.
5. Within the tab, you can:

   - Use **Search** to find specific history entries.
   - Use **Filter** to filter the history and display specific changes based on action type (Insert, Update, or Delete), who made the change, when the change occurred, or who approved the change (if approvals are enabled).
   - Use [**Export**](../powertable-how-to-bulk-edit-data#export-history) to export the available history records.
   - Use **Audit logs** to review changes made to the task in detail. For more information, see [Audit logs](../powertable-how-to-view-audit-logs).

## Move stacks

You can rearrange stacks by using drag and drop. Drag a stack to the position where you want it to go to rearrange the stacks.

![Screenshot of the To Do stack being moved by drag and drop, with the hand cursor highlighted in a red box.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/move-stacks.png)

## Move tasks between stacks

You can rearrange task cards within a stack or between stacks.

- Drag and drop a task card within a stack to reposition the task visually.
- Drag a task card from one stack to another to update its **Stage**. After drag and drop, select **Save to Database** to update the changes in the database.

For example, when work begins, drag a task from **To Do** to **In Progress**. The task's **Stage** automatically updates to **In Progress**.

![Screenshot of a task board showing the Configure CI Pipeline card being dragged from the To Do stack toward the In Progress stack.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/move-tasks-between-stacks.png)

Alternatively, select the vertical ellipsis on a task card and use **Move To** to move it to another stage.

[![Screenshot of the Kanban board showing the vertical ellipsis menu on a task card with the Move To submenu open.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/move-to-stack-option.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/move-to-stack-option.png#lightbox)

## Duplicate a task

To duplicate a task, select the vertical ellipsis on the task card and then select **Duplicate**.

[![Screenshot of the Kanban board showing the vertical ellipsis menu on the Fix Payment Gateway Bug card with the Duplicate option highlighted.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/duplicate-task.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/duplicate-task.png#lightbox)

PowerTable duplicates the selected task and opens the form editor. You can edit the details you want in the form editor and select **Apply** to save changes.

## Delete a task

To delete a task, select the vertical ellipsis on the task card and then select **Delete**. Alternatively, right-click the card and select **Delete**.

[![Screenshot of the Kanban board showing the vertical ellipsis menu on the Add Audit Logging card with the Delete option highlighted.](../media/powertable-layouts/how-to-add-manage-kanban-tasks/delete-task.png)](../media/powertable-layouts/how-to-add-manage-kanban-tasks/delete-task.png#lightbox)

Note

The [**Manage Access**](../powertable-how-to-set-up-access-control#delete) menu controls your delete access. If **Delete** is disabled, select **Manage Access** to update the delete access settings.

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
