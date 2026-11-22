---
title: "Show visuals using scripting functions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/show-visual](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/show-visual) · Last updated on **2026-11-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Show visuals using scripting functions

Summarize this article for me

Use the SHOW\_VISUAL function to show a visual or visual group in an intelligence sheet. For example, configure a toggle parameter that lets users display a visual when they turn the toggle on.

## Syntax

Use the following syntax to show a visual or visual group.

```
SHOW_VISUAL(visualLabel)
```

Replace visualLabel with the label of the visual or visual group you want to show. When you reference a visual by its label, use the visual reference syntax supported by the intelligence sheet.

## Example

The following example uses a toggle parameter to control the visibility of a visual named Overlapped column@6 in an intelligence sheet. When the toggle is on, the SHOW\_VISUAL function displays the visual. The example also uses HIDE\_VISUAL in the toggle's off action so users can hide the visual again.

### Configure a toggle parameter

1. Open the intelligence sheet and create or edit an action parameter.
2. Set **Interface Type** to **Toggle**.
3. Enable **Enable Script**.
4. Set **Default State** to **Hide**.
5. Under **On Actions**, add an action, set **Apply to** to **Root**, and enter the following formula in **Formula Script**.

   ```
   SHOW_VISUAL(visuals."Overlapped column@6")
   ```
6. Under **Off Actions**, add an action, set **Apply to** to **Root**, and enter the following formula in **Formula Script**.

   ```
   HIDE_VISUAL(visuals."Overlapped column@6")
   ```
7. Save the action parameter.

   [![Screenshot of the action parameter configuration with SHOW_VISUAL and HIDE_VISUAL actions for the Overlapped column visual.](../media/scripting-functions/show-visual/show-visual-configuration.png)](../media/scripting-functions/show-visual/show-visual-configuration.png#lightbox)

### Test the toggle

Open the **Parameter** pane and turn the toggle on to run SHOW\_VISUAL and display the specified visual. Turn the toggle off to run HIDE\_VISUAL and hide the visual again.

[![Screenshot of the intelligence sheet with the specified visual hidden while the Show Visual toggle is off.](../media/scripting-functions/show-visual/show-visual-hidden.png)](../media/scripting-functions/show-visual/show-visual-hidden.png#lightbox)

[![Screenshot of the intelligence sheet with the specified visual displayed while the Show Visual toggle is on.](../media/scripting-functions/show-visual/show-visual-shown.png)](../media/scripting-functions/show-visual/show-visual-shown.png#lightbox)

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
