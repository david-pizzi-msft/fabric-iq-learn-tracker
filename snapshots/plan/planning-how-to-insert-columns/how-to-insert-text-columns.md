---
title: "Insert text input columns in planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-text-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-text-columns) · Last updated on **2026-08-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert text input columns in planning sheet

Summarize this article for me

This article explains how to insert a text input column in a planning sheet.

Use text columns to capture free-form input in reports. A text column accepts short text, long text, numbers, and alphanumeric inputs.

## Insert a text column

To insert a text column:

1. Go to **Planning** > **Insert Column** > **Text.**

   ![Screenshot of inserting a text column.](../media/planning-how-to-insert-columns/how-to-insert-text-columns/insert-column-text.png)
2. Enter a title and configure the required settings in the side panel that opens when you select **Text**, as shown in the following image.

   ![Screenshot of side panel with configuration options for text column.](../media/planning-how-to-insert-columns/how-to-insert-text-columns/side-panel.png)
3. Select **Create.**

After you create the column, double-click a cell to enter text and press Enter to save. You can [modify a text column](how-to-insert-data-input-columns#modify-column-properties) to edit its configuration.

![Screenshot of entering a text in the text column.](../media/planning-how-to-insert-columns/how-to-insert-text-columns/entering-text.png)

## Configure text input column properties

Configure key properties such as **Insert As**, **Input type**, **Default Value**, **Allow entry on Totals/Subtotals**, **On Change Formula**, **Allow Input**, and **Description** as you do for other data input columns. For more information, see [configure data input column properties](how-to-insert-data-input-columns#configure-data-input-column-properties).

Text columns also support the following properties:

- **Word wrap**: Enable word wrap for long text values to improve readability. Use the **word wrap** option in the **Format** tab to adjust text based on column width.
- **Prevent Null**: Prevents users from leaving the value empty. To enable this option, configure a **Default value** to ensure that a value is entered when the column is created or updated.

  Note

  The **Prevent Null** option is available only for the **Short Text** input type and isn't available for **Long Text**.
- **Text validation** - Validate text input to ensure data quality. You can:

  - Define **minimum** and **maximum length** to control the length of text input.

    [![Screenshot of defining minimum and maximum length of the text.](../media/planning-how-to-insert-columns/how-to-insert-text-columns/min-max-length.png)](../media/planning-how-to-insert-columns/how-to-insert-text-columns/min-max-length.png#lightbox)
  - Restrict input type (numeric, email, alphanumeric) by selecting the required option from the **Field Validation** dropdown.

    [![Screenshot of field validation option.](../media/planning-how-to-insert-columns/how-to-insert-text-columns/field-validation.png)](../media/planning-how-to-insert-columns/how-to-insert-text-columns/field-validation.png#lightbox)
  - Use the **Custom** option to apply a regular expression (regex). Select **Custom** and enter the required text pattern.

    [![Screenshot of field validation custom option.](../media/planning-how-to-insert-columns/how-to-insert-text-columns/field-validation-custom.png)](../media/planning-how-to-insert-columns/how-to-insert-text-columns/field-validation-custom.png#lightbox)

Note

Only text that satisfies the validation rules is accepted. Invalid entries display an error.

| Field Validation | Allowed Text |
| --- | --- |
| **Any Value** | Allows numbers, alphabets, punctuation, and special symbols |
| **Numeric** | Only numbers |
| **Non Numeric** | Everything except numbers |
| **Alpha Numeric** | Numbers and alphabets |
| **Email** | Valid email addresses |
| **URL** | Valid URL links |
| **Custom** | Text that matches the defined pattern |

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
