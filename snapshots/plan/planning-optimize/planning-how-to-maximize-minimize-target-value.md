---
title: "Maximize or minimize a target value"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-optimize/planning-how-to-maximize-minimize-target-value](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-optimize/planning-how-to-maximize-minimize-target-value) · Last updated on **2026-08-12**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Maximize or minimize a target value

Summarize this article for me

Direction-based optimization adjusts one or more data input measures to maximize or minimize the selected objective measure while satisfying the defined constraints.

## Prerequisites

Before you begin, review the [Prerequisites section for Optimize](optimizer-overview#prerequisites) to understand the initial setup requirements.

## Maximize a calculated field

To demonstrate direction-based optimization, maximize the calculated field *Profit forecast* by optimizing independent variables - *Revenue Forecast*, *Purchase Forecast*, *Advertising Forecast*, and *Transport Forecast*.

Note

You can optimize values at any hierarchy level. In this example, optimize at the total level. When Optimize runs on a parent cell, it recalculates the required change and distributes the updated value to the underlying editable child cells.

1. Select the target cell in the calculated measure. In the **Planning** ribbon, select **Optimize**. In this example, select the target cell from the *Profit Forecast* measure.

   [![Screenshot of a calculated measure and formula used as the dependent measure to optimize.](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/calculated-measure-optimize-formula.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/calculated-measure-optimize-formula.png#lightbox)
2. To achieve direction-based optimization,

   - Set **Objective** to **Maximize** to achieve the highest possible value. For example, maximize revenue, profit, or return on investment.
   - Set **Objective** to **Minimize** to achieve the lowest possible value. For example, minimize cost, expenses, or inventory holding costs.
     In this example, set the **Objective** to **Maximize** to arrive at the maximum *Profit Forecast*.

   [![Screenshot of setting the optimize objective to maximize.](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/target-maximize-minimize-objective.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/target-maximize-minimize-objective.png#lightbox)
3. Select the data input or forecast measures (independent variables) to optimize from **Variables to Update**. In this case, Optimize adjusts the *Revenue Forecast*, *Purchase Forecast*, *Advertising Forecast*, and *Transport Forecast* to maximize the *Profit Forecast*. Select **Next**.

   [![Screenshot of selecting the independent measures to optimize.](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/select-independent-variables-optimize.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/select-independent-variables-optimize.png#lightbox)
4. Select **Add Constraint** to define the minimum and maximum limits for the data input measure. For more information, see [Configure optimization thresholds](optimizer-overview#configure-optimization-thresholds).

   Tip

   Adding constraints is optional. Directly select **Run** to skip defining constraints; however, as a best practice, explicitly specify constraints for all the independent measures used in Optimize.
5. Choose the measure to apply the constraint from **Apply to Variable**. Select **Range** for the **Set Type** option. Enter the minimum and maximum optimization thresholds.

   [![Screenshot of adding a range constraint to independent measures. ](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/add-range-constraint-independent-measure.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/add-range-constraint-independent-measure.png#lightbox)
6. Select **Apply**. Select **Add** to specify additional constraints. Select **Run** after you define all the constraints.

   [![Screenshot of adding multiple constraints for each independent measure in Optimize.](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/add-multiple-optimize-constraints.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/add-multiple-optimize-constraints.png#lightbox)
7. Review the adjusted values and select **Apply** to update the values of the independent measures. For more information about Optimize parameters, see [Adjust parameters to achieve targets](optimizer-overview#adjust-parameters-to-achieve-targets).

   [![Screenshot of maximized target value and optimized independent values.](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/optimize-maximized-profit-forecast-values.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/optimize-maximized-profit-forecast-values.png#lightbox)
8. Optimize increases the *Profit Forecast* to 50.46m from 43.92m after adjusting independent measures within the specified constraints. Since you applied Optimize on a total value, the update cascades to all the related child dimensions.

   Note

   Optimize doesn't change the values of locked cells. The target value is maximized or minimized by adjusting the values of editable cells.

   [![Screenshot of applying the optimized values and updating the measures in the planning sheet.](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/optimized-values-applied-measures-updated.png)](../media/planning-optimize/planning-how-to-maximize-minimize-target-value/optimized-values-applied-measures-updated.png#lightbox)

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
