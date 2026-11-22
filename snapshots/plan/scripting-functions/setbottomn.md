---
title: "SETBOTTOMN"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setbottomn](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/setbottomn) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SETBOTTOMN

Summarize this article for me

Use SETBOTTOMN to display the bottom N records for a category in a planning sheet. Configure the function in a parameter action to let users switch between different bottom-N views.

## Syntax

```
SETBOTTOMN(category, number, boolean)
```

## Parameters

The following table describes the parameters that the SETBOTTOMN function accepts.

| Parameter | Description |
| --- | --- |
| category | The category to rank and filter. Select the relevant category field from the available references. |
| number | The number of bottom records to display. For example, use 1 to display the lowest-ranked record or 3 to display the bottom three records. |
| boolean | A Boolean value that enables or disables bottom-N ranking. Use TRUE to enable ranking and FALSE to disable ranking. |

## Example

Use a toggle parameter to switch between the bottom one and bottom three records for the Sub-Category category in a planning sheet. Configure the parameter actions as follows.

1. Create a parameter and set **Type** to **Action**.
2. Enter a name, such as **Set Bottom N**.
3. Set **Interface Type** to **Toggle** and select **Enable Script**.
4. In **On State Configuration**, set **Label** to **Bottom 1**. Set **Apply to** to **Planning**, and enter the following formula in **Formula Script**:

   ```
   SETBOTTOMN(Sub_Category_D_13871156346345963805, 1, TRUE)
   ```

   [![Screenshot of the On State Configuration for the Set Bottom N parameter, with the label Bottom 1 and a SETBOTTOMN formula that displays the bottom record.](../media/scripting-functions/setbottomn/setbottomn-configuration-on.png)](../media/scripting-functions/setbottomn/setbottomn-configuration-on.png#lightbox)
5. In **Off State Configuration**, set **Label** to **Bottom 3**. Set **Apply to** to **Planning**, and enter the following formula in **Formula Script**:

   ```
   SETBOTTOMN(Sub_Category_D_13871156346345963805, 3, TRUE)
   ```

   [![Screenshot of the Off State Configuration for the Set Bottom N parameter, with the label Bottom 3 and a SETBOTTOMN formula that displays the bottom three records.](../media/scripting-functions/setbottomn/setbottomn-configuration-off.png)](../media/scripting-functions/setbottomn/setbottomn-configuration-off.png#lightbox)
6. Set **Default State** to **Bottom 1**, and save the parameter.

   When the toggle is set to **Bottom 1**, the planning sheet displays the lowest-ranked subcategory records within each parent category.

   [![Screenshot of a planning sheet displaying the bottom one subcategory record within each parent category.](../media/scripting-functions/setbottomn/setbottomn-result-on.png)](../media/scripting-functions/setbottomn/setbottomn-result-on.png#lightbox)

   When the toggle is set to **Bottom 3**, the planning sheet displays the three lowest-ranked subcategory records within each parent category.

   [![Screenshot of a planning sheet displaying the bottom three subcategory records within each parent category.](../media/scripting-functions/setbottomn/setbottomn-result-off.png)](../media/scripting-functions/setbottomn/setbottomn-result-off.png#lightbox)

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
