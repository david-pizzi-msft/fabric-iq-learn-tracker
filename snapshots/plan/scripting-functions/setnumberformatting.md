---
title: "SETNUMBERFORMATTING"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setnumberformatting](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setnumberformatting) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SETNUMBERFORMATTING

Summarize this article for me

Use SETNUMBERFORMATTING to switch the number formatting applied to values in a planning sheet. The function supports four formatting modes: Native, Uniform, Measure Level, and Auto.

## Syntax

The following example switches the planning sheet to uniform number formatting.

```
SETNUMBERFORMATTING(NUMBERFORMATTING.UNIFORM)
```

## Parameters

| Parameter | Description |
| --- | --- |
| NUMBERFORMATTING.NATIVE | Uses the native number formatting behavior. |
| NUMBERFORMATTING.UNIFORM | Applies uniform number formatting to values in the planning sheet. |
| NUMBERFORMATTING.MEASURELEVEL | Uses the number formatting configured for each measure. |
| NUMBERFORMATTING.AUTO | Uses automatic number formatting. |

The function accepts one formatting mode from the NUMBERFORMATTING reference. Select the mode that matches how you want values to appear in the planning sheet.

## Example

Create a parameter that lets users switch between uniform number formatting and measure-level number formatting.

1. Open the planning sheet.
2. Open the **Parameters** pane and create a new parameter.
3. Set **Type** to **Action**.
4. Enter a name, such as **Choose Number Format**.
5. Set **Interface Type** to **Toggle**.
6. Enable **Enable Script**.
7. Set **Default State** to **Uniform**.
8. Add an action for each toggle state.

   For the **On** state, set the label to **Uniform** and enter the following formula in **Formula Script**:

   ```
   SETNUMBERFORMATTING(NUMBERFORMATTING.UNIFORM)
   ```

   [![Screenshot of the On State Configuration with Uniform selected and the SETNUMBERFORMATTING formula.](../media/scripting-functions/setnumberformatting/setnumberformatting-configuration-on.png)](../media/scripting-functions/setnumberformatting/setnumberformatting-configuration-on.png#lightbox)

   For the **Off** state, set the label to **Measure level** and enter the following formula in **Formula Script**:

   ```
   SETNUMBERFORMATTING(NUMBERFORMATTING.MEASURELEVEL)
   ```

   [![Screenshot of the Off State Configuration with Measure level selected and the SETNUMBERFORMATTING formula.](../media/scripting-functions/setnumberformatting/setnumberformatting-configuration-off.png)](../media/scripting-functions/setnumberformatting/setnumberformatting-configuration-off.png#lightbox)
9. Select **Include in read mode** if users must be able to switch the formatting mode in read mode.
10. Save the parameter and update the planning sheet.

    When the toggle is on, the planning sheet uses uniform number formatting. In the example, the values are displayed to one decimal place.

    [![Screenshot of the planning sheet with Uniform number formatting enabled and values displayed to one decimal place.](../media/scripting-functions/setnumberformatting/setnumberformatting-result-uniform.png)](../media/scripting-functions/setnumberformatting/setnumberformatting-result-uniform.png#lightbox)

    When the toggle is off, the planning sheet uses the number formatting configured at the measure level. In the example, the values retain two decimal places and the measure headers include the unit label.

    [![Screenshot of the planning sheet with Measure level number formatting enabled and values displayed to two decimal places.](../media/scripting-functions/setnumberformatting/setnumberformatting-result-mesaure-level.png)](../media/scripting-functions/setnumberformatting/setnumberformatting-result-mesaure-level.png#lightbox)

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
