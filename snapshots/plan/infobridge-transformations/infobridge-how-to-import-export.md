---
title: "Import and export transformation steps"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-import-export](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-import-export) · Last updated on **2026-07-09**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Import and export transformation steps

Summarize this article for me

Use the **Export** and **Import** commands to reuse transformation steps across multiple queries. Exporting a query creates a `.bck` file that contains its transformation steps. Then import the file into another query.

Reusing transformation steps helps maintain consistency across similar datasets and reduces the time required to recreate the same data preparation workflow.

Find the **Import** and **Export** commands on the **Transform** tab.

[![Screenshot highlighting the Import and Export commands on the Transform tab and the Performed Steps pane.](../media/infobridge-transformations/infobridge-how-to-import-export/import-export-command.png)](../media/infobridge-transformations/infobridge-how-to-import-export/import-export-command.png#lightbox)

## Export transformation steps

The following example shows how to export transformation steps from a query.

1. Open the query that contains the transformation steps that you want to reuse.
2. Verify that the **Performed Steps** pane lists the required transformation steps.
3. On the **Transform** tab, select **Export**.
4. Save the generated `.bck` file to your computer.

[![Screenshot showing the exported .bck file after selecting Export.](../media/infobridge-transformations/infobridge-how-to-import-export/export-complete.png)](../media/infobridge-transformations/infobridge-how-to-import-export/export-complete.png#lightbox)

The exported `.bck` file contains all transformation steps from the selected query.

## Import transformation steps

The following example shows how to import transformation steps into another query.

1. Open the target query.
2. On the **Transform** tab, select **Import**.
3. In the **Import Steps** dialog, browse to or drag and drop the exported `.bck` file.

   [![Screenshot showing the Import Steps dialog for selecting or dragging a .bck file.](../media/infobridge-transformations/infobridge-how-to-import-export/import-steps-dialog.png)](../media/infobridge-transformations/infobridge-how-to-import-export/import-steps-dialog.png#lightbox)
4. After the file uploads successfully, select **Upload**.

   [![Screenshot showing the uploaded .bck file ready to be imported.](../media/infobridge-transformations/infobridge-how-to-import-export/import-upload.png)](../media/infobridge-transformations/infobridge-how-to-import-export/import-upload.png#lightbox)
5. After the import completes, the imported transformation steps appear in the **Performed Steps** pane of the target query.

   [![Screenshot showing imported transformation steps displayed in the Performed Steps pane.](../media/infobridge-transformations/infobridge-how-to-import-export/imported-steps.png)](../media/infobridge-transformations/infobridge-how-to-import-export/imported-steps.png#lightbox)

Continue transforming the query, or write the transformed data to a destination.

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
