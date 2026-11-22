---
title: "Calculate variance and standard deviation"
---

!!! info "Snapshot"
    Source: [https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation](https://learn.microsoft.com/en-us/fabric/iq/plan/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation) · Last updated on **2026-08-19**

<!-- /meta -->
You can try [signing in](#) or changing directories.

Access to this page requires authorization. You can try changing directories.

# Calculate variance and standard deviation

Summarize this article for me

Planning provides functions to calculate variance and standard deviation in a dataset. Use the functions in this section to measure how widely values are spread around the mean, making it easier to analyze data variability and distribution.

## VARS

The *VARS* function returns the sample variance of a set of numbers. It measures how widely values are spread from the mean when the data represents a sample of a larger population. The calculation uses *(n â 1)* in the denominator to provide an unbiased estimate.

### Syntax

```
VARS(number1, [number2], ...)
```

### Arguments

- `number1`, `number2`, ...: The numbers or range of values used to calculate the sample variance.

### Return value

Returns the sample variance of the specified set of numbers.

### Examples

```
VARS(10, 20, 30)
```

Returns the sample variance of the specified set of numbers. In this example, the function returns `100`.

```
VARS(10, 20, 30, 40, 50)
```

Returns the sample variance of the specified set of numbers. In this example, the function returns `250`.

You can use the *VARS* function to analyze how widely values are spread from the mean for metrics such as sales, revenue, or performance scores.

[![Screenshot of a Planning sheet with VARS function.](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/vars.png)](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/vars.png#lightbox)

### Excel equivalent

[VAR.S](https://support.microsoft.com/en-us/office/var-s-function-913633de-136b-449d-813e-65a00b2b990b)

## VARP

The *VARP* function returns the population variance of a set of numbers. It measures how widely values are spread from the mean when the data represents the entire population. The calculation uses *n* in the denominator.

### Syntax

```
VARP(number1, [number2], ...)
```

### Arguments

- `number1`, `number2`, ...: The numbers or range of values used to calculate the population variance.

### Return value

Returns the population variance of the specified set of numbers.

### Examples

```
VARP(10, 20, 30)
```

Returns the population variance of the specified set of numbers. In this example, the function returns `66.67`.

```
VARP(10, 20, 30, 40, 50)
```

Returns the population variance of the specified set of numbers. In this example, the function returns `200`.

You can use the *VARP* function to analyze how widely values are spread from the mean for metrics such as sales, revenue, or performance scores.

[![Screenshot of a Planning sheet with VARP function.](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/varp.png)](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/varp.png#lightbox)

Note

Use the [*VARS*](#vars) function when working with sample data, as it calculates the sample variance using *(n â 1)* in the denominator. Use the *VARP* function when working with the entire population, as it calculates the population variance using *n* in the denominator.

### Excel equivalent

[VAR.P](https://support.microsoft.com/en-us/office/varp-function-26a541c4-ecee-464d-a731-bd4c575b1a6b)

## STDEVS

The *STDEVS* function returns the sample standard deviation of a set of numbers. It measures how widely values are dispersed from the mean when the data represents a sample of a larger population. The calculation uses *(n â 1)* in the denominator to provide an unbiased estimate.

### Syntax

```
STDEVS(number1, [number2], ...)
```

### Arguments

- `number1`, `number2`, ...: The numbers or range of values used to calculate the sample standard deviation.

### Return value

Returns the sample standard deviation of the specified set of numbers.

### Example

```
STDEVS(10, 20, 30, 40, 50)
```

Returns the sample standard deviation of the specified set of numbers. In this example, the function returns `15.81`.

You can use the *STDEVS* function to analyze how widely values are spread from the mean for metrics such as sales, revenue, or performance scores.

[![Screenshot of a Planning sheet with STDEVS function.](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/stdevs.png)](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/stdevs.png#lightbox)

### Excel equivalent

[STDEV.S](https://support.microsoft.com/en-us/office/stdev-s-function-7d69cf97-0c1f-4acf-be27-f3e83904cc23)

## STDEVP

The *STDEVP* function returns the population standard deviation of a set of numbers. It measures how widely values are dispersed from the mean when the data represents the entire population. The calculation uses *n* in the denominator.

### Syntax

```
STDEVP(number1, [number2], ...)
```

### Arguments

- `number1`, `number2`, ...: The numbers or range of values used to calculate the population standard deviation.

### Return value

Returns the population standard deviation of the specified set of numbers.

### Example

```
STDEVP(10, 20, 30, 40, 50)
```

Returns the population standard deviation of the specified set of numbers. In this example, the function returns `14.14`.

You can use the *STDEVP* function to analyze how widely values are spread from the mean for metrics such as sales, revenue, or performance scores.

[![Screenshot of Planning sheet with STDEVP function.](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/stdevp.png)](../../media/planning-reference-formulas/statistical-functions/calculate-variance-standard-deviation/stdevp.png#lightbox)

Note

Use the [*STDEVS*](#stdevs) function when working with sample data, as it calculates the sample standard deviation using *(n â 1)* in the denominator. Use the *STDEVP* function when working with the entire population, as it calculates the population standard deviation using *n* in the denominator.

### Excel equivalent

[STDEV.P](https://support.microsoft.com/en-us/office/stdevp-function-1f7c1c88-1bec-4422-8242-e9f7dc8bb195)

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
