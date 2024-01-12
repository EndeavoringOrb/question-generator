## Gram-Schmidt Orthonormalization Process:

### Let B = {$\vec{v}_1$, $\vec{v}_2$, ..., $\vec{v}_n$} be a basis for inner product space V.

### Let B' = {$\vec{w}_1$, $\vec{w}_2$, ..., $\vec{w}_n$}, where
1. $\vec{w}_1$ = $\vec{v}_1$
2. $\vec{w}_2$ = $\vec{v}_2$ - $\frac{<\vec{v}_2, \vec{w}_1>}{<\vec{w}_1, \vec{w}_1>}\cdot\vec{w}_1$
3. $\vec{w}_3$ = $\vec{v}_3$ - $\frac{<\vec{v}_3, \vec{w}_1>}{<\vec{w}_1, \vec{w}_1>}\cdot\vec{w}_1$ - $\frac{<\vec{v}_3, \vec{w}_2>}{<\vec{w}_2, \vec{w}_2>}\cdot\vec{w}_2$
4. $\vec{w}_n$ = $\vec{v}_n$ - $\sum_{i=1}^{n-1}\frac{<\vec{v}_n, \vec{w}_i>}{<\vec{w}_i, \vec{w}_i>}\cdot\vec{w}_i$
5. Then B' is an orthogonal basis for V.

### Let $\vec{u}_i$ = $\frac{\vec{w}_i}{||\vec{w}_i||}$, $1$ $\le$ $i$ $\le$ $n$.
Then B'' = {$\vec{u}_1$, $\vec{u}_2$, ..., $\vec{u}_n$} is an orthonormal basis for V.