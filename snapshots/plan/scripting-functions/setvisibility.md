---
title: "SETVISIBILITY"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setvisibility](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setvisibility) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SETVISIBILITY

Summarize this article for me

Use SETVISIBILITY to show or hide one or more measures in a planning sheet. Use this function in a parameter action to switch between measures, such as showing actual values or plan values.

## Syntax

```
SETVISIBILITY(measure, boolean)
```

## Parameters

The SETVISIBILITY function uses the following parameters to control the visibility of measures in a planning sheet.

| Parameter | Description |
| --- | --- |
| measure | The measure to show or hide. Select the relevant measure from the available references. |
| boolean | A Boolean value that specifies whether to show or hide the measure. Use TRUE to show the measure and FALSE to hide it. |

## Example

Use a toggle parameter to switch between the Actuals and Plan measures in a planning sheet. Configure the parameter actions as follows.

1. Create a parameter and set **Interface Type** to **Toggle**.
2. Enable **Enable Script**.
3. Set **Default State** to **Show Actuals**.
4. In **On State Configuration**, set **Label** to **Show Actuals**. Set **Apply to** to **Planning**, and enter the following formulas in **Formula Script**:

   ```
   SETVISIBILITY(Actuals_M_11925419800285133932, true)
   SETVISIBILITY(Plan_M_16435073439253070543, false)
   ```

   [![Screenshot of the On State Configuration for the Show Actuals toggle, showing the Actuals measure set to visible and the Plan measure set to hidden.](../media/scripting-functions/setvisibility/setvisibility-configuration-on.png)](../media/scripting-functions/setvisibility/setvisibility-configuration-on.png#lightbox)
5. In **Off State Configuration**, set **Label** to **Show Plan**. Set **Apply to** to **Planning**, and enter the following formulas in **Formula Script**:

   ```
   SETVISIBILITY(Actuals_M_11925419800285133932, false)
   SETVISIBILITY(Plan_M_16435073439253070543, true)
   ```

   [![Screenshot of the Off State Configuration for the Show Plan toggle, showing the Actuals measure set to hidden and the Plan measure set to visible.](../media/scripting-functions/setvisibility/setvisibility-configuration-off.png)](../media/scripting-functions/setvisibility/setvisibility-configuration-off.png#lightbox)
6. Save the parameter.

   When the toggle is set to **Show Actuals**, the sheet displays the Actuals measure and hides the Plan measure.

   [![Screenshot of the planning sheet displaying the Actuals measure while the Plan measure is hidden.](../media/scripting-functions/setvisibility/setvisibility-result-actuals.png)](../media/scripting-functions/setvisibility/setvisibility-result-actuals.png#lightbox)

   When the toggle is set to **Show Plan**, the sheet displays the Plan measure and hides the Actuals measure.

   [![Screenshot of the planning sheet displaying the Plan measure while the Actuals measure is hidden.](../media/scripting-functions/setvisibility/setvisibility-result-plan.png)](../media/scripting-functions/setvisibility/setvisibility-result-plan.png#lightbox)

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
