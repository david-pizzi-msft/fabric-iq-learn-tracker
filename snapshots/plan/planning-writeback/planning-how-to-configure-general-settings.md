---
title: "Configure general settings for writeback"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-configure-general-settings](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-configure-general-settings) · Last updated on **2026-05-07**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure general settings for writeback

Summarize this article for me

In **Writeback Settings**, the **General** tab lets you configure writeback behavior for a planning sheet. These settings control how data is structured, filtered, and written to the destination.

## Writeback Type

Use **Writeback Type** to define the table structure.

[![Screenshot of writeback type.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type.jpg#lightbox)

There are four supported types:

- **Long** is the default writeback type. This setting stores each cell in a measure as a key-value pair. Only **Long** supports writing back comments and notes.

  [![Screenshot of writeback type long.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-long.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-long.jpg#lightbox)
- **Wide** stores measures as columns. As additional measures are added, the writeback table automatically adds corresponding columns. Totals and subtotals aren't written back in **Wide** format.

  [![Screenshot of writeback type wide.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-wide.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-wide.jpg#lightbox)
- **Long with changes** uses delta writeback. Only modified values are written back. The original values are stored in **PreviousValue**, and new values are stored in **Value**. The system also sets `IsLatest = 1` to identify the latest row. Delta writeback works for both numeric and text data type adjustments.

  [![Screenshot of writeback type long with changes.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-long-with-changes.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-long-with-changes.jpg#lightbox)
- **Wide with changes** uses delta writeback, but each measure is stored in a separate column. It maintains change history and uses `IsLatest` to identify the active record.

  [![Screenshot of writeback type wide with changes.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-wide-with-changes.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-type-wide-with-changes.jpg#lightbox)

After the first writeback, changing the **Writeback Type** displays a warning before existing tables are deselected in **Settings > Destinations**. The table can be reselected for writeback; however, the system checks for conflicts between the existing table type and the selected **Writeback type**. If a conflict is detected, the system prompts to drop and write back the table. When in doubt, create a new table and run writeback instead of dropping an existing table.

Changing row or column dimensions displays a warning before it drops and writes back the table.

## Filter Type

Use filters to control which data gets written back to the destination. Select from predefined options or apply custom filters.

[![Screenshot of writeback filter type.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-filter-type.png)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-filter-type.png#lightbox)

The options are:

- **None**: Writes back the entire report or scenario without applying any filter.
- **Data with Comments only**: Writes back the cells that contain comments. This option only works with the **Long** writeback type.
- **Calculated rows only**: Writes back only calculated rows, including any notes added to those rows.

## Date Key configuration

Select **Add Date Key** to add a date key column to the writeback table. For high-level planning scenarios such as revenue by year or month, planning appends a representative date to the date dimension. The system uses the first day of the year, month or quarter. For example, when the column dimensions are yearâmonth, planning writes *01-01-2025* for January 2025.

Note

**Add Date Key** only works when a date hierarchy is used in column dimensions.

[![Screenshot of writeback with additional coloumn configuration.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-additional-column-configuration.png)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-additional-column-configuration.png#lightbox)

In this example, the planning is done at month level. The record date column in the writeback table captures the date key for each month.

[![Screenshot of writeback with additional column in destination page.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-additional-column-in-destination-database.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-additional-column-in-destination-database.jpg#lightbox)

## Decimal Precision

Use **Decimal Precision** to define the number of digits after the decimal point. This is a one-time setting that applies to all destinations configured for a planning sheet. Set the precision when you configure the first writeback destination.

[![Screenshot of writeback with decimal precision.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-decimal-precision.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-decimal-precision.jpg#lightbox)

The configured precision is displayed in the **Decimal Precision** section under writeback settings.

[![Screenshot of writeback settings configured with decimal precision.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-configured-decimal-precision.jpg)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-configured-decimal-precision.jpg#lightbox)

## Text Length

Use **Text Length** to control the number of characters written back for text fields. The default limit is 512 characters. When you add the first destination, you can either keep the default limit or allow writeback up to the maximum supported by the backend. This is also a one-time setting for all database destinations on that report page.

[![Screenshot of writeback settings with text length' text length.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-text-field-length.png)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-text-field-length.png#lightbox)

The **Text Length** section in writeback settings shows the set text length as follows.

[![Screenshot of writeback settings configured with text length' text length.](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-configured-text-length.png)](../media/planning-writeback/planning-how-to-configure-general-settings/writeback-configured-text-length.png#lightbox)

After setting this option, writeback fails if the actual text length exceeds the configured limit.

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
