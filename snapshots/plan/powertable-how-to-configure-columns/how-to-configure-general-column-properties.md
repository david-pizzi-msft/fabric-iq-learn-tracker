---
title: "Configure general properties for a column"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-configure-columns/how-to-configure-general-column-properties](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-configure-columns/how-to-configure-general-column-properties) · Last updated on **2026-09-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure general properties for a column

Summarize this article for me

Use the **General** tab to set the data type, validation rules, constraints, and default value for a column.

## Configure general properties

To configure the general properties:

1. Select **Setup** > **Columns**.

   ![Screenshot of the Column option under the Setup tab.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/setup-columns.png)
2. The column configuration window opens. Select the pencil icon next to the column name or double-click the column name.

   [![Screenshot of the edit icon beside the column name for configuring column properties.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/edit-icon-column-name.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/edit-icon-column-name.png#lightbox)
3. Select the **General** tab in the side panel.

   [![Screenshot of the General tab in the side panel.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/general.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/general.png#lightbox)

You can configure the following properties:

- [Input type](#input-type)
- [Constraints](#constraints)
- [Default value](#default-value)

## Input type

Use the **Input Type** property to specify how to enter, store, and display data in a column.

PowerTable sheet supports a wide range of input types. The available input types depend on the column's underlying SQL data type.

For example:

- Numeric data types such as `INT`, `BIGINT`, `FLOAT`, and `DECIMAL` support input types such as **Number**, **Single Select**, **Decimal**, **Currency**, **Percent**, **Percent Complete**, and **Rating**.

  [![Screenshot of the input types for numeric data types.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/input-type-number.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/input-type-number.png#lightbox)
- Date and time data types support input types such as **Date Time** and **Single Select**.

  [![Screenshot of the input types for date and time data types.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/input-type-date-time.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/input-type-date-time.png#lightbox)
- Text-based data types such as `VARCHAR` and `NVARCHAR` support input types such as **Text**, **Email**, **URL**, **Phone Number**, **Person** (name or email), **Image** (URL-based), **Single Select**, and **Check Box**.
- If your data contains Japanese and other non-English text, define the column's input type as `NVARCHAR`, so non-English characters in the data are supported and rendered correctly in PowerTable.

  [![Screenshot of the input types for text data types.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/input-type-text.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/input-type-text.png#lightbox)
- Boolean data types support input types such as **Check Box**.

Depending on the input type you choose, you can set more properties. For example, you can set minimum and maximum values for numeric input types and a list of selectable values for single select columns.

For a complete list of supported column types and their input types, see [Supported column input types](../powertable-reference-supported-column-input-types).

## Constraints

Use the **Constraints** section to restrict input values within a range and configure field validation.

### Minimum and maximum values

Use **Minimum** and **Maximum** to set the range of allowed values for a column. The system doesn't accept values outside the configured range.

These constraints apply to the input types of **Number**, **Currency**, and **Date Time**.

[![Screenshot of the Minimum and Maximum constraints fields where you can set limits.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/min-max.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/min-max.png#lightbox)

Existing table values stay the same. When you enter new values outside the configured range, PowerTable sheet shows a message that indicates the permitted limits.

[![Screenshot of the error message.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/min-max-error.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/min-max-error.png#lightbox)

Note

You can set a minimum value, a maximum value, or both.

For **Date** and **Date Time** columns, you can define a valid date range or a date-time range. The system doesn't accept values outside the configured range.

[![Screenshot of the Minimum and Maximum constraints for the Date Time input type.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/min-max-date.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/min-max-date.png#lightbox)

### Field validation

Use **Field Validation** to control the type of values that a **text** column accepts.

The following validation options are available:

- **Any value**
- **Numeric**
- **Alphanumeric**
- **Non Numeric**
- **Regex**

When you select **Regex**, specify a regular expression pattern to validate user input. PowerTable rejects values that don't match the configured validation rule or the regex pattern.

[![Screenshot of the Field Validation options for text input type.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/field-validation.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/field-validation.png#lightbox)

### Other number properties

For decimal input type, you can configure the default number of decimal places to display.

Select **Allow Negative Numbers** to allow negative entries in the column.

[![Screenshot of the allowed Decimal Points configuration.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/decimal-points.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/decimal-points.png#lightbox)

## Default value

Use **Default Value** to automatically populate a column when you create new rows. This setting helps ensure that new records already contain a valid initial value and reduces manual data entry. Existing column values remain unchanged.

Set default values by using a **manual** static value or a **formula**.

### Manual value

To configure a static default value:

1. Select **Manual**.
2. Enter the required value.

The following example uses **NA** as the default value for the **Product Description** column.

[![Screenshot of entering manual default value.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/default-manual.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/default-manual.png#lightbox)

When you insert a new row, the default value automatically populates the cell, and you can modify it later as needed.

[![Screenshot of the table with automatically populated default value.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/default-value-populated.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/default-value-populated.png#lightbox)

### Reset to default on update

Turn on **Reset to default on update** to automatically reset the column to its configured default value whenever you update the record.

[![Screenshot of Reset to Default on Update checkbox.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/reset-default-on-update.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/reset-default-on-update.png#lightbox)

When you enable this option:

- Existing values stay unchanged until you update the record.
- The value resets to the configured default when you modify other fields in the same record.

In this example, changing the product name automatically resets the product description to the default value NA.

[![Screenshot of the column value resetting to its default value in the table when the record is updated.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/resets-default-value.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/resets-default-value.png#lightbox)

Other default value options are available for specific input types:

- **Person**: Use a user's name or email address as the default value.
- **Single Select**: Select a default value from the configured list of options.

  [![Screenshot of the default value options for the Single Select input type.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/single-select-default.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/single-select-default.png#lightbox)
- **Check Box**: Configure default values such as True/False, 1/0, Yes/No, or custom text by selecting **Checked** or **Unchecked**.

  [![Screenshot of the default value options for the Check Box input type.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/checkbox-default.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/checkbox-default.png#lightbox)

### Formula

Use **Formula** to calculate default values dynamically.

PowerTable sheet supports formulas and functions for generating default values. These values automatically recalculate based on the underlying reference data.

The following input types support formula-based default values:

- Number
- Decimal
- Text
- Date Time
- Person
- Email

### Recalculate data on update

Enable **Recalculate data on update** to automatically reset the column to its calculated default value whenever you update the record.

[![Screenshot of the Recalculate data on update checkbox.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/recalculate-data-on-update.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/recalculate-data-on-update.png#lightbox)

When you enable this option:

- Existing values stay unchanged until you update the record.
- When you modify another field in the same record, the value resets to the formula-derived default.

In this example, changing the product size calculates the default value and resets the product price to it.

[![Screenshot of the column value resetting to its default value when the record is updated.](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/recalculate-exisiting-value.png)](../media/powertable-how-to-configure-columns/how-to-configure-general-column-properties/recalculate-exisiting-value.png#lightbox)

## FAQ

### What's the difference between Input Type and Data Type in the **Edit Column** dialog?

- **Data Type** is the underlying SQL data type for the column, such as **VARCHAR** for **Logo URL** or **INT** for **Product Key**. It appears greyed out in the **Edit Column** dialog and you can't modify it.
- **Input Type** controls how PowerTable displays and captures values in the sheet.

For example, changing the **Logo URL** column to the **Image** input type changes only how the data is displayed. The column continues to store the URL as a **VARCHAR** value.

### What does the Image input type accept?

The **Image** input type accepts:

- Direct image URLs.
- Base64-encoded image strings that begin with `data:image`.

### What are the supported input types in PowerTable?

For information about the supported input types in PowerTable, see [Supported input types](../powertable-reference-supported-column-input-types#supported-input-types).

### My table has non-English text, such as Japanese. How do I display it in PowerTable?

If your data contains Japanese and other non-English text, define the column's input type as `NVARCHAR`, so non-English characters in the data are supported and rendered correctly in PowerTable.

### Does setting a default value change existing rows?

No. Default values apply only to new records. Existing records aren't affected.

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
