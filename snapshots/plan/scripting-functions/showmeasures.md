---
title: "Show or hide measures using scripting functions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/showmeasures](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/showmeasures) · Last updated on **2026-11-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Show or hide measures using scripting functions

Summarize this article for me

Use the SHOWMEASURES function to show or hide all measures in a planning sheet. Pass TRUE to show the measures or FALSE to hide them.

## Syntax

Use the following syntax to show or hide measures.

```
SHOWMEASURES(TRUE)
```

To hide all measures, use the following formula:

```
SHOWMEASURES(FALSE)
```

## Example

The following example uses a toggle parameter to show or hide all measures in a planning sheet. When the toggle is on, the SHOWMEASURES function displays the measures. When the toggle is off, the function hides the measures.

### Configure a toggle parameter

1. In the planning sheet, create an **Action** parameter named **Show Measures**.
2. Set the **Interface Type** to **Toggle** and select **Enable Script**.
3. Under **On Actions**, add a planning action and enter the following formula in **Formula Script**:

   ```
   SHOWMEASURES(TRUE)
   ```

   [![Screenshot of the On State Configuration dialog with SHOWMEASURES(TRUE) entered in Formula Script.](../media/scripting-functions/showmeasures/showmeasures-configuration-on.png)](../media/scripting-functions/showmeasures/showmeasures-configuration-on.png#lightbox)
4. Under **Off Actions**, add a planning action and enter the following formula in **Formula Script**:

   ```
   SHOWMEASURES(FALSE)
   ```

   [![Screenshot of the Off State Configuration dialog with SHOWMEASURES(FALSE) entered in Formula Script.](../media/scripting-functions/showmeasures/showmeasures-configuration-off.png)](../media/scripting-functions/showmeasures/showmeasures-configuration-off.png#lightbox)
5. Set **Default State** to **Show Measures**.
6. Save the parameter.

### Test the toggle

Open the **Parameter** pane and switch the toggle between **Show Measures** and **Hide Measures**.

- When the toggle is on, the planning sheet displays all measures.

  [![Screenshot of the planning sheet displaying all measures when the Show Measures toggle is on.](../media/scripting-functions/showmeasures/showmeasures-result-on.png)](../media/scripting-functions/showmeasures/showmeasures-result-on.png#lightbox)
- When the toggle is off, the planning sheet hides all measures while retaining the row hierarchy.

  [![Screenshot of the planning sheet with all measures hidden and the row hierarchy still visible when the Show Measures toggle is off.](../media/scripting-functions/showmeasures/showmeasures-result-off.png)](../media/scripting-functions/showmeasures/showmeasures-result-off.png#lightbox)

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
