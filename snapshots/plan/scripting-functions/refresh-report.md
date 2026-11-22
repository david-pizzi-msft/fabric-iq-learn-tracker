---
title: "REFRESH_REPORT function"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/refresh-report](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/refresh-report) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# REFRESH\_REPORT function

Summarize this article for me

Use the REFRESH\_REPORT function to refresh the entire report when a user runs a script in a planning item. For example, configure a button that refreshes the report when a user selects it.

## Syntax

The following syntax refreshes the entire report.

```
REFRESH_REPORT()
```

## Example

The following example configures a button that refreshes the report when a user selects it.

```
REFRESH_REPORT()
```

### Configure a button to refresh a report

1. Open the planning item and create or edit an action parameter.
2. In the **Edit Parameter** pane, set **Type** to **Action**, enter a name such as **Refresh Report**, and provide a description such as **Refreshes the report when a user selects the button.**
3. Under **Interface Options**, set **Interface Type** to **Button** and select **Enable Script**.
4. Under **Button Configuration**, set **Label** to **Refresh**.
5. Add an action, set **Apply to** to **Root**, and enter `REFRESH_REPORT()` in **Formula Script**.
6. Select **Save** in the **Button State Configuration** window, and then select **Update** in the **Edit Parameter** pane.
7. In the **Parameter** pane, select **Refresh** to run the script and refresh the report.

[![Screenshot of the Button State Configuration window with REFRESH_REPORT() entered in Formula Script and the Refresh button configured in the Edit Parameter pane.](../media/scripting-functions/refresh-report/refresh-report-configuration.png)](../media/scripting-functions/refresh-report/refresh-report-configuration.png#lightbox)

After you select the **Refresh** button, the report refreshes and the updated data appears in the report.

[![Screenshot of the planning item after the Refresh button runs REFRESH_REPORT() and the report displays refreshed data.](../media/scripting-functions/refresh-report/refresh-report-result.png)](../media/scripting-functions/refresh-report/refresh-report-result.png#lightbox)

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
