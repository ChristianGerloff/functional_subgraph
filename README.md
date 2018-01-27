Detection of Functional Subgraphs from Dynamic Networks
====================

This package includes a Python implementation (with Numpy and Scipy) of
numerical algorithms for decomposing a time-varying graph into 
parts-based, additive subgraphs.



Requirements
------------

Numpy (https://www.numpy.org) and Scipy (https://www.scipy.org) need to be
installed.

Echobase toolbox is not required for core functionality, but is required to run tutorial notebooks (https://github.com/akhambhati/echobase).



Quick-Start
-----------
Non-Negative Matrix Factorization for dynamic networks, such that:

    A ~= WH
    Constraints:
        A, W, H >= 0
        L2-Regularization on W
        L1-Sparsity on H
        
Implementation is based on :

    1. Jingu Kim, Yunlong He, and Haesun Park. Algorithms for Nonnegative
            Matrix and Tensor Factorizations: A Unified View Based on Block
            Coordinate Descent Framework.
            Journal of Global Optimization, 58(2), pp. 285-319, 2014.
            
    2. Jingu Kim and Haesun Park. Fast Nonnegative Matrix Factorization:
            An Active-set-like Method And Comparisons.
            SIAM Journal on Scientific Computing (SISC), 33(6),
            pp. 3261-3281, 2011.
            
Modified from: https://github.com/kimjingu/nonnegfac-python
