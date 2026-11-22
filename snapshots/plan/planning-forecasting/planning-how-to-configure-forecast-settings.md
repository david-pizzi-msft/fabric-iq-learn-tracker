---
title: "Configure forecast settings"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-configure-forecast-settings](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-configure-forecast-settings) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure forecast settings

Summarize this article for me

Keep forecasts aligned with reporting cycles by editing the forecast period, managing closed periods, configuring aggregation, and defining how actuals update forecast results.

## Prerequisites

- A forecast measure must be created in the planning sheet.

## Editing forecasts

Select **Planning** > **Insert Column** > **Manage Measures** and select the edit icon for the forecast measure.

Tip

You can also edit forecasts by selecting **Edit Measure** from the column gripper.

The following edit options are available:

- To extend or shorten the open period, select the end period in **Forecast Period**.

  [![Screenshot of editing the forecast period.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/edit-forecast-period.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/edit-forecast-period.png#lightbox)

  The open forecast is shortened until Q3, and the Q4 forecast is removed.

  [![Screenshot of shortening the forecast period.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/edit-forecast-period-result.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/edit-forecast-period-result.png#lightbox)
- Use **Closed Period Range** to reopen forecasts. Select the period up to which closed forecasts should be reopened.

  Tip

  Select **Reset closed period range** to reopen all closed forecast periods.

  [![Screenshot of option to extend or shorten the closed period range.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/edit-closed-period-range.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/edit-closed-period-range.png#lightbox)

  The Q2 forecast is reopened.

  [![Screenshot of reopening closed forecasts.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/reopen-forecast.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/reopen-forecast.png#lightbox)
- To change the values used to populate open and closed forecasts, select **Re-configure** and edit the default value configuration.

  [![Screenshot of options to change the values used to initialize closed and open forecasts.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/reconfigure-default-values.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/reconfigure-default-values.png#lightbox)

## Set aggregation for forecast column totals

When the grand total or subtotal columns are enabled, configure how the forecast measure total is calculated:

- To calculate the total as the sum of open and closed forecast periods, set **Aggregate total** to **All Periods**.

  [![Screenshot of option to set aggregation method for forecast total and subtotal columns.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/set-aggregation.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/set-aggregation.png#lightbox)
- To calculate the total as the sum of closed forecast periods, set **Aggregate total** to **Closed Periods**.

  [![Screenshot of forecast aggregation set to closed periods.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/aggregation-closed-periods.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/aggregation-closed-periods.png#lightbox)
- To include only open forecasts in the total, set **Aggregate total** to **Open Periods**.

## Control forecast updates from actuals

Define how the forecast responds as actuals are loaded: replace forecast values with actuals or keep forecast values unchanged.

To replace forecasted values with actuals as they become available, set **Closed Period** to **Measure**.

[![Screenshot of setting closed period to measure.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/retain-forecast-prerequisite.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/retain-forecast-prerequisite.png#lightbox)

Then, choose an **Action for closed periods**:

- To replace forecasted values with actuals when the forecast for that period is closed, choose **Overwrite forecasts**.

  [![Screenshot of overwriting forecasts with actuals.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/overwrite-forecast-result.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/overwrite-forecast-result.png#lightbox)
- To preserve forecasted values, choose **Retain forecasts**.

  [![Screenshot of option to retain forecast values.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/retain-forecast.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/retain-forecast.png#lightbox)
- To leave empty forecast cells unchanged when the forecast is closed, select **Retain blank values**.

  [![Screenshot of retaining blank forecast values when actuals become available.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/retain-blank-forecasts-option.jpg)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/retain-blank-forecasts-option.jpg#lightbox)

  When the forecast is closed, blank values are replaced with actuals unless they're explicitly retained.

  [![Screenshot of replacing blank forecasts with actuals when the retain option isn't selected.](../media/planning-forecasting/planning-how-to-configure-forecast-settings/replace-blank-values-actuals.png)](../media/planning-forecasting/planning-how-to-configure-forecast-settings/replace-blank-values-actuals.png#lightbox)

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
