---
title: "Fabric planning tutorial part 3: Optimize data input measures to achieve a target result"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-3-forecasting-writeback](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-tutorial/planning/tutorial-3-forecasting-writeback) · Last updated on **2026-09-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Fabric planning tutorial part 3: Optimize data input measures to achieve a target result

Summarize this article for me

In this tutorial, you learn how to create rolling forecasts in planning sheets:

- Build a rolling 2026 forecast anchored on 24 months of actuals
- Generate a statistical forecast using the Trend Decomposition with MSTL algorithm
- Close January 2026 as actuals arrive
- Extend the horizon to January 2027
- Commit the finalized forecast to a Fabric SQL database

## Prerequisites

Before you start this tutorial, ensure you complete the first three tutorials:

- [Introduction to planning in Microsoft Fabric](tutorial-0-introduction)
- [Allocations and collaboration](tutorial-1-allocation-collaboration)
- [Optimize input values](tutorial-2-optimizer)

This tutorial uses the plan app and the Fabric SQL database you created in the previous tutorials.

## Create a rolling forecast sheet

In this section, you set up the forecast planning sheet and create a blank forecast measure for 2026, ready to be populated by the statistical model.

1. In *Northwind\_FMCG\_Plan*, select **New Planning Sheet** in the **Home** ribbon. Enter *Forecast* and select **Create**.
2. Configure the field assignments:

   | Field | Value |
   | --- | --- |
   | Rows | Category â Sub-Category |
   | Columns | Date hierarchyâYear, Quarter, Month Short |
   | Values | Gross Revenue |
3. In the **Filter** panel in the sidebar, apply a year filter for 2024 and 2025. Only these two yearsâ values feed into the statistical forecast.
4. In the **Planning** ribbon, select **Totals** and enable **Column Subtotal** on the left.

   [![Screenshot of the Totals menu in the Planning ribbon with Column Subtotal enabled.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/planning-ribbon-enable-column-subtotal.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/planning-ribbon-enable-column-subtotal.png#lightbox)
5. In the **Model** ribbon, select **Forecast**.
6. Enter *Forecast* as the measure name. Set the *Forecast Period* to Jan 2026 to Dec 2026. Select **Next**.

   [![Screenshot of entering the forecast measure name and selecting the forecast period.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-measure-name-period-range.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-measure-name-period-range.png#lightbox)
7. In the closed period configuration, select **Link to Measure** and set **Source Measure** to *Gross Revenue*. This configuration brings in the corresponding Gross Revenue actuals once a period closes. Select **Next**.

   [![Screenshot of configuring closed periods to use Gross revenue as the source.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/closed-period-source-gross-revenue.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/closed-period-source-gross-revenue.png#lightbox)
8. In the open period configuration, select **Data Input** and set **Default Value** to **None**. Leaving open periods blank allows the predict feature to populate the forecast using statistical methods. Select **Save**.

   [![Screenshot of the data input option for configuring open periods.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/open-period-data-input.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/open-period-data-input.png#lightbox)
9. Observe that the 2024 and 2025 forecast columns appear greyed out, indicating closed periods. The 2026 columns are open and empty, ready for the statistical model.

   [![Screenshot of a blank forecast created for 2026 with 2024 and 2025 forecasts populated with Gross Revenue values.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-grid-2026-blank-closed-periods-greyed.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-grid-2026-blank-closed-periods-greyed.png#lightbox)

## Generate the statistical forecast

In this section, you run the statistical forecast across the full JanuaryâDecember 2026 horizon using 24 months of historical actuals. The Trend Decomposition with MSTL algorithm detects seasonal patterns at both annual and quarterly cycles and generates a complete year of forecasted values in one pass.

1. Select the cell at the intersection of the *All* row and the Forecast subtotal column for 2026.
2. In the **Model** ribbon, select **Predict**. The Predict panel opens.
3. Use the lock icon to freeze the selection. Confirm **Row Selected** is *Grand Total* and **Select Measure** is *Forecast*.
4. Confirm the following default selections:

   | Setting | Value |
   | --- | --- |
   | Historic data range | Jan 2024âDec 2025 |
   | Forecast date range | Jan 2026âDec 2026 |
5. Configure the forecast as follows:

   | Setting | Value |
   | --- | --- |
   | Confidence | 90% |
   | Growth factor | 4% |
   | Evaluation | Bottom Up |
   | Round all negative values to zero | No |

   [![Screenshot of the predict forecast settings to set the confidence, growth factor, and evaluation.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/predict-settings-evaluation-confidence.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/predict-settings-evaluation-confidence.png#lightbox)
6. Under **Choose Algorithm**, confirm **Trend Decomposition with MSTL** is selected. Under **Customize Algorithm**, select both **Year** and **Quarter** under **Set Seasonality**. This selection tells the model to detect and account for patterns at both cycle levels at the same time. Select **Run Forecast**.

   [![Screenshot of selecting the trend decomposition algorithm and setting the seasonality to Year and Quarter.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/select-trend-decomposition-seasonality.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/select-trend-decomposition-seasonality.png#lightbox)
7. The forecast preview appearsâhistorical data in grey, predicted values in green, with the confidence range shown as green shading.

   [![Screenshot of the forecast preview graph showing historical values in grey, predicted values in green, and a shaded confidence interval.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/predict-values-preview-graph.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/predict-values-preview-graph.png#lightbox)
8. Scroll down to see the forecast table. Select **Save Forecast**.

   [![Screenshot of the actual predict values displayed in tabular format along with the confidence interval.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-predicted-values-table-view.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-predicted-values-table-view.png#lightbox)
9. Confirm the forecast measure and the date range, and then select **Save**. The statistical forecast is created with values calculated at the most granular level of the row and column hierarchies, then aggregated up to higher levels.

   [![Screenshot of statistical forecast values applied to the planning sheet.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/statistical-forecast-created-using-predict.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/statistical-forecast-created-using-predict.png#lightbox)

## Close the period and extend the forecast horizon

In this section, you reveal January 2026 actuals, close the period to lock them in, extend the horizon to January 2027, and reforecast the newly opened month.

### Reveal January 2026 actuals

In this part, you add 2026 to the year filter to reveal January's actual Gross Revenue alongside the statistical forecast. Comparing the two values shows how closely the forecast matched actuals.

1. In the **Filter** panel, edit the existing year filter and add 2026 alongside 2024 and 2025.
2. Expand the column headers and compare the two January 2026 values side by side:

   - Forecast: $2.09mâthe value generated by the statistical model
   - Gross Revenue: $1.92mâthe actual January figure

   [![Screenshot of actuals populated for 2026 and comparing the predicted forecast with actuals.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/enable-revenue-actuals-2026.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/enable-revenue-actuals-2026.png#lightbox)

### Close January forecast and extend the horizon

In this section, you close the January 2026 forecast to lock in the actuals and extend the forecast horizon by one month. This action keeps a continuous 12-month forward view as each period closes.

1. In the **Model** ribbon, select the **Period** dropdown and select **Close Period**.
2. In the **Close Period** dialog box, select the **Close period till** dropdown and select **Custom**. Set the period to January 2026.
3. Select **Extend Forecast Range** and set **Duration** to 1 Month. This action maintains a continuous 12-month forward window. As January closes, January 2027 is added to the horizon.

   [![Screenshot of the Close Period dialog with January 2026 set as the custom period and the forecast range extended by one month.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/close-period-configuration-extend-one-month.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/close-period-configuration-extend-one-month.png#lightbox)
4. Select **Preview**. Verify the following values, and then select **Save**:

   | Field | Value |
   | --- | --- |
   | Measure | Forecast |
   | Closed period | Jan 2024âJan 2026 |
   | Open period | Feb 2026- Jan 2027 |
5. January 2026 is now populated with actual gross revenue and greyed out. The forecast horizon extends automatically to January 2027.

   [![Screenshot of closing the January 2026 forecast and creating a rolling forecast by extending it to January 2027.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-extended-2027.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/forecast-extended-2027.png#lightbox)

### Reforecast January 2027

In this section, you reforecast the newly opened January 2027 period using January 2026 actuals as a baseline. This approach gives the extended month a realistic starting value instead of an empty cell.

1. In the **Model** ribbon, select **Reforecast** and select **Reforecast Column**. Configure it as follows and select **Apply**:

   | Setting | Value |
   | --- | --- |
   | Target period | Jan 2027âJan 2027 |
   | Copy source | Gross Revenue |
   | Apply operation | Single Period |
   | Source periods | Jan 2026 |

   [![Screenshot of the reforecast configuration for January 2027 using the Single Period operation with source period Jan 2026.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/reforecast-configuration-single-period.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/reforecast-configuration-single-period.png#lightbox)
2. January 2027 is seeded from January 2026 actuals ($1.92M), giving a realistic baseline for the extended horizon.
3. Double-click the Jan 2027 grand total cell, enter +4%, and select the check mark. January 2027 is now populated at $2M.

   [![Screenshot of increasing the forecast for 2027 by four percent.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/reforecast-increase-value-four-percent.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/reforecast-increase-value-four-percent.png#lightbox)

## Commit the forecast to the database

In this section, you add a writeback destination, configure writeback settings, run writeback, and verify the results in the database.

For an overview of writeback concepts, see [Writeback in Planning](../../planning-writeback/planning-how-to-persist-data).

### Add a writeback destination

In this section, you add the Fabric SQL database as a writeback destination for the forecast measure. This destination determines where committed values are written when you run writeback.

1. In the **Writeback** ribbon, select **Add destination**.
2. In **Create Destination**, configure the settings as shown in the following table and select **Add**:

   | Setting | Value |
   | --- | --- |
   | Select connection | Northwind\_FMCG (created in Tutorial 1) |
   | Database name | Northwind\_FMCG\_Lisa Taylor (created in Tutorial 1) |
   | Schema | dbo |
   | Table name | Forecast |
   | Decimal precision | 2 |
   | Text length | 512 |
3. A confirmation message appears when you add the destination successfully.
   <Add image here - image 56 with writeback add destination settings>

### Configure writeback settings

In this section, you configure how the forecast is written to the database - the writeback type, which measures are included, and the destination. These settings determine what gets written and how each writeback run behaves.

1. In the **Writeback** ribbon, select **Settings**. The settings panel has four tabsâ**General**, **Data**, **Destinations**, and **Advanced**.
2. In the **General** tab, select the information icon next to each writeback type to review the options:

   | Type | Behavior |
   | --- | --- |
   | Long | One row per observation. Full snapshot every run. |
   | Wide | Each measure as a separate column. Full snapshot every run. |
   | Long with Changes | Writes only changed values. Builds an audit history over time. |
   | Wide with Changes | Same as Wide but writes only changed values. |
3. Select **Long with Changes**. A warning appears confirming the destination will be turned off. Select **Proceed**.
4. Confirm **Filter type** is set to **None**âthis writes back all data without filtering.

   [![Screenshot of general settings for writeback with the writeback type set to Long with Changes and filter type set to None.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/general-settings-writeback-type-filter.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/general-settings-writeback-type-filter.png#lightbox)
5. Select the **Data** tab. Deselect *Gross Revenue*âthis is a read-only actuals measure and doesn't need to be committed to the database. Only Forecast should be selected.

   [![Screenshot of selecting the Forecast measure and deselecting the native Gross Revenue measure for writeback.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/writeback-data-settings-select-forecast.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/writeback-data-settings-select-forecast.png#lightbox)
6. Open the **Destinations** tab and select the Fabric SQL destination created in [Add a writeback destination](#add-a-writeback-destination).

   [![Screenshot of selecting the Fabric SQL writeback destination.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/select-fabric-sql-destination.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/select-fabric-sql-destination.png#lightbox)

### Run writeback and verify data

In this section, you run writeback and confirm that writeback saves forecast data correctly in the Fabric SQL database. You also review the writeback logs to see the run's status and details.

1. In the **Writeback** ribbon, select **Writeback**. A confirmation message that states, *Writeback Completed*, appears within a few seconds.
2. Open your training workspace folder and open the Northwind\_FMCG SQL database.
3. Expand **Northwind\_FMCG** > **dbo** > **Tables** and select the *Forecast* table. Verify the forecast data appears in the preview.

   [![Screenshot of forecast data from the planning sheet written back to a Fabric SQL table in the Northwind_FMCG database.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/verify-forecast-writeback-fabric-sql.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/verify-forecast-writeback-fabric-sql.png#lightbox)
4. Go back to the plan app. In the **Writeback** ribbon, select **Logs**. Review the log details - status, duration, user who performed the writeback, measures written back, and writeback type.

   [![Screenshot of writeback logs screen with details including the job id, duration, status, trigger time and user who initiated the writeback instance.](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/writeback-logs.png)](../../media/planning-tutorial/planning/tutorial-3-forecasting-writeback/writeback-logs.png#lightbox)

## Next steps

Build a P&L measure model, then create and compare scenarios in tree view in the next tutorial, [Build a P&L hierarchy](tutorial-4-measure-model)

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
