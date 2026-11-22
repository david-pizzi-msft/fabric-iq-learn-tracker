---
title: "Calculate normal distribution values"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/statistical-functions/calculate-normal-distribution](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/statistical-functions/calculate-normal-distribution) · Last updated on **2026-08-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Calculate normal distribution values

Summarize this article for me

## NORMDIST

The *NORMDIST* function returns the normal distribution for a specified mean and standard deviation. It can return either the cumulative distribution function (CDF) or the probability density function (PDF), depending on the value of the cumulative argument.

### Syntax

```
NORMDIST(x, mean, std_dev, cumulative)
```

### Arguments

- `x`: The value for which the distribution is calculated.
- `mean`: The arithmetic mean of the distribution.
- `std_dev`: The standard deviation of the distribution.
- `cumulative`: Specifies the type of distribution to return.
  - `TRUE`: Returns the cumulative distribution function (CDF).
  - `FALSE`: Returns the probability density function (PDF).

### Return value

Returns the normal distribution value for the specified input based on the selected distribution type.

### Example

```
NORMDIST(42, 40, 1.5, TRUE)
```

Returns the cumulative normal distribution for the specified value. In this example, the function returns `0.9087`.

You can use the *NORMDIST* function to analyze the probability of outcomes in datasets that follow a normal distribution, such as estimating the likelihood of meeting a revenue target or evaluating test scores.

[![Screenshot of the NORMDIST function.](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/normdist.jpg)](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/normdist.jpg#lightbox)

### Excel equivalent

[NORMDIST](https://support.microsoft.com/en-us/office/normdist-function-126db625-c53e-4591-9a22-c9ff422d6d58)

## NORMSDIST

The *NORMSDIST* function returns the standard normal distribution for a specified value. It is a special case of the normal distribution where the mean is `0` and the standard deviation is `1`. The function can return either the cumulative distribution function (CDF) or the probability density function (PDF), depending on the value of the cumulative argument.

### Syntax

```
NORMSDIST(value, cumulative)
```

### Arguments

- `value`: The numeric value for which the distribution is calculated.
- `cumulative`: Specifies the type of distribution to return.
  - `TRUE`: Returns the cumulative distribution function (CDF).
  - `FALSE`: Returns the probability density function (PDF).

### Return value

Returns the standard normal distribution value for the specified input based on the selected distribution type.

### Example

```
NORMSDIST(1, TRUE)
```

Returns the cumulative standard normal distribution for the specified value. In this example, the function returns `0.8413`.

You can use the *NORMSDIST* function to analyze standardized data and determine the probability or percentile of a specific outcome within a standard normal distribution.

[![Screenshot of a Planning sheet with NORMSDIST function.](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/normsdist.png)](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/normsdist.png#lightbox)

### Excel equivalent

[NORMSDIST](https://support.microsoft.com/en-us/office/normsdist-function-463369ea-0345-445d-802a-4ff0d6ce7cac)

## NORMINV

The *NORMINV* function returns the inverse of the normal cumulative distribution for a specified mean and standard deviation. It calculates the value corresponding to a given probability on a normal distribution curve.

### Syntax

```
NORMINV(probability, mean, std_dev)
```

### Arguments

- `probability`: The probability corresponding to the normal distribution.
- `mean`: The arithmetic mean of the distribution.
- `std_dev`: The standard deviation of the distribution.

### Return value

Returns the value corresponding to the specified probability for the given normal distribution.

### Example

```
NORMINV(0.90, 50, 5)
```

Returns the value corresponding to the specified probability. In this example, the function returns `56.41`.

You can use the *NORMINV* function to determine critical values or thresholds, such as calculating the score required to be in the top 10% of a dataset or finding the target value corresponding to a specified probability.

[![Screenshot of a Planning sheet with a NORMINV function.](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/norminv.png)](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/norminv.png#lightbox)

### Excel equivalent

[NORMINV](https://support.microsoft.com/en-us/office/norminv-function-87981ab8-2de0-4cb0-b1aa-e21d4cb879b8)

## NORMSINV

The *NORMSINV* function returns the inverse of the standard normal cumulative distribution. It assumes a normal distribution with a mean of `0` and a standard deviation of `1`.

### Syntax

```
NORMSINV(probability)
```

### Arguments

- `probability`: The probability corresponding to the standard normal distribution.

### Return value

Returns the value corresponding to the specified probability for the standard normal distribution.

### Example

```
NORMSINV(0.90)
```

Returns the value corresponding to the specified probability. In this example, the function returns `1.28`.

You can use the *NORMSINV* function to determine the number of standard deviations a value is from the mean. This is useful for calculating z-scores and creating standardized benchmarks to compare values across different datasets.

[![Screenshot of a Planning sheet with NORMSINV function.](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/normsinv.png)](../../media/planning-reference-formulas/statistical-functions/calculate-normal-distribution/normsinv.png#lightbox)

### Excel equivalent

[NORMSINV](https://support.microsoft.com/en-us/office/normsinv-function-8d1bce66-8e4d-4f3b-967c-30eed61f019d)

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
