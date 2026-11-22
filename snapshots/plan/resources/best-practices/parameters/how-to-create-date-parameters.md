---
title: "Create date parameters"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-date-parameters](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-date-parameters) · Last updated on **2026-11-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create date parameters

Summarize this article for me

Use date parameters in dashboards and planning applications that dynamically pass specific dates or date ranges into visual charts, calculations, and financial models.

Unlike standard hard-coded filters, date parameters act as flexible inputs that can simultaneously drive conditional formatting and dynamic titles.

## Apply conditional formatting to date-based charts

By combining a date parameter with conditional formatting, you can create interactive, visually intuitive reports. Instead of filtering data out of view, this approach retains the full context of your dataset while dynamically highlighting specific date ranges based on user selection.

By evaluating report dates against a flexible date variable, conditional rules automatically apply visual emphasis to the selected timeframe. This approach enables users to track trends, identify specific performance windows, and focus on key timeframes without losing sight of surrounding historical or future data.

1. Create a new parameter and set the type to **Date**.
2. Set the **Date Mode** to **Date Range** to pass a specific timeframe to the chart visual.
3. Set the interface to **Date Picker** to use a calendar control to select the date range. You can also use a slider.

   [![Screenshot of configuring a date parameter with date mode set to date range and interface set to date picker.](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/configure-date-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/configure-date-parameter.png#lightbox)
4. In your intelligence sheet, select the chart visual and select **Conditional Formatting** > **New Rule**.
5. In the conditional formatting side pane, set **Impacts on** to **Chart** to highlight chart sections based on the parameter value.
6. Configure the condition to set the date range based on the parameter value.

   [![Screenshot of configuring a conditional formatting rule to set the order date to the date selector parameter value.](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/configure-conditional-formatting.png)](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/configure-conditional-formatting.png#lightbox)
7. Updating the date selection in the parameter automatically emphasizes the chosen data range in the chart.

   [![Screenshot of a chart highlighting the date range selected in the date parameter through conditional formatting.](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/chart-selection-date-range-highlighted.png)](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/chart-selection-date-range-highlighted.png#lightbox)

## Insert custom dates in report headers

If you pass custom date parameters directly into a report's title, dynamic titles display the time period selected in the parameter controlsâfor example, "Selected period: Jan 01, 2026 â Mar 31, 2026". Displaying a parameter in a header doesn't filter the report or restrict the exported data to that period. Apply matching date filters separately if the export should contain only the selected period, and configure the PDF export settings to include the header.

1. Create a date parameter. Set the **Date Mode** to **Date Range** and interface to slider.

   [![Screenshot of a date parameter configured with Date Mode set to Date Range and the interface set to slider.](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/create-date-range-parameter-configuration.png)](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/create-date-range-parameter-configuration.png#lightbox)
2. In your planning sheet, double-click the header to enable the **Header & Footer** ribbon.
3. Select **Parameters** in the **Header & Footer** ribbon, and select the configured date parameter.

   [![Screenshot of inserting the date selector parameter in the header.](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/insert-date-parameter-header.png)](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/insert-date-parameter-header.png#lightbox)
4. The header displays the dates selected by using the slider control.

   [![Screenshot of the selected date range reflected in the header.](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/display-selected-date-header.png)](../../../media/resources/best-practices/parameters/how-to-create-date-parameters/display-selected-date-header.png#lightbox)

## Related content

Apply conditional formatting to planning sheets: [Conditional formatting in planning sheets](/en-us/fabric/iq/plan/planning-conditional-formatting/concept-conditional-formatting)

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
