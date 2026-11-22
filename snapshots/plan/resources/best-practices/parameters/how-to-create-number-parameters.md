---
title: "Create number parameters"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-number-parameters](https://learn.microsoft.com/en-us/fabric/iq/plan/resources/best-practices/parameters/how-to-create-number-parameters) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create number parameters

Summarize this article for me

Number parameters pass numeric or percentage values dynamically into conditional formatting rules, calculated measures, or data filters. Use them to interactively adjust values, such as interest rates or thresholds, and see instant updates across reports without manually modifying underlying formulas or filters each time.

## Reference number parameters in formulas

Bind parameters directly into calculated measures to enable interactive "what-if" analysis. To demonstrate this feature, we use the formula: Real Sales = Sales / (1 + i)t

In the formula:

- i is the inflation rate, which you pass as a parameter
- t is the tenure, which you also pass as a parameter
- Sales is a native measure from the semantic model

Follow the steps outlined to create number parameters and use them in a calculated measure.

1. Create a new parameter and set the **Type** to **Number**. This parameter captures the inflation rate.
2. Select **Show as Percentage** to display the inflation rate as a percentage. Planning internally converts it to a numeric value to use in calculations.
3. Enter a unique parameter ID to reference the parameter value in a formula.
4. Under **Interface Options**, select the interface type as **Slider**.
5. Set the minimum and maximum values to ensure users don't set a value outside the allowed range.
6. Set the **Step Increment / Decrement**. This value determines how much the value increases or decreases each time you drag the slider.
7. Select **Show Min/Max Labels** to display the allowed range (configured in step 5) on the slider control.
8. Select **Show Current Value** to display the active slider value above the control. Select **Add**. The following image shows the configuration:

   [![Screenshot of configuring a number parameter to capture the inflation rate.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/inflation-parameter-configuration.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/inflation-parameter-configuration.png#lightbox)
9. Follow the same steps to configure a parameter to capture the tenure but leave **Show as Percentage** cleared so the value represents a number of periods rather than a percentage.
10. For the tenure, set the interface type to **Tiles**. Set **Columns per View** to the total number of tiles to display in one row.

    [![Screenshot of creating a number parameter with a tiles interface to capture the tenure.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/create-tenure-parameter.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/create-tenure-parameter.png#lightbox)

    The following image shows the parameter pane with the inflation rate and tenure:

    [![Screenshot of tenure and inflation rate parameters created with a slider and tile interface.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/inflation-rate-tenure-parameters-created.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/inflation-rate-tenure-parameters-created.png#lightbox)
11. To create a calculated measure, in the **Planning** ribbon, go to **Insert Column** > **Formula**. Enter the formula. Press Ctrl + Spacebar to use IntelliSense to add references to the parameters in the formula.

    [![Screenshot of referencing the tenure and inflation rate parameters in a formula.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/create-real-sales-formula-measure.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/create-real-sales-formula-measure.png#lightbox)
12. Planning recalculates the *RealSales* values dynamically as you change the inflation and tenure parameters.

    [![Animation showing how planning recalculates the formula when changing the inflation rate and tenure parameter values.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameters-formula.gif)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameters-formula.gif#lightbox)

## Rank data by using numeric parameters

Dynamically display top or bottom items by passing numeric parameter values directly into your ranking filters.

1. Create a new parameter and set the **Type** to **Number**. This parameter captures how many ranks to display.
2. Set the interface type to **Tiles** or **Radio** to allow users to select from predefined ranking values.
3. Set the minimum and maximum ranks to display.
4. For radio buttons, define the **Layout Direction** - arrange the radio buttons one below the other or side by side.

   [![Screenshot of number parameter configuration with the interface type set to radio button and layout direction set to vertical.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-ranking-configuration-planning-sheet.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-ranking-configuration-planning-sheet.png#lightbox)

   The following image shows the number parameter created with a radio button interface.

   [![Screenshot of a number parameter created with a radio button interface.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-ranking-parameter-created-planning-sheet.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-ranking-parameter-created-planning-sheet.png#lightbox)
5. In the **Planning** ribbon of your planning sheet, select **Tools** > **TopN**.
6. Select the parameter in the TopN configuration.

   [![Screenshot of selecting the ranking parameter in the topN configuration in the planning sheet.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-ranking-configure-top-n.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-ranking-configure-top-n.png#lightbox)
7. Selecting a parameter value automatically ranks the data in the planning sheet.

   [![Animation showing how changing the parameter value applies ranking in the planning sheet.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-change-ranks-planning-sheet.gif)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-change-ranks-planning-sheet.gif#lightbox)

To learn how to configure ranking in intelligence sheets by using parameters, see [Use parameters in intelligence sheets](how-to-configure-parameters?tabs=intelligence-sheets#configure-parameters).

## Enter conditional formatting thresholds

Pass threshold values directly into conditional formatting to automatically highlight key data across your intelligence dashboards without configuring additional rules.

1. Create a number parameter to pass the threshold value. In this example, use parameters to drive the conditional formatting for *Profit Margin* in the chart visuals and *Sales Amount* in the matrix visual.
2. Set the interface type. In this example, use a slider.

   [![Screenshot of configuring a number parameter with a slider interface.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-configuration-threshold-intelligence.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-configuration-threshold-intelligence.png#lightbox)
3. In your intelligence visual, select **Conditional Formatting** > **Create Rule**.
4. In the side pane, set **Format by** to **Rules (If Conditions)**.
5. Reference the defined parameter in your conditional formatting rule. In this example, the rule highlights the categories when the *Profit Margin* falls below the threshold value set in the slider parameter.

   [![Screenshot of configuring a conditional formatting rule to reference the threshold parameter.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-conditional-formatting-intelligence-rule.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-conditional-formatting-intelligence-rule.png#lightbox)
6. Create a second number parameter to highlight the *Sales Amount* in the matrix visual when the amount falls below the entered threshold value. Refer to the configuration shown in the following screenshot.

   [![Screenshot of creating a parameter to capture the threshold for sales amount.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-threshold-sales-amount.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-threshold-sales-amount.png#lightbox)
7. In the **Matrix** tab of the visual, go to **Conditional Formatting** > **Create Rule** and configure the rule to reference the parameter created in step 6.

   [![Screenshot of configuring a conditional formatting rule that references the threshold parameter.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-conditional-formatting-matrix.png)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-conditional-formatting-matrix.png#lightbox)

   The chart categories and matrix data are highlighted based on the parameter values.

   [![Animation showing how changing the threshold parameters applies formatting to the dashboard.](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-conditional-formatting-intelligence.gif)](../../../media/resources/best-practices/parameters/how-to-create-number-parameters/number-parameter-conditional-formatting-intelligence.gif#lightbox)

To learn how to configure conditional formatting in planning sheets by using parameters, see [Use parameters in planning sheets](how-to-configure-parameters?tabs=planning-sheets#configure-parameters).

## Best practices for selecting the UI control

- Use sliders when visual exploration matters more than entering an exact decimal point (for example, "What if sales drop 5%?").
- Use input boxes when users need precise control or need to enter values outside a fixed range.
- Use tiles or radio buttons when business rules require planners to pick from a specific set of allowed standard values rather than arbitrary numbers.

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
