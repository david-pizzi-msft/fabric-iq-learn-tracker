---
title: "Configure and manage resource layout"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-configure-resource-overview](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-configure-resource-overview) · Last updated on **2026-08-16**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure and manage resource layout

Summarize this article for me

When your data includes tasks with an assignee or resource column and start and end dates, use the resource layout to organize tasks by their assigned resources. The layout displays each resource with their assigned tasks and task timelines.

Use the resource layout to view task distribution across resources and track the schedule of tasks assigned to each resource.

## Use cases

The use cases for resource layout include the following:

- **Resource allocation** - View the tasks assigned to each resource and identify how work is distributed.
- **Workload tracking** - Review the number and duration of tasks assigned to each resource.
- **Schedule management** - Track the start and end dates of tasks assigned to each resource.
- **Task monitoring** - Monitor task schedules across multiple resources from a single view.
- **Project planning** - Identify scheduling overlaps and manage task assignments based on resource availability.
- **Milestone tracking** - Track important events, deadlines, and completion points within the project schedule.

## Prerequisites

Before creating a resource layout, ensure that the table contains the following:

- A column that identifies the **resource** or **assignee** for each task.
- A **Start Date** column containing the task start dates.
- An **End Date** or a **Duration** column containing the task end dates or task duration.

## Create a resource layout

To create a resource layout:

1. In the **PowerTable** tab, expand **Layout** and select **Resource**.

   [![Screenshot of the PowerTable tab with the Layout menu open and the Resource option highlighted.](../media/powertable-layouts/how-to-configure-resource-overview/resource.png)](../media/powertable-layouts/how-to-configure-resource-overview/resource.png#lightbox)

   The **Resource Layout Configuration** window opens.

   [![Screenshot of the Resource Layout Configuration window.](../media/powertable-layouts/how-to-configure-resource-overview/configuration-window.png)](../media/powertable-layouts/how-to-configure-resource-overview/configuration-window.png#lightbox)
2. Configure the [properties](#configuration-properties) to create a resource layout.
3. Select **Save**.

## Configuration properties

This section explains the required and optional properties you need to configure for the resource layout.

- The required resource layout fields include the following:

  - **Resource**: Select the column that contains the resource or assignee information.
  - **Start Date**: Select the column that contains the task start dates.
  - **End Date/Duration**: Select the column that contains the task end dates or the task duration.
- The optional layout properties include:

  - **Estimated Effort**: Select the column that contains the estimated effort in hours.
  - **Filter Columns**: Select the columns that you want to make available for filtering in the **Filter** side panel. If you don't select any columns, all columns are available for filtering.

    [![Screenshot of the Resource Layout Configuration window with configured properties.](../media/powertable-layouts/how-to-configure-resource-overview/configured-resource-layout.png)](../media/powertable-layouts/how-to-configure-resource-overview/configured-resource-layout.png#lightbox)

The resource layout opens and displays each resource along with their assigned tasks and the duration of each task across the timeline.

[![Screenshot of the PowerTable Resource layout displaying each resource along with their assigned tasks.](../media/powertable-layouts/how-to-configure-resource-overview/resource-layout.jpg)](../media/powertable-layouts/how-to-configure-resource-overview/resource-layout.jpg#lightbox)

Select the **Filter** icon on the right side to open the **Filter** pane. In this example, only the configured columns are available for filtering.

[![Screenshot of the PowerTable Resource layout with expanded Filter pane containing only the configured columns.](../media/powertable-layouts/how-to-configure-resource-overview/filter.png)](../media/powertable-layouts/how-to-configure-resource-overview/filter.png#lightbox)

## Manage the resource layout

After you create a resource layout, you can modify its field mappings to change how resources and tasks are displayed.

To modify the resource layout:

1. In the **PowerTable** tab, select **Layout** > **Manage Layout**.

   [![Screenshot of the PowerTable tab with the Layout menu open and the Manage Layout option highlighted.](../media/powertable-layouts/how-to-configure-resource-overview/manage-layout.png)](../media/powertable-layouts/how-to-configure-resource-overview/manage-layout.png#lightbox)
2. In the **Layout Configuration** window, update the **Resource**, **Start Date**, **End Date**, or other field mappings as needed.
3. Select **Save**.

   [![Screenshot of the Layout Configuration window of the Resource layout to update or reset the configured properties.](../media/powertable-layouts/how-to-configure-resource-overview/layout-configuration-window.png)](../media/powertable-layouts/how-to-configure-resource-overview/layout-configuration-window.png#lightbox)

The resource layout refreshes based on the updated field mappings.

Note

Selecting **Reset** clears all configured field mappings and layout settings in the **Resource Layout Configuration** window.

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
