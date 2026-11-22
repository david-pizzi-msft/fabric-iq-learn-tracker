---
title: "Extract comments in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-extract-comments](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-extract-comments) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Extract comments in Infobridge

Summarize this article for me

Use the **Extract Comments** transformation to extract cell-level comments and related metadata into your query. The extracted information helps preserve business context and collaboration details for downstream reporting and analysis.

## About extracting comments

The **Extract Comments** transformation adds the comment text together with metadata such as the user who updated the comment, the date, and time the comment was added, the thread status, and the assigned user.

You can find the **Extract Comments** transformation on the **Transform** tab.

## Extract comments

On the **Transform** tab, select **Extract Comments**.

[![Screenshot highlighting the Extract Comments command on the Transform tab.](../media/infobridge-transformations/infobridge-how-to-extract-comments/extract-comments-command.png)](../media/infobridge-transformations/infobridge-how-to-extract-comments/extract-comments-command.png#lightbox)

After the transformation completes, Infobridge adds the following columns to the query:

- **comment**: Shows the extracted comment text.
- **updatedByUser**: Shows the user who last updated the comment.
- **dateTime**: Shows the date and time when the comment was added or last updated.
- **threadStatus**: Shows the current status of the comment thread.
- **threadAssignedId**: Shows the user assigned to the comment thread.

[![Screenshot showing the comment, updatedByUser, dateTime, threadStatus, and threadAssignedId columns added to the query after applying the Extract Comments transformation.](../media/infobridge-transformations/infobridge-how-to-extract-comments/extracted-comments.png)](../media/infobridge-transformations/infobridge-how-to-extract-comments/extracted-comments.png#lightbox)

Continue transforming the query, or write the extracted comments and metadata to a destination.

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
