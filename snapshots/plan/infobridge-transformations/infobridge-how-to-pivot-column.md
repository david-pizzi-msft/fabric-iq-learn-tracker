---
title: "Pivot and unpivot columns in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-pivot-column](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-pivot-column) · Last updated on **2026-06-23**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Pivot and unpivot columns in Infobridge

Summarize this article for me

Use the **Pivot Column** and **Unpivot Column** transformations in Infobridge to reorganize data into formats that are easier to analyze and report on.

Pivoting converts values from a selected column into multiple columns, while unpivoting converts multiple columns back into rows.

## Pivot column

The **Pivot Column** transformation converts values from a selected dimension into separate columns. This transformation lets you compare measures across categories more effectively.

### Example: Pivot segment sales data

The following example shows sales data in a tabular format, where each segment appears as a row.

| Country | Segment | Sales |
| --- | --- | --- |
| Canada | Channel Partners | 491.16K |
| Canada | Enterprise | 3.97M |
| Canada | Government | 10.74M |
| Canada | Midmarket | 510.21K |
| Canada | Small Business | 9.18M |
| France | Channel Partners | 372.09K |
| France | Enterprise | 3.89M |
| France | Government | 12.13M |
| France | Midmarket | 593.80K |
| France | Small Business | 7.37M |

After you pivot the **Segment** column, each segment value appears as a separate column.

| Country | Enterprise | Government | Midmarket | Small Business | Channel Partners |
| --- | --- | --- | --- | --- | --- |
| Canada | 3.97M | 10.74M | 510.21K | 9.18M | 491.16K |
| France | 3.89M | 12.13M | 593.80K | 7.37M | 372.09K |
| Germany | 4.09M | 11.45M | 301.34K | 7.33M | 336.43K |
| Mexico | 3.32M | 9.79M | 511.14K | 7.10M | 234.38K |
| United States of America | 4.35M | 8.39M | 465.39K | 11.46M | 366.53K |

### Create a pivot column

The following procedure pivots the **Segment** column and aggregates values from the **Sum of Sales** measure.

[![Screenshot showing source data that contains Country, Segment, Sum of Sales, and Sum of COGS columns before applying a pivot transformation.](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-source-data.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-source-data.png#lightbox)

1. On the **Transform** tab, select **Pivot Column**.
2. In **Category**, select **Segment**.
3. In **Operations**, select the aggregation type.
4. In **Values**, select **Sum of Sales**.
5. Select **Apply**.

[![Screenshot showing the Pivot dialog configured with Segment as the category, Sum as the aggregation operation, and Sum of Sales as the value field.](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-configuration.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-configuration.png#lightbox)

After you apply the transformation, each segment value becomes a separate column.

[![Screenshot showing the results of a pivot transformation where Segment values become separate columns including Enterprise, Government, Midmarket, Small Business, and Channel Partners.](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-results.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-results.png#lightbox)

### Choose an aggregation type

The **Operations** field determines how to aggregate values when multiple records exist for the same combination of dimensions.

Available aggregation options include:

- Sum
- Average
- Minimum
- Maximum

[![Screenshot showing available aggregation options including Sum, Average, Minimum, and Maximum in the Pivot dialog.](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-aggregation-options.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/pivot-column-aggregation-options.png#lightbox)

## Unpivot column

The **Unpivot Column** transformation reverses a pivot operation by converting multiple columns into rows.

### Select columns to unpivot

For example, after pivoting the **Segment** column, each segment exists as an individual column. Unpivoting converts those segment columns back into row values.

[![Screenshot showing a pivoted table where each segment appears as a separate column before unpivoting.](../media/infobridge-transformations/infobridge-how-to-pivot-column/unpivot-column-source-data.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/unpivot-column-source-data.png#lightbox)

1. On the **Transform** tab, select **Unpivot Column**.
2. In **Category**, select the columns to convert into rows.
3. Select **Apply**.

The following example selects all segment columns.

[![Screenshot showing the Unpivot dialog with Enterprise, Government, Midmarket, Small Business, and Channel Partners columns selected.](../media/infobridge-transformations/infobridge-how-to-pivot-column/unpivot-column-configuration.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/unpivot-column-configuration.png#lightbox)

After you apply the transformation, the selected columns become two new columns:

- **Attribute**: Contains the original column names.
- **Value**: Contains the corresponding measure values.

For example, segment names such as Enterprise, Government, and Small Business move into the **Attribute** column, and their corresponding sales values appear in the **Value** column.

[![Screenshot showing Attribute and Value columns created after unpivoting the selected segment columns.](../media/infobridge-transformations/infobridge-how-to-pivot-column/unpivot-column-results.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/unpivot-column-results.png#lightbox)

## Rename unpivoted columns

After unpivoting, the generated **Attribute** and **Value** column names might not match your business terminology.

Use **Rename Column** to replace the default column names with names that better reflect your business data.

1. On the **Transform** tab, select **Rename Column**.
2. Select the column to rename.
3. Enter a new column name.
4. Select **Apply**.

The following example renames the **Value** column to **Sales**.

[![Screenshot showing the Rename Column dialog used to rename the Value column to Sales.](../media/infobridge-transformations/infobridge-how-to-pivot-column/rename-unpivoted-column.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/rename-unpivoted-column.png#lightbox)

After you apply the rename operation, the column displays the updated name.

[![Screenshot showing the renamed Sales column after applying the Rename Column transformation.](../media/infobridge-transformations/infobridge-how-to-pivot-column/renamed-sales-column.png)](../media/infobridge-transformations/infobridge-how-to-pivot-column/renamed-sales-column.png#lightbox)

You can use the renamed column in subsequent transformations, calculations, and reporting scenarios.

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
