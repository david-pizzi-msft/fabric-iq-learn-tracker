---
title: "Use the Round transformation in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-round](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-round) · Last updated on **2026-07-08**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Use the Round transformation in Infobridge

Summarize this article for me

Use the **Round** transformation to simplify numeric values by reducing the number of decimal places displayed in a measure. This transformation improves report readability while preserving the underlying data for analysis.

The **Round** transformation provides three rounding methods:

- **Round** rounds values to the nearest value based on the specified precision.
- **Round Up** rounds values by using the **Round Up** method.
- **Round Down** rounds values by using the **Round Down** method.

You can find the **Round** transformation on the **Transform** tab.

## Round numeric measures

The following example demonstrates how to apply a rounding transformation to the **Actuals - ZAVA** measure.

- On the **Transform** tab, select **Rounding**.

  [![Screenshot highlighting the Rounding command on the Transform tab.](../media/infobridge-transformations/infobridge-how-to-round/infobridge-query-created.png)](../media/infobridge-transformations/infobridge-how-to-round/infobridge-query-created.png#lightbox)

The following image shows the **Rounding** dialog, including the **Round**, **Round Up**, and **Round Down** methods.

[![Screenshot showing the Rounding dialog with the Round, Round Up, and Round Down options.](../media/infobridge-transformations/infobridge-how-to-round/rounding-options.png)](../media/infobridge-transformations/infobridge-how-to-round/rounding-options.png#lightbox)

The following sections demonstrate each rounding method by applying it to the **Actuals - ZAVA** measure.

[![Screenshot showing the Actuals - ZAVA measure before applying a rounding transformation.](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-before-rounding.png)](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-before-rounding.png#lightbox)

## Apply the Round transformation

Use the **Round** option to round values to the nearest value based on the specified precision.

1. On the **Transform** tab, select **Rounding**.
2. In the **Rounding** dialog:

   1. Select **Actuals - ZAVA** as the **Measure**.
   2. Select **Round** as the **Type**.
   3. Specify the required value for **Number of Characters**.
3. Select **Apply**.

   [![Screenshot showing the Rounding dialog configured to apply the Round transformation to the Actuals - ZAVA measure.](../media/infobridge-transformations/infobridge-how-to-round/round-dialog.png)](../media/infobridge-transformations/infobridge-how-to-round/round-dialog.png#lightbox)

The selected measure is rounded according to the specified precision.

[![Screenshot showing the Actuals - ZAVA measure after applying the Round transformation.](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-after-round.png)](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-after-round.png#lightbox)

## Apply the Round Up transformation

**Round Up** rounds values by using the **Round Up** method.

1. On the **Transform** tab, select **Rounding**.
2. In the **Rounding** dialog:
   1. Select **Actuals - ZAVA** as the **Measure**.
   2. Select **Round Up** as the **Type**.
3. Select **Apply**.

[![Screenshot showing the Rounding dialog configured to apply the Round Up transformation.](../media/infobridge-transformations/infobridge-how-to-round/round-up-dialog.png)](../media/infobridge-transformations/infobridge-how-to-round/round-up-dialog.png#lightbox)

The selected measure is rounded by using the **Round Up** transformation. All of the values in the **Actuals - ZAVA** column are rounded up to the nearest whole number.

[![Screenshot showing the Actuals - ZAVA measure after applying the Round Up transformation.](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-after-round-up.png)](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-after-round-up.png#lightbox)

## Apply the Round Down transformation

**Round Down** rounds values by using the **Round Down** method.

1. On the **Transform** tab, select **Rounding**.
2. In the **Rounding** dialog:
   1. Select **Actuals - ZAVA** as the **Measure**.
   2. Select **Round Down** as the **Type**.
3. Select **Apply**.

[![Screenshot showing the Rounding dialog configured to apply the Round Down transformation.](../media/infobridge-transformations/infobridge-how-to-round/round-down-dialog.png)](../media/infobridge-transformations/infobridge-how-to-round/round-down-dialog.png#lightbox)

The selected measure is rounded by using the **Round Down** transformation. All of the values in the **Actuals - ZAVA** column are rounded down to the nearest whole number.

[![Screenshot showing the Actuals - ZAVA measure after applying the Round Down transformation.](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-after-round-down.png)](../media/infobridge-transformations/infobridge-how-to-round/actuals-measure-after-round-down.png#lightbox)

After applying a rounding method, you can continue transforming the query or write the results to a destination.

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
