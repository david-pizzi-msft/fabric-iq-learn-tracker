---
title: "Analyze planning outcomes with scenarios"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-set-up-scenarios](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-set-up-scenarios) · Last updated on **2026-07-20**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Analyze planning outcomes with scenarios

Summarize this article for me

Scenarios let you create multiple planning versions within a planning sheet to evaluate different business outcomes. Use scenarios to compare budgets, forecasts, and alternative business assumptions without affecting the base data.

## Prerequisites

Before you create a scenario, make sure that you have the following prerequisites in place:

- You have access to the planning sheet.
- Required fields and dimensions are added.
- The planning model includes a scenario dimension.
- You have permission to edit planning data.

## Create a scenario

1. Go to **Model > Scenario**.
2. Enter a name for the scenario in **Scenario name**.
3. Select the series to be simulated and select **Create**.

   [![Screenshot showing the steps to create a scenario.](media/planning-how-to-set-up-scenarios/create-scenario.png)](media/planning-how-to-set-up-scenarios/create-scenario.png#lightbox)
4. Adjust the slider to increase or decrease cell values and simulate sales values. Net revenue is recalculated accordingly.

   [![Screenshot showing the value slider for a cell.](media/planning-how-to-set-up-scenarios/value-slider.png)](media/planning-how-to-set-up-scenarios/value-slider.png#lightbox)
5. Review the results and select **Save** to save the scenario.
6. To create more scenarios, select the **+** icon at the bottom of the page. When you're done, select **Save** to save the report.

   [![Screenshot of adding another scenario and saving the report.](media/planning-how-to-set-up-scenarios/save-add.png)](media/planning-how-to-set-up-scenarios/save-add.png#lightbox)

The new scenario is added to the planning sheet and is available for planning and analysis.

## Scenario toolbar

Use the **Scenario** tab to create, manage, and analyze scenarios in the planning sheet.

[![Screenshot showing the  scenario toolbar.](media/planning-how-to-set-up-scenarios/scenario-toolbar.png)](media/planning-how-to-set-up-scenarios/scenario-toolbar.png#lightbox)

## Compare scenarios

Use **Compare scenarios** to analyze differences between two scenarios across measures, time periods, and dimensions. This view helps you evaluate performance, identify variances, and make data-driven decisions.

### Open scenario comparison

1. Go to the planning view.
2. Select **Compare Scenario**.
3. The **Scenario Comparison** view opens.

   [![Screenshot showing the compare scenario.](media/planning-how-to-set-up-scenarios/compare-scenario-tab.png)](media/planning-how-to-set-up-scenarios/compare-scenario-tab.png#lightbox)

### Configure comparison

The following configuration options are available:

- **Compare**: Select the primary scenario you want to analyze.
- **With**: Select the scenario to compare against.
- **Measures**: Choose the measures to include in the comparison. Select **All Measures** or a specific measure.

### Key elements of the comparison view

The comparison grid displays data across selected dimensions and time periods.

- **Scenarios**: Displays values for both selected scenarios.
- **Î Scenario**: Shows the variance between the two scenarios.
  - Positive values indicate an increase.
  - Negative values indicate a decrease.
- **Time periods**: Data is grouped by periods such as **Q1** and **Q2**.
- **Measures**: Displays values for selected measures.
- **Dimensions**: Rows represent hierarchical categories such as *Category*, *Beverages*, and *Water*.

### Exit comparison

Select **Exit Compare** to return to the standard view shown in the following image.

[![Screenshot showing the compare scenario view.](media/planning-how-to-set-up-scenarios/compare-scenario.png)](media/planning-how-to-set-up-scenarios/compare-scenario.png#lightbox)

## Update scenario settings

Update scenario settings such as the name, included measures, and lock status in **Edit Scenario** under **Scenario > Settings**.

- **Scenario name**: Update the name of the scenario.
- Under **Include series in scenarios**, select the measures to include:

  - Choose one or more series.
  - Only selected series are included in the simulation.
- **Lock the scenario**: Select **Lock Scenario** to prevent changes to the scenario.

  Note

  When a scenario is locked, you cannot modify values or settings until it is unlocked.
- Select **Apply** to save changes, or select **Cancel** to discard changes.

  [![Screenshot showing the scenario settings.](media/planning-how-to-set-up-scenarios/scenario-settings.png)](media/planning-how-to-set-up-scenarios/scenario-settings.png#lightbox)

## Configure input method

Use the **Input Method** to simulate and adjust values directly in the planning sheet.

![Screenshot for configuring the input in scenario.](media/planning-how-to-set-up-scenarios/configure-input.png)

### Simulation

Adjust the slider to increase or decrease cell values and test different outcomes.

Enter a custom value in a cell to apply a specific adjustment.

[![Screenshot for configuring the input using simulation in scenario.](media/planning-how-to-set-up-scenarios/scenario-simulation.png)](media/planning-how-to-set-up-scenarios/scenario-simulation.png#lightbox)

### Distribution

Distribution lets you apply consistent or trend-based changes quickly across multiple data points. Use the distribution options to apply values across rows or columns.

When adjusting distribution values, use the slider to increase or decrease values proportionally. Enter a custom value in a cell to apply a specific adjustment.

Available distribution options:

- **Copy until last row in <category>**: Apply the value to all rows from the selected category until the last row.
- **Copy until last row with trend in <category>**: Apply values across rows based on an existing trend.
- **Copy to all rows in <category>**: Distribute the value to all rows in the selected category.
- **Copy to all rows**: Apply the value across all rows in the sheet.
- **Copy until last column**: Apply the value across columns until the last column.
- **Copy until last column with trend**: Distribute values across columns using a trend.
- Select **Reset value** to revert changes to the original value.

  [![Screenshot for configuring the input using distribution in scenario.](media/planning-how-to-set-up-scenarios/scenario-distribution.png)](media/planning-how-to-set-up-scenarios/scenario-distribution.png#lightbox)

## Show variance

View differences between scenario values and base values when **Show variance** is checked.

![Screenshot for showing variance in scenario.](media/planning-how-to-set-up-scenarios/show-variance.png)

### Slider settings

Select **Slider settings** to open the **Variance settings** pane.

### Variance settings options

The **Variance settings** pane has the following options:

- **Series**: Displays the series included in the scenario.
- **Increase is good**: Enabled by default.
  - When enabled, increases are shown in green and decreases in red.
  - When disabled, increases are shown in red.
- **Value range**: Specify the maximum value for the range.
  - The default value is **100%**.

    [![Screenshot for showing slider settings in scenario.](media/planning-how-to-set-up-scenarios/slider-settings.png)](media/planning-how-to-set-up-scenarios/slider-settings.png#lightbox)

## Reset

Revert changes made in the scenario.

## Copy scenario data to base

Use **Copy to base** to apply simulated values from a scenario to the base sheet.

You can copy scenario values to the base by following these steps:

1. Select **Copy to base** from the **Scenario** toolbar, or select the **More options (â®)** menu next to the scenario tab.
2. Review the selected columns.
3. Select **Proceed**.

[![Screenshot for copying the scenario to base.](media/planning-how-to-set-up-scenarios/copy-base.png)](media/planning-how-to-set-up-scenarios/copy-base.png#lightbox)

The selected scenario values are copied to the corresponding base measures. After copying, the base report reflects the updated values from the selected scenario.

Note

Only simulated values are copied to the base. Native measures are not copied from scenarios to the base.

## Bulk edit in scenarios

Use **Bulk edit** to apply changes to multiple values in a scenario at once. Use bulk edit to efficiently perform large-scale scenario simulations without updating individual cells.

### Open and configure bulk edit

1. Select **Bulk Edit** from **Scenario**.
2. In the **Bulk Edit** pane, configure the following:
   - **Measure**: Select the scenario measure to update.
   - **Row dimensions**: Select the required categories and subcategories.
   - **Column dimensions**: Select the required columns or time periods.

Note

As you select dimensions, the planning sheet updates to reflect the filtered data.

### Apply bulk changes

1. **Set value**: Assign a specific value to the selected cells. Use the slider or input box to define the value or adjustment, or specify the value or percentage to apply.
2. Select **Apply**.

   [![Screenshot for bulk editing the scenario.](media/planning-how-to-set-up-scenarios/bulk-edit.png)](media/planning-how-to-set-up-scenarios/bulk-edit.png#lightbox)

The selected values are updated across the specified dimensions.

- **Cancel**: Closes the dialog without saving changes.
- **Reset**: Clears all selections and restores default settings.

## Pivot

Change the layout to analyze data from different perspectives. Use **Pivot** in the **Scenario** tab to create alternate row-level views for analyzing and simulating scenarios. Pivoting lets you rearrange dimensions, such as Category and Sub Category, without affecting the underlying data.

### Create a pivot

1. Go to the **Scenario** tab.
2. Select **Pivot**.
3. The **Row Pivot** dialog opens.
4. In the **Row Pivot** dialog, select **+ Add** to create a new pivot.
5. Enter a name for the pivot in the **Name** field.
6. In **Available fields**, select the dimensions to include.
7. Add selected fields to the **Fields** section. Arrange the fields in the desired order.
8. Select **Save**.

A pivot called *pivot 2* is created for subcategories.

[![Screenshot for applying pivots in scenario.](media/planning-how-to-set-up-scenarios/pivot-scenario.png)](media/planning-how-to-set-up-scenarios/pivot-scenario.png#lightbox)

## Writeback scenarios

Use **Writeback** to persist scenario data from the planning view to the underlying data source. You can write back all scenarios or a selected scenario. Use writeback to:

- Save planning inputs and updates
- Commit scenario changes to the data source
- Share finalized data with other users or systems

To write back scenarios,

1. Go to the **Scenario** tab.
2. Select **Writeback**.
3. Choose one of the following:

   - **Writeback All**: Writes back all available scenarios.
   - **Writeback**: Writes back only the selected scenario.
4. Writeback is completed.

   [![Screenshot for writeback in scenario.](media/planning-how-to-set-up-scenarios/writeback-scenario.png)](media/planning-how-to-set-up-scenarios/writeback-scenario.png#lightbox)

Note

The writeback option is enabled only after the destination is added. For more information, see [Write back data](planning-how-to-write-back-data).

## Logs

Use **Logs** to track and review all writeback activities. Go to **Scenario** > **Logs**. This view provides detailed information about each writeback operation, including status, duration, and user details.

[![Screenshot for writeback logs in scenario.](media/planning-how-to-set-up-scenarios/writeback-logs.png)](media/planning-how-to-set-up-scenarios/writeback-logs.png#lightbox)

## Close scenario

Exit the current scenario by selecting **Close Scenario** from **Scenario**.

## Configure scenario access

Control who can access, manage, and interact with scenario using the **Security** settings.

1. Select **Security** from the toolbar.
2. In the left pane, select **Scenario**.
3. **Who can access scenario**: Specify users who can view and interact with each scenario. Enter names to grant access.
4. Select **Save** to apply changes, or select **Cancel** to discard the changes.

   [![Screenshot for  scenario access.](media/planning-how-to-set-up-scenarios/scenario-access.png)](media/planning-how-to-set-up-scenarios/scenario-access.png#lightbox)

## FAQ

### Is Base an editable scenario, or is it a fixed reference point?

Base represents the current committed plan and acts as the reference point against which you compare other scenarios. You create scenarios like *Best Case* as separate simulation layers on top of Base rather than as direct edits to it.

### After creating a scenario, do its values carry forward into new scenarios?

Noâeach new scenario is its own separate simulation layer on top of the original Base figures. You don't build new scenarios on top of another scenario's adjusted values.

### Can calculated measures that use native measures be simulated?

You can't directly simulate calculated measures that reference native measures because they don't store independent values. Instead, their values come from the underlying native measures through a calculation or formula.

### **How do simulated changes propagate through dependent measures?**

When you apply a simulated change to a leaf-level value, the update automatically propagates through all dependent measures in the hierarchy. Parent measures that aggregate child values and calculated measures that reference those aggregations are recalculated in real time. This process ensures that every affected value across the hierarchy instantly reflects the simulated change, without requiring manual updates.

### Can more than one scenario exist at the same time without one overwriting the other?

Yesâdifferent scenarios, such as *Best Case* and *Cost Restructuring*, can coexist. They're separate and independently referenceable.

### Are scenario simulations permanent once created, or can I delete them without affecting the base scenario?

Simulations exist within their scenario and don't alter Base or the underlying data source values. You can adjust or delete them without any permanent impact on the actual plan.

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
