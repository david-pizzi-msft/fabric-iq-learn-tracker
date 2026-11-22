---
title: "Insert dropdown list columns in planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-dropdown-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-dropdown-columns) · Last updated on **2026-08-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert dropdown list columns in planning sheet

Summarize this article for me

You can create single select or multiselect dropdown list columns in a planning sheet by using a predefined list of values.

- **Single Select** - Select one value for a row from a list of options.
- **Multi-select** - Select multiple values for a row from a list of options.

For the single select type, you can define the list of options manually or select one from the available presets. For the multiselect type, you can configure the list of options.

## Create a dropdown list column

To insert a list column:

1. Go to **Planning** > **Insert Column** > **List**.
2. Select **Single Select** or **Multi-select**.

   ![Screenshot of selecting the List option.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/insert-column-list.png)

## Configure list of values

After selecting **Single Select** or **Multi-select**, a side panel opens where you can define the list of values (LOVs) by using **List** or **Presets**.

![Screenshot of configuration options in the side panel.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/side-panel-list.png)

### List

1. Select **List** to display three default options with colors.
2. Rename, add a new option, or modify the existing options. To learn more about adding or modifying the options, see [Modify column properties and list of values](#modify-column-properties-and-list-of-values).

   ![Screenshot of dropdown options.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/options-list.png)

### Presets

1. Select **Presets** to open a list of predefined value sets.
2. Hover to preview the values.
3. Select a preset and choose **Apply**.

   [![Screenshot of presets dropdown options.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/options-preset.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/options-preset.png#lightbox)

You configured the list of values. The following section explains how to configure other column properties.

## Configure dropdown column properties

You can configure other properties such as **Insert as**, **Input type**, **On Change Formula**, **Allow entry on Totals/Subtotals**, **Allow Input**, and **Description**. For more information, see [configure data input column properties](how-to-insert-data-input-columns#configure-data-input-column-properties).

In addition, you can configure these specific properties for dropdown columns:

- **Options Style**: Choose how dropdown values are displayed - **Chip**, **Arrow**, or **Plain text**. All three styles are illustrated in the following image.

  [![Screenshot of various styles available for displaying options.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/options-style.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/options-style.png#lightbox)
- **Icon Position**: Choose the desired icons and control where the icon appears in the option:

  - You can choose to display the icon on the left or right.
  - This option isn't applicable for **Chip** style.

    [![Screenshot of icon position.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/icon-position.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/icon-position.png#lightbox)
- **Allow user to add new option**: When enabled, users can create new options directly from the dropdown, without opening the configuration panel. Select **Create** from the dropdown in the planning sheet to add a new option.

  [![Screenshot of allowing user to add new option.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/allow-user-add-new-option.jpg)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/allow-user-add-new-option.jpg#lightbox)
- **Prevent Null**: Prevents users from leaving the value empty. To enable this option, configure a **Default value** to ensure that a value is entered when the column is created or updated.

  Note

  The **Prevent Null** option is available only for the **Single Select** input type and isn't available for **Multi Select**.
- **Default Value**: You can define a default selection to avoid empty cells in the column. The default value can be one of the following types:

  - **Static**: Select a predefined value from the dropdown values.

    [![Screenshot of defining a static default value.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/default-value-static.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/default-value-static.png#lightbox)
  - **Dimension**: Select one of the available row dimensions to populate the default values.

    [![Screenshot of defining default values using dimension.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/default-value-dimension.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/default-value-dimension.png#lightbox)
  - **Measure** - Select a measure to populate the default values.

  Tip

  When you use **Dimension** or **Measure** as the **Default Value**, enable **Allow user to add new option**. This setting allows you to create a new option if no existing dimension or measure values match.

After configuring the column and list of values, select **Create**. A dropdown column is added to the planning sheet with the configured properties.

## Modify column properties and list of values

You can modify an existing dropdown column by using the same steps as other data input columns. For more information, see [modify column properties](how-to-insert-data-input-columns#modify-column-properties).

1. Go to **Insert Column** > **Manage measures** and select the **Edit** (pencil) icon.
2. A side panel opens where you can update the required properties and also modify the list of values.

   - **Edit options and colors**: Modify option names by typing over existing values or change colors by using the color picker.

     ![Screenshot of editing options.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/edit-options.png)
   - **Add new options**: To add a new option, select **Add option**, enter a value, and press **Enter**.
   - **Delete or reorder**: Use the reorder handle and the delete (bin) icon to reorder or delete options.

     ![Screenshot of add new option, delete, and reorder options.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/delete-reorder-options.png)
3. After making the changes, select **Update**.

## Localization of options list

You can display dropdown values in different languages based on user preferences.

To configure localization:

1. Go to **Format** > **Translations**.
2. Add translation entries for the required keys and languages by selecting **Add New** or the **+** icon that appears when you hover over a row.
3. To add translation entries in bulk, select **Export** to download the Excel template, add the required translation entries, and then select **Import** to import the updated file.
4. Select **Save** to apply the changes.

   [![Screenshot of adding translation keys for localization.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/format-translations.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/format-translations.png#lightbox)
5. Then, in the **Single Select** data input column, use the ***GETLOCALELABEL*** function in the **Options** field and pass the key defined in the localization settings.

Now the dropdown values automatically display in the corresponding language based on the user's locale. The following example demonstrates this feature.

### Example

In the example below, the dropdown options are displayed in French based on the current language settings.

[![Screenshot of the dropdown options based on the local language.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/example-translations.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/example-translations.png#lightbox)

## Using the dropdown column

The following steps demonstrate how to use a dropdown column.

1. Select a cell in the column to open the dropdown.
2. Choose the required value.

   [![Screenshot of choosing a dropdown option in a cell.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/use-dropdown.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/use-dropdown.png#lightbox)
3. For multiselect columns, you can select multiple values in a single cell.

   [![Screenshot of choosing more than one dropdown options in a cell.](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/use-dropdown-multiselect.png)](../media/planning-how-to-insert-columns/how-to-insert-dropdown-columns/use-dropdown-multiselect.png#lightbox)

The selected options are added based on your configuration.

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
