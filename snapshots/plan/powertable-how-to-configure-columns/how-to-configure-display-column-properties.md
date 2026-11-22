---
title: "Configure display properties for a column"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-configure-columns/how-to-configure-display-column-properties](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-configure-columns/how-to-configure-display-column-properties) · Last updated on **2026-08-02**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure display properties for a column

Summarize this article for me

Use the **Display** tab in the panel to control how column headers and values appear in the table.

To configure display properties:

1. Select **Setup** > **Columns**.

   ![Screenshot of the Columns option under Setup tab.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/setup-columns.png)
2. The column configuration window opens. Select the pencil icon next to the column name or double-click the column name.

   [![Screenshot of the edit icon beside the column name used to configure display properties.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/edit-icon-column-name.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/edit-icon-column-name.png#lightbox)
3. Select the **Display** tab in the side panel.

   [![Screenshot of the Display tab in the side panel.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/display.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/display.png#lightbox)

The following display properties are available:

## Format

Use the **Format** property to define how date and date-time values appear in a column.

Choose from various date-time formats, such as `MM/DD/YYYY`, `DD/MM/YYYY`, `DD MMM, YYYY hh:mm:ss`, and more. Select **Default Locale** to use your locale's date and time *format*.

[![Screenshot of the date and time formatting options.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/format.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/format.png#lightbox)

## Display name

Use the **Display Name** property to specify a user-friendly column header that differs from the actual field name in the database.

For example, the database field *ProductSubcategoryKey* can be displayed as *Product Subcategory* in the table.

[![Screenshot of the Display Name text box.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/display-name.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/display-name.png#lightbox)

Tip

PowerTable column names support displaying only English labels. Use the **Display Name** property to specify non-English column names, such as Japanese, so they display non-English labels.

## Description

Use the **Description** property to provide extra information about a column.

When you configure a description, an information icon appears next to the column header. Users can hover over the icon to view the description.

[![Screenshot of the Description text box.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/description.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/description.png#lightbox)

## Thousand separator

Use the **Thousand Separator** property to improve the readability of large numeric values.

You can set a comma (,), period (.), or space ( ) as the separator for each group of thousands.

[![Screenshot of the Thousand Separator text box.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/thousand-separator.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/thousand-separator.png#lightbox)

## Prefix

Use the **Prefix** property to add up to two characters before numeric or decimal values.

Use this property to add currency symbols.

[![Screenshot of the Prefix text box.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/prefix.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/prefix.png#lightbox)

## Suffix

Use the **Suffix** property to add up to two characters after numeric or decimal values.

Use this property to add measurement units such as kilograms (kg), centimeters (cm), or percentages (%).

## Large number abbreviation

Use the **Large Number Abbreviation** property to display large numeric values in a shortened and more readable format.

The following options are available:

- **None** - Displays the full value without abbreviation.
- **Thousand (K)** - Displays values in thousands. For example, 15,000 is displayed as 15K.
- **Million (M)** - Displays values in millions. For example, 2,500,000 is displayed as 2.5M.
- **Billion (B)** - Displays values in billions. For example, 1,500,000,000 is displayed as 1.5B.
- **Trillion (T)** - Displays values in trillions. For example, 2,000,000,000,000 is displayed as 2T.

[![Screenshot of the options under Large Number Abbreviation dropdown.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/large-number-abbreviation.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/large-number-abbreviation.png#lightbox)

Use this option when displaying large numeric values in reports and dashboards where space is limited.

## Negative value

Use the **Negative Value** property to control how negative numbers are displayed.

The following formats are available:

- **-0** - Displays the negative sign before the value. For example, -500.
- **0-** - Displays the negative sign after the value. For example, 500-.
- **(0)** - Displays negative values within parentheses. For example, (500).

[![Screenshot of the options under Negative Value dropdown.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/negative-value.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/negative-value.png#lightbox)

This option helps align number formatting with organizational or accounting standards.

## Show value as percentage

Select the **Show value as percentage** checkbox to display numeric values as percentages.

When you enable this option, the value automatically formats with a percentage symbol (%). For example, a value of 25 displays as 25%.

[![Screenshot of the options under Show value as percentage dropdown.](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/show-value-as-percentage.png)](../media/powertable-how-to-configure-columns/how-to-configure-display-column-properties/show-value-as-percentage.png#lightbox)

This option is useful for columns that represent rates, ratios, percentages, or other proportional values.

## FAQ

### If I change the Display Name, does the column get renamed in the database?

No. **Display Name** is a presentation label on the **Display** tab. It changes only how the column name appears in the PowerTable sheet and doesn't rename the physical column in the database.

### What is the Description field on the Display tab used for?

The text in the **Description** field appears when a user hovers over the column header.

Use this field to provide:

- Business context.
- A definition of the column.
- Additional information that helps users understand the column.

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
