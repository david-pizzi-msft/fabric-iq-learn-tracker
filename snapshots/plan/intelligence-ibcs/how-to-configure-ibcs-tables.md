---
title: "Table templates"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-tables](https://learn.microsoft.com/en-us/fabric/iq/plan/intelligence-ibcs/how-to-configure-ibcs-tables) · Last updated on **2026-09-16**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Table templates

Summarize this article for me

IBCS table templates present business data using standardized layouts and semantic formatting. Use these templates to display actual values, variances, and key performance metrics in a consistent, easy-to-read format.

## T03: Table with measure rows

Table template (T03) visually structures a calculation scheme such as a profit and loss statement directly within its rows. According to IBCS, the calculation logic is detailed in the first column, allowing clear line-by-line financial tracking across prior year, plan, actual, and variance figures.

1. In the **Matrix** ribbon, select **Templates** and select **T03** from the **Performance** section.
2. Select the relative variance column, select **Conditional Formatting** > **Quick Rule** > **Negative** to highlight negative variances.

   ![Screenshot of the T03 template and conditional formatting option to highlight negative values.](../media/intelligence-ibcs/how-to-configure-ibcs-tables/t03-template-conditional-formatting-negative-variance.png)
3. To invert categories such as *costs*, in the **Data** ribbon, select the rows, then select **Invert**.

   [![Screenshot of the Invert option in the Data ribbon used to invert selected rows such as costs.](../media/intelligence-ibcs/how-to-configure-ibcs-tables/data-ribbon-invert-option.png)](../media/intelligence-ibcs/how-to-configure-ibcs-tables/data-ribbon-invert-option.png#lightbox)
4. To add an = sign, hover over a row, select the row gripper, and select **Add "=" symbol**.

   [![Screenshot of the row gripper menu with the Add '=' symbol command selected in a table row.](../media/intelligence-ibcs/how-to-configure-ibcs-tables/row-gripper-add-equal-symbol-option.png)](../media/intelligence-ibcs/how-to-configure-ibcs-tables/row-gripper-add-equal-symbol-option.png#lightbox)
5. To display positive signs at the start of each row, in the **Format** tab, go to **Appearance**> **Numbers** and enable **Show Positive Sign**.

   [![Screenshot of the Show Positive Sign option under Appearance and Numbers on the Format tab.](../media/intelligence-ibcs/how-to-configure-ibcs-tables/format-numbers-show-positive-sign-option.png)](../media/intelligence-ibcs/how-to-configure-ibcs-tables/format-numbers-show-positive-sign-option.png#lightbox)
6. To customize cell and row borders, select the cell or row, go to the **Format** ribbon, select the border icon, and select **Custom**.

   [![Screenshot of the Format ribbon border icon with the Custom option selected for a table cell or row.](../media/intelligence-ibcs/how-to-configure-ibcs-tables/custom-cell-row-border-options.png)](../media/intelligence-ibcs/how-to-configure-ibcs-tables/custom-cell-row-border-options.png#lightbox)

## T04: Measure rows and integrated waterfalls

Visualize variance and relative variance values in an income statement by using the T04 template.

- Variance values are automatically plotted as a vertical waterfall chart.
- Relative variance values are rendered as lollipop charts.

1. In the **Matrix** ribbon, select **Templates** and select **T04** from the **Performance** section.
2. Follow the customization steps outlined in the [T03: Table with measure rows](#t03-table-with-measure-rows) section.

   [![Screenshot of the T04 template showing variances as waterfall charts and relative variances as pin charts. ](../media/intelligence-ibcs/how-to-configure-ibcs-tables/t04-integrated-waterfall.png)](../media/intelligence-ibcs/how-to-configure-ibcs-tables/t04-integrated-waterfall.png#lightbox)

## T05: Hierarchical bars and integrated bars

Visualize the actuals and variances in an income statement by using the T05 template.

- Current and prior year actuals are plotted using solid bar charts.
- Variance values are automatically plotted as colored bars.
- Relative variance values are rendered as lollipop charts.

1. In the **Matrix** ribbon, select **Templates** and select **T05** from the **Performance** section.
2. To customize cell and row borders, select the cell or row, go to the **Format** ribbon, select the border icon, and select **Custom**.

   [![Screenshot of the T05 performance matrix template showing actuals as bars, variance as colored bars, and relative variance as lollipop charts.](../media/intelligence-ibcs/how-to-configure-ibcs-tables/t05-hierarchical-integrated-bars.png)](../media/intelligence-ibcs/how-to-configure-ibcs-tables/t05-hierarchical-integrated-bars.png#lightbox)

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
