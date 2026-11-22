---
title: "Insert date columns in planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-date-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-date-columns) · Last updated on **2026-08-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert date columns in planning sheet

Summarize this article for me

Create and use a date column in the planning sheet to insert date values for each row. Define the date format, a default date, and acceptable date range as needed.

## Insert a date column

To insert a date column:

1. Go to **Planning** > **Insert Column** > **Date.**

   ![Screenshot of inserting a date column.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/insert-column-date.png)
2. Enter a title and configure the required properties in the side panel.

   ![Screenshot of side panel with configuration options for a date column.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/side-panel-date.png)
3. Select **Create** to add an empty date column to the report with the default configuration.
4. To enter a date, double-click a cell and select a value from the date picker or calendar.

   [![Screenshot of entering a date in date column.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/entering-date.png)](../media/planning-how-to-insert-columns/how-to-insert-date-columns/entering-date.png#lightbox)

Note

You can [modify a date input column](how-to-insert-data-input-columns#modify-column-properties) to update its properties.

## Configure date column properties

You can define properties such as **Insert As**, **Input type**, **Allow entry on Totals/Subtotals**, **On Change Formula**, **Allow Input**, and **Description**, similar to other data input columns. For more information, see [configure data input column properties](how-to-insert-data-input-columns#configure-data-input-column-properties).

Additional configurations for date columns include:

- **Format**: Select the required date format from the **Format** dropdown.

  ![Screenshot of selecting a date format.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/format-date.png)
- **Minimum and maximum date**: Set the allowed date range by defining minimum and/or maximum values. Users can't enter dates outside this range.

  [![Screenshot of defining minimum and maximum date.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/min-max-date.png)](../media/planning-how-to-insert-columns/how-to-insert-date-columns/min-max-date.png#lightbox)
- **Default value**: Pre-fill the column with a default date to avoid manual entry. Set the default value by using:

  - **Static**: Use the date picker to define a common date for all rows.

    [![Screenshot of defining a static default value.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/default-value-static.png)](../media/planning-how-to-insert-columns/how-to-insert-date-columns/default-value-static.png#lightbox)
  - **Measure/Column**: Select a measure or column (native, formula, or date input) to source the default value.

    [![Screenshot of defining a default value from an existing column.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/default-value-column.png)](../media/planning-how-to-insert-columns/how-to-insert-date-columns/default-value-column.png#lightbox)

After configuring the properties, select **Create** to insert the column. You can overwrite the default value by double-clicking a cell and selecting a new date from the date picker.

![Screenshot of overwriting a date value.](../media/planning-how-to-insert-columns/how-to-insert-date-columns/overwriting-date.png)

Note

The default value option is available for both visual measures and visual columns. The system automatically handles invalid date formats as blank values to ensure clean export and writeback.

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
