---
title: "SHOW_MESSAGE"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/show-message](https://learn.microsoft.com/en-us/fabric/iq/plan/scripting-functions/show-message) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# SHOW\_MESSAGE

Summarize this article for me

Use the SHOW\_MESSAGE function to display a toast message to users when a script runs. For example, display a confirmation, provide a short instruction, or direct users to contact a person.

## Syntax

The following syntax displays a message.

```
SHOW_MESSAGE("message")
```

Replace message with the text you want to display. Enclose the message in double quotation marks.

## Example

The following example displays a message that directs users to email the contact person at Contoso.

```
SHOW_MESSAGE("Email the contact person at Contoso.com.")
```

## Configure a button to display a message

1. Open the planning item and create or edit an action parameter.
2. Set **Type** to **Action**.
3. Enter a name, such as Contact Person.
4. In **Description**, explain what the action does. For example, enter: Displays a message directing users to email the contact person at Contoso.com.
5. Under **Interface Options**, set **Interface Type** to **Button**.
6. Select **Enable Script**.
7. Under **Button Configuration**, set **Label** to Contact.
8. Add an action, select the root scope, and enter the following formula script:

   ```
   SHOW_MESSAGE("Email the contact person at Contoso.com.")
   ```
9. Save the button configuration, and then select **Update**.

   [![Screenshot of the button configuration for the SHOW_MESSAGE function.](../media/scripting-functions/show-message/show-message-configuration.png)](../media/scripting-functions/show-message/show-message-configuration.png#lightbox)

   When a user selects **Contact**, the planning item displays the message as a toast notification.

   [![Screenshot of the toast message displayed after a user selects the Contact button.](../media/scripting-functions/show-message/show-message-result.png)](../media/scripting-functions/show-message/show-message-result.png#lightbox)

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
