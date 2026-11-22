---
title: "Configure row properties in a model"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-row-model/planning-how-to-configure-model-row-properties](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-row-model/planning-how-to-configure-model-row-properties) · Last updated on **2026-10-29**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure row properties in a model

Summarize this article for me

This article explains row properties and how to configure them in a model.

## Configure closed and open periods

The model builder looks like the following image. There are two tabs: **Closed Period** and **Open Period**.

[![Screenshot of hybrid row configuration showing open and closed periods.](../media/planning-row-model/planning-how-to-configure-model-row-properties/hybrid-row.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/hybrid-row.png#lightbox)

By default, the row configurations are the same for both closed and open periods. Toggle between the tabs to specify different row configurations for the open and the closed periods.

Open period row values represent the plan, forecast, or any projection measures. Closed period values refer to the actuals. Using this option, you can configure different formulas, data sources, or manual values for the actuals and the forecast.

## Row properties

To configure the row properties, select the **Type**, **Configuration**, and **Aggregation** dropdown menus from the model builder view. Make sure to choose the correct period, open or closed.

[![Screenshot of row type and configuration dropdowns.](../media/planning-row-model/planning-how-to-configure-model-row-properties/row-type.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/row-type.png#lightbox)

Or, hover over a row and select the pencil icon beside the row name to edit the complete row properties.

![Screenshot of edit icon beside the row name.](../media/planning-row-model/planning-how-to-configure-model-row-properties/edit-row-properties.png)

A side panel opens to configure the properties. It has **General** and **Display** tabs. In the **General** tab, configure all row properties. In the **Display** tab, configure node display settings for the tree view.

[![Screenshot of row properties side panel.](../media/planning-row-model/planning-how-to-configure-model-row-properties/row-properties-panel.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/row-properties-panel.png#lightbox)

The following sections describe the setting options.

### Row name

Enter or edit the name of the row.

## Type

Assign the type of the row to set up the right configuration. Select one of the following row types:

| Row type | Description |
| --- | --- |
| Formula | Row values are derived from the user-defined formula for the row. |
| Data Source | Row values are retrieved from the corresponding source data. |
| Data Input | Row allows users to manually enter the values. |
| Aggregate | Row aggregates values from child rows (for example, sum, product, average, and so on). |
| Driver Input | Row values are calculated based on the configured driver row, driver method, and driver inputs. |
| Distribution | Specified row total is distributed based on weights derived from the row itself or other rows, or is equally distributed. You can also use it to copy row values from another row instead of a distribution function. |
| Linked Row | The row values, its properties, and simulation settings are linked to another row. This type can be configured for rows in the Open Period. |

## Configuration

Based on the row type, fill in the configuration as follows.

### Formula

For a **Formula** row, enter the configuration as a formula. You can type the formula and select from the suggestions that appear as you start typing.

[![Screenshot of formula editor.](../media/planning-row-model/planning-how-to-configure-model-row-properties/formula-editor.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/formula-editor.png#lightbox)

To access help suggestions with examples, press **Ctrl + Space**. A suggestions pop-up opens with two tabs: **References** and **Functions**.

- Select the **References** tab to reference and add the row names you want in the formula.
- Select the **Functions** tab to view the list of supported functions. Select one to view its syntax and example and then insert it.

For hierarchical rows, typing a row reference in the formula box inserts the full path from the root node to the referenced row, as shown in the following image. Verify the row path to ensure that you reference the correct row.

[![Screenshot of the Enter Formula box with row references prefixed by the parent path, such as [Income Before Tax (EBT)].[Interest Income].](../media/planning-row-model/planning-how-to-configure-model-row-properties/hierarchical-row.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/hierarchical-row.png#lightbox)

### Data Source

For **Data Source** rows, the row values are retrieved from the source data based on the row you select from the dropdown menu.

[![Screenshot of data source row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/data-source-row.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/data-source-row.png#lightbox)

### Data Input

For **Data Input** rows, you can either enter values manually or copy values from an existing row.

- **Row**: Select a data source row whose values you want to copy.
- **Static**: Enter a value to be applied across all periods.

The following example demonstrates both options configured.

[![Screenshot of data input row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/data-input-row.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/data-input-row.png#lightbox)

### Aggregate

This type offers various aggregation options, letting you define how child rows are aggregated. Options include *Sum*, *Subtract*, *Product*, *Divide*, *Minimum*, *Maximum*, *First*, *Last*, *Average*, and *Average (Leaf Only).*

![Screenshot of aggregate row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/aggregate-row.png)

### Linked Row

In a **Linked Row**, you can select another row to link to. Linked rows share the same values, properties, configuration, and simulation behavior, ensuring they remain in sync.

Use this type when you need to reuse the same row in multiple parts of the model, so you can change all instances at once. For example, you can share global software licensing fees across regional budgets or reuse a standard salary and benefits configuration across departments. Changes to the linked row are reflected across its instances, helping maintain consistency and reduce duplicate data entry.

You can specify this type for open period rows.

[![Screenshot of linked row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/linked-row.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/linked-row.png#lightbox)

### Driver Input

If you choose the **Driver Input** type for a row, define how its values are calculated by selecting a **driver row** (the source row that influences it) and a **driver method**âsuch as addition, subtraction, multiplication, division, percentage of, or growth by.

You can specify the aggregation and distribution methods for Driver Input rows.

[![Screenshot of driver input row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/driver-input.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/driver-input.png#lightbox)

Based on the inputs you enter in the planning sheet, this row automatically calculates by using the selected driver configuration. To learn more, see [Create a row model](how-to-create-row-model).

[![Screenshot of driver input entered in the planning sheet.](../media/planning-row-model/planning-how-to-configure-model-row-properties/driver-input-planning-sheet.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/driver-input-planning-sheet.png#lightbox)

### Distribution

This row type lets you specify how the entered row total value is distributedâeither equally, based on weights, or by copying values by trend.

If you select to distribute by weight, specify the row from which the weights are derived.

If you select **Copy**, choose how values are copied:

- Copy without trend
- Copy with trend by value
- Copy with trend by percentage, and specify the trend values

Enter the total in the planning sheet. The values are distributed or copied accordingly based on the selected method.

[![Screenshot of distribution type row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/distribution-row.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/distribution-row.png#lightbox)

### Formatting

Use the following options to control how values are displayed:

- **Scale:** Choose a number scaling option, such as *None*, *Auto*, *Thousands*, *Millions*, *Billions*, or *Trillions*.
- **Decimal Points:** Specify the number of decimal places to display for numeric values.
- **Prefix:** Add a prefix to values, such as a currency symbol.
- **Suffix:** Add a suffix to values, such as units.

![Screenshot of formatting, trend, and simulation options.](../media/planning-row-model/planning-how-to-configure-model-row-properties/formatting-trend-simulation.png)

### Tree view layout

Use the Desired Trend and Simulation settings in the tree view layout.

#### Desired trend

Set the desired trend for a row to *Increase* or *Decrease* depending on the row context. For instance, the desired trend for the *Revenue* row is *Increase*, while for the *Expense* row, it's *Decrease*.

This setting controls how node values are represented visually in the tree layout. When you simulate in the direction of the desired trend, the node is represented in green; when you simulate in the opposite direction, the node is represented in red.

#### Simulation

**Slide Right to:** To increase the node value on sliding right, set the Slide Right to property as *Positive Simulation*. To decrease the value, set it as *Negative Simulation*.

**Value:** Set the maximum simulation range. The default simulation range is 100, so the simulation percentages are calculated as a percentage of 100.

## Aggregation

Specify how the total row value is aggregated from the period or column values.

[![Screenshot of column aggregation for a row.](../media/planning-row-model/planning-how-to-configure-model-row-properties/column-aggregation.png)](../media/planning-row-model/planning-how-to-configure-model-row-properties/column-aggregation.png#lightbox)

The following table shows the available aggregations:

| Time aggregation | Description |
| --- | --- |
| Sum | Adds all the period values. |
| Minimum | Returns the minimum value among the period values. |
| Maximum | Returns the maximum value among the period values. |
| Average (children) | Calculates the average of the immediate child node values. |
| Average (leaf) | Calculates the average of the leaf node values. |
| Average excluding zeros | Calculates the average of the non-zero period values. |
| First | Displays the first period value of the node. |
| Last | Displays the last period value of the node. |
| Weighted average | Calculates the weighted average of the period values based on selected nodes. |
| Standard deviation | Calculates the standard deviation of the period values. |
| Formula | Calculates and applies a custom formula entered by the user. |

## Other options

- **Distribute parent value to children:** For Data Input rows, select this option to distribute the entered parent row value to child rows.
- **Include in total**: When enabled, the row values are included in the parent total. This setting is enabled by default.
- **Bind for Cross filter/RLS**: Enable **Bind for Cross filter/RLS** to ensure that cross-filter selections and row-level security (RLS) rules are applied to formula rows and data input rows that reference other rows. If the Bind for cross filter/RLS option is disabled, a manager responsible for Canada accounts can see a manually inserted row that references US data.
- **Minimum and Maximum values**: For driver input and distribution type rows, specify the minimum and maximum permissible input values.
- **Description:** Enter any text describing the row or technical notes in the Description box.

## Next steps

[Create a row model](how-to-create-row-model)

## Related content

[What is a row model?](planning-concept-row-model)

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
