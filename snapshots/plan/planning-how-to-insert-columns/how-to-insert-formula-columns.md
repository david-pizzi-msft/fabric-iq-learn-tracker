---
title: "Insert formula columns in planning sheet"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-formula-columns](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-how-to-insert-columns/how-to-insert-formula-columns) · Last updated on **2026-08-27**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Insert formula columns in planning sheet

Summarize this article for me

In planning, you can insert calculated columns or measures directly into your planning sheets. You can format these columns and reuse them in subsequent calculations. You create these measures and columns directly on the visual, without modifying the underlying data model.

The Excel-like formula engine supports more than 50 functions, including logical, boolean, and mathematical functions. The formula editor provides capabilities such as syntax assistance, examples, autocomplete, and multiline editing to help you create and troubleshoot formulas efficiently.

Note

For more information, see [Formula syntax](../planning-reference-formulas/formulas-overview) for a detailed list of supported functions, operators, and identifiers.

In this article, you learn how to insert formula measures and columns and use the formula editor to perform the required calculations with an example.

## Insert a formula measure

In this example, consider sales data for two years (2024 and 2025) by quarter. You create a measure to calculate percentage variance by using the formula:
`(2025 Actuals - 2024 Actuals) / 2024 Actuals`.

To insert a formula measure:

1. Go to **Planning** > **Insert Column** and select **Formula**.

   ![Screenshot of inserting a formula column.](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/insert-column-formula.png)
2. In the **Formula Measure** side panel:

   - Enter a **Title**.
   - In **Insert as**, select **Visual Measure** (default).

   You can also choose **Visual Column** to add a column at the end of the table, outside of the column hierarchy.
3. Enter the formula in the [editor](#working-with-the-formula-editor) and select **Create**.

   ![Screenshot of entering a formula.](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/entering-formula.png)
4. To convert the values of the *Variance%* measure to a percentage format, select the measure and then select the **%** icon on the **Planning** tab.

   [![Screenshot of converting column values to persentage.](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/convert-percentage.png)](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/convert-percentage.png#lightbox)

Note

When you select the *Variance%* measure, its formula appears in the formula bar. You can view and modify formulas in the underlying formula columns directly from the formula bar.

## Working with the formula editor

- When you place the cursor in the editor, a context assistant appears with **Functions** and **References**.
- As you type, the editor automatically filters suggestions.
- Use the **References** tab to reference measures or visual columns.
- Use the **Functions** tab to insert functions such as SUM, MIN, MAX, and AVERAGE.

  ![Screenshot of the formula editor.](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/formula-editor.png)
- You can also insert column references directly from the visual by placing the cursor in the formula editor and selecting the required columns.

  [![Screenshot of referring a column directly from the visual.](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/referencing-column.png)](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/referencing-column.png#lightbox)

After creating the measure, you can format it (for example, as a percentage or currency) from the **Planning** tab.

## Configure formula measure properties

Configure the properties for formula measures in the same way as other data input measures. For more information, see [configure data input column properties](how-to-insert-data-input-columns#configure-data-input-column-properties).

To edit the properties or to hide or delete a formula column, use the [Manage measures](how-to-insert-data-input-columns#modify-column-properties) menu.

Note

If the report doesn't contain a column hierarchy, **Insert as Measure** behaves the same as inserting a visual column, even when **Visual Measure** is selected.

## Handle calculation errors

You might encounter errors such as division by zero. You can handle these errors in the following ways:

### Use appearance settings

- Go to **Format** > **Appearance** > **Numbers**.
- Turn on **Suppress calculation errors**.
- Enter a custom value, such as `0` or `N.A.`.

### Use conditional functions

- Use **IFNA**, **IF**, or nested IF statements to explicitly handle conditions and replace error values.

## Aggregation for formula measures

By default, **Row aggregation type** is set to *Formula* and **Column aggregation type** is set to *Sum*.

You can change the aggregation type in the configuration panel or from the **Manage aggregation** interface.

![Screenshot of row and column aggregation.](../media/planning-how-to-insert-columns/how-to-insert-formula-columns/aggregation.png)

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
