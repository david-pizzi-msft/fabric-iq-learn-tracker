---
title: "Customize resource layout"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-customize-resource-layout](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-layouts/how-to-customize-resource-layout) · Last updated on **2026-08-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Customize resource layout

Summarize this article for me

Customize the resource layout to control how tasks and related information are displayed. You can configure task properties, navigate time periods, view summary information, customize timescales, and apply formatting to meet your requirements.

## Navigate resource layout

The time period of data currently visible in the resource layout is displayed at the top of the layout. Use the **left** and **right** arrows to navigate to the previous or next time period.

[![Screenshot of the resource layout toolbar showing the date range selector and arrows.](../media/powertable-layouts/how-to-customize-resource-layout/navigate.png)](../media/powertable-layouts/how-to-customize-resource-layout/navigate.png#lightbox)

Select **Today** to quickly navigate to the time period that includes the current date.

[![Screenshot of the resource layout with the Today button highlighted abd a Today line.](../media/powertable-layouts/how-to-customize-resource-layout/today.png)](../media/powertable-layouts/how-to-customize-resource-layout/today.png#lightbox)

Use **Expand All** to expand all rows and **Collapse All** to collapse all rows.

[![Screenshot of the resource layout with the Expand All and Collapse All menu options highlighted in the Assigned To column header.](../media/powertable-layouts/how-to-customize-resource-layout/expand-collapse.png)](../media/powertable-layouts/how-to-customize-resource-layout/expand-collapse.png#lightbox)

## Configure task properties

Control how task information is displayed in the resource layout by using the options available under **Properties**.

1. Select **Properties**.

   [![Screenshot of the resource layout with the Properties menu open showing Data Label, Today Line, and Estimate on bar toggles.](../media/powertable-layouts/how-to-customize-resource-layout/properties.png)](../media/powertable-layouts/how-to-customize-resource-layout/properties.png#lightbox)
2. Use the available toggles to show or hide the corresponding information:

   - **Data Label** - Displays labels on the task bars. This option is enabled by default.
   - **Today Line** - Displays a line indicating the current date in the timeline. This option is enabled by default.
   - **Estimate on bar** - Displays the estimated hours on the task bars. If the estimate isn't visible on the bar, hover over the task bar to view it.

   [![Screenshot of the resource view with Estimate on bar enabled, showing hour values on bars and a tooltip on hover.](../media/powertable-layouts/how-to-customize-resource-layout/estimate-on-bar.png)](../media/powertable-layouts/how-to-customize-resource-layout/estimate-on-bar.png#lightbox)

## View summary information

Use the **Summary Bar** to view summary information for each resource across the timeline. The **Summary Bar** provides metrics such as **Total Tasks**, **Scheduled Hours**, **Availability**, and **Utilizations %** for the selected timescale.

To display a summary bar:

1. In the resource layout, select **Summary Bar**.

   [![Screenshot of the resource layout with the Summary Bar dropdown open, showing None, Total Tasks, Scheduled Hours, Availability, and Utilizations % options.](../media/powertable-layouts/how-to-customize-resource-layout/summary-bar.png)](../media/powertable-layouts/how-to-customize-resource-layout/summary-bar.png#lightbox)
2. Select the metric you want from the dropdown. You can choose from the following options:

   - **None** - Hides the summary bar.
   - **Total Tasks** - Displays the total number of tasks for each resource across each time interval.

     [![Screenshot of the resource layout with the Summary Bar - Total Tasks option highlighted in the toolbar and task counts displayed per day.](../media/powertable-layouts/how-to-customize-resource-layout/total-tasks.png)](../media/powertable-layouts/how-to-customize-resource-layout/total-tasks.png#lightbox)
   - **Scheduled Hours** - Displays the total scheduled hours for each resource across each time interval.

     [![Screenshot of the resource layout with the Summary Bar - Scheduled Hours option highlighted and showing scheduled hours.](../media/powertable-layouts/how-to-customize-resource-layout/scheduled-hours.png)](../media/powertable-layouts/how-to-customize-resource-layout/scheduled-hours.png#lightbox)
   - **Availability** - Displays the available hours for each resource across each time interval. Availability is calculated as the difference between the total allocated hours and scheduled hours.

     [![Screenshot of the resource layout with Summary Bar - Availability highlighted in the toolbar and daily available hours shown per resource.](../media/powertable-layouts/how-to-customize-resource-layout/availability.png)](../media/powertable-layouts/how-to-customize-resource-layout/availability.png#lightbox)
   - **Utilizations %** - Displays the percentage of utilized hours for each resource across each time interval.

     [![Screenshot of the resource layout with Summary Bar - Utilizations % highlighted in the toolbar and daily utilization percentages per resource.](../media/powertable-layouts/how-to-customize-resource-layout/utilizations.png)](../media/powertable-layouts/how-to-customize-resource-layout/utilizations.png#lightbox)

The selected summary metric is displayed for each resource across the corresponding time intervals in the resource layout.

## Switch and manage timescales

Use timescales to control the level of detail displayed in the Resource layout. Switch between available timescales to view task schedules at different levels of detail, or customize timescales to control the date range and timeline levels.

### Switch the timescale

View the resource layout at different timescale levels to analyze task schedules at varying levels of detail. Select a timescale from the dropdown in the layout.

[![Screenshot of the resource layout with the timescale dropdown open showing Full Range, Year, Quarter, Month, Week, and Manage Timescale.](../media/powertable-layouts/how-to-customize-resource-layout/timescale.png)](../media/powertable-layouts/how-to-customize-resource-layout/timescale.png#lightbox)

The following timescales are available:

- **Full Range** - Displays the complete task timeline with year, quarter, and month levels expanded for a detailed view.

  [![Screenshot of the Resource layout with Full Range selected in the timescale dropdown, showing year, quarter, and month headers.](../media/powertable-layouts/how-to-customize-resource-layout/full-range.png)](../media/powertable-layouts/how-to-customize-resource-layout/full-range.png#lightbox)
- **Year** - Displays the timeline at the year level, with quarters and months shown within each year.

  [![Screenshot of the Resource layout with Year selected in the timescale dropdown, showing year, quarter, and month headers above task bars.](../media/powertable-layouts/how-to-customize-resource-layout/year.png)](../media/powertable-layouts/how-to-customize-resource-layout/year.png#lightbox)
- **Quarter** - Displays the timeline at the quarter level, with the corresponding months and weeks shown within each quarter.

  [![Screenshot of the Resource layout with Quarter selected in the timescale dropdown, showing quarter, month, and week headers above task bars.](../media/powertable-layouts/how-to-customize-resource-layout/quarter.png)](../media/powertable-layouts/how-to-customize-resource-layout/quarter.png#lightbox)
- **Month** - Displays the timeline at the month level, with the corresponding weeks and individual days shown within the month.

  [![Screenshot of the Resource layout with Month selected in the timescale dropdown, showing month, week, and day headers above task bars.](../media/powertable-layouts/how-to-customize-resource-layout/month.png)](../media/powertable-layouts/how-to-customize-resource-layout/month.png#lightbox)
- **Week** - Displays the timeline at the week level, with individual days shown within each week.

  [![Screenshot of the Resource layout with Week selected in the timescale dropdown, showing week and day headers above task bars.](../media/powertable-layouts/how-to-customize-resource-layout/week.png)](../media/powertable-layouts/how-to-customize-resource-layout/week.png#lightbox)

### Manage timescale

You can customize a timescale to control the date range and levels displayed in the resource layout.

To manage a timescale:

1. In the resource layout, select **Manage Timescale**. The **Manage Timescale** side panel opens and displays the available timescales: **Full Range**, **Year**, **Quarter**, **Month**, and **Week**.

   [![Screenshot of the Manage Timescale side panel listing Full Range, Year, Quarter, Month, and Week with Edit icons highlighted.](../media/powertable-layouts/how-to-customize-resource-layout/manage-timescale.png)](../media/powertable-layouts/how-to-customize-resource-layout/manage-timescale.png#lightbox)
2. Select the **Edit** icon for the timescale that you want to customize. The **Customize Timescale** panel opens.
3. In the **Title** field, edit the name of the timescale if needed.
4. Under **Timescale**, select the **Range** and specify the **Value** for the timescale.
5. Under **Level Format**, configure the available levels and their display formats.
   For each available level, select the required time unit, interval, and display format.
6. Select **Save**.

   [![Screenshot of the Customize Timescale panel with Title, Timescale range, and Level Format options.](../media/powertable-layouts/how-to-customize-resource-layout/customize-timescale.png)](../media/powertable-layouts/how-to-customize-resource-layout/customize-timescale.png#lightbox)

The customized timescale is available in the timescale dropdown and can be selected to display the **Resource** layout using the configured date range and levels.

## Customize resource layout components

Customize the appearance and display settings of components in the **Resource** layout. Use **Edit Resource** to configure timeline settings, milestone styles, data colors, and labels displayed in the layout.

To customize resource layout components:

1. In the **Format** tab, select **Edit Resource**, and then select any component that you want to customize.

   ![Screenshot of the Format tab with Edit Resource selected, showing Timeline, Milestone, Data Color, and Label options.](../media/powertable-layouts/how-to-customize-resource-layout/edit-resource.png)
2. The **Edit Resource** side panel opens with separate tabs for each component:

   - **Timeline**
   - **Milestone**
   - **Data Color**
   - **Label**
3. Select the tab you want to configure.

   [![Screenshot of the Edit Resource panel displaying Timeline, Milestone, Data Color, and Label tabs.](../media/powertable-layouts/how-to-customize-resource-layout/edit-resource-side-panel.png)](../media/powertable-layouts/how-to-customize-resource-layout/edit-resource-side-panel.png#lightbox)
4. Modify the settings and view the changes in the resource layout.
5. Select **Save to Database** to save the changes.

### Configure timeline settings

Use the **Timeline** tab to configure timeline and scheduling settings for the resource layout.

- **Fiscal Year Starting Month** - Specify the month that marks the beginning of the fiscal year used in the timeline.
- **Week Start Day** - Define the first day of the week displayed in the timeline.
- **Work Week** - Specify the working days used for task scheduling and resource allocation calculations.
- **Daily Capacity** - Define the number of working hours available per day for each resource. Use this value to calculate **Scheduled Hours**, **Availability**, and **Utilizations %** in the **Summary Bar**.
- **Holidays & Exceptions** - Configure non-working days, holidays, and other exceptions that affect scheduling.
- **Color** - Set the color used to highlight non-working periods in the timeline.
- **Pattern** - Specify the fill pattern used to display non-working periods and exceptions in the timeline. Select a pattern from the available options.
- **Zoom Using Mouse Wheel** - Enable or disable zooming the timeline using the mouse wheel.

[![Screenshot of the Edit Resource panel with the Timeline tab selected, showing fiscal year, work week, holidays, color, and pattern settings.](../media/powertable-layouts/how-to-customize-resource-layout/timeline.png)](../media/powertable-layouts/how-to-customize-resource-layout/timeline.png#lightbox)

### Customize milestone appearance

Use the **Milestone** tab to customize milestone appearance in the Resource layout.

- **Shape**: Select a milestone shape.
- **Fill**: Configure milestone fill color.
- You can also upload a custom milestone icon by selecting **Upload** and choosing an icon.

[![Screenshot of the Edit Resource panel with the Milestone tab selected, showing Shape and Fill options with an open shape picker and Upload button.](../media/powertable-layouts/how-to-customize-resource-layout/milestone.png)](../media/powertable-layouts/how-to-customize-resource-layout/milestone.png#lightbox)

### Configure data colors

Use the **Data Color** tab to customize the colors for task bars.

- Select **All** to apply a single color to all task bars.

  [![Screenshot of the Edit Resource panel with the Data Color tab selected and Color by set to All, showing a single Fill color applied to all task bars.](../media/powertable-layouts/how-to-customize-resource-layout/data-color-all.png)](../media/powertable-layouts/how-to-customize-resource-layout/data-color-all.png#lightbox)
- To color task bars by column, select **Column**, and then choose a column from **Option Columns**. Only **Single Select** columns are available in **Option Columns**.
- Each task bar gets a color based on the option you select for that task in the chosen column. For example, if you select the **Status** column, tasks with different status options appear in different colors.

  [![Screenshot of the Edit Resource panel with Data Color tab, Color by set to Column, and Option Columns list showing Task Type, Priority, and Status.](../media/powertable-layouts/how-to-customize-resource-layout/data-color-column.png)](../media/powertable-layouts/how-to-customize-resource-layout/data-color-column.png#lightbox)

### Configure task labels

Use the **Label** tab to configure the labels that appear on task bars.

You can:

- Turn data labels on or off.
- Select the field for the label.
- Set the font size.
- Change the text and background colors.
- Turn on **Adaptive label** to adjust the label based on available space.

[![Screenshot of Label tab settings including Enable Data Label, Based On, Font Size, Text Color, and Adaptive label toggles.](../media/powertable-layouts/how-to-customize-resource-layout/label.png)](../media/powertable-layouts/how-to-customize-resource-layout/label.png#lightbox)

Note

Changes you make in the **Edit Resource** panel affect the appearance and display settings of the Resource layout. Use **Reset to Default Styling** to restore the default component settings.

## Create formatting rules

Use format rules to highlight task bars, summary bars, and milestones based on specified conditions. Format rules help you visually identify tasks and summary information that meet defined criteria.

To create a format rule:

1. In the **Format** tab, select **Format Rules** > **Create Rule**.

   ![Screenshot of the Format tab with Format Rules menu open and Create Rule highlighted.](../media/powertable-layouts/how-to-customize-resource-layout/create-rule.png)
2. In the **Create Formatting Rule** side panel, enter a name in the **Title** field.
3. In **Impacts On**, select one or more components to which the rule should apply. They include:

   - **Bar**
   - **Summary Bar**
   - **Milestone**
4. Configure the condition in the **Condition If** section.
5. Under **Rule Highlight**, specify the formatting to apply when the condition is met.
6. Select **Apply**.

### Configure conditions for task bars

When you select **Bar** in **Impacts On**, define the condition by using a table column.

1. Select a column from the first dropdown.
2. Select a comparison operator.
3. Select or enter a value for the selected column.
4. Configure the highlight settings for the task bar.

   [![Screenshot of the Create Formatting Rule panel with Bar impact, condition Status is Done, and green bar highlight color.](../media/powertable-layouts/how-to-customize-resource-layout/create-rule-bar.png)](../media/powertable-layouts/how-to-customize-resource-layout/create-rule-bar.png#lightbox)

In this example, task bars with the **Status** value **Done** are displayed in green.

[![Screenshot of a resource layout where tasks with Status Done appear as green bars.](../media/powertable-layouts/how-to-customize-resource-layout/formatted-task-bars.png)](../media/powertable-layouts/how-to-customize-resource-layout/formatted-task-bars.png#lightbox)

### Configure conditions for summary bars

When you select **Summary Bar** in **Impacts On**, specify the summary bar elements to format.

1. In **Apply To**, select one or more summary bar components, such as:

   - **Bar**
   - **Data Label**
2. In **Condition If**, select a summary metric and define the condition.
3. Configure the highlight settings for the selected summary bar components.

   [![Screenshot of Rule Highlight settings with red Bar color and black Data Label for a summary bar rule.](../media/powertable-layouts/how-to-customize-resource-layout/create-rule-summary-bar.png)](../media/powertable-layouts/how-to-customize-resource-layout/create-rule-summary-bar.png#lightbox)

In this example, summary bars where **Scheduled Hours** is greater than **8** are displayed in red.

[![Screenshot of a resource layout where scheduled hours over 8 appear as red cells and lower values appear in purple.](../media/powertable-layouts/how-to-customize-resource-layout/formatted-summary-bars.png)](../media/powertable-layouts/how-to-customize-resource-layout/formatted-summary-bars.png#lightbox)

Note

Select **Scheduled Hours** from the **Summary Bar** dropdown to view the applied formatting.

### Add multiple conditions

You can define multiple conditions within a single format rule.

1. Select **Add Rule**.
2. Configure the additional condition.
3. Connect conditions using **AND** or **OR** operators.

   [![Screenshot of the Create Formatting Rule panel with Add Rule and AND/OR operator options highlighted.](../media/powertable-layouts/how-to-customize-resource-layout/create-rule-multiple-conditions.png)](../media/powertable-layouts/how-to-customize-resource-layout/create-rule-multiple-conditions.png#lightbox)

Use multiple conditions to create more specific formatting scenarios based on different field values. In this example, tasks with the **Task Type** value **Story** and the **Status** value **Completed** are highlighted in pink.

[![Screenshot of the resource layout where taskbars with task type story and status completed are highlighted in pink.](../media/powertable-layouts/how-to-customize-resource-layout/formatted-multiple-conditions.png)](../media/powertable-layouts/how-to-customize-resource-layout/formatted-multiple-conditions.png#lightbox)

Note

You can apply a single format rule to multiple components by selecting **Bar**, **Summary Bar**, and **Milestone** in **Impacts On**. This approach lets you reuse the same condition across components without creating separate rules for each one.

### Manage format rules

Use **Manage Rule** to modify and organize existing format rules in the resource layout.

To manage format rules:

1. In the **Format** tab, select **Format Rules** > **Manage Rule**.

   ![Screenshot of the Format tab with Format Rules menu open and Manage Rules highlighted.](../media/powertable-layouts/how-to-customize-resource-layout/manage-rules.png)
2. In the **Manage Rule** side panel, view all available format rules.
3. Use the available actions to manage rules:

   - **Edit** - Modify the rule conditions, affected components, or highlight settings.
   - **Duplicate** - Create a copy of an existing rule to use as a starting point for a new rule.
   - **Delete** - Remove a rule from the resource layout.
   - **Show/Hide** - Enable or disable a rule without deleting it.
   - **Drag and reorder** - Change the order of rules by dragging them to the required position.
4. Select **Create New Rule** to add a new format rule from the **Manage Rule** panel.

   [![Screenshot of the Manage Rule side panel listing format rules with edit, duplicate, delete, and toggle actions highlighted.](../media/powertable-layouts/how-to-customize-resource-layout/manage-rule-side-panel.png)](../media/powertable-layouts/how-to-customize-resource-layout/manage-rule-side-panel.png#lightbox)

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
