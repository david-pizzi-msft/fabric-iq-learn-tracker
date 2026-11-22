---
title: "Create data entry forms with PowerTable sheets"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-generate-forms](https://learn.microsoft.com/en-us/fabric/iq/plan/powertable-how-to-generate-forms) · Last updated on **2026-11-06**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Create data entry forms with PowerTable sheets

Summarize this article for me

*Forms* allow you to collect data from users and write them directly to your database.

Forms can be used for various scenarios, such as capturing expense reports, collecting survey responses, running polls or quizzes, gathering customer feedback, registering event attendees, managing internal requests, or onboarding new users. Their structured layout and configurable fields make data collection easier and streamline workflows for both individuals and teams.

In this article, you learn how to quickly generate forms from your table to collect user inputs, store them in your PowerTable app, and write them back to the database.

You can create one or more forms for a PowerTable sheet and set up a form as the default form for the sheet.

## Create a form

1. Select **Setup > Forms**.

   [![Screenshot of the Forms button in the Setup tab of the menu ribbon.](media/powertable-how-to-generate-forms/forms-setup.png)](media/powertable-how-to-generate-forms/forms-setup.png#lightbox)
2. Select **Create a Form**. A form is generated with all the fields in the database.

   [![Screenshot of the configuration options for creating a new form.](media/powertable-how-to-generate-forms/create-form.png)](media/powertable-how-to-generate-forms/create-form.png#lightbox)

## Configure form settings

Use the **Form Setup** pane to customize the form title, description, appearance, field labels, and submission behavior.

[![Screenshot of the Form Setup pane showing Title, Description, Show Title, Show Logo, Field label, and Submission Options settings.](media/powertable-how-to-generate-forms/form-setup-pane.png)](media/powertable-how-to-generate-forms/form-setup-pane.png#lightbox)

### Form details

- **Title**: Enter the title that you want to display at the top of the form.
- **Description**: Enter a description to provide users with more information about the form.

### General

Enable or disable these options as you need:

- **Show Title**: Show or hide the form title.
- **Show Logo**: Show or hide the logo in the form.
- **Field label**: Choose how you want the field labels to appear on the form:

  - **Stacked**: Display field labels above their input fields.
  - **Inline**: Display field labels beside their input fields.

### Submission options

- **Limit to one response**: Enable this option to allow users to submit the form only once.
- **Show message on submission**: Enter the confirmation message that's displayed after a user submits the form.

## Preview and save form

- To set the form as the default form for the table, turn on the **Set as default form editor** option.
- Select **Preview** to see how your form looks to the users.
- Select **Save** to generate the form.

[![Screenshot of the form editor with the Set as default form editor toggle and Preview button highlighted for the Enter Product Details form.](media/powertable-how-to-generate-forms/select-preview.png)](media/powertable-how-to-generate-forms/select-preview.png#lightbox)

Note

To learn more about customizing your form, see [Customize form](#customize-form).

## Share form

After selecting **Save**, the **Share** pop-up appears as shown in the following image. Alternatively, select **Share** after creating the form to generate a shareable link for your form.

[![Screenshot of the Share pop-up with access options, an Expiry Date picker, and a Generate Link button after Form 1 is created.](media/powertable-how-to-generate-forms/share-pop-up-appears.png)](media/powertable-how-to-generate-forms/share-pop-up-appears.png#lightbox)

- **All users in this domain**: Select this option to share the form with all users in the domain.
- **Specific users**: Select this option to restrict access to specific users by entering their email addresses.

Choose an expiration date for the link. Select **Generate Link**.

[![Screenshot of generating a link to share the form.](media/powertable-how-to-generate-forms/share-form.png)](media/powertable-how-to-generate-forms/share-form.png#lightbox)

Select **Copy Link** to copy the form link and share it with users.

[![Screenshot of the Share dialog showing specific users, an expiry date, the form URL, and the highlighted Copy link button.](media/powertable-how-to-generate-forms/copy-link.png)](media/powertable-how-to-generate-forms/copy-link.png#lightbox)

The users who get the link can enter the details and select **Submit** to submit the form. The details are added to the table as a new record.

[![Screenshot of a shared form showing ProductKey, ProductSubcategoryKey, ProductSKU, ProductName, and ModelName fields with a Submit button.](media/powertable-how-to-generate-forms/submit-form.png)](media/powertable-how-to-generate-forms/submit-form.png#lightbox)

## Manage links

If you generate multiple links for a form, manage them by selecting **Manage Links**.

![Screenshot of the Enter Product Details form editor with the Manage Links button highlighted in the toolbar.](media/powertable-how-to-generate-forms/manage-links.png)

A window displays the list of form links and their details, including the link creator, creation date and time, access permissions, status, response count, and expiry date. Use the options in the **Action** column to copy or delete a form link.

[![Screenshot of the Manage Links window listing three active form links, with the copy and delete icons in the Action column highlighted.](media/powertable-how-to-generate-forms/actions-manage-links.png)](media/powertable-how-to-generate-forms/actions-manage-links.png#lightbox)

## Customize form

This section describes the ways in which you can customize your forms.

### Add logo

Select **Add Logo** to add your organization's logo.

### Delete field

Select the field and select the **Delete (bin)** icon to remove it. You can't delete the **primary key** field.

![Screenshot of deleting a field from the form.](media/powertable-how-to-generate-forms/delete-field.png)

### Add field

1. Select **Add Field** to add a new field from the table.

   [![Screenshot of adding a field using the plus icon.](media/powertable-how-to-generate-forms/add-field-plus.png)](media/powertable-how-to-generate-forms/add-field-plus.png#lightbox)
2. Select the required fields from the list. Select **Select All** to select all the table fields to add to the form.

   [![Screenshot of selecting all the fields to add them to the form.](media/powertable-how-to-generate-forms/add-field-select-all.png)](media/powertable-how-to-generate-forms/add-field-select-all.png#lightbox)
3. Alternatively, select the **+** icon below or beside the required field to add a new field.

   [![Screenshot of the highlighted plus icon below the ProductSize field opening a field list with search and Select all options.](media/powertable-how-to-generate-forms/plus-icon-add-field.png)](media/powertable-how-to-generate-forms/plus-icon-add-field.png#lightbox)

   [![Screenshot of grouping fields together using the plus icon.](media/powertable-how-to-generate-forms/group-plus-icon.png)](media/powertable-how-to-generate-forms/group-plus-icon.png#lightbox)

### Edit field

1. Select a field to edit it.
2. In **Edit Field**, enter an optional description.
3. Set a default value for the field if needed, so that it is prefilled.
4. Turn on the **Required** toggle to make the field entry mandatory for the users.

   [![Screenshot of the Edit Field pane for ProductSize with Description, Default Value set to L, and Required toggle highlighted.](media/powertable-how-to-generate-forms/edit-field.png)](media/powertable-how-to-generate-forms/edit-field.png#lightbox)

### Create field groups

To make user inputs more readable and organized, you can group related or similar fields together. In address blocks, for example, you can group related fields such as house number, street name, city, state, zip code, and so on.

Grouped fields also enable you to perform bulk operations on fields, such as hiding them or formatting them at once.

1. Select **Add Group** to create a new group.
2. Add fields to the new field group.

   [![Screenshot of adding a new field group and adding fields to it.](media/powertable-how-to-generate-forms/add-group.png)](media/powertable-how-to-generate-forms/add-group.png#lightbox)

### Edit group

1. Select the group to start editing it.
2. In the **Edit Group** side pane, enter the group name and a description.
3. Enable or disable the following options as needed:

   - **Show Title**: Enable this option to display the group name, or disable it to hide the name.
   - **Highlight Background**: Enable this option to highlight the group's background.

   [![Screenshot of the form editor showing the Edit Group side pane with Title, Description, Show Title, and Highlight Background settings.](media/powertable-how-to-generate-forms/edit-group.png)](media/powertable-how-to-generate-forms/edit-group.png#lightbox)

### Add tab

You can split your form into multiple tabs and arrange relevant fields within each tab.

1. Select **Add Tab** to add a new tab in your form as shown in the following image.

   [![Screenshot of the form editor with the Add Tab option highlighted and a new Tab 1 added beside the General tab.](media/powertable-how-to-generate-forms/add-tab.png)](media/powertable-how-to-generate-forms/add-tab.png#lightbox)
2. Select **Tab 1** to add a name and description for the tab.

   [![Screenshot of the form editor with Tab 1 selected and the Edit Tab pane showing Product Details entered in the Title box.](media/powertable-how-to-generate-forms/add-tab-title.png)](media/powertable-how-to-generate-forms/add-tab-title.png#lightbox)
3. In the new tab, select **Add Field** to add the fields you want.

   ![Screenshot of the Product Details tab with the Add Field button highlighted and a dropdown listing fields such as ProductName and ModelName with checkboxes.](media/powertable-how-to-generate-forms/add-tab-field.png)
4. Select the dropdown beside it and select **Add Group** to add a field group.

   ![Screenshot of the Product Details tab with the dropdown beside Add Field highlighted and the Add Group option displayed.](media/powertable-how-to-generate-forms/add-field-group-tab.png)
5. Add fields to the group by selecting the **+** icon.

   [![Screenshot of Group 1 in the Product Details tab with the + icon highlighted and a field list showing checkboxes for fields like ProductName.](media/powertable-how-to-generate-forms/add-field-to-group-tab.png)](media/powertable-how-to-generate-forms/add-field-to-group-tab.png#lightbox)

Follow the same steps to create as many tabs as you want. To delete a tab, select it and then select the bin icon beside it.

## Manage forms

You can create and manage multiple forms for a table in the **Forms** window.

![Screenshot of the Forms window listing two forms, with the Form 2 ellipsis menu open showing Delete Form, Duplicate Form, and Allow Submission options.](media/powertable-how-to-generate-forms/manage-forms.png)

Select the horizontal ellipsis (...) next to a form to delete it, duplicate it, or allow submissions to the form.

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
