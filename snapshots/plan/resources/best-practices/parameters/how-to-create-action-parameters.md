---
title: "Run scripts by using action parameters"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-action-parameters](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-action-parameters) · Last updated on **2026-11-18**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Run scripts by using action parameters

Summarize this article for me

Action parameters help end-users to interactively trigger custom scripts directly from report controls like buttons or toggles. Unlike traditional dashboard controls that rely on DAX measures or modifying underlying semantic models, Action Parameters execute predefined operations natively within the report environment.

Viewers can perform advanced layout and analytical operations such as drilling down, rolling up hierarchies, switching visual layouts, or applying conditional formatting rules on the fly without requiring edit permissions or deep technical knowledge of report authoring.

## Prerequisites

When you configure an action parameter, select **Enable Script** under **Interface Options** to define custom scripts. Select **Include in read mode** for every parameter that viewers need to use, including threshold inputs.

## Drill down and roll up hierarchies

Action parameters allow report authors to attach hierarchy-navigation scripts directly to UI controls like buttons or toggle switches. Instead of forcing users to rely on default visual header icons or context menus, action parameters offer a one-click experience to adjust the depth of data granularity.

1. Create a new parameter and set the type to **Action**.
2. Set the interface to **Toggle**. Changing the toggle triggers different scripts.

   [![Screenshot of creating an action parameter with the interface type set to toggle.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/drill-down-parameter-configuration.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/drill-down-parameter-configuration.png#lightbox)
3. To define the scripts that run when the toggle is enabled, select the **+ Add button** in the **On Actions** section.
4. In the **On State Configuration** window, enter a descriptive label for when the toggle is enabled (defaults to ON). Use a label that clearly indicates the action triggered in this state, such as *Drill Down*.
5. Use the **Apply to** dropdown to choose the scope of the script: the entire dashboard (Root) or a specific visual. In this example, select the **Treemap** visual to enable drill-down and roll-up capabilities.

   [![Screenshot of the Apply to dropdown with the Treemap visual selected as the script scope.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/apply-to-dropdown-treemap-visual-selection.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/apply-to-dropdown-treemap-visual-selection.png#lightbox)
6. In the **Formula Script** section, select the built-in scripts to define the actions for each state, and then select Save. Use the `DRILL_DOWN` function in the On state configuration and `DRILL_UP` in the Off state configuration.

   [![Screenshot of toggle On and Off state configurations with drill-down and roll-up formula scripts applied to the treemap visual.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/toggle-on-off-state-drill-down-roll-up-scripts.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/toggle-on-off-state-drill-down-roll-up-scripts.png#lightbox)
7. Choose whether the toggle loads as On or Off when the report opens. Setting the toggle's default state to Off ensures the visual opens in the rolled-up view automatically.
8. Enabling the toggle drills down the treemap to the subcategory level, while disabling it rolls the data back up to the category level.

   [![Animation showing a toggle control to drill down and roll up hierarchical dimensions in the treemap.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-drill-down-roll-up.gif)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-drill-down-roll-up.gif#lightbox)

## Apply conditional formatting by using scripts

When you bind a script to UI controls like toggles or buttons, you can highlight performance thresholds, flag variance outliers, or change color scales across tables, charts, and KPI cards. This approach provides a clean, highly interactive way to surface visual insights.

To demonstrate this feature, start by creating a number parameter that accepts a threshold value. Then use this number parameter to define a conditional formatting rule and finally trigger the rule with a button control.

1. Create a number parameter. Enter the parameter ID and name, specify an optional default value, and set the **Interface Type** to **Input Box**.

   [![Screenshot of configuring a number parameter with the interface type set to input box.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/create-number-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/create-number-parameter.png#lightbox)
2. Select your chart visual. Select **Conditional Formatting** > **New Rule** from the respective ribbon.
3. Configure the rule to set a custom background color when the sales value is below the threshold parameter you created in step 1.

   [![Screenshot of a conditional formatting rule that sets a custom background color when sales are below the threshold parameter value.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/create-conditional-formatting-rule-number-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/create-conditional-formatting-rule-number-parameter.png#lightbox)
4. Create an action parameter to apply conditional formatting on demand. In the script, use the `RULES` identifier to select the conditional formatting rule you defined in step 3.

   [![Screenshot of creating an action parameter script to apply the conditional formatting rule.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/create-action-parameter-conditional-formatting.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/create-action-parameter-conditional-formatting.png#lightbox)
5. Use the `TOGGLE_RULE` formula for the on-state configuration and the `SET_RULE_ENABLED` formula for the off-state configuration.

   Note

   After you select the rule in your script, planning converts the rule name to the rule identifier.

   [![Screenshot of TOGGLE_RULE and SET_RULE_ENABLED scripts in the on-state and off-state configuration of an action parameter.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/conditional-formatting-action-rule-scripts.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/conditional-formatting-action-rule-scripts.png#lightbox)
6. Enable the toggle to highlight region panels whose sales values are below the threshold value defined in the number parameter.

   [![Animation showing a background color applied when the switch is enabled and the sales is below entered threshold.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-apply-conditional-formatting.gif)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-apply-conditional-formatting.gif#lightbox)

## Set number formatting

Use action parameters to switch number formatting modes across a planning sheet without altering the sheet structure. Tie scripts to controls like dropdowns or toggle buttons so viewers can switch between automatic and native number formatting.

1. Create a new action parameter.
2. Use the `SETNUMBERFORMATTING` function to change the number scaling.

   [![Screenshot of using the SETNUMBERFORMATTING function to change the scaling.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/change-number-formatting-script.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/change-number-formatting-script.png#lightbox)
3. Select the button to apply the number formatting script. The example shows how to switch between auto scaling and native scaling in the planning sheet.

   [![Screenshot showing how to use a button parameter to change the scaling in a planning sheet.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameters-number-formatting.gif)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameters-number-formatting.gif#lightbox)

## Change layouts

By changing planning sheet layouts dynamically by using scripts, report authors and end-users can alter how data is structured and visualized on the fly, without manually altering the base sheet design. Tie layout scripts to interactive elements like buttons or toggle switches to give report viewers flexibility to customize their layout perspective without needing edit permissions.

1. Create a new action parameter. Enter a parameter name, parameter ID, and set the interface type to **Toggle**.

   [![Screenshot of configuring an action parameter with the interface type set to toggle.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-toggle-interface-type.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-toggle-interface-type.png#lightbox)
2. Use the `SETLAYOUT` function with `LAYOUT` references to set a specific layout. In this example, you use scripts to switch between table and hierarchy layouts.

   [![Screenshot of the on-state script to set the layout to table and the off state script to switch to hierarchy.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/layout-toggle-scripts-table-hierarchy.png)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/layout-toggle-scripts-table-hierarchy.png#lightbox)
3. Enable the switch to change the layout to table and disable it to switch back to the hierarchy layout.

   [![Screenshot of using a toggle to switch between hierarchy and table layouts.](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-change-layout.gif)](../../../media/resources/best-practices/parameters/how-to-create-action-parameters/action-parameter-change-layout.gif#lightbox)

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
