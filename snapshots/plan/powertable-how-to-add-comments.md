---
title: "Comment and collaborate in PowerTable"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-add-comments](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-add-comments) · Last updated on **2026-07-28**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Comment and collaborate in PowerTable

Summarize this article for me

By using the commenting and collaboration features, you can add contextual discussions directly within the PowerTable sheet. Use these capabilities with your team to collaborate, review data, provide feedback, assign tasks, and track discussions all within the table.

## Prerequisites

- A PowerTable sheet with the required data table.
- You have appropriate [user permissions](#configure-comment-access) to create, reply to, or manage comments.

## Add comments

Use comments to add context or discussions to a specific **cell**, **row**, or **column** in the table.

Note

To add row-level comments, set up the [comments column](#add-comments-column).

To add a comment to a cell or a column,

1. Select the **cell** or **column** where you want to add a comment.
2. Select **Comments** from the toolbar or **Add new comment** from the **Comments** dropdown.

   [![Screenshot of the Comments menu highlighted in the PowerTable ribbon, with Add new comment selected and a ModelName cell selected in the grid.](media/powertable-how-to-add-comments/add-new-comments.png)](media/powertable-how-to-add-comments/add-new-comments.png#lightbox)
3. Enter the comment in the **comment editor**.
4. Apply text formatting, such as bold, italic, or underline, by using the standard keyboard shortcuts **Ctrl+B**, **Ctrl+I**, and **Ctrl+U**.

   [![Screenshot of the PowerTable comment editor with bold formatting applied.](media/powertable-how-to-add-comments/format-comment.png)](media/powertable-how-to-add-comments/format-comment.png#lightbox)
5. Select **Assign to User** to assign a user from the dropdown list as needed. By using this feature, you can assign and track tasks for effective workflow collaboration.

   [![Screenshot of the PowerTable comment editor with the Assign to user dropdown highlighted and the Send icon beside it.](media/powertable-how-to-add-comments/assign-to-user.png)](media/powertable-how-to-add-comments/assign-to-user.png#lightbox)
6. After assigning the user, select the **Send** icon to post the comment.

   [![Screenshot of the PowerTable comment editor with an assigned user and the Send icon highlighted in a red box.](media/powertable-how-to-add-comments/post-comment.png)](media/powertable-how-to-add-comments/post-comment.png#lightbox)

After the comment is posted,

- A green triangle appears in the top right corner of the cell, indicating that the cell contains a comment.
- PowerTable saves the comment with metadata such as the author name, timestamp, and, if applicable, the assigned user.

  [![Screenshot of a PowerTable comment thread with star, resolve, and close icons, plus a 'Comment added successfully' message.](media/powertable-how-to-add-comments/comment-added.png)](media/powertable-how-to-add-comments/comment-added.png#lightbox)
- To make a comment important, select the star icon on the added thread and make it a starred comment.
- When you assign a comment to a user, PowerTable sends them a Microsoft Teams notification. The notification includes the PowerTable sheet name, the comment's cell location, the assigner's name, the comment text, and a link to the PowerTable sheet.
- The assigned user can then take action or [reply to the comment](#reply-to-comments).

## Mention users to collaborate and assign tasks

In addition to assigning a user by using **Assign to user**, notify more users by using ***@*** and mentioning them in the comment. Comments with mentions help you assign and track tasks for effective workflow collaboration.

1. Select the cell and add a comment.
2. Type **@** followed by the userâs name.
3. Select the user from the list of suggestions.
4. Post the comment by selecting the **Send** icon.

   [![Screenshot of a cell comment showing a comment with an @mention of a user and also an Assigned to entry below it.](media/powertable-how-to-add-comments/mention-users.png)](media/powertable-how-to-add-comments/mention-users.png#lightbox)

Mentioned users also receive Teams notifications with all the comment details and a link to the sheet so they can respond or take action.

The task status is initially **Open**. You can later update it to [Resolved](#resolve-and-reopen-comment-threads) when you complete the task.

## Reply to comments

Comments support threaded conversations where multiple users collaborate.

1. Hover over the green comment indicator to open the comment thread.
2. Enter your response in the **Reply** editor.
3. Post the message by selecting the **Send** icon.
   Replies appear as part of the same comment thread, making it easier to track discussions.

![Screenshot of the comment popup over a table row with Reply box and Send arrow for posting a response.](media/powertable-how-to-add-comments/reply-comment.png)

## Resolve and reopen comment threads

You can manage comment threads to control discussions.

To resolve a thread:

1. Hover over the comment indicator to open the comment thread.
2. Select the **Resolve Thread** icon.

   ![Screenshot of an open comment thread on a grid cell with the Resolve Thread checkmark icon highlighted.](media/powertable-how-to-add-comments/resolve-thread.png)
3. You can reopen a resolved thread if you need further discussion. Reopen the thread by selecting the undo icon or by replying to the thread.

   ![Screenshot of a resolved comment thread on a grid cell with the undo icon highlighted to reopen the thread.](media/powertable-how-to-add-comments/reopen-thread.png)

## Add comments column

Add a **Comments** column to the sheet to capture row-level discussions.

To add a comments column:

1. Go to the **Comments** dropdown, select **Settings**, and then turn on the **Show comments column** toggle in the side panel. The table gets a **Comments** column.

   [![Screenshot of the PowerTable Comments dropdown with Settings highlighted and the Show comments column toggle enabled in the side panel.](media/powertable-how-to-add-comments/show-comments-column.png)](media/powertable-how-to-add-comments/show-comments-column.png#lightbox)
2. Double-click the row you want in the **Comments** column. The comment editor opens.
3. Enter the comment, and then select the **Send** icon to post it.

   [![Screenshot of PowerTable showing the added Comments column and a comment thread panel with Send button.](media/powertable-how-to-add-comments/add-comments-column.png)](media/powertable-how-to-add-comments/add-comments-column.png#lightbox)

After the comment is posted,

- Comments in the **Comments** column support replies, user assignments, and task status tracking.
- When you assign or mention a user in a comment, PowerTable automatically adds the **Status** and **Assignee** columns. The **Assignee** column shows the assigned user, and the **Status** column shows the current status of the assigned comment, such as *Open* or *Resolved*.

  [![Screenshot of PowerTable showing added Status and Assignee columns next to the Comments column for an assigned comment.](media/powertable-how-to-add-comments/status-assignee-columns.png)](media/powertable-how-to-add-comments/status-assignee-columns.png#lightbox)
- To show or hide the **Assignee** and **Status** columns, select the **>** icon in the **Comments** column header.
- To remove the **Comments** column, turn off the **Show comments column** toggle in the **Comment Settings** panel.
- You can view all row-level comments in the [All Comments](#view-all-comments) panel under **Row Comments**.

## View all comments

You can view all comments in a centralized panel to track discussions across rows, columns, and cells.

Select **View all comments** from the **Comments** dropdown. The **All Comments** panel opens.

[![Screenshot of the Comments dropdown with View all comments highlighted and the All Comments panel open beside the table.](media/powertable-how-to-add-comments/view-all-comments.png)](media/powertable-how-to-add-comments/view-all-comments.png#lightbox)

The panel organizes comments by category and shows the number of comments in each category:

- **Row Comments**: Comments associated with specific rows (comments in the comments column).
- **Column Comments**: Comments associated with specific columns.
- **Cell Comments**: Comments added to individual cells.

Expand each section by selecting **>** to view the associated comments.

## Configure comment settings

You can customize how you want to show comments and configure notification settings.

To open the **Comment Settings** pane, select the **Comments** dropdown, and then select **Settings**.

![Screenshot of the Comments dropdown with Settings highlighted and the Comment Settings pane showing toggles.](media/powertable-how-to-add-comments/comment-settings.png)

The following options are available:

- **Show Indicators:** Enable or disable the green comment indicator on the PowerTable sheet. When you disable this option, PowerTable hides the comment indicators and comments from the sheet. You can view them only in the [All Comments](#view-all-comments) panel.
- **Show comments column**: Show or hide the dedicated **Comments** column. To learn more, see [Add comments column](#add-comments-column).
- **Notification**: Turn Microsoft Teams notifications for comments on or off.
- **Delete all comments**: Permanently remove all comments from the table.
- **Reset**: Discard any unsaved changes and restore the previously saved settings.

Finally, select **Save** to apply the changes you made in the **Comment Settings** pane.

Note

Deleting all comments permanently removes all comment threads from the table. This action can't be undone.

## Configure comment access

Use the **Security** settings to control who can access, manage, and interact with comments.

1. Select **Security** from the toolbar.
2. Select the **Roles** tab on the left and scroll down to the **Comments** section.
3. Use the following options to define access:

   - **Who can view comments**: Specify users who can view comments. Enter names or email addresses to grant access.
   - **Who can add comments**: Specify users who can add comments. Enter names or email addresses to grant access.
   - **Who can star comments**: Specify users who can mark comments as important (starred).

Select **Save Changes** to apply changes.

Note

Report authors and editors can delete comments from other users, such as inappropriate comments.

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
