---
title: "Hide visuals using scripting functions"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/hide-visual](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/hide-visual) · Last updated on **2026-11-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Hide visuals using scripting functions

Summarize this article for me

Use the HIDE\_VISUAL function to hide a visual or visual group in an intelligence sheet. For example, configure a toggle parameter that lets users hide a visual when they turn the toggle off.

## Syntax

Use the following syntax to hide a visual or visual group.

```
HIDE_VISUAL(visualLabel)
```

Replace visualLabel with the label of the visual or visual group you want to hide. When you reference a visual by its label, use the visual reference syntax supported by the intelligence sheet.

## Example

The following example uses a toggle parameter to control the visibility of a visual named Overlapped column@6 in an intelligence sheet. When the toggle is off, the HIDE\_VISUAL function hides the visual. The example also uses SHOW\_VISUAL in the toggle's on action so users can display the visual again.

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

   [![Screenshot of the action parameter configuration with SHOW_VISUAL and HIDE_VISUAL actions for the Overlapped column visual.](../media/scripting-functions/hide-visual/hide-visual-configuration.png)](../media/scripting-functions/hide-visual/hide-visual-configuration.png#lightbox)

### Test the toggle

Open the **Parameter** pane and turn the toggle off to run HIDE\_VISUAL and hide the specified visual. Turn the toggle on to run SHOW\_VISUAL and display the visual again.

[![Screenshot of the intelligence sheet with the specified visual hidden while the Show Visual toggle is off.](../media/scripting-functions/hide-visual/hide-visual-hide.png)](../media/scripting-functions/hide-visual/hide-visual-hide.png#lightbox)

[![Screenshot of the intelligence sheet with the specified visual displayed while the Show Visual toggle is on.](../media/scripting-functions/hide-visual/hide-visual-show.png)](../media/scripting-functions/hide-visual/hide-visual-show.png#lightbox)

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
