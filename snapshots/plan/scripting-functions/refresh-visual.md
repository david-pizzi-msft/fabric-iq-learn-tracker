---
title: "REFRESH VISUAL"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/refresh-visual](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/refresh-visual) · Last updated on **2026-11-10**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# REFRESH VISUAL

Summarize this article for me

Use the REFRESH\_VISUAL function to refresh a specific visual in an intelligence sheet. For example, configure a button that refreshes a visual.

## Syntax

The following syntax refreshes a specific visual.

```
REFRESH_VISUAL(visuals.visualLabel)
```

Replace visualLabel with the reference to the visual you want to refresh.

## Example

The following example refreshes the visual named Overlapped column in an intelligence sheet.

```
REFRESH_VISUAL(visuals."Overlapped column@6")
```

## Configure a button to refresh a visual

1. Open the intelligence sheet and create or edit an action parameter.
2. Set **Type** to **Action**.
3. Enter a name, such as Refresh Visual.
4. In **Description**, explain what the action does. For example, enter: Refreshes the specified visual when the user selects the button.
5. Under **Interface Options**, set **Interface Type** to **Button**.
6. Select **Enable Script**.
7. Under **Button Configuration**, set **Label** to Refresh.
8. Add an action, set the action scope to Root, and enter the following formula script:

   ```
   REFRESH_VISUAL(visuals."Overlapped column@6")
   ```
9. Save the button configuration, and then select **Update**.

   [![Screenshot of the button configuration for the REFRESH_VISUAL function in an intelligence sheet.](../media/scripting-functions/refresh-visual/refresh-visual-configuration.png)](../media/scripting-functions/refresh-visual/refresh-visual-configuration.png#lightbox)

   When a user selects **Refresh**, the intelligence sheet refreshes the specified visual.

   [![Screenshot of the intelligence sheet after the REFRESH_VISUAL function refreshes the visual.](../media/scripting-functions/refresh-visual/refresh-visual-result.png)](../media/scripting-functions/refresh-visual/refresh-visual-result.png#lightbox)

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
