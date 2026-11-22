---
title: "Configure and customize layouts"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-change-layouts](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-change-layouts) · Last updated on **2026-05-20**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure and customize layouts

Summarize this article for me

Layout options control how data is structured and displayed in the report. You can configure both table layouts and measure layouts to customize how categories and values appear.

## Prerequisites

Before you configure layout options, ensure that you have the following prerequisites:

- Access to a planning sheet with data loaded.
- Permissions to edit the planning sheet.

## Configure table layouts

1. Open the planning sheet.
2. Go to **Layout options**.
3. From the **Layout** dropdown list, select the required layout. Various types of [table](#types-of-table-layouts) and [measure layouts](#types-of-measure-layouts) are available.

   [![Screenshot showing the steps to open layouts.](media/planning-how-to-change-layouts/layout-option.png)](media/planning-how-to-change-layouts/layout-option.png#lightbox)

## Types of table layouts

Table layouts determine how row categories are presented in the report.

### Hierarchy

This view displays data in a hierarchical format with expand and collapse functionality. This layout is the default.

[![Screenshot showing the hierarchy layouts.](media/planning-how-to-change-layouts/hierarchy-layout.png)](media/planning-how-to-change-layouts/hierarchy-layout.png#lightbox)

### Table

This view displays data in a tabular format without hierarchical expansion for rows. Column hierarchies can still support the expand and collapse functionality.

[![Screenshot showing the table layouts.](media/planning-how-to-change-layouts/table-layout.png)](media/planning-how-to-change-layouts/table-layout.png#lightbox)

### Tree layout

Use the tree layout to customize the structure and display of your data. The tree layout also helps you visualize absolute and relative variances between measures.

1. Go to **Home** > **Layout** > **Tree**.
2. In the **Configure Tree View** dialog, select the baseline and comparison measures that you want, and then select **Save**.

[![Screenshot showing the tree layouts configuration.](media/planning-how-to-change-layouts/tree-layout-configuration.png)](media/planning-how-to-change-layouts/tree-layout-configuration.png#lightbox)

Now you can see **Tree View** on the toolbar. You can use these options to further customize the tree layout.

[![Screenshot showing the tree layouts with tree view options.](media/planning-how-to-change-layouts/tree-layout.png)](media/planning-how-to-change-layouts/tree-layout.png#lightbox)

#### Tree view options

The tree view provides the following options:

- **Quick format**: Choose the number scaling format.
- **Baseline**: Select the baseline measure.
- **Comparison**: Select the measure to compare against the baseline.
- **KPI**: Select key performance indicator measures.
- **Create scenario**: Create and simulate scenarios.
- **Compare scenario**: Compare multiple scenarios.
- **Display settings**: Customize the tree layout display.

  - **Node customization**: Preview and customize node scope, style, and components.
  - **Level configuration**: Customize node style settings at the dimension level.
  - **Appearance**: Configure font color, primary color, background color, and conditional formatting.

[![Screenshot showing the display settings of tree layout.](media/planning-how-to-change-layouts/display-settings.png)](media/planning-how-to-change-layouts/display-settings.png#lightbox)

#### Node actions

You can use the node menu to perform actions such as editing, viewing details, and adding comments.

1. Select a node in the view to open the node menu.
2. Select **More options** (**â¦**) on the node.

The node action menu appears. The following actions are available:

- **Pin node**: Pin the selected node for quick access.
- **Edit node**: Modify node properties, such as name, aggregation, and formatting.
- **Simulate per period**: Run simulations for the node across periods when you create scenarios.
- **View details**: View additional information about the node.
- **Add comment**: Add comments to the node for collaboration.
- **Simulation lock**: Lock the node to prevent changes during simulation when you create a scenario.

[![Screenshot showing the node settings of tree layout.](media/planning-how-to-change-layouts/node-settings.png)](media/planning-how-to-change-layouts/node-settings.png#lightbox)

##### Edit a node

You can edit a node to update its name, aggregation behavior, and formatting. See [Tree view options](#tree-view-options) for a list of display settings.

###### Update general settings

Under **General**, you can modify the following:

- **Row name**: Update the name of the node.
- **Include in total**: Include the node in the total calculation.

###### Update formatting

Under **Formatting**, you can configure how values are displayed:

- **Scale**: Select how values are scaled (for example, automatically).
- **Decimal points**: Specify the number of decimal places.
- **Prefix**: Add a prefix to values.
- **Suffix**: Add a suffix to values.

###### Apply changes

- Select **Apply** to save changes.
- Select **Cancel** to discard changes.

[![Screenshot showing the node formatting of tree layout.](media/planning-how-to-change-layouts/node-formatting.png)](media/planning-how-to-change-layouts/node-formatting.png#lightbox)

Select a node to view additional information, such as trends, details, variance, and dependents. You can also analyze performance over time and compare values against a baseline.

- **Trends**: Displays time-based performance.
- **Details**: Shows detailed data for the selected node.
- **Variance**: Highlights differences between actuals and comparison values.
- **Dependents**: Shows dependent elements related to the selected node.

You can also select between these view options:

- Select **Graph** to display a visual chart of trends.
- Select **Table** to view the same data in tabular format.

[![Screenshot showing the additional information of tree layout.](media/planning-how-to-change-layouts/additional-information.png)](media/planning-how-to-change-layouts/additional-information.png#lightbox)

## Types of measure layouts

Measure layouts determine how values (measures) are displayed in the report.

### Measures in rows

This option displays measures as rows instead of columns. You can reorder measures by dragging rows or by using the **Manage rows** option.

[![Screenshot showing measures in rows.](media/planning-how-to-change-layouts/measure-rows.png)](media/planning-how-to-change-layouts/measure-rows.png#lightbox)

### Measures in columns

This option displays measures across columns above the column hierarchy categories.

[![Screenshot showing measures in columns.](media/planning-how-to-change-layouts/measure-columns.png)](media/planning-how-to-change-layouts/measure-columns.png#lightbox)

### Ragged hierarchy

A *ragged hierarchy* is a hierarchy in which branches have an uneven number of levels. Ragged hierarchies are also known as *unbalanced hierarchies*, because they contain uneven or unbalanced levels. The number of levels depends on the underlying data. Some members don't have values at all levels.

Use this setting to improve readability in hierarchical views by hiding blank or placeholder rows.

#### Turn on ragged hierarchy

When ragged hierarchy is turned on, only available levels are displayed, and empty rows are removed.

1. From the **Layout** dropdown list, select **Ragged Hierarchy**.
2. Turn on **Ragged Hierarchy**.

[![Screenshot showing the ragged hierarchy turned on.](media/planning-how-to-change-layouts/ragged-on.png)](media/planning-how-to-change-layouts/ragged-on.png#lightbox)

When ragged hierarchy is turned on, you see the following options:

- **Hide blanks**: Hides missing levels based on value, category, or both.
- **Suppress zeros**: Hides rows with zero values.
- **Hide blank columns**: Hides columns with no data.

When ragged hierarchy is turned off:

- All levels are displayed, even if values or categories are missing.

  [![Screenshot showing the ragged hierarchy turned off.](media/planning-how-to-change-layouts/ragged-off.png)](media/planning-how-to-change-layouts/ragged-off.png#lightbox)

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
