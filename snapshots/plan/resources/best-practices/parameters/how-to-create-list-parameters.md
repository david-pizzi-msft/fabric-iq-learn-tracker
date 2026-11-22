---
title: "Create list parameters"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-list-parameters](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-list-parameters) · Last updated on **2026-11-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create list parameters

Summarize this article for me

A list parameter lets users select values from a predefined or dynamic list of options, such as product categories, business units, regions, or specific months. You can source list parameters directly from a semantic model or hard-code them as custom options. Users can dynamically apply formatting or feed categorical inputs into planning models without modifying the underlying report layout.

## Apply conditional formatting based on selected values

When you combine list parameters with conditional formatting, you can highlight data points on a visual based on the user's categorical selections. Instead of filtering out nonselected items entirely, parameter-driven conditional formatting evaluates the current parameter value against target rules, such as highlighting sales performance bars, threshold alerts, or profit margins only for the user-selected products or months.

1. Before you begin, [create a number parameter](how-to-create-number-parameters#enter-conditional-formatting-thresholds) for the COGS threshold used in this example.
2. Create a new parameter and set the type to **List**.
3. Set the source to **Data set** to fetch the dropdown values from your semantic model.
4. Select the dimension from your semantic model. The list sources values from the unique categories in the selected dimension.

   [![Screenshot of selecting the dimension to source the list categories.](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/select-list-source-dimension.png)](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/select-list-source-dimension.png#lightbox)
5. Create a second parameter to select the product category.
6. In this example, radio buttons control the product category parameter, and a multiselect dropdown lets users select multiple months.

   [![Screenshot of list parameters with radio buttons for product category and a multiselect dropdown for month.](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/list-parameter-created.png)](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/list-parameter-created.png#lightbox)
7. Select the visual, and then select **Conditional Formatting** > **New Rule**.
8. Configure the rule as shown in the following image. In this example, you create a rule to highlight the profit margin bars when the COGS falls below the threshold entered in the number parameter and for the months selected in the list parameter.

   [![Screenshot of configuring a conditional formatting rule that uses the number and list parameters.](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/conditional-formatting-rule-number-list-parameters.png)](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/conditional-formatting-rule-number-list-parameters.png#lightbox)
9. Repeat step 7 to create parameter-driven conditional formatting rules for other visuals in your dashboard.
10. Planning applies conditional formatting based on the thresholds and values set in the parameters.

    [![Animation showing profit margin bars highlighted based on months selected in a list parameter and a COGS number parameter threshold.](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/list-parameter-conditional-formatting.gif)](../../../media/resources/best-practices/parameters/how-to-create-list-parameters/list-parameter-conditional-formatting.gif#lightbox)

## Best practices for selecting the UI control

- Use radio buttons for high-visibility choices that require immediate comparison without opening a menu. They're ideal for two to five options.
- Use tiles for touch-friendly, modern layouts, such as categories or years. They're ideal for two to six options.
- Use single-select dropdowns when users must select exactly one option from a large or dynamic list, such as choosing a specific store ID or employee.
- Use multi-select dropdowns for complex filtering across multiple categories simultaneously.

## Related content

- [Configure parameters](how-to-configure-parameters).
- [Create numeric input parameters](how-to-create-number-parameters).

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
