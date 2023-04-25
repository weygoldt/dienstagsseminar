# Baby steps towards lienar regression

Notes from [Baby steps towards linear regression, M1, Tuebingen](https://www.youtube.com/watch?v=lWGdFeMsjzg&list=PL05umP7R6ij35ShKLDqccJSDntugY4FQT&index=2)

See: mathematics for machine learning, free online
Add Bishop ML Book to repo

**Supervised learning** Data is labeled.
**Unsupervised learning** No labels, data is clustered.
**Reinforcment learning** Problem is more like an agent. E.g. play chess.

## Linear regression

- Just one predictor: E.g. predict height from the age
- We need to optimize parameters until it fits the data best: For that we need a loss or cost function: Sum of squared values of the sqared deviation between the actual value and the prediction. The average. I.e., the mean squared error.

**insert loss function here**

- Why is this the loss function of the lienar regression? There are many alternatives. Later lectures will answer this. 
- This kind of LR is called the ordinary least squares regression (OLR)

## Baby linear regression

... With a simpler model, just a single $\beta$ so the intercept is always at zero and the loss function has just a single parameter.

$$
\mathcal{L}(\beta) = \frac{1}{n}\sum_{i} (y_i - \beta x_i)^2
$$

- If we plot the Loss function as a function of Beta, there is a minimum that we need to find. The standard tool to find the minimum is the gradient descent

### Baby gradient descent

- Look at the derivative at some random point as a guide to in which direction you should go in the next step. Add a **graph here**. When the derivative is 0 then we have the minimum.

The update rule can be formulated as the following:
$$
\beta \leftarrow \beta - \eta \frac{d\mathcal(\beta)}{d\beta}
$$
**Problem:** What if we descent to a local minimum and are stuck in a bad minimum. The update rule is a so called non-convex function that is very hard to optimize. In the baby linear regression, the loss function just has a single minimum.

The **learning rate** just governs the size of the steps. 
- If the learning rate is too large, we just jump around.
- If the learning rate is too small, it will take forever.

Lets assume we have a good learning rate and the loss function decreases. We also need a stopping criterion. E.g. 
- when the loss decreases by a very small value, we can just stop. 
- Or when the derivative is small.
- Or just when the number of iterations is just fixed.

To do that, we can intergrate the loss function:
$$
\mathcal{L}(\beta) = \frac{1}{n}\sum_{i} (y_i - \beta x_i)^2
$$
$$
\mathcal{L}'(\beta) = \frac{1}{n}\sum_{i}2(y_i - \beta x_i)(-x_i) = \text{finish this later}
$$
At the minimum the derivative is 0 and this beta is the solution to the linear regression.

## Normal linear regression

The space in which we can optimize the parameters is 2D so the loss is now a surface. To find a minimum on a surface, we need **partial derivatives**. This is basically deriving on of the parameters at the time. So we compute the normal derivative just for each dimension seperately.

But what is the actual **gradient?**. The Gradient is a vector in 2D, composed of the two partial derivatives in a vector. The gradient is always perpendicular to the curve on constant height. After each step, we look at the gradient again. 

**Add analytical solution from whiteboard here**

