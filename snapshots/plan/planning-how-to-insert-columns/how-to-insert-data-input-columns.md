---
title: "Insert data input columns in planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-data-input-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-data-input-columns) · Last updated on **2026-08-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert data input columns in planning sheet

Summarize this article for me

Planning and what-if analysis often require you to enter values, projections, or other details that don't exist in the underlying dataset. Data input columns let you add and manage these values directly within a report, making it easier to perform planning, forecasting, and scenario analysis.

In planning, you can insert data input columns and measures directly in your reports without writing Data Analysis Expressions (DAX). You can format these columns and reuse them for subsequent calculations and analysis.

In this article, you learn how to insert and configure data input columns and measures.

## Data input types

Planning supports various data input column types to accommodate different planning and reporting scenarios. Depending on the information you want to capture, you can create columns for numeric values, formulas, text, users, and predefined option selections.

The following table describes the available data input column types.

| Input type | Description |
| --- | --- |
| [Number](how-to-insert-number-columns) | Double-click and start typing numerical values directly into a cell. |
| [Text](how-to-insert-text-columns) | Enter text with multi-line support and word wrapping. |
| [Checkbox](how-to-insert-checkbox-columns) | Capture binary values such as Yes/No or True/False. |
| [Person](how-to-insert-person-columns) | Select users from your organization. |
| [List](how-to-insert-dropdown-columns) | Use predefined values or create your own list of values. Supports both single select and multi-select options. |
| [Date](how-to-insert-date-columns) | Select a date using the date picker. |
| [Simulate](../planning-how-to-use-simulation-measures) | Use this column to simulate the number columns. |

## Create a data input column

To add a data input column to your report:

1. Go to **Planning** > **Insert Column**.
2. Select the data input column type that you want.

   ![Screenshot of inserting a column using Planning tab.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/planning-insert-column.png)
3. Configure the column properties and select **Create**.

Note

For detailed instructions on configuring each data input column type, see the related articles linked in the [Data input types](#data-input-types) section.

## Configure data input column properties

Configure the following properties while creating a data input column:

- **Insert As**: Choose how to add the column:

  - **Visual measure**: Inserts the input column across each category when a column hierarchy exists.

    [![Screenshot of inserting a column as visual measure.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/insert-as-visual-measure.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/insert-as-visual-measure.png#lightbox)
  - **Visual column**: Inserts a single column regardless of hierarchy.

    [![Screenshot of inserting a column as visual column.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/insert-as-visual-column.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/insert-as-visual-column.png#lightbox)
- **Input type**: Change the type of data input column before creating it.

  ![Screenshot of different types of input.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/input-type.png)

  Note

  You can't change the **Insert as** and **Input type** settings after you create the column or measure.
- **Default value**: Specifies the value to display in empty cells. Depending on the input type, use a **Static** value, **Dimension**, or **Measure**. If the underlying measure or formula changes, the default value updates accordingly.

  Note

  - For visual columns, set default values only by using **static values**.
  - The **Default value** option isn't available for **Long Text**, **Multi Select**, or **Person** input types.
- **Entry in total and subtotal rows**: Allows users to enter values in total and subtotal rows. This option is enabled by default. Clear **Allow entry on Total/Subtotals** to prevent entries in these rows.

  [![Screenshot of disabling entry in total & subtotal rows.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/entry-total-subtotal-rows.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/entry-total-subtotal-rows.png#lightbox)

  Note

  The **Allow entry on Totals/Subtotals** option is available for all input types except **Number**.
- **On Change Formula**: Defines the action to perform when a value in the column changes. Specify a formula or script that automatically executes whenever the value updates. Use this option to trigger calculations, update related values, or perform other actions based on the change.

  Note

  The **On Change Formula** option is available for all input types except **Long Text**.
- **Allow input**: Control when users can enter data:

  - **In both read and edit mode**: Users can enter data in both reading and editing modes (default).

    [![Screenshot of allowing inputs in both read and edit mode.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/both-read-and-edit-mode.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/both-read-and-edit-mode.png#lightbox)
  - **Only in edit mode**: Users can enter data only in editing mode. In reading mode, the cells are disabled for entries.

    [![Screenshot of allowing inputs only in edit mode.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/edit-mode.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/edit-mode.png#lightbox)
  - **Based on formula**: Users can enter input only when a condition is met. Planning evaluates the condition using a user-defined formula.

    [![Screenshot of allowing inputs based on a formula.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/based-on-formula.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/based-on-formula.png#lightbox)
- **Add Breakdown**: Select this option to enable multi-dimensional value allocation. For more information, see [Plan across multiple dimensions with cubes](../planning-how-to-create-cube).
- **Description**: Add a note for reference.

## Modify column properties

To modify the properties of an existing data input column:

1. Go to **Planning** > **Insert Column** > **Manage Measures**.
2. Select the option you want:

   - **Edit** (pencil icon) to modify the column properties.
   - **Delete** to remove the column.
   - **Show/Hide** to control column visibility.

   [![Screenshot of manage measures options.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/manage-measures-options.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/manage-measures-options.png#lightbox)

   Alternatively, use the column gripper:
3. Hover over the column or measure header to display the column gripper.
4. Select the column gripper and choose the action you want, such as **Edit Measure**, **Delete Measure**, or **Hide Column**.

   ![Screenshot of modifying options in column gripper.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/column-gripper-modify-options.png)
5. If you select **Edit**, a side panel opens where you can update the properties. After you make the changes, select **Update**.

## Access control

With planning, you can control read and write access for data input columns.

To configure access:

1. Select **Security** to open the access control window.

   [![Screenshot of security options.](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/security.png)](../media/planning-how-to-insert-columns/how-to-insert-data-input-columns/security.png#lightbox)
2. Locate the column or measure that you want to configure.
3. Configure the access settings. The options are **Read Access** and **Read + Write Access**.
4. Add users to the appropriate access column by entering their name or email address. Select the user from the search results.

   - **Read Access**: Provides view-only access to the data input column.
   - **Read + Write Access**: Provides permissions to view and edit the column.

## Other considerations

- Multiple users can enter data in the same published report, including in reading view. You can track all changes by using the audit log.
- By default, users can view data entered by others. When row-level security (RLS) is enabled, users can see only the data that they're authorized to access.
- You don't need additional setup to enable data entry. You can use the data input feature to add input fields of various types.
- You can write back data input columns to external destinations such as SQL database in Fabric. You can also export them to formats such as PDF or Excel.

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
