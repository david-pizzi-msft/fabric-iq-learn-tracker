---
title: "Configure Group by transformations"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-group-by](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-group-by) · Last updated on **2026-06-16**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Configure Group by transformations

Summarize this article for me

Use Group by transformations to summarize data and calculate aggregated metrics such as totals, averages, minimum values, and maximum values. Group by transformations aggregate measures based on selected dimensions to create summarized datasets for analysis and reporting.

For example, Group by can calculate metrics such as average salary by region, total sales by quarter, or minimum experience by department.

## Sample data

The following sample data set is used for the examples in this article.

Sample employee table:

| Employee ID | Department | Region | Salary | Experience |
| --- | --- | --- | --- | --- |
| Employee\_7916 | Operations | North America | 86907 | 12.4 |
| Employee\_9890 | Operations | North America | 88255 | 2.0 |
| Employee\_2263 | Sales | North America | 37957 | 3.0 |
| Employee\_7835 | Marketing | North America | 112324 | 10.5 |
| Employee\_5774 | HR | North America | 105082 | 6.4 |
| Employee\_9297 | IT | EMEA | 65848 | 11.9 |
| Employee\_5061 | Operations | EMEA | 62345 | 5.6 |
| Employee\_6237 | Operations | EMEA | 91959 | 6.8 |
| Employee\_1004 | HR | EMEA | 57706 | 13.6 |
| Employee\_2950 | Finance | APAC | 114873 | 14.4 |
| Employee\_8722 | Marketing | APAC | 51200 | 9.2 |
| Employee\_8165 | Marketing | APAC | 113498 | 6.6 |
| Employee\_2388 | IT | APAC | 58881 | 14.0 |
| Employee\_6852 | Operations | APAC | 64887 | 10.8 |
| Employee\_7678 | Operations | APAC | 87371 | 2.5 |

Summary of aggregated data:

| Region | Avg Salary | Headcount |
| --- | --- | --- |
| North America | 86105 | 5 |
| EMEA | 69464.5 | 4 |
| APAC | 81785 | 6 |

## Open Group by

Open **Group by** from the **Transform** ribbon to configure aggregations and summarize data.

[![Screenshot of the Group by transformation in Infobridge.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-interface.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-interface.png#lightbox)

## Configure Group by for a single measure

Use a single aggregation to summarize one measure by a selected dimension.

1. Open **Group by**.
2. Select **Quarter** from the **Category** dropdown menu.
3. Select **Minimum** from the **Operations 1** dropdown menu.
4. Select **InterestRate** from the **Values** dropdown menu.

   [![Screenshot of Group by configured with a Minimum aggregation for InterestRate by Quarter.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-single-measure-configuration.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-single-measure-configuration.png#lightbox)
5. Select **Apply**.

The results display the minimum interest rate for each quarter.

[![Screenshot of grouped results displaying the minimum interest rate by quarter.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-single-measure-results.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-single-measure-results.png#lightbox)

## Configure Group by for multiple measures

Use multiple aggregations to summarize more than one measure within the same transformation.

1. Open **Group by**.
2. Select **Quarter** from the **Category** dropdown menu.
3. Configure the first aggregation: **Minimum** for **InterestRate**
4. Select **Add Aggregation**.

   [![Screenshot of the first aggregation configured for InterestRate. The Add option is highlighted.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-configuration.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-configuration.png#lightbox)
5. Configure the second aggregation: **Average** for **COGS**.
6. Select **Add Aggregation** again.

   [![Screenshot of the second aggregation configured for COGS. The Add option is highlighted.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-configuration-adding-second-measure.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-configuration-adding-second-measure.png#lightbox)
7. Configure the third aggregation: **Sum** for **Sales**

   [![Screenshot of the third aggregation configured for Sales.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-configuration-added-third-measure.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-configuration-added-third-measure.png#lightbox)
8. Select **Apply**.

   The results display aggregated values for all configured measures.

   [![Screenshot of grouped results displaying multiple aggregated measures.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-results.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-measures-results.png#lightbox)

## Configure Group by for multiple dimensions

Use multiple dimensions to create more detailed aggregations.

1. Open **Group by**.
2. Select multiple dimensions from the **Category** dropdown menu. For example,

   - **Country**
   - **Quarter**
3. Configure the first aggregation. For example:

   - **Maximum** for **InterestRate**

   [![Screenshot of Quarter and Country selected in the Category dropdown menu with a Maximum aggregation configured for InterestRate.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-dimensions-configuration.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-dimensions-configuration.png#lightbox)
4. Configure other aggregations. For example:

   - **Sum** for **Sales**
   - **Average** for **COGS**

   [![Screenshot showing additional aggregations configured for Sales and COGS.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-dimensions-configuration-added-additional-operations.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-dimensions-configuration-added-additional-operations.png#lightbox)
5. Select **Apply**.

   The results display aggregated measures for each dimension combination.

   [![Screenshot of summarized data grouped by multiple dimensions.](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-dimensions-results.png)](../media/infobridge-transformations/infobridge-how-to-group-by/group-by-multiple-dimensions-results.png#lightbox)

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
