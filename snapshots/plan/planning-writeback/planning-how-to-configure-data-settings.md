---
title: "Configure data settings for writeback"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-configure-data-settings](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-writeback/planning-how-to-configure-data-settings) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure data settings for writeback

Summarize this article for me

This article explains how to view all series configurations and select the series to include in writeback. This process defines which data is written back to the destination.

## Select series for writeback

The **Series allowed for Writeback** section of the **Writeback Settings** tab lists all series that are available for writeback. By default, all series are selected.

Clear series that should not be written back to the destination.

[![Screenshot of the Writeback Settings.](../media/planning-writeback/planning-how-to-configure-data-settings/writeback-settings.jpg)](../media/planning-writeback/planning-how-to-configure-data-settings/writeback-settings.jpg#lightbox)

## Show text inputs with HTML formatting

Include HTML content in text data input columns and DAX measures for writeback.

### Configure writeback behavior for HTML content

Control whether HTML content is saved as plain text or with HTML tags during writeback.

1. Go to **Writeback > Settings > Data**.
2. Enable or disable the **Show Text Inputs with HTML Formatting** toggle.

   - When disabled, the content is written back as plain text.
   - When enabled, the content is written back with HTML tags preserved.

   ![Screenshot of the Writeback Settings with the Show Text Inputs with HTML Formatting toggle enabled.](../media/planning-writeback/planning-how-to-configure-data-settings/writeback-settings-dialog-box.png)

### Export HTML content

The **Show Text Inputs with HTML Formatting** toggle controls how HTML content is exported:

- When enabled, HTML content in both text input columns and DAX measures is preserved and rendered correctly in outputs such as PDF exports.
- When disabled, the content is exported as plain text without HTML rendering.

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
