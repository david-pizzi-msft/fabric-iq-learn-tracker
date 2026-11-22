---
title: "SHOWCLOSEDFORECAST"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/showclosedforecast](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/showclosedforecast) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SHOWCLOSEDFORECAST

Summarize this article for me

Use SHOWCLOSEDFORECAST to show or hide forecast values for closed periods in a planning sheet.

## Syntax

```
SHOWCLOSEDFORECAST(boolean)
```

## Parameters

The following parameter controls whether the planning sheet displays forecast values for closed periods. Set the Boolean value to TRUE to show the values or FALSE to hide them.

| Parameter | Description |
| --- | --- |
| boolean | Specifies whether to show forecast values for closed periods. Use TRUE to show closed forecast values or FALSE to hide them. |

## Example

The following example configures a toggle parameter that lets users show or hide forecast values for closed periods.

1. Open the planning sheet and select **Add new** in the **Parameter** pane.
2. In **Type**, select **Action**.
3. Enter a name, such as **Show closed forecast**. The parameter ID is **SHOWCLOSEDFORECAST**.
4. In **Description**, enter a brief explanation, such as: Show or hide forecast values for closed periods in the planning sheet.
5. Under **Interface Options**, set **Interface Type** to **Toggle**.
6. Enable **Enable Script**.
7. Under **Default State**, select **Show closed forecast**.
8. Configure the on state:

   1. Set **Label** to **Show closed forecast**.
   2. Set **Apply to** to **Planning**.
   3. Enter the following formula in **Formula Script**:

      ```
      SHOWCLOSEDFORECAST(TRUE)
      ```

      [![Screenshot of the on state configuration for the Show closed forecast toggle, with SHOWCLOSEDFORECAST(TRUE) in the formula script.](../media/scripting-functions/showclosedforecast/showclosedforecast-configuration-on.png)](../media/scripting-functions/showclosedforecast/showclosedforecast-configuration-on.png#lightbox)
9. Configure the off state:

   1. Set **Label** to **Hide closed forecast**.
   2. Set **Apply to** to **Planning**.
   3. Enter the following formula in **Formula Script**:

      ```
      SHOWCLOSEDFORECAST(FALSE)
      ```

      [![Screenshot of the off state configuration for the Show closed forecast toggle, with SHOWCLOSEDFORECAST(FALSE) in the formula script.](../media/scripting-functions/showclosedforecast/showclosedforecast-configuration-off.png)](../media/scripting-functions/showclosedforecast/showclosedforecast-configuration-off.png#lightbox)
10. Select **Save** to save the parameter configuration.
11. In the parameter settings, select **Include in read mode** if users must be able to use the toggle in read mode.
12. Select **Update**, and then save the planning sheet.

## Results

When the toggle is on, the planning sheet displays forecast values for closed periods.

[![Screenshot of the planning sheet showing forecast values for closed periods when the Show closed forecast toggle is on.](../media/scripting-functions/showclosedforecast/showclosedforecast-result-on.png)](../media/scripting-functions/showclosedforecast/showclosedforecast-result-on.png#lightbox)

When the toggle is off, the planning sheet hides forecast values for closed periods.

[![Screenshot of the planning sheet with forecast values for closed periods hidden when the Hide closed forecast toggle is on.](../media/scripting-functions/showclosedforecast/showclosedforecast-result-off.png)](../media/scripting-functions/showclosedforecast/showclosedforecast-result-off.png#lightbox)

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
