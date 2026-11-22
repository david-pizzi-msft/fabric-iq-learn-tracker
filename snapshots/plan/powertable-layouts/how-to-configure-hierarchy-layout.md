---
title: "Configure and use hierarchy layout"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-configure-hierarchy-layout](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-configure-hierarchy-layout) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure and use hierarchy layout

Summarize this article for me

The **Hierarchy** layout organizes records into parent-child relationships, making it easier to navigate and analyze multilevel data. It provides an alternative to the default **Table** layout. This layout is useful for datasets such as organizational structures, product categories, customer orders, and similar hierarchical data.

This article explains the steps to configure the hierarchy layout by using an example.

To configure a hierarchy layout:

1. In the **PowerTable** tab, select **Layout** > **Hierarchy**.

   ![Screenshot of PowerTable tab with Layout menu open showing Hierarchy option highlighted.](../media/powertable-layouts/how-to-configure-hierarchy-layout/select-hierarchy-layout.png)

   The **Hierarchy Layout Configuration** dialog opens.

   [![Screenshot of Hierarchy Layout Configuration dialog with Primary Key and Hierarchy Column options.](../media/powertable-layouts/how-to-configure-hierarchy-layout/hierarchy-layout-configuration.jpeg)](../media/powertable-layouts/how-to-configure-hierarchy-layout/hierarchy-layout-configuration.jpeg#lightbox)
2. Select the **Primary Key Column**.

   The primary key uniquely identifies each record in the table. In the example, *Employee\_Id* is the primary key.
3. Select the **Hierarchy Column**.

   The hierarchy column defines the parent-child relationship between records. In the example, *Manager\_Id* is the hierarchy column because it links each employee to their manager in a parent-child hierarchy format.
4. Select the **Display Column**.

   The display column specifies which values appear in the hierarchy view. It must be different from the hierarchy column. In the example, *Full\_Name* is the display column.
5. Select **Save**.

   [![Screenshot of Hierarchy layout configured with Manager_Id and Full_Name columns to create an employee tree.](../media/powertable-layouts/how-to-configure-hierarchy-layout/hierarchy-layout-configured.jpeg)](../media/powertable-layouts/how-to-configure-hierarchy-layout/hierarchy-layout-configured.jpeg#lightbox)

   The table appears in **Hierarchy** layout.

   [![Screenshot of a table in Hierarchy layout showing an employee tree with expandable rows.](../media/powertable-layouts/how-to-configure-hierarchy-layout/powertable-sheet-hierarchy-layout.jpeg)](../media/powertable-layouts/how-to-configure-hierarchy-layout/powertable-sheet-hierarchy-layout.jpeg#lightbox)

## Hierarchy layout structure

After you configure the hierarchy:

- The layout automatically pins the selected display column.
- The layout organizes parent and child records into a hierarchical structure.
- The number of child records appears next to each parent record.
- You can expand or collapse parent records to show or hide child records.

[![Screenshot of a hierarchical table displaying parent records with child record counts in parentheses and expand arrows.](../media/powertable-layouts/how-to-configure-hierarchy-layout/expand-hierarchy.png)](../media/powertable-layouts/how-to-configure-hierarchy-layout/expand-hierarchy.png#lightbox)

## Modify the configured hierarchy

You can modify the configuration for an existing hierarchy layout.

To modify and manage the hierarchy configuration:

1. In the **PowerTable** tab, select **Layout** > **Manage Layout**.

   ![Screenshot of PowerTable Layout menu with Manage Layout option highlighted.](../media/powertable-layouts/how-to-configure-hierarchy-layout/modify-hierarchy.png)
2. In the **Layout Configuration** window, select **Hierarchy**.

   [![Screenshot of Layout Configuration window with Hierarchy tab selected showing Primary Key, Hierarchy, and Display Column fields.](../media/powertable-layouts/how-to-configure-hierarchy-layout/reconfigure-hierarchy-layout.png)](../media/powertable-layouts/how-to-configure-hierarchy-layout/reconfigure-hierarchy-layout.png#lightbox)
3. Update the required fields such as **Hierarchy Column** and **Display Column** as needed.
4. Select **Save**.

## Insert and manage hierarchy records

Use the three-dot menu on a parent record to perform the following actions:

![Screenshot of hierarchy table with three-dot menu open showing Expand, Insert Child Row, Move To, and Show Hierarchy options.](../media/powertable-layouts/how-to-configure-hierarchy-layout/parent-record-menu.png)

- **Expand**: Expands the selected parent record to display its child records.
- **Collapse**: Collapses the selected parent record to hide its child records.
- **Insert Child Row**: Adds a new child record under the selected parent. The hierarchy column value (*Manager\_Id*) populates automatically. Enter the required values in the remaining fields.

  [![Screenshot of PowerTable showing a newly inserted child row with NULL values and pre-filled Manager_Id under the selected parent record.](../media/powertable-layouts/how-to-configure-hierarchy-layout/insert-child-row.png)](../media/powertable-layouts/how-to-configure-hierarchy-layout/insert-child-row.png#lightbox)
- **Move To**: Moves the selected record to another parent. Select the required parent from the list, and then select **Move**.

  [![Screenshot of Select a parent to move dialog with search box and list of records showing hierarchy paths.](../media/powertable-layouts/how-to-configure-hierarchy-layout/move-child-row.png)](../media/powertable-layouts/how-to-configure-hierarchy-layout/move-child-row.png#lightbox)
- **Show Hierarchy**: Displays the complete hierarchy for the selected record.

  [![Screenshot of PowerTable Hierarchy Path dialog displaying the reporting chain for the selected employee record.](../media/powertable-layouts/how-to-configure-hierarchy-layout/show-hierarchy-path.png)](../media/powertable-layouts/how-to-configure-hierarchy-layout/show-hierarchy-path.png#lightbox)

To expand or collapse all parent records, use **Expand** or **Collapse All** from the same menu, available at the highest level of the hierarchy.

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
