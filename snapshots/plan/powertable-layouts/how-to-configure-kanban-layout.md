---
title: "Configure Kanban layout"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-configure-kanban-layout](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-configure-kanban-layout) · Last updated on **2026-10-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure Kanban layout

Summarize this article for me

Kanban layout displays records as cards organized into columns or stacks based on a selected field. It provides a visual way to track work, monitor progress, and move records through different stages of a workflow.

Each card represents a single record and displays key information, such as the task name, assignee, and other configured fields. You can drag cards between the stacks to update their status, edit records directly from the board, and quickly identify work that requires attention.

This article explains how to create a Kanban layout by using a sample **Tasks** table.

## Use cases

Use the Kanban layout to:

- Track work items through stages such as **Backlog**, **To Do**, **In Progress**, **Review**, and **Done**.
- Monitor task ownership by displaying the assignee on each card.
- Visualize the distribution of work across different workflow stages.
- Drag and drop tasks between the stacks to update their status.
- Identify bottlenecks and prioritize pending work.
- Manage software development tasks, project activities, support tickets, approval workflows, or any process that progresses through defined stages.

## Prerequisites

Before you create a Kanban layout, ensure that your table includes the following mandatory fields:

- **Task ID:** Uniquely identifies each Kanban card. Configure this field as the **primary key**.
- **Task Name:** Contains the name or title displayed on each Kanban card.
- **Stack By:** Contains the values used to group Kanban cards into columns, such as **To Do**, **In Progress**, and **Completed**.
- Ensure that all fields used in the Kanban layout have the appropriate data types configured in the table.

## Create the Kanban layout

This section explains how to create the Kanban layout to organize records into stacks based on a selected field. In this example, you create a Kanban board for a **Tasks** table, where tasks are grouped by their status or their workflow stage.

The sample **Tasks** table contains the following fields: Task ID, Title, Status, Priority, Assignee, Sprint, Due Date, Story Points, Category, Description, and Progress.

1. In the **PowerTable** tab, go to **Layout** > **Kanban**. The **Board Layout Configuration** opens.

   [![Screenshot of the PowerTable tab with the Layout menu open and the Kanban option highlighted.](../media/powertable-layouts/how-to-configure-kanban-layout/select-kanban.png)](../media/powertable-layouts/how-to-configure-kanban-layout/select-kanban.png#lightbox)
2. Configure the following properties:

   - **Task ID**: Select the column that uniquely identifies each task. In this example, select **Task ID**.
   - **Task Name**: Select the column to display as the primary label on each Kanban card. In this example, select **Title**.
   - **Stack by**: Select the column used to group tasks into Kanban stacks. In this example, select **Status**.
   - **Assignee** (optional): Select the column that displays the task owner on each card. In this example, select **Assignee**.
   - **Progress** (optional): Select a column that represents the progress of each task.

   [![Screenshot of the Board Layout Configuration dialog with Task ID, Title, Status, Assignee, and Progress selected, and the Save button.](../media/powertable-layouts/how-to-configure-kanban-layout/configure-board-layout.png)](../media/powertable-layouts/how-to-configure-kanban-layout/configure-board-layout.png#lightbox)
3. Select **Save**.

The Kanban view is created. PowerTable groups tasks into stacks based on their status, such as **Backlog**, **To Do**, **In Progress**, **Review**, and **Done**. Each task card has the task name, progress bar, and assignee.

[![Screenshot of the PowerTable Kanban view with task cards grouped into Backlog, Done, In Progress, Review, and To Do stacks by Status.](../media/powertable-layouts/how-to-configure-kanban-layout/created-kanban-layout.png)](../media/powertable-layouts/how-to-configure-kanban-layout/created-kanban-layout.png#lightbox)

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
