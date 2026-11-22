---
title: "Generate statistical forecasts by using the Predict feature"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-create-statistical-forecasts](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-forecasting/planning-how-to-create-statistical-forecasts) · Last updated on **2026-08-11**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Generate statistical forecasts by using the Predict feature

Summarize this article for me

Statistical forecasting uses historical data to identify trends, seasonality, and other statistical patterns. It generates forecasts automatically without requiring manual calculations. The Predict feature enables forward-looking analysis by estimating future values from historical observations.

The Predict feature supports confidence interval, seasonality, growth factor, algorithm, and hierarchy evaluation method configuration (Top-Down or Bottom-Up), allowing forecasts across planning hierarchies. You can review forecast results in graphical and tabular formats.

## How forecasting works

The Predict feature uses the selected measure cell as a time series. It analyzes historical data within the selected historical date range and generates estimated values for the selected forecast period.

During forecasting, the system considers the following characteristics of the time series:

- **Level** â The underlying baseline value of the series.
- **Trend** â A sustained upward or downward movement over time.
- **Seasonality** â A repeating pattern that occurs at regular calendar or operational intervals.
- **Past-value relationships** â The extent to which previous observations help explain future values.
- **Past-error relationships** â The extent to which previous forecast errors improve future predictions.

## Prerequisites

Before running a statistical forecast, ensure the following conditions:

- A forecast measure exists with either blank initial values or prepopulated values.
- The planning sheet contains sufficient historical data.
  - For monthly data, provide at least **24 months** of historical data.
  - For quarterly data, provide at least **24 quarters** of historical data.
  - Some forecasting algorithms require **36** or **48** historical periods to produce more reliable forecast results.

## Configure statistical forecasts

1. Create a planning model by assigning **row** fields, **column** fields, and measures under the **value** field.

   Consider the model in the following image.

   [![Screenshot of a planning model configured with row fields, column fields, and measures.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/configuring-model.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/configuring-model.png#lightbox)
2. Create a forecast measure (for example, *2026 Forecast*) by selecting the required forecast period through December 2026.

   [![Screenshot of creating a forecast measure for a future planning period.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/forecast-measure.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/forecast-measure.png#lightbox)
3. Select the *All Row Total* cell of the *2026 Forecast* measure.
4. On the **Model** tab, select **Predict**.

   [![Screenshot of the Predict option in the Model tab.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/predict-option.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/predict-option.png#lightbox)

   **Row Selected** represents the hierarchy member for which the forecast is generated.

   **Measure Selected** is used as the historical input series, and forecast values are written into this measure.

   These fields are automatically populated based on the selected planning sheet cell. Selecting another visible cell updates the selected row and measure in the Predict panel.

   Lock the selection to prevent selecting another cell from changing the selected row or measure.

   [![Screenshot showing locked row and measure selection in the Predict panel.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/locking-row-measure-selection.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/locking-row-measure-selection.png#lightbox)
5. Specify the date ranges used for forecasting.

   **Historic Data Range** specifies the historical periods used to build the statistical model. By default, the system selects all closed periods.

   **Forecast Date Range** specifies the future periods for which forecasts are generated. By default, the system selects all open periods.

   You can modify both ranges to suit your business requirements.

   Note

   The forecast period can extend beyond the open period. This extension is useful when only a short open planning horizon exists (for example, Q1 only), but you need forecasts for a longer period to support planning and forecast validation.

   [![Screenshot showing historical and forecast date range selection.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/assigning-period-range.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/assigning-period-range.png#lightbox)
6. Select an existing forecast profile or create a new one by selecting **More options (â¯)**.

   A **profile** is a saved collection of forecast settings that helps standardize forecast execution.

   A profile includes:

   - Confidence (%)
   - Growth Factor (%)
   - Hierarchy evaluation
   - Negative-value handling
   - Algorithm choices
   - Seasonality choices

   You can create, duplicate, delete, or reset profiles. Use descriptive profile names so forecast configurations can be easily reproduced.

   [![Screenshot showing forecast profile configuration.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/setting-profile.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/setting-profile.png#lightbox)
7. Set **Confidence (%)**.

   **Confidence (%)** specifies the confidence level used when generating the forecast confidence interval. It represents the probability that the actual value falls within the predicted range.

   Typical confidence level choices include:

   - **80%** â Produces a narrower confidence interval suitable for central planning.
   - **90%** â A balanced confidence level for most business forecasts.
   - **95%** â Produces a wider, more conservative confidence interval.
8. Set **Growth Factor (%)**.

   **Growth Factor (%)** applies a business adjustment to the statistical forecast. It applies a business adjustment to forecast values by increasing or decreasing the generated forecast by the specified percentage.

   Examples:

   - **5%** increases forecast values to reflect an expected business uplift.
   - **-5%** decreases forecast values.
   - **0%** preserves the statistical forecast without adjustment.
9. Choose an **Evaluation** method.

   **Bottom-Up** generates forecasts at detailed hierarchy levels and aggregates them into higher-level totals.

   **Top-Down** generates forecasts at higher hierarchy levels and distributes them into lower levels.
10. Set **Round all negative values to zero**.

    - Select **Yes** if the forecasted measure can't contain negative values.
    - Select **No** if negative values are valid for the business scenario.

    [![Screenshot showing forecast configuration options, including evaluation method and negative value handling.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/configuring-forecast-options.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/configuring-forecast-options.png#lightbox)
11. Choose a forecasting **algorithm** that best matches the characteristics of your historical data.

    The following forecasting algorithms are available:

    - **Trend Decomposition with MSTL** â Breaks down complex data with multiple repeating patterns into simple parts so they're easier to handle.
    - **Exponential Smoothing** â Focuses on smooth trends and clear, single-cycle seasons, giving more weight to recent data.
    - **ARIMA** â Looks at recent spikes, drops, and lags to project where the trend is heading next.

    For more information about forecasting algorithms, statistical models, and model orders, see [Forecasting algorithms](../planning-concept-predict).
12. Configure **Seasonality**.

    Seasonality is a repeating pattern in data that occurs at regular intervals, such as yearly, quarterly, or both.

    Select one of the following options:

    - **Year** â Use when the pattern repeats annually.
    - **Quarter** â Use when the pattern repeats quarterly.
    - **Both** â Use when the pattern repeats annually and quarterly.

    Note

    The Seasonality list doesn't display the lowest level of the time dimension.
13. Select **Run Forecast**.

    [![Screenshot showing forecasting algorithm selection.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/setting-algorithm.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/setting-algorithm.png#lightbox)
14. Review the forecast preview.

    The preview is available in graphical and tabular formats.

    - Historical values appear in **grey**.
    - Forecast values appear in **green**.
    - The shaded green band represents the selected confidence interval.

    [![Screenshot showing the graphical forecast preview with historical values, forecast values, and confidence interval.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/preview-graphical-format.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/preview-graphical-format.png#lightbox)

    [![Screenshot showing the tabular forecast preview.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/preview-tabular-format.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/preview-tabular-format.png#lightbox)
15. If necessary, select **Reconfigure** or **Re-run Forecast** to adjust the forecasting parameters.

    When you're satisfied with the results, select **Save Forecast**.

    [![Screenshot showing the Save Forecast option.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/save-forecast.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/save-forecast.png#lightbox)
16. Apply the forecast values to a planning scenario or export the results to a CSV file.

    [![Screenshot showing options to apply the forecast or export it to a CSV file.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/other-save-options.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/other-save-options.png#lightbox)
17. Generate forecasts for the selected measure and row category. When you use the Bottom-Up approach, the system automatically aggregates values to the parent levels.

    [![Screenshot showing forecast values in the planning sheet after the forecast is generated.](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/forecasted-value.png)](../media/planning-forecasting/planning-how-to-generate-statistical-forecasts-using-predict-feature/forecasted-value.png#lightbox)

## Choose a forecasting algorithm

Use the following table to help determine which forecasting algorithm best matches your data or when you have a question like **"Which algorithm should I choose?"**.

| Data pattern | Recommended algorithm |
| --- | --- |
| Stable data with no trend or seasonality | Simple Exponential Smoothing |
| Trend only | Holt's Linear Trend |
| Trend gradually weakens | Holt's Damped Trend |
| Trend with constant seasonal variation | Holt-Winters Additive |
| Trend with seasonal variation proportional to the level | Holt-Winters Multiplicative |
| Multiple seasonal patterns | MSTL |
| Non-seasonal data with autocorrelation | ARIMA |
| Seasonal data | SARIMA |
| Unsure which ETS model to use | Auto ETS |
| Unsure which ARIMA model to use | Auto ARIMA |

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
