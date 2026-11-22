---
title: "Customize Kanban layout"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-customize-kanban-layout](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-customize-kanban-layout) · Last updated on **2026-10-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Customize Kanban layout

Summarize this article for me

PowerTable provides various options to customize the Kanban layout.

## Stack by different column

After you create the Kanban layout, use the **Stack By** dropdown to instantly change the column by which tasks are grouped.

[![Screenshot of PowerTable Kanban board with the Stack By dropdown, labeled Status, open and listing Title, Stage, Priority, Assignee, Sprint, Category, and Description.](../media/powertable-layouts/how-to-customize-kanban-layout/stack-by-different-field.png)](../media/powertable-layouts/how-to-customize-kanban-layout/stack-by-different-field.png#lightbox)

The following image shows the layout stacked by the **Priority** field.

[![Screenshot of PowerTable Kanban board stacked by Priority, showing Critical, High, Low, and Medium columns of task cards.](../media/powertable-layouts/how-to-customize-kanban-layout/stack-priority-field.png)](../media/powertable-layouts/how-to-customize-kanban-layout/stack-priority-field.png#lightbox)

## Group tasks

Select **Group By**, and then select the column by which you want to group similar tasks within the stack. This feature groups the tasks into sections, making related tasks easier to identify and manage.

The following image shows the tasks grouped by priority within the existing stacks.

[![Screenshot of Kanban board stacked by Status and grouped by Priority, showing expanded Critical tasks and collapsed High, Low, and Medium groups.](../media/powertable-layouts/how-to-customize-kanban-layout/group-tasks.png)](../media/powertable-layouts/how-to-customize-kanban-layout/group-tasks.png#lightbox)

Select **None** in **Group By** to ungroup and go back to the previous view.

## Expanded and compact view

Select the **Expanded View** in the top right corner to expand all the task cards and view complete task details. You can then toggle back to the default **Compact View**.

[![Screenshot of Kanban board in Expanded View with Expanded View button highlighted, showing full task card details across Backlog, To Do, In Progress, Review, and Done stacks.](../media/powertable-layouts/how-to-customize-kanban-layout/expanded-view.png)](../media/powertable-layouts/how-to-customize-kanban-layout/expanded-view.png#lightbox)

## Collapse a stack

To collapse or minimize a stack, select the vertical ellipsis for the stack, and then select **Collapse**.

[![Screenshot of Kanban board with the To Do stack's vertical ellipsis menu open and the Collapse option highlighted, alongside Hide, Move right, and Move left.](../media/powertable-layouts/how-to-customize-kanban-layout/collapse-stack.png)](../media/powertable-layouts/how-to-customize-kanban-layout/collapse-stack.png#lightbox)

Use this option when you have many stacks and want to view them in a more compact layout and fit all of them on a screen.

[![Screenshot of Kanban board with the To Do stack collapsed into a narrow vertical column highlighted, showing the >> expand arrow.](../media/powertable-layouts/how-to-customize-kanban-layout/result-collapsed-stack.png)](../media/powertable-layouts/how-to-customize-kanban-layout/result-collapsed-stack.png#lightbox)

Select the arrow **>>** to expand it.

## Hide or unhide a stack

To hide a stack, select the vertical ellipsis on the stack header, and then select **Hide**.

[![Screenshot of a Kanban board with the Backlog stack's vertical ellipsis menu open and the Hide option highlighted.](../media/powertable-layouts/how-to-customize-kanban-layout/hide-stack.png)](../media/powertable-layouts/how-to-customize-kanban-layout/hide-stack.png#lightbox)

Note

Hiding a column applies only to the current **Stack By** field. If you [change the **Stack By** field](#stack-by-different-column), the hidden columns become visible again.

To unhide a column, select **Properties** and then toggle on **Unhide Stack**.

[![Screenshot of a Kanban board with the Properties dropdown open and the Unhide Stack toggle highlighted.](../media/powertable-layouts/how-to-customize-kanban-layout/unhide-stack.png)](../media/powertable-layouts/how-to-customize-kanban-layout/unhide-stack.png#lightbox)

## Header count

To show or hide the number of tasks in each stack header, use the **Header Count** toggle under **Properties**.

[![Screenshot of a Kanban board with the Properties dropdown open and the Header Count toggle turned on and highlighted.](../media/powertable-layouts/how-to-customize-kanban-layout/header-count.png)](../media/powertable-layouts/how-to-customize-kanban-layout/header-count.png#lightbox)

## Customize Kanban color and styling

Select **Edit Kanban** > **Data Color** to customize the data cards and their borders with your preferred color and style.

- **Card:** This section opens the color options for Kanban cards.
  - **Card Fill:** Set the background color of the task cards.
  - **Progress Bar Fill:** Set the color of the progress bar displayed on the cards.
  - **Text Color:** Set the color of the text displayed on the cards.
- **Border:** This section opens the styling options for the cards' borders.
  - **Border Position:** Select one or more positions to display the card border: **Left**, **Right**, **Top**, or **Bottom**.
  - **Border Fill:** Set the color of the card border.
- **Reset to Default Styling:** Use this option to restore the default Kanban styling.

The following image shows a customized Kanban layout.

[![Screenshot of a customized Kanban board with the Edit Kanban pane open, showing Card Fill, Progress Bar Fill, Text Color, and Border options.](../media/powertable-layouts/how-to-customize-kanban-layout/customized-kanban.png)](../media/powertable-layouts/how-to-customize-kanban-layout/customized-kanban.png#lightbox)

## Format based on rules

Format the Kanban layout based on specified conditions. In addition to formatting the table by setting the formatting rules in the table layout, you can also highlight task cards, progress bars, borders, text, and header icons based on specified conditions.

Use **Format Rules** to define conditions that automatically format Kanban cards, making tasks that meet the specific criteria easier to identify.

To create a format rule:

1. In the **Format** tab, select **Format Rules** > **Create Rule**.

   [![Screenshot of the Format tab with the Format Rules menu open and Create Rule highlighted above a Kanban board.](../media/powertable-layouts/how-to-customize-kanban-layout/create-rule.png)](../media/powertable-layouts/how-to-customize-kanban-layout/create-rule.png#lightbox)
2. In the side panel, enter a name in the **Title** field.
3. In **Impacts On**, select one or more visual components to which the formatting should apply. They include:

   - Card Fill
   - Border
   - Progress Bar
   - Text
   - Header Icon

   [![Screenshot of the Create Formatting Rule panel with Critical tasks as the title and the Impacts On dropdown showing Text selected.](../media/powertable-layouts/how-to-customize-kanban-layout/configure-rule.png)](../media/powertable-layouts/how-to-customize-kanban-layout/configure-rule.png#lightbox)
4. Configure the condition in the **Condition If** section. You can add more rules by selecting **Add Rule**.
5. Under **Rule Highlight**, specify the formatting to apply when the condition is met.
6. Select **Apply**.

### Example 1: Impact on border and text

In the following example, you want to identify critical tasks visually by formatting the border and text.

**Impacts On**: Select **Border** and **Text**.

**Condition**: If **Priority** is *Critical*, the rule displays a **red left border** and changes the **Title** text color to red, making critical tasks easier to identify.

[![Screenshot of the Create Formatting Rule pane with Border selected, Priority is Critical condition, red left border, and red text color applied to Title.](../media/powertable-layouts/how-to-customize-kanban-layout/border-text.png)](../media/powertable-layouts/how-to-customize-kanban-layout/border-text.png#lightbox)

### Example 2: Impact on progress bars and cards based on multiple conditions

The following example shows how you can use multiple conditions to create more specific formatting rules based on different field values.

This example highlights both the progress bars and task cards based on the task's progress.

1. Select **Format Rules** > **Create Rule** to create another rule.
2. Name the rule in the **Title** field.
3. Select **Card Fill** and **Progress Bar** in **Impacts On**.

   ![Screenshot of the Create Formatting Rule pane with Card Fill and Progress Bar selected in the Impacts On dropdown.](../media/powertable-layouts/how-to-customize-kanban-layout/card-fill-progress-bar.png)
4. Select a table column from the first dropdown. For example, select *Progress* to check tasks by progress column.
5. Select a comparison operator. Since *Progress* is a number column, you can choose one of the comparison operators, such as *Greater than*, *Less than, Is equal to* and so on.
6. Select **Number** and enter the value to compare.

   ![Screenshot of the Create Formatting Rule pane with two conditions, Progress greater than 90 OR Status is Done, and the Add Rule button highlighted.](../media/powertable-layouts/how-to-customize-kanban-layout/add-combine-rules.png)
7. Add another condition by selecting **Add Rule**.
8. Combine the rules using **AND** or **OR.**
9. Configure the fill colors for the progress bars and the task cards that meet the set conditions.
10. Select **Apply**.

In the following image, tasks with **Progress** greater than **90%** or a **Completed** status are highlighted in light green, with a dark green progress bar.

[![Screenshot of a Kanban board where tasks with progress over 90% or Done status show light green cards and dark green progress bars, beside the Create Formatting Rule pane.](../media/powertable-layouts/how-to-customize-kanban-layout/result-after-combine-rules.png)](../media/powertable-layouts/how-to-customize-kanban-layout/result-after-combine-rules.png#lightbox)

### Example 3: Impact on header icon

This example adds a header icon to tasks that are overdue by comparing the **Due Date** with the current date and checking that the task is still **In Progress**.

1. In **Impacts On**, select **Header Icon**.
2. Under **Condition If**, configure the first condition:
   - Select **Due Date**.
   - Select **is in the last** in the next dropdown. You can also use other operators, such as **Greater than** and **Less than**, and other date-based conditions to compare the **Due Date** with a specified date or time period.
   - Enter **2** and select **weeks**. Select one of the time frames, such as days, weeks, months, years, calendar weeks, and more.
3. Select **+ Add Rule** to add another condition.
4. Select **AND** or **OR** to specify how the conditions are evaluated.
5. Configure the second condition by using the appropriate dropdown menus:
   - Select **Status** from the first dropdown menu.
   - Select **is** and **In Progress** in the subsequent menus.
6. Under **Rule Highlight**, configure the icon formatting:
   - **Position:** Select where to display the icon, such as **Left of data**.
   - **Select Icon:** Select the icon to display.
   - **Icon Colour:** Select the color of the icon.

The rule applies the selected icon formatting when the configured conditions are met.

[![Screenshot of a Kanban board beside the Create Formatting Rule pane, with red exclamation icons shown on matching task cards.](../media/powertable-layouts/how-to-customize-kanban-layout/header-icon-format.png)](../media/powertable-layouts/how-to-customize-kanban-layout/header-icon-format.png#lightbox)

## Manage format rules

Use the **Manage Rules** option to modify, organize, duplicate, or delete existing format rules.

In the **Format** tab, select **Format Rules** > **Manage Rules**.

[![Screenshot of the Format Rules dropdown showing Create Rule and Manage Rules options, with Manage Rules highlighted in red.](../media/powertable-layouts/how-to-customize-kanban-layout/manage-rules.png)](../media/powertable-layouts/how-to-customize-kanban-layout/manage-rules.png#lightbox)

In the **Manage Rule** side panel, view all the formatting rules that you configured.

[![Screenshot of the Manage Rule panel listing three format rules, with the edit, duplicate, delete, and toggle controls for Progress indicator highlighted in red.](../media/powertable-layouts/how-to-customize-kanban-layout/edit-delete-duplicate-enable-disable-rule.png)](../media/powertable-layouts/how-to-customize-kanban-layout/edit-delete-duplicate-enable-disable-rule.png#lightbox)

Each rule has a set of actions that you can use to manage it:

- **Edit rule** - Modify the rule conditions, affected components, or color and highlight settings.
- **Duplicate** - Create a copy of an existing rule to use as a starting point for a new rule.
- **Delete** - Delete a rule that you configured.
- **Show/Hide** - Use this toggle to enable or disable a rule without deleting it.
- **Drag and reorder** - Select the drag handle and drag and drop a rule to the required position to change its order for visibility.
- Select **Create New Rule** to add a new formatting rule from the **Manage Rule** panel.

## Modify layout

To modify the existing Kanban layout and configure a new one, go to **Layout** under the **PowerTable** tab and then select **Manage Layout**. Select the layout, and then reset or reconfigure the properties.

[![Screenshot of the PowerTable Layout menu with Manage Layout highlighted and the Layout Configuration dialog showing Kanban settings.](../media/powertable-layouts/how-to-customize-kanban-layout/manage-layout.png)](../media/powertable-layouts/how-to-customize-kanban-layout/manage-layout.png#lightbox)

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
