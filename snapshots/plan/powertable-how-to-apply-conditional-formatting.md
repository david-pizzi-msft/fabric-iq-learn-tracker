---
title: "Apply conditional formatting in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-apply-conditional-formatting](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-apply-conditional-formatting) · Last updated on **2026-08-02**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Apply conditional formatting in PowerTable

Summarize this article for me

The conditional formatting feature in PowerTable sheets helps highlight specific data based on defined conditions. Use conditional formatting to emphasize records with text styles, borders, icons, font colors, or background colors. This formatting makes it easier to identify trends, exceptions, outliers, and other important data points.

PowerTable automatically applies conditional formatting rules to table data when the data meets the specified conditions. You can create, manage, edit, and remove rules to customize how data appears and improve the readability of your sheets.

Common use cases for conditional formatting include:

- Highlighting values that exceed or fall below a target threshold.
- Identifying records that require attention or follow-up.
- Visualizing performance metrics using color indicators.
- Emphasizing specific text values or statuses.
- Drawing attention to missing, duplicate, or exceptional data.

By using conditional formatting, you can quickly interpret large datasets and focus on the information that matters most.

In this article, you learn how to apply conditional formatting by configuring and managing rules.

## Create a conditional formatting rule

To create a conditional formatting rule:

1. Go to the **Format** tab and select **Format Rules** > **Create Rule**.

   [![Screenshot of the create rule option in the Format tab of the menu ribbon.](media/powertable-how-to-apply-conditional-formatting/format-create-rule.png)](media/powertable-how-to-apply-conditional-formatting/format-create-rule.png#lightbox)

   A side panel opens, as the following image shows.

   [![Screenshot of the create formatting rule side panel.](media/powertable-how-to-apply-conditional-formatting/side-panel-create-format-rule.png)](media/powertable-how-to-apply-conditional-formatting/side-panel-create-format-rule.png#lightbox)
2. In **Title**, enter a name for the rule.
3. In **Apply To**, select the [column](#apply-to-column) or [rows](#apply-to-rows) to format.

   ![Screenshot of the apply to option in the create formatting rule side panel.](media/powertable-how-to-apply-conditional-formatting/apply-to.png)
4. Use **Conditions** to define the criteria for the rule. The available operators and comparison options vary based on the selected column type.
5. In **Style**, configure the formatting to apply when the condition is true. You can customize font color, font style, borders, background color, or specific icons.

   ![Screenshot of configuring the condition if and style options.](media/powertable-how-to-apply-conditional-formatting/condition-if-style.png)
6. Select **Add Rule** to add more conditions. You can combine multiple conditions by using **AND** or **OR** operators.

   ![Screenshot of the add rule option in the create formatting rule side panel.](media/powertable-how-to-apply-conditional-formatting/add-rule.png)
7. Select **Apply** to save and apply the rule. To discard the changes, select **Cancel**.

### Apply to column

When you select a column, formatting applies only to the records in the **selected** column that meet the specified condition. For example:

1. Select the *ProductSKU* column in the **Apply To** dropdown.
2. Configure the condition as *ProductPrice* **Greater than** 700 in the **Condition If** section.
3. Configure the formatting style by applying bold text, the required font color, and background color.
4. Optionally, use the **Add Prefix/Suffix** option to add text or an icon before or after the cell value by customizing the icon type, icon color, text, and position.

   Note

   The **Add Prefix/Suffix** option is available only when you select a column in the **Apply To** field.

   ![Screenshot of the conditional formatting rule configuration for a selected column.](media/powertable-how-to-apply-conditional-formatting/apply-to-column.png)

The following image shows the formatted records in the **ProductSKU** column that meet the configured condition.

[![Screenshot of the column after the conditional formatting rules are applied.](media/powertable-how-to-apply-conditional-formatting/apply-to-column-output.png)](media/powertable-how-to-apply-conditional-formatting/apply-to-column-output.png#lightbox)

### Apply to rows

To apply formatting to all columns in rows that meet the specified condition, select **Rows** in the **Apply To** dropdown. For example:

Consider formatting rows that contain products with a price greater than 700 and a subcategory of mountain bikes or road bikes.

1. To format all columns in the rows that meet the specified conditions, select **Rows** in the **Apply To** dropdown.
2. In the **Condition If** section, set the first condition to *ProductPrice* **Greater than** 700.
3. Select **Add Rule** to add the second condition.
4. Set the second condition to *ProductSubcategoryKey* **is** *Mountain Bikes* or *Road Bikes*.
5. Select **AND** to combine the two conditions.
6. Select **Apply**.

   ![Screenshot of the conditional formatting rule configuration for rows.](media/powertable-how-to-apply-conditional-formatting/apply-to-rows.png)

All columns in rows that meet the configured conditions are formatted as shown in the following image.

[![Screenshot of the table after the conditional formatting rules are applied to all rows that meet the condition.](media/powertable-how-to-apply-conditional-formatting/apply-to-rows-output.png)](media/powertable-how-to-apply-conditional-formatting/apply-to-rows-output.png#lightbox)

## Manage conditional formatting rules

Use **Manage Rules** to view, edit, duplicate, disable, or delete existing conditional formatting rules.

To manage rules:

1. Select **Format Rules** > **Manage Rules**. A side panel opens and shows all configured rules.

   [![Screenshot of the manage rules option in the format tab.](media/powertable-how-to-apply-conditional-formatting/format-manage-rules.png)](media/powertable-how-to-apply-conditional-formatting/format-manage-rules.png#lightbox)
2. Use the available actions for a rule to edit, duplicate, delete, enable, or disable it.

   [![Screenshot of the manage rules side panel.](media/powertable-how-to-apply-conditional-formatting/manage-rule-side-panel.png)](media/powertable-how-to-apply-conditional-formatting/manage-rule-side-panel.png#lightbox)

## FAQ

### When should I use 'Apply to Rows' instead of formatting individual cells?

Use **Apply to Rows** when you want to highlight an entire record rather than a single cell. When the specified condition is met, PowerTable applies the formatting to all cells in the row, making related data easier to identify and review.

If you want, you can format only a particular cell by selecting the appropriate cell when you create or edit the formatting rule.

### Where are formatting rules stored after I create them? Can I disable a rule without deleting it?

The **Manage Rule** dialog stores formatting rules. You can access it from **Format Rules** on the **Format** tab.

Yes, you can enable or disable rules without deleting them.

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
