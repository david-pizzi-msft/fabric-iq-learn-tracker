---
title: "Pivot data in a planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-pivot-table](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-pivot-table) · Last updated on **2026-06-17**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Pivot data in a planning sheet

Summarize this article for me

Use *Pivot Table* to reorganize dimensions and measures and configure aggregations for totals and subtotals.

[![Screenshot of the Pivot Table interface.](../media/infobridge-transformations/infobridge-how-to-pivot-table/pivot-table-interface.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/pivot-table-interface.png#lightbox)

## Convert row dimensions and column dimensions

Move dimensions between the **Rows** and **Columns** buckets to change how data is displayed.

For example, convert the **Region** column dimension into a row dimension.

[![Screenshot of the Region dimension in the Columns bucket.](../media/infobridge-transformations/infobridge-how-to-pivot-table/region-column-dimension.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/region-column-dimension.png#lightbox)

1. Open **Pivot Table**.
2. Drag **Region** from **Columns** to **Rows**.

The dimension is displayed as a row dimension instead of a column dimension.

[![Screenshot of the Region dimension moved from Columns to Rows.](../media/infobridge-transformations/infobridge-how-to-pivot-table/column-to-row-conversion.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/column-to-row-conversion.png#lightbox)

## Configure measure aggregations

Configure aggregations for numeric measures when totals and subtotals are enabled.

Supported aggregation types include:

- Sum
- Average
- Minimum
- Maximum

[![Screenshot of aggregation type options.](../media/infobridge-transformations/infobridge-how-to-pivot-table/aggregation-type.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/aggregation-type.png#lightbox)

1. Enable totals or subtotals.
2. Select the measure to aggregate.
3. Select an aggregation type.

For example, apply **Sum** to the **Profit** measure and **Average** to the **Sales** measure.

[![Screenshot of measures with different aggregation types applied.](../media/infobridge-transformations/infobridge-how-to-pivot-table/aggregated-measures.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/aggregated-measures.png#lightbox)

## Convert dimensions into measures

Convert a text dimension into a measure by moving it to the **Values** bucket.

1. Open **Pivot Table**.
2. Drag the dimension to **Values**.

[![Screenshot of converting a text dimension into a measure by moving it to the values bucket.](../media/infobridge-transformations/infobridge-how-to-pivot-table/convert-dimensions-into-measures.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/convert-dimensions-into-measures.png#lightbox)

The dimension is converted into a measure and can be aggregated with other values.

## Concatenate text values

Use **Concat** to combine text values from multiple rows into a single value by using a delimiter.

For example, concatenate all accounts within a segment while retaining the underlying information.

[![Screenshot of concatenating text values by using a delimiter.](../media/infobridge-transformations/infobridge-how-to-pivot-table/concatenating-text-measures.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/concatenating-text-measures.png#lightbox)

1. Drag the text field to the **Values** bucket.
2. Select **Concat** as the aggregation type.
3. Specify a delimiter.

The resulting value provides a summarized view of the underlying records and can be used in downstream visuals.

[![Screenshot of concatenated text values displayed in the pivot table.](../media/infobridge-transformations/infobridge-how-to-pivot-table/aggregated-text-measure.png)](../media/infobridge-transformations/infobridge-how-to-pivot-table/aggregated-text-measure.png#lightbox)

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
