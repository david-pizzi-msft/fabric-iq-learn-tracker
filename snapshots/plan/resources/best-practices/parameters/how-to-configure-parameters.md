---
title: "Build interactive controls with parameters"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-configure-parameters](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-configure-parameters) · Last updated on **2026-11-05**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Build interactive controls with parameters

Summarize this article for me

Create parameters in planning to enable viewers in reading mode to interactively analyze and control reports without making manual edits or modifying the underlying setup. By using graphical controls like buttons, checkboxes, or sliders, users can filter datasets, change visual layouts, and run ad hoc scripts. This interactive capability allows team members to quickly rank data and dynamically navigate complex datasets across different timeframes and dimension categories while keeping the original planning structure intact.

## Prerequisite

Create a planning item that has at least one planning sheet or an intelligence sheet.

## Configure parameters

You can define parameters at two levels depending on your scope:

- **Page-level parameters**: Apply specifically to an individual page, giving users localized control over that view.
- **Global parameters**: Apply universally across all planning and intelligence sheets to maintain consistent filtering and logic throughout the app.

Fabric planning supports the following types:

| Parameter type | Planning use case |
| --- | --- |
| **Number** | - Dynamic calculations: Pass an exchange rate or adjust a discount percentage for price sensitivity analysis. - Ranking: Set a Top-N ranking, such as viewing the top 10 products by margin. - Threshold values: Apply conditional formatting, such as highlighting categories with sales > 10k. |
| **Text** | - Add custom header or footer content before printing a report. - Add custom text like a summary to a report header .  - Pass values to a filter . |
| **Date** | - Add custom dates to a report header. |
| **List** | - Category filtering: Choose a target department or entity for budget allocation. - Select a currency, such as USD, EUR, or GBP. |
| **Action (Script)** | - Run scripts to execute multi-step workflows, such as updating layouts, reformatting visuals, applying conditional rules, or adjusting ranking. |

- [Use parameters in intelligence sheets](#tabpanel_1_intelligence-sheets)
- [Use parameters in planning sheets](#tabpanel_1_planning-sheets)

The following steps show how to create and use parameters in intelligence sheets:

1. To create a new parameter, expand the **Parameter** pane and select **+Add new**. To create a global parameter, select the **+Add new** option from the **Global** tab.

   [![Screenshot of page level and global level parameters options and the add new button.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/intelligence-sheets-parameter-pane-add-new.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/intelligence-sheets-parameter-pane-add-new.png#lightbox)
2. Select the parameter type. In this example, you create a number parameter that captures the number of ranks to display.
3. Enter the parameter name and an optional default value if applicable.
4. Enter a unique **Parameter ID**. You need the parameter ID to reference the parameter in formulas.
5. Add an optional description to help users understand what this parameter controls. This description is displayed as a tooltip when you hover over the parameter.
6. Select an interface type. Fabric planning supports various interface options such as toggles, sliders, dropdowns, radio buttons, and text boxes to assign values to parameters. The interface options vary based on the parameter type.
7. Select **Include in Read Mode** to display the parameter controls in read-only view and allow users to change the parameters.

   [![Screenshot of the parameter creation pane showing type, name, ID, description, and interface options for a number parameter.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/create-number-parameter-options-pane.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/create-number-parameter-options-pane.png#lightbox)
8. Select **Add** to create the parameter. Since you set the interface type to Input Box, you create the parameter with an input box that accepts numeric values.

   [![Screenshot of a number parameter created with an input box interface.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameter-input-box-created.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameter-input-box-created.png#lightbox)
9. In this example, use parameters to rank data in a dashboard. Select the TopN option from the intelligence visual. Repeat this step for each visual in an intelligence dashboard.
10. Set the **By** option to **Parameters** and select the configured ranking parameter. Select **Apply**.

    [![Screenshot of using parameters in the topN ranking configuration in a chart visual.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/top-ranking-by-parameter-configuration.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/top-ranking-by-parameter-configuration.png#lightbox)
11. Changing parameter values instantly re-ranks data across your entire dashboard.

    [![Animation showing how changing the parameter values applies ranking to the matrix and chart visuals.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/parameter-change-ranks-dashboard-visuals.gif)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/parameter-change-ranks-dashboard-visuals.gif#lightbox)

The following steps show how to create and use parameters in planning sheets:

1. To create a new parameter, expand the **Parameter** pane and select **+Add new**. To create a global parameter, select the **+Add new** option from the **Global** tab.

   [![Screenshot of the +Add new option in the Parameter pane of a planning sheet.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/add-new-parameter-planning-sheet.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/add-new-parameter-planning-sheet.png#lightbox)
2. Select the parameter type. In this example, you create a number parameter that captures the sales threshold for conditional formatting.
3. Enter the parameter name and an optional default value if applicable.
4. Enter a unique **Parameter ID**. You need the parameter ID to reference the parameter in formulas.
5. Add an optional description to help users understand what this parameter controls. This description is displayed as a tooltip when you hover over the parameter.
6. Select an interface type. Fabric planning supports various interface options such as toggles, sliders, dropdowns, radio buttons, and text boxes to assign values to parameters. The interface options vary based on the parameter type.
7. Select **Include in Read Mode** to display the parameter controls in read-only view and allow users to change the parameters.

   [![Screenshot of number parameter settings in a planning sheet, including name, parameter ID, description, interface type, and include in read mode options.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameter-threshold-configuration-planning-sheet.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameter-threshold-configuration-planning-sheet.png#lightbox)
8. Select **Add** to create the parameter. Since you set the interface type to Input Box, you create the parameter with an input box that accepts numeric values.

   [![Screenshot of a number parameter created in a planning sheet with an input box interface to accept conditional formatting thresholds.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameter-threshold-created-planning-sheet.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameter-threshold-created-planning-sheet.png#lightbox)
9. In the **Format** ribbon of your planning sheet, select **Conditional Formatting** > **Create Rule**. In the side pane, set **Format by** to **Rules (If Conditions)**.
10. Configure the rule as shown in the following image. You can select the threshold parameter and use it in the rule condition. In this example, you highlight the cells where the *Total Sales* is lower than the value entered in the threshold parameter.

    [![Screenshot of using the threshold parameter in a conditional formatting rule to highlight values.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/select-parameter-create-conditional-formatting-rule.png)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/select-parameter-create-conditional-formatting-rule.png#lightbox)
11. Select **Apply** to create the rule. The cells with sales less than the specified threshold are dynamically highlighted based on the parameter value you enter.

    [![Animation showing how conditional formatting is applied as you change the threshold value.](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameters-conditional-formatting.gif)](../../../media/resources/best-practices/parameters/how-to-configure-parameters/number-parameters-conditional-formatting.gif#lightbox)

## Related content

Apply conditional formatting to planning sheets: [Conditional formatting in planning sheets](/en-us/fabric/iq/plan/planning-conditional-formatting/concept-conditional-formatting)

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
