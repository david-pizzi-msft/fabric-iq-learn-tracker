---
title: "Use Find and Replace in Infobridge"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-find-replace](https://learn.microsoft.com/en-us/fabric/iq/plan/infobridge-transformations/infobridge-how-to-find-replace) · Last updated on **2026-06-23**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Use Find and Replace in Infobridge

Summarize this article for me

Use the **Find and Replace** transformation to search for values within one or more columns and replace them with new values. Use this transformation to standardize dimension members, simplify reporting categories, and clean source data before loading it into a planning sheet or report.

The following examples demonstrate how to use **Find and Replace** on the **Market & Geography** column.

## Replace a text value

In this example, the **Market & Geography** column contains values such as *Channel Partners,Canada*, *Enterprise,Canada*, and *Government,Canada*.

[![Screenshot of Market and Geography values before applying Find and Replace.](../media/infobridge-transformations/infobridge-how-to-find-replace/market-geography-source-values.png)](../media/infobridge-transformations/infobridge-how-to-find-replace/market-geography-source-values.png#lightbox)

To replace all occurrences of **Canada** with **CA**:

1. On the **Transform** tab, select **Find and Replace**.
2. In **Target Columns**, select **Market & Geography**.
3. In **Find**, enter **Canada**.
4. Select **Fuzzy Match**.
5. In **Replace With**, enter **CA**.
6. Select **Apply**.

[![Screenshot of Find and Replace dialog configured to replace Canada with CA in the Market and Geography column by using the Fuzzy Match option.](../media/infobridge-transformations/infobridge-how-to-find-replace/find-replace-canada-to-ca.png)](../media/infobridge-transformations/infobridge-how-to-find-replace/find-replace-canada-to-ca.png#lightbox)

After you apply the transformation, the **Market & Geography** column uses the abbreviated country code.

[![Screenshot of Market and Geography column showing values such as Channel Partners,CA, Enterprise,CA, and Government,CA after replacing Canada with CA.](../media/infobridge-transformations/infobridge-how-to-find-replace/market-geography-country-code-replaced.png)](../media/infobridge-transformations/infobridge-how-to-find-replace/market-geography-country-code-replaced.png#lightbox)

## Replace values by using a regular expression

Use regular expressions to replace multiple matching values with a single standardized value.

In this example, you group all values in the **Market & Geography** column that end with **CA** into a single category called **Canada Market**.

1. On the **Transform** tab, select **Find and Replace**.
2. In **Target Columns**, select **Market & Geography**.
3. In **Find**, enter `.*,CA$`.
4. Select **Use Regular Expression**.
5. In **Replace With**, enter **Canada Market**.
6. Select **Apply**.

The regular expression `.*,CA$` matches any value that ends with **CA**.

[![Screenshot of Find and Replace dialog configured to use the regular expression dot star comma CA dollar sign and replace matching values with Canada Market.](../media/infobridge-transformations/infobridge-how-to-find-replace/find-replace-regex-canada-market.png)](../media/infobridge-transformations/infobridge-how-to-find-replace/find-replace-regex-canada-market.png#lightbox)

After you apply the transformation, all matching values appear as **Canada Market**.

[![Screenshot of Market and Geography column showing Canada Market after applying a regular expression based Find and Replace transformation.](../media/infobridge-transformations/infobridge-how-to-find-replace/market-geography-canada-market-result.png)](../media/infobridge-transformations/infobridge-how-to-find-replace/market-geography-canada-market-result.png#lightbox)

## Match case options

The **Find and Replace** transformation supports the following matching methods:

- **Fuzzy Match**: Finds values that approximately match the search text.
- **Fuzzy Case Match**: Finds approximate matches while considering letter casing.
- **Match Full String**: Replaces values only when the entire value matches the search text.
- **Use Regular Expression**: Uses regular expression patterns to identify matching values.

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
