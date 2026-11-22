---
title: "Configure column properties for a PowerTable sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-configure-columns/how-to-configure-column-properties-summary](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-configure-columns/how-to-configure-column-properties-summary) · Last updated on **2026-07-09**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure column properties for a PowerTable sheet

Summarize this article for me

Configuring column properties helps ensure data accuracy and consistency in the database. By defining appropriate data types, constraints, default values, and relationships, you can prevent data-entry errors and maintain data integrity.

Column properties also help improve the usability, maintainability, and scalability of your tables by controlling how data is displayed and managed.

In this article, you learn how to access and configure column properties in a PowerTable sheet.

## Column properties

Column properties control various aspects of a column, including:

- Input type
- Editability
- Nullability
- Default values
- Minimum and maximum values
- Lookups and relationships
- Prefixes and suffixes
- Display settings

## Configuring columns during setup

- When you create a powertable app by importing data from a CSV file, creating a table from scratch, or connecting to a database, you can set the column properties during the setup process.
- Powertable automatically detects and configures the input type and other basic column settings. You can retain the detected settings or modify them to meet your business requirements.

[![Screenshot of the Configure Table window.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/configure-table.jpg)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/configure-table.jpg#lightbox)

## Configuring columns in the created PowerTable sheet

After loading data into the PowerTable sheet, you can configure column properties at any time in the **Columns** section.

To access column properties:

1. Select **Setup** > **Columns**.

   ![Screenshot of selecting Columns option from the Setup menu.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/setup-columns.png)

   Alternatively, you can go to the **PowerTable** ribbon and select **Manage Columns** > **Edit Config**.

   [![Screenshot of the Manage Column window with Edit Config option.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/edit-config.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/edit-config.png#lightbox)
2. The **Column Setup** window opens as shown in the following image.

   [![Screenshot of the column setup window.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-setup-window.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-setup-window.png#lightbox)

## Add columns

To add a new column to the table, use the **Add Visual Column**, **Add Formula Column**, or **Add Database Column** options available in the column setup window.

[![Screenshot of the options for adding new columns.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/add-columns.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/add-columns.png#lightbox)

For more information about these column types, see [Supported column types](../powertable-reference-supported-column-input-types#supported-column-types) and [Insert columns](../powertable-how-to-insert-columns/how-to-insert-visual-columns).

## Set column constraints

PowerTable enables you to configure column constraints without writing code. You can apply a unique constraint to a single column or define a composite unique constraint across multiple columns to ensure that each value or combination of values remains unique. Unique constraints help maintain data integrity by preventing duplicate values.

To configure column constraints:

1. Select **Column Constraints** in the column setup window.

   [![Screenshot of the Column Constraints option.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-constraints.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-constraints.png#lightbox)
2. The **Column Constraints** window opens, as shown in the following image.

   [![Screenshot of the Column Constraints pop-up window.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-constraints-window.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-constraints-window.png#lightbox)

### Unique Value

Use the **Unique Value** option to ensure that all values in a selected column are unique.

1. Under **Unique Value**, select a column from the dropdown list.

   [![Screenshot of the Unique Value dropdown.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/unique-value.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/unique-value.png#lightbox)
2. To configure additional unique constraints, select **Add** and choose another column.
3. Select **Save**.

   [![Screenshot of the Add option to configure additional unique constraints.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/unique-value-add.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/unique-value-add.png#lightbox)

After you apply the constraint, users can't enter duplicate values in the selected column.

For example, if *ProductSKU* is configured as a unique column, users can't enter a SKU value that already exists in the table.

Note

Primary key columns don't appear in the **Unique Value** dropdown because they're unique by default.

If a selected column already contains duplicate values, PowerTable sheet displays an error and doesn't allow you to save the constraint until you remove the duplicate values.

### Unique Combination

Use **Unique Combination** to ensure that a specific combination of values across multiple columns remains unique.

1. Under **Unique Combination**, select the required columns from the dropdown list.
2. To configure additional unique combinations, select **Add** and choose another set of columns.
3. Select **Save**.

   [![Screenshot of the Unique Combination dropdown.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/unique-combination.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/unique-combination.png#lightbox)

Note

You can't select columns configured with the **Unique Value** constraint in the **Unique Combination** constraint.

After you apply the constraint, users can't enter records that duplicate an existing combination of values in the selected columns.

For example, if *ModelName* and *ProductName* are configured as a unique combination, each *ModelName* - *ProductName* pair must be unique. Users can reuse an individual value in either column, but the same combination of values can't exist more than once.

If a user attempts to enter a duplicate combination, PowerTable sheet displays a validation error and prevents the record from being saved.

To remove a configured constraint, select the **Delete** icon next to it.

[![Screenshot of the Delete icons in the Column Constraints window.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-constraints-delete.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-constraints-delete.png#lightbox)

## Display or hide columns

Use the **Display** option to control whether a column is visible in the table.

Clear the **Display** checkbox to hide a column while retaining its data in the table. This option is useful when a column contains information that should be available but doesn't need to be displayed to users.

[![Screenshot of the Display column in the column setup window.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/display.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/display.png#lightbox)

To adjust column widths, drag the column header boundary or configure the width through [Manage Columns](../powertable-how-to-manage-columns).

## Allow or restrict `NULL` values

Use the **Required** option to specify whether a column must contain a value. When enabled, users must provide a value before a record can be saved. When disabled, the column can be left `NULL`.

Primary key and business key columns are typically configured as required fields.

[![Screenshot of the Required column in the column setup window.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/required.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/required.png#lightbox)

## Configure other properties

To configure or modify other properties for a column, select the pencil icon next to the column or double-click the column name.

[![Screenshot of the edit icon and column name to select for configuring properties.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/edit-icon-column-name.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/edit-icon-column-name.png#lightbox)

To edit the properties of a specific column directly from the table, select the column header menu (**...**) and then select **Edit**.

![Screenshot of the Edit option in the column header context menu.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/column-edit.png)

Column properties are grouped and classified into two tabs:

- [General](how-to-configure-general-column-properties) - Configure the **Input Type**, **Constraints**, **Default values**, and other data-related settings.
- [Display](how-to-configure-display-column-properties) - Configure the **Display name** and **Description** for a column. For numeric columns, additional formatting options are available, including the **Prefix**, **Suffix**, **Thousand Separator**, and other number formatting settings.

  [![Screenshot of the General and Display tabs.](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/general-display.png)](../media/powertable-how-to-configure-columns/how-to-configure-column-properties-summary/general-display.png#lightbox)

## Related content

- [Configure general properties for a column](how-to-configure-general-column-properties)
- [Configure display properties for a column](how-to-configure-display-column-properties)

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
