---
title: "Enable writeback in reading mode"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-enable-writeback-reading-mode](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-enable-writeback-reading-mode) · Last updated on **2026-08-31**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Enable writeback in reading mode

Summarize this article for me

Planning users can perform writeback even when a report is in reading view. You can also review logs from [Logs](#logs) under the **Writeback** tab.

[![Screenshot showing the Writeback ribbon tab with the Writeback and Logs buttons available.](../media/planning-writeback/planning-how-to-enable-writeback-reading-mode/writeback-enable-reading-mode.jpg)](../media/planning-writeback/planning-how-to-enable-writeback-reading-mode/writeback-enable-reading-mode.jpg#lightbox)

## Access the Writeback tab

The **Writeback** tab option is only available when at least one destination is configured and the user has writeback permissions.

The following options are displayed for users in the reading view who also have writeback access:

[![Screenshot showing the available writeback options and report data for authorized users in reading mode.](../media/planning-writeback/planning-how-to-enable-writeback-reading-mode/writeback-with-access.png)](../media/planning-writeback/planning-how-to-enable-writeback-reading-mode/writeback-with-access.png#lightbox)

## Writeback

Select **Writeback** to write report data to the configured destination. Planning respects row-level security (**RLS**) in the source dataset. If a viewer has RLS applied, planning only writes back the rows allowed by that security rule.

## Logs

Select **Logs** to open the writeback logs page.

[![Screenshot of the writeback logs interface displaying a table of past writeback events, durations, and statuses.](../media/planning-writeback/planning-how-to-enable-writeback-reading-mode/writeback-logs.png)](../media/planning-writeback/planning-how-to-enable-writeback-reading-mode/writeback-logs.png#lightbox)

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
