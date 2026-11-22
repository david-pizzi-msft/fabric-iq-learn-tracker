---
title: "Use a min-max rule"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-allocation-rules-controls/how-to-use-min-max-rule](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-allocation-rules-controls/how-to-use-min-max-rule) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Use a min-max rule

Summarize this article for me

Use a min-max rule to control the values that users can enter in a planning sheet. Set a fixed minimum and maximum value, or use measures to define dynamic limits. You can also restrict the rule to specific measures or visual columns, rows, and periods.

## Create a min-max rule

1. Open the planning sheet where you want to restrict data input.
2. On the ribbon, open the rule menu and select **Min-Max Rule**.

   [![Screenshot of the rule menu with the Min-Max Rule option highlighted.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/min-max-rule-menu.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/min-max-rule-menu.png#lightbox)
3. In **Rule Name**, enter a descriptive name for the rule.
4. In **Apply to Measures**, choose which measures or visual columns the rule applies to. The available options are:

   - **All Measures**: Apply the rule to all visual measures, including measures added later to the planning sheet. The rule covers data input and forecast measures, whether visible or hidden, based on the selected rows and columns.
   - **Selected Measures**: Apply the rule only to the measures selected in **Choose Measures**.
   - **All Visual Columns**: Apply the rule to all visual columns, including columns added later to the planning sheet.
   - **Selected Visual Columns**: Apply the rule only to the columns selected in **Choose Columns**.

   If you select **Selected Measures**, use **Choose Measures** to select the measures. If you select **Selected Visual Columns**, use **Choose Columns** to select the columns.

   [![Screenshot of the Apply to Measures menu showing All Measures, Selected Measures, All Visual Columns, and Selected Visual Columns.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/apply-rule-to-measures-options.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/apply-rule-to-measures-options.png#lightbox)
5. In **Rule Type**, select **Min-Max Rule**.
6. Configure the minimum and maximum values. For each boundary, choose **Static** to enter a fixed value or **Measure** to use a measure as the boundary.

   - **Static**: Enter a numeric value in the corresponding value field.
   - **Measure**: Select the measure that supplies the minimum or maximum value. The allowed input range is evaluated using the selected measures.

   You can select **Set Exclusive** for either boundary to exclude that boundary value from the allowed range. Leave it cleared to include the boundary value.

## Limit the rule to rows and columns

Use **Rows Selection** and **Columns Selection** to define where the rule applies.

### Select rows for the min-max rule

In **Rows Selection**, choose which rows the rule applies to.

- **All Rows**: Apply the rule to all rows for the selected measures and columns.
- **Custom**: Apply the rule only to selected rows. Use the selection filter to choose the required rows.

[![Screenshot of the Rows Selection menu showing All Rows and Custom options.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/row-selection-options.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/row-selection-options.png#lightbox)

When you select **Custom**, select the filter next to **Custom Rows** and choose the required rows. You can use the selection filter or a text filter with advanced grouping to narrow the selection.

[![Screenshot of the custom row selector with a row selection being configured.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/select-custom-rows.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/select-custom-rows.png#lightbox)

### Select columns and periods for the rule

In **Columns Selection**, choose the columns or periods to which the rule applies. The available options are:

- **Open Period**: Apply the rule to all columns in the open period.
- **Period Range**: Apply the rule to a selected range of periods.
- **Custom**: Select specific columns by using a selection filter or an advanced filter.

[![Screenshot of the Columns Selection menu showing Open Period, Period Range, and Custom options.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/column-selection-options.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/column-selection-options.png#lightbox)

When you select **Custom**, select the filter next to **Custom Columns** and choose the required columns.

[![Screenshot of the custom column selector with column selection being configured.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/select-custom-columns.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/select-custom-columns.png#lightbox)

## Create a rule with static values

Use static values to define fixed minimum and maximum limits for data input.

1. In **Minimum Value**, select **Static** and enter the lower limit.
2. In **Maximum Value**, select **Static** and enter the upper limit.
3. Configure **Rows Selection** and **Columns Selection** to define where the rule applies.
4. Select **Create** to save the rule and apply it to the configured scope.

For example, configure a minimum value of 0 and a maximum value of 4,000,000. With **Set Exclusive** cleared for both boundaries, users can enter values from 0 through 4,000,000, inclusive, in the rows and columns covered by the rule.

In the example, entering 2 million for Juices in Q1 2026 is accepted because it is within the configured range.

[![Screenshot of a user entering a 2 million value for Juices in Q1 2026 under a static min-max rule.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/enter-static-value-within-range.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/enter-static-value-within-range.png#lightbox)

[![Screenshot of the planning sheet showing that the 2 million input is accepted by the static min-max rule.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/static-rule-accepts-valid-value.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/static-rule-accepts-valid-value.png#lightbox)

An entry of 5 million is rejected because it exceeds the maximum value of 4,000,000.

[![Screenshot of the validation error displayed when a user enters 5 million, which exceeds the static maximum value.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/static-rule-rejects-value-outside-range.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/static-rule-rejects-value-outside-range.png#lightbox)

## Configure custom rows and columns for the measure-based example

The following example uses **Forecast** as the minimum measure and **Sales Target** as the maximum measure. It also limits the rule to a custom row and custom columns.

[![Screenshot of the Add Rule pane showing the measure-based limits and the custom row selector.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/configure-custom-rows-for-measure-based-rule.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/configure-custom-rows-for-measure-based-rule.png#lightbox)

[![Screenshot of the Add Rule pane showing the measure-based limits and the custom column selector.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/configure-custom-columns-for-measure-based-rule.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/configure-custom-columns-for-measure-based-rule.png#lightbox)

## Create a rule with measure-based values

Use measure-based values when the allowed input range must change according to values in other measures.

1. In **Minimum Value**, select **Measure**, and then select the measure to use as the lower limit.
2. In **Maximum Value**, select **Measure**, and then select the measure to use as the upper limit.
3. Configure **Rows Selection** and **Columns Selection** to define where the rule applies.
4. Select **Create** to save the rule and apply it to the configured scope.

For example, configure **Forecast** as the minimum value and **Sales Target** as the maximum value. For each applicable row and period, the input must be greater than or equal to the Forecast value and less than or equal to the Sales Target value when **Set Exclusive** is cleared.

In the example, enter 3 million for Juices in Q1 2026. The rule rejects the value because it is above the applicable Sales Target maximum.

[![Screenshot of a user entering 3 million for Juices in Q1 2026 under a measure-based min-max rule.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/enter-value-for-measure-based-rule.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/enter-value-for-measure-based-rule.png#lightbox)

[![Screenshot of the validation error displayed when 3 million exceeds the Sales Target measure for Juices in Q1 2026.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/dynamic-rule-rejects-value-above-maximum.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/dynamic-rule-rejects-value-above-maximum.png#lightbox)

Enter 2.7 million for the same row and period. The value is accepted because it falls within the range defined by Forecast and Sales Target.

[![Screenshot of a user entering 2.7 million for Juices in Q1 2026 under a measure-based min-max rule.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/enter-value-within-measure-based-range.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/enter-value-within-measure-based-range.png#lightbox)

[![Screenshot of the planning sheet showing that the 2.7 million input is accepted by the measure-based min-max rule.](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/dynamic-rule-accepts-valid-value.png)](../media/planning-allocation-rules-controls/how-to-use-min-max-rule/dynamic-rule-accepts-valid-value.png#lightbox)

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
