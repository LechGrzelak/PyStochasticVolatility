import numpy as np
import numba as nb


# We suppose that the distributions of the jumps is exp(N(jumpmean, jumpstd))
@nb.jit("c16[:](f8[:], f8, f8, f8, f8, f8, f8)", nopython=True, nogil=True)
def get_merton_cf(w, t, x, sigma, jumpmean, jumpstd, lambda_t):
    jumpmean_transform = jumpmean - 0.5 * jumpstd * jumpstd
    alpha = (np.exp(jumpmean_transform + 0.5 * jumpstd * jumpstd) - 1.0) * lambda_t * t
    x_i_u = (x - 0.5 * sigma * sigma * t) * 1j * w
    x_u = - 0.5 * np.power(w * sigma, 2.0) * t
    nu_t = (np.exp((1j * w * jumpmean_transform - 0.5 * np.power(w * jumpstd, 2.0))) - 1.0) * lambda_t * t - alpha
    return np.exp(x_i_u + x_u + nu_t)

