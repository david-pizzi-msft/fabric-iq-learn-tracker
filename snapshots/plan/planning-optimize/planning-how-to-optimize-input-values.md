---
title: "Optimize input values to meet a target"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-optimize/planning-how-to-optimize-input-values](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-optimize/planning-how-to-optimize-input-values) · Last updated on **2026-08-12**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Optimize input values to meet a target

Summarize this article for me

Use target-based optimization to determine the input values required to achieve a specific business objective, such as a revenue target. Optimize recalculates one or more selected input measures and updates them with the values needed to achieve the specified result.

## Prerequisites

Before you begin, review the [Prerequisites section for Optimize](optimizer-overview#prerequisites) to understand the initial setup requirements.

## Achieve a target value on a calculated field

To demonstrate target-based optimization, set a target for the calculated field *Profit forecast* by optimizing independent variables - *Revenue Forecast*, *Purchase Forecast*, *Advertising Forecast*, and *Transport Forecast*.

Note

You can optimize values at any hierarchy level. In this example, optimize at the total level. When Optimize runs on a parent cell, it recalculates the required change and distributes the updated value to the underlying editable child cells.

1. Select the target cell in the calculated measure. In the **Planning** ribbon, select **Optimize**. In this example, select the target cell from the *Profit Forecast* measure.

   [![Screenshot of a calculated measure and formula used as the dependent measure to optimize.](../media/planning-optimize/planning-how-to-optimize-input-values/calculated-measure-optimize-formula.png)](../media/planning-optimize/planning-how-to-optimize-input-values/calculated-measure-optimize-formula.png#lightbox)
2. To achieve a specific target, set **Objective** to **Target** and enter the target value. In this example, set the target value to 45m.

   [![Screenshot of setting the optimize objective to maximize.](../media/planning-optimize/planning-how-to-optimize-input-values/target-maximize-minimize-objective.png)](../media/planning-optimize/planning-how-to-optimize-input-values/target-maximize-minimize-objective.png#lightbox)
3. Select the data input or forecast measures (independent variables) to optimize from **Variables to Update**. In this case, Optimize adjusts the *Revenue Forecast*, *Purchase Forecast*, *Advertising Forecast*, and *Transport Forecast* to achieve the target *Profit Forecast*. Select **Next**.

   [![Screenshot of selecting the independent measures to optimize.](../media/planning-optimize/planning-how-to-optimize-input-values/select-independent-variables-optimize.png)](../media/planning-optimize/planning-how-to-optimize-input-values/select-independent-variables-optimize.png#lightbox)
4. Select **Add Constraint** to define the minimum and maximum limits for the data input measure. For more information, see [Configure optimization thresholds](https://docs.fabricplan.com/documentation/readme/planning-sheets/how-tos/optimize-overview#configure-optimization-thresholds).

   Tip

   Adding constraints is optional. Directly select **Run** to skip defining constraints; however, as a best practice, explicitly specify constraints for all the independent measures used in Optimize.
5. Choose the measure to apply the constraint from **Apply to Variable**. Select **Range** for the **Set Type** option. Enter the minimum and maximum optimization thresholds.

   [![Screenshot of adding a range constraint to independent measures. ](../media/planning-optimize/planning-how-to-optimize-input-values/add-range-constraint-independent-measure.png)](../media/planning-optimize/planning-how-to-optimize-input-values/add-range-constraint-independent-measure.png#lightbox)
6. Select **Apply**. Select **Add** to specify additional constraints. Select **Run** after you define all the constraints.

   [![Screenshot of adding multiple constraints for each independent measure in Optimize.](../media/planning-optimize/planning-how-to-optimize-input-values/add-multiple-optimize-constraints.png)](../media/planning-optimize/planning-how-to-optimize-input-values/add-multiple-optimize-constraints.png#lightbox)
7. Review the adjusted values, then select **Apply** to update the independent measures with the optimized values. For more information about Optimize parameters, see [Adjust parameters to achieve targets](optimizer-overview#adjust-parameters-to-achieve-targets)

   [![Screenshot of maximized target value and optimized independent values.](../media/planning-optimize/planning-how-to-optimize-input-values/optimize-target-profit-forecast-value-achieved.png)](../media/planning-optimize/planning-how-to-optimize-input-values/optimize-target-profit-forecast-value-achieved.png#lightbox)
8. Optimize increases the *Profit Forecast* to 45m from 43.92m after adjusting independent measures within the specified constraints. Since you applied Optimize to a total value, the update cascades to all the related child dimensions.

   Note

   Optimize doesn't change the values of locked cells. The target value is maximized or minimized by adjusting the values of editable cells.

   [![Screenshot of applying the optimized values and updating the measures in the planning sheet.](../media/planning-optimize/planning-how-to-optimize-input-values/optimized-values-applied-measures-updated.png)](../media/planning-optimize/planning-how-to-optimize-input-values/optimized-values-applied-measures-updated.png#lightbox)

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
