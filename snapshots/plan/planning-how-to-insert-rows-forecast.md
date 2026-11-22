---
title: "Insert forecast rows"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-rows-forecast](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-rows-forecast) · Last updated on **2026-05-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert forecast rows

Summarize this article for me

Create row-level forecasts to predict outcomes at a detailed level, such as by region or product line. After you create a forecast measure, you can generate forecasts at the row level by inserting a forecast row.

This article explains how to create and configure forecast rows.

Note

The **Forecast** row option is only available when the report contains forecast measures. For more information, see [Forecast measures](planning-forecasting/planning-how-to-build-forecasts).

## Insert a forecast row

1. Select the row where you want to create the forecast.
2. Go to **Planning** > **Insert Row** > **Forecast**, or use the **row gripper** > **Insert** > **Forecast Row**.

   ![Screenshot of inserting a forecast row using planning tab.](media/planning-how-to-insert-rows-forecast/insert-forecast-row-planning-tab.png)

   ![Screenshot of inserting a forecast row using row gripper.](media/planning-how-to-insert-rows-forecast/insert-forecast-row-row-gripper.png)
3. In the Forecast configuration window, enter a row name and [configure](#configure-forecast-row-properties) the required options.
4. Select **Save** to generate the forecast row.

## Configure forecast row properties

The following options can be configured while creating a forecast row:

- **Row name**: Specifies the label for the forecast row.
- **Insert As**: Choose one of the following options.

  - **Single Row**: Inserts a single forecast row.
  - **Templated Row**: Replicates the forecast row across all hierarchy levels.

  ![Screenshot of configuring row name and insert as option.](media/planning-how-to-insert-rows-forecast/insert-as.png)
- **Closed period**: Populate past or closed periods by choosing one of the following options.

  - Referencing another row: Select **Linked Row** in **Closed Period** and choose the row you want to refer.

    ![Screenshot of configuring closed period through linked row option.](media/planning-how-to-insert-rows-forecast/linked-row.png)
  - Defining a formula: Select **Formula** in **Closed Period** and define the formula.

    ![Screenshot of configuring closed period through formula option.](media/planning-how-to-insert-rows-forecast/formula.png)
- **Open period**: Populate future periods using one of the following options.

  - **Linked row**: Reference values from another row.

    ![Screenshot of options available in open period.](media/planning-how-to-insert-rows-forecast/open-period.png)
  - **Formula**: Define a formula for forecast values.
  - **Data input**: Manually enter forecast values with optional default values using a **static** value, another **row**, or a **formula**.

    ![Screenshot of options available in data input type in open period.](media/planning-how-to-insert-rows-forecast/open-period-data-input.png)

Note

Select the **Templated** option when the row categories repeat across all levels of the hierarchy.

## Configure forecast range

The forecast time frame is configured when you [create a forecast measure](planning-forecasting/planning-how-to-build-forecasts). After configuring forecast row properties, select **Next** to define the forecast time range in **Target Periods**.

Note

The **Next** option to configure the period range is only available when **Data input** is selected for the **Open period**.

The forecast range can be configured using one of the following options:

- Apply a single configuration for the entire period.

  ![Screenshot of configuring single forecast range.](media/planning-how-to-insert-rows-forecast/single-configuration.png)
- Split the forecast into multiple time ranges using **Add Range**.

  ![Screenshot of configuring multiple forecast range.](media/planning-how-to-insert-rows-forecast/multiple-time-range.png)

  When you split the forecast period, ensure that all time ranges together cover the entire forecasting duration. Otherwise, the forecast cannot be created.

## Configure forecast source

- **Set source**: Choose how to populate forecast values:

  - Use a blank forecast (manual input).
  - Reference another row.

    ![Screenshot of set source option.](media/planning-how-to-insert-rows-forecast/set-source.png)
- **Source row**: Select the row whose values will be used when sourcing by row.

  ![Screenshot of source row option.](media/planning-how-to-insert-rows-forecast/source-row.png)
- **Operation**: Define how forecast values are calculated:

  - **Period range**: Copy values from a selected time range.
  - **Single period**: Use values from a specific period.
  - **Average of period range**: Use the average of selected periods.

    ![Screenshot of options available in operation.](media/planning-how-to-insert-rows-forecast/operation.png)

## Edit and update a forecast row

Edit an existing forecast row by selecting the edit icon on the row. The side pane opens where the following properties can be updated:

[![Screenshot of the side pane when editing a forecast row.](media/planning-how-to-insert-rows-forecast/edit-update.png)](media/planning-how-to-insert-rows-forecast/edit-update.png#lightbox)

- Edit the **Title** as needed.
- Reconfigure **Period Settings** to update forecast values for closed and open periods.
- Configure **Scaling Factor**, **Bind for Cross filter/RLS**, **Include in total**, **Allow Input** and **Description**.

For more information, see [data input row properties](planning-how-to-insert-rows-data-input#data-input-row-properties). After making the required changes, select **Update**.

[![Screenshot of the side pane with more options when editing a forecast row.](media/planning-how-to-insert-rows-forecast/edit-update-more-options.png)](media/planning-how-to-insert-rows-forecast/edit-update-more-options.png#lightbox)

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
