---
title: "Add columns in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-add-column](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-add-column) · Last updated on **2026-06-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Add columns in Infobridge

Summarize this article for me

Use transformation commands on the **Transform** ribbon to create calculated measures, dimensions, split columns, and conditional columns. These transformations enrich bridge data without modifying the source report and cascade to downstream reports.

## Open transformation commands

After creating a bridge, open the **Transform** tab to access data transformation options.

The Transform ribbon provides these commands:

- Add Measure
- Add Dimension
- Split Column
- Conditional Column

[![Screenshot showing the Add Measure, Add Dimension, Split Column, and Conditional Column commands in the Transform ribbon.](../media/infobridge-transformations/infobridge-how-to-add-column/add-column-interface.png)](../media/infobridge-transformations/infobridge-how-to-add-column/add-column-interface.png#lightbox)

## Add a measure

Use **Add Measure** to create calculated measures with expressions and built-in functions.

The following example creates a measure named **Gross Profit Margin (%)** that calculates profit as a percentage of sales.

1. On the **Transform** ribbon, select **Add Measure**.
2. Enter **Gross Profit Margin (%)** as the measure name.
3. Select **Formula**.
4. Enter the following expression:

   ```
   ("Sum of Profit" / "Sum of Sales") * 100
   ```
5. Select **Apply**.

[![Screenshot showing the Add Measure dialog with a Gross Profit Margin percentage calculation.](../media/infobridge-transformations/infobridge-how-to-add-column/add-measure-configuration.png)](../media/infobridge-transformations/infobridge-how-to-add-column/add-measure-configuration.png#lightbox)

The new measure appears in the bridge and is available for reporting and other transformations.

[![Screenshot showing the Gross Profit Margin percentage measure added to the bridge.](../media/infobridge-transformations/infobridge-how-to-add-column/add-measure-results.png)](../media/infobridge-transformations/infobridge-how-to-add-column/add-measure-results.png#lightbox)

## Add a dimension

Use **Add Dimension** to create new dimensions with expressions and conditional logic.

The following example creates a **Profit Rating** dimension that categorizes records based on profit values.

1. On the **Transform** ribbon, select **Add Dimension**.
2. Enter **Profit Rating** as the dimension name.
3. Create a CASE expression that evaluates profit ranges and returns a category.
4. Select **Apply**.

Example logic:

```
CASE
WHEN "Sum of Profit" < 1000 THEN 'Decommission'
WHEN "Sum of Profit" > 1000 AND "Sum of Profit" < 5000 THEN 'Break even'
WHEN "Sum of Profit" > 5000 AND "Sum of Profit" < 10000 THEN 'Average Sales'
WHEN "Sum of Profit" > 10000 THEN 'Target achieved'
ELSE 'N/A'
END
```

[![Screenshot showing the Add Dimension dialog used to create a Profit Rating dimension.](../media/infobridge-transformations/infobridge-how-to-add-column/add-dimension-configuration.png)](../media/infobridge-transformations/infobridge-how-to-add-column/add-dimension-configuration.png#lightbox)

The new dimension appears in the bridge.

[![Screenshot showing the Profit Rating dimension added to the bridge.](../media/infobridge-transformations/infobridge-how-to-add-column/add-dimension-results.png)](../media/infobridge-transformations/infobridge-how-to-add-column/add-dimension-results.png#lightbox)

## Split a column

Use **Split Column** to divide a dimension into multiple dimensions with a delimiter or character position.

The following example splits the comma-separated values in the **Market & Geography** column into separate columns.

1. On the **Transform** ribbon, select **Split Column**.
2. Select **Market & Geography** as the target column.
3. Select **By delimiter** as the split type.
4. Enter a comma (`,`) as the delimiter.
5. Select **Apply**.

[![Screenshot showing the Split Column dialog configured to split the Market and Geography column by a comma delimiter.](../media/infobridge-transformations/infobridge-how-to-add-column/split-column-configuration.png)](../media/infobridge-transformations/infobridge-how-to-add-column/split-column-configuration.png#lightbox)

The transformation creates separate columns for each value segment.

[![Screenshot showing Market and Geography values split into separate columns.](../media/infobridge-transformations/infobridge-how-to-add-column/split-column-results.png)](../media/infobridge-transformations/infobridge-how-to-add-column/split-column-results.png#lightbox)

## Add a conditional column

Use **Conditional Column** to create values based on business rules and conditions.

For example, a conditional column can categorize records into risk levels, regions, business segments, or other classifications.

### Example: Categorize debt-to-equity ratios

The following example categorizes debt-to-equity ratios into risk levels.

| Debt-to-Equity Ratio | Risk Level |
| --- | --- |
| 2.5 | Moderate Risk |
| 1.8 | Low Risk |
| 3.0 | High Risk |

### Example: Assign tax and shipping rates

The following example assigns tax rates and shipping rates based on region.

| Region | Tax Rate | Shipping Rate ($) |
| --- | --- | --- |
| North America | 20% | 50 |
| Europe | 15% | 70 |
| Asia | 12% | 60 |
| Africa | 8% | 40 |

### Create a conditional column

Use conditional logic to create a **Global Market** column based on country values.

| Country | Global Market |
| --- | --- |
| Canada | NAMER |
| France | EMEA |
| Germany | EMEA |
| Mexico | LATAM |
| United States of America | DOMESTIC |

1. On the **Transform** ribbon, select **Conditional Column**.
2. Enter **Global Market** as the column name.
3. Configure the required conditions and output values.
4. Optionally define a default value in the **Else** section.
5. Select **Apply**.

[![Screenshot showing a Global Market conditional column configured using country-based rules.](../media/infobridge-transformations/infobridge-how-to-add-column/conditional-column-configuration.png)](../media/infobridge-transformations/infobridge-how-to-add-column/conditional-column-configuration.png#lightbox)

The new conditional column appears in the bridge.

[![Screenshot showing the Global Market column added to the bridge after applying conditional logic.](../media/infobridge-transformations/infobridge-how-to-add-column/conditional-column-results.png)](../media/infobridge-transformations/infobridge-how-to-add-column/conditional-column-results.png#lightbox)

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
