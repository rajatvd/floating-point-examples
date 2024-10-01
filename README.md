# Simple Example of Floating Point Errors

* Subtraction is the only ill-conditioned operation in floating point arithmetic.
* The relative error can grow by an unbounded factor depending on how close the inputs are.

## Example

Consider $f(x) = x - 5$. This has very bad conditioning for $x \approx 5$.

$$d(\log|x - 5|)) = \frac{dx}{|x - 5|}.$$

$$\frac{1}{|x-5|} \to \infty \text{ as } x \to 5.$$
