---
title: "Create a P&L forecast"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-build-forecasts](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-build-forecasts) · Last updated on **2026-11-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create a P&L forecast

Summarize this article for me

Use the Forecast feature to extend the time horizon of a planning sheet by creating a visual measure for future periods. For example, if a planning sheet contains data for 2024 and 2025, create a forecast measure to project values for 2026. You can visualize future-period projections alongside historical or existing planning data without modifying the underlying planning data.

In this article, you learn to:

- Create a forecast using historical actuals as a baseline
- Create a zero-based forecast
- Top-down and bottom-up forecast allocation
- Lock forecast values
- Create statistical forecasts using Predict
- Generate deviation between budgets and forecasts

## Prerequisites

- Create a planning sheet and assign row and column dimensions.
- The column dimension should be a standard date hierarchy such as Year > Quarter > Month.

  [![Screenshot of a standard date hierarchy assigned to the column dimension data well in a planning sheet.](../media/planning-forecasting/planning-how-to-build-forecasts/prerequisite-date-hierarchy-columns.jpg)](../media/planning-forecasting/planning-how-to-build-forecasts/prerequisite-date-hierarchy-columns.jpg#lightbox)

  Note

  The maximum forecast range depends on the finest (lowest) granularity level in your time dimension. For example, if the lowest level in your hierarchy is Month, you can extend the forecast range up to 25 years.

  The maximum forecast horizon for each granular unit is:

  - Year - Up to 100 years
  - Quarter - Up to 50 years
  - Month - Up to 25 years
  - Week - Up to 10 years
  - Day - Up to 5 years

## Create a forecast from historical actuals

Configure forecasts using historical actuals as the starting point for future periods. This approach carries forward historical trends and values to provide a baseline for forecasting, which you can adjust in response to expected business changes.

1. In the **Model** ribbon, select **Forecast**.
2. The default measure name is set to *Forecast.* Set a custom name if required, and then select the future period to forecast. The plan automatically populates the forecast period based on the existing data. Select **Next** to configure closed periods.

   [![Screenshot of entering the forecast measure name and selecting the forecast period.](../media/planning-forecasting/planning-how-to-build-forecasts/forecast-measure-name-period-selection.jpg)](../media/planning-forecasting/planning-how-to-build-forecasts/forecast-measure-name-period-selection.jpg#lightbox)
3. Closed periods represent past periods for which actual data is available. Forecast values for closed periods are locked and can't be edited. Use an existing measure or formula to populate closed forecast periods.

   To use existing measure values for closed forecasts, select **Link to Measure** and choose the measure from **Source Measure**. In this example, you populate closed periods with values from the *Actuals* measure. Select **Next** to configure open periods.

   [![Screenshot of the closed period link to measure configuration that uses actuals.](../media/planning-forecasting/planning-how-to-build-forecasts/closed-forecast-actuals-link-measure.jpg)](../media/planning-forecasting/planning-how-to-build-forecasts/closed-forecast-actuals-link-measure.jpg#lightbox)
4. Select **Data Input** to manually enter forecasts. Retain the default **None** option for **Default Value.**

   [![Screenshot of data input option to enter open period forecasts manually.](../media/planning-forecasting/planning-how-to-build-forecasts/open-period-data-input-option.jpg)](../media/planning-forecasting/planning-how-to-build-forecasts/open-period-data-input-option.jpg#lightbox)
5. To prepopulate open forecasts from historical data, expand the **Pre-fill Open Periods** section. To initialize forecast values from a specific historical period:

   - Configure **Copy from** with the measure that contains the source values.
   - Set **Operation** to **Period Range**.
   - Define the periods to copy by specifying the **Source Range** as the historical period and the **Target Range** as the future period. Planning copies the values from the source range to the corresponding periods in the target range to initialize the forecast.

   In this example, you initialize the 2026 *Budget* with the 2025 *Actuals*.

   [![Screenshot of prefill option for data input open periods with the period range option to copy values from 2025 to the 2026 forecast.](../media/planning-forecasting/planning-how-to-build-forecasts/open-period-prefill-period-range.png)](../media/planning-forecasting/planning-how-to-build-forecasts/open-period-prefill-period-range.png#lightbox)

   After you save the configuration, the plan creates the *Budget* measure as a time extension for 2026. Notice that *Actuals* aren't available for the forecast period.

   - The *Budget* measure is locked for 2023, 2024, and 2025 and populated with *Actuals* according to the configuration in Step 3.
   - The 2026 *Budget* remains available for forecasting.

   [![Screenshot of the closed forecast that is locked and editable open forecast initialized with prior year actuals.](../media/planning-forecasting/planning-how-to-build-forecasts/closed-period-locked-open-period-initialized-actuals.png)](../media/planning-forecasting/planning-how-to-build-forecasts/closed-period-locked-open-period-initialized-actuals.png#lightbox)
6. To analyze specific periods in a forecast, select **Period** from the **Model** ribbon. Select the **Calendar** icon to define the required time range. To focus only on actual and forecast values, clear **Show Closed Periods** to hide locked historical values from the view.

   [![Screenshot of options to display a specific forecasting period and hide closed periods.](../media/planning-forecasting/planning-how-to-build-forecasts/period-settings-hide-closed-periods.png)](../media/planning-forecasting/planning-how-to-build-forecasts/period-settings-hide-closed-periods.png#lightbox)

   In Step 3, you selected **Period Range** to initialize the open forecast periods. Based on this configuration, planning creates the 2026 *Budget* by copying the corresponding *Actuals* values from 2025. This provides an initial forecast for 2026 using the values from the selected historical period.

   [![Screenshot of initializing a forecast using the period range option and copying historical values from the corresponding past period.](../media/planning-forecasting/planning-how-to-build-forecasts/period-range-forecast-prefill-historical-data.png)](../media/planning-forecasting/planning-how-to-build-forecasts/period-range-forecast-prefill-historical-data.png#lightbox)

## Create a zero-based forecast

Use zero-based forecasts to enter new forecast values based on current assumptions, targets, or business expectations.

1. To create another forecast measure, expand the **Measures** pane and select **Add new measure.**

   [![Screenshot of option to add a new forecast measure from the forecasting window.](../media/planning-forecasting/planning-how-to-build-forecasts/add-new-forecast-measure.png)](../media/planning-forecasting/planning-how-to-build-forecasts/add-new-forecast-measure.png#lightbox)
2. Follow the same steps as in the previous section to configure the forecast timeframe and closed periods.

   [![Screenshot of creating a new forecast measure and entering the measure name and forecast period.](../media/planning-forecasting/planning-how-to-build-forecasts/new-forecast-measure-closed-period-initial-settings.png)](../media/planning-forecasting/planning-how-to-build-forecasts/new-forecast-measure-closed-period-initial-settings.png#lightbox)
3. In the **Open Period** configuration, ensure that you select **Data Input.** Leave the other options unchanged. Select **Save**.

   [![Screenshot of selecting the data input option to create zero based forecasts.](../media/planning-forecasting/planning-how-to-build-forecasts/zero-based-forecast-open-period.png)](../media/planning-forecasting/planning-how-to-build-forecasts/zero-based-forecast-open-period.png#lightbox)

   The screenshot shows the *Budget* sourced from *Actuals* alongside the zero-based *Forecast*. The budget values are initialized using the corresponding actuals, while the forecast starts with zero values for the open forecast periods.

   [![Screenshot of a budget forecast created from historical data and a zero based forecast.](../media/planning-forecasting/planning-how-to-build-forecasts/budget-historical-data-zero-based-forecast.png)](../media/planning-forecasting/planning-how-to-build-forecasts/budget-historical-data-zero-based-forecast.png#lightbox)

## Allocate forecasts across hierarchical data

Top-down and bottom-up allocation provide complementary approaches to distributing forecast values across business dimensions.

Top-down allocation starts with a high-level forecast and distributes it to lower-level entities, while bottom-up allocation builds the forecast from detailed inputs and aggregates them to higher levels.

1. Before allocation, in the **Planning** ribbon, change the scaling to **None**.

   [![Screenshot of changing the number scaling to None to show the full number.](../media/planning-forecasting/planning-how-to-build-forecasts/number-scaling-select-none.png)](../media/planning-forecasting/planning-how-to-build-forecasts/number-scaling-select-none.png#lightbox)
2. For top-down allocation, double-click the grand total cell for *Budget* and enter the new value.

   [![Screenshot of entering a value for the grand total budget for top down allocation.](../media/planning-forecasting/planning-how-to-build-forecasts/top-down-allocation-enter-value-grand-total-level.png)](../media/planning-forecasting/planning-how-to-build-forecasts/top-down-allocation-enter-value-grand-total-level.png#lightbox)
3. The value you enter is automatically allocated to child nodes.

   [![Screenshot of the grand total budget value allocated from parent to child nodes based on self weight.](../media/planning-forecasting/planning-how-to-build-forecasts/entered-value-allocated-child-nodes-self-weight.png)](../media/planning-forecasting/planning-how-to-build-forecasts/entered-value-allocated-child-nodes-self-weight.png#lightbox)
4. You can enable subtotals before bottom-up allocations. In the **Planning** tab, set **Column Subtotal** to **Left**. This action shows the *2026 Total* column.

   [![Screenshot of enabling the column subtotal and displaying it on the left side.](../media/planning-forecasting/planning-how-to-build-forecasts/enable-column-subtotal-left-position.png)](../media/planning-forecasting/planning-how-to-build-forecasts/enable-column-subtotal-left-position.png#lightbox)
5. Select a leaf node or subtotal node and enter the required value.

   [![Screenshot of entering a forecast value for a subtotal chart of accounts row.](../media/planning-forecasting/planning-how-to-build-forecasts/enter-value-leaf-node-subtotal-node.png)](../media/planning-forecasting/planning-how-to-build-forecasts/enter-value-leaf-node-subtotal-node.png#lightbox)
6. The value you enter aggregates to the grand total *Budget*.

   [![Screenshot of bottom-up allocation with the entered value aggregated to the grand total Budget row.](../media/planning-forecasting/planning-how-to-build-forecasts/value-entered-aggregated-grand-total.png)](../media/planning-forecasting/planning-how-to-build-forecasts/value-entered-aggregated-grand-total.png#lightbox)

## Lock forecasts

Lock values entered in a planning sheet to prevent further edits and preserve approved planning data.

1. In the **Model** ribbon, go to **Rules** > **Locking Rule**.
2. To lock edits to the *Budget* measure, set **Apply to Measures** to **Selected Measures**, and then select *Budget* from **Choose Measures**. Select **Apply to Children** to prevent editing child nodes.

   [![Screenshot of locking rule configuration for a particular measure and specific row.](../media/planning-forecasting/planning-how-to-build-forecasts/locking-rule-selected-measure-selected-row-dimension.png)](../media/planning-forecasting/planning-how-to-build-forecasts/locking-rule-selected-measure-selected-row-dimension.png#lightbox)
3. Select **Create**. This rule locks the *Budget* measure.

   [![Screenshot of the locking rule applied to the Budget measure, showing locked cells in the planning grid.](../media/planning-forecasting/planning-how-to-build-forecasts/budget-measure-editing-locked.png)](../media/planning-forecasting/planning-how-to-build-forecasts/budget-measure-editing-locked.png#lightbox)

## Create statistical forecasts based on seasonality and trends

Statistical forecasting uses historical data and statistical models to identify patterns and trends, and generates forecasts without manual input. For more information about Predict, see [Generating statistical forecasts](planning-how-to-generate-statistical-forecasts-using-predict-feature).

1. Before using **Predict**, in the **Model** ribbon, go to **Period** to display historical data from 2023 and 2024. Hide closed forecasts to focus on historical data and the periods available for forecasting.
2. Predict works on any hierarchy level. In this example, select the grand total *Forecast,* then select **Predict** on the **Model** ribbon. The plan displays the selected row and measure.

   [![Screenshot of the Predict side pane showing the selected measure and forecast row.](../media/planning-forecasting/planning-how-to-build-forecasts/predict-pane-selected-measure-forecast-row.png)](../media/planning-forecasting/planning-how-to-build-forecasts/predict-pane-selected-measure-forecast-row.png#lightbox)
3. Set **Evaluation** to **Bottom Up**. This option generates the predicted future value based on the trend of individual leaf nodes; in this example, the chart of accounts.
4. The **Trend Decomposition** forecasting algorithm is selected by default. For more information about algorithms, see [Statistical forecasting algorithms](../planning-concept-predict). Select **Year** for **Set Seasonality** and select **Run Forecast**.

   [![Screenshot of the evaluation options and seasonality option in predict.](../media/planning-forecasting/planning-how-to-build-forecasts/predict-evaluation-seasonality-option.png)](../media/planning-forecasting/planning-how-to-build-forecasts/predict-evaluation-seasonality-option.png#lightbox)
5. Preview the predicted forecast values in a graph to visualize the expected trends and patterns across future periods.

   [![Screenshot of graph showing the trend of predicted values with the confidence range.](../media/planning-forecasting/planning-how-to-build-forecasts/predict-graph-forecasted-values.png)](../media/planning-forecasting/planning-how-to-build-forecasts/predict-graph-forecasted-values.png#lightbox)
6. Scroll down to view the actual predicted values and the confidence interval and range for each value.

   [![Screenshot of table showing the actual predicted values and the confidence interval.](../media/planning-forecasting/planning-how-to-build-forecasts/predict-table-view-actual-forecasted-values.png)](../media/planning-forecasting/planning-how-to-build-forecasts/predict-table-view-actual-forecasted-values.png#lightbox)
7. Select **Save Forecast**. Review the forecast measure and period, and then select **Save** to apply the predicted values in the planning sheet.

   [![Screenshot of the planning sheet with statistical forecast predicted values applied for the selected forecast period.](../media/planning-forecasting/planning-how-to-build-forecasts/statistical-forecast-values-applied-planning-sheet.png)](../media/planning-forecasting/planning-how-to-build-forecasts/statistical-forecast-values-applied-planning-sheet.png#lightbox)

## Generate deviation between budget and forecast

Deviation shows how actual or forecasted results differ from the original budget or target. It helps you identify where performance is above or below expectations and highlights areas that might require corrective action.

1. In the **Planning** ribbon, select **Forecast**. Set the **Measure Name** to *Deviation*. Keep the default forecast period for Jan - Dec 2026.
2. In the **Closed Period** configuration, select **Formula** and enter the formula to calculate the deviation between *Budget* and *Forecast*.

   [![Screenshot of closed period configuration to populate values based on a deviation formula.](../media/planning-forecasting/planning-how-to-build-forecasts/closed-period-formula-based-deviation.png)](../media/planning-forecasting/planning-how-to-build-forecasts/closed-period-formula-based-deviation.png#lightbox)
3. Use the same configuration for open periods. Select **Save**.

   [![Screenshot of open period configuration to populate values using a deviation formula.](../media/planning-forecasting/planning-how-to-build-forecasts/open-period-formula-based-deviation.png)](../media/planning-forecasting/planning-how-to-build-forecasts/open-period-formula-based-deviation.png#lightbox)

   This action creates the deviation measure.

   ![Screenshot of the deviation measure created between the budget and forecast measures.](../media/planning-forecasting/planning-how-to-build-forecasts/create-deviation-budget-forecast.png)

## Related content

- To learn about setting up customized fiscal years for your planning data, see [Fiscal year setup in planning and reporting](../planning-concept-fiscal-year-setup).
- For best practices on using supported date formats for automatic time intelligence, see [Best practices and supported date formats for automatic time intelligence](../resources/best-practices/time-intelligence).
- To manually set up and map date formats when plan fails to detect the date format automatically, see [Map date fields manually](../resources/how-to-manually-map-time-intervals).

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
