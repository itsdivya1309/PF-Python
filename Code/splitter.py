"""Generate candidate splitter."""

import numpy as np

def get_parameter_value(X=None):
    """For a list of distance measures, generate a dictionary 
    of parameterized distances.
    
    Parameters
    ----------
    X : np.ndarray of shape (n_cases, n_timepoints)
        
    Returns
    -------
    distance_param : a dictionary of distances and their 
        parameters.
    """
    X_std = X.std()
    param_ranges = {
        "euclidean": {},
        "dtw": {"window": (0,0.25)},
        "ddtw": {"window": (0,0.25)},
        "wdtw": {"g": (0,1)},
        "wddtw": {"g": (0,1)},
        "erp": {"g": (X_std/5,X_std)},
        "lcss": {"epsilon": (X_std/5,X_std),
                 "window": (0,0.25)}
    }
    random_params = {}
    for measure, ranges in param_ranges.items():
        random_params[measure] = {param: np.round(np.random.uniform(low,high),3)
                                  for param, (low,high) in ranges.items()}
        
    # For TWE
    lmbda = np.random.randint(0,9)
    exponent_range = np.arange(1,6)  # Exponents from -5 to 1 (inclusive)
    random_exponent = np.random.choice(exponent_range)
    nu = 1/10**random_exponent
    random_params["twe"] = {"lmbda": lmbda,
                            "nu": nu}
    
    # For MSM
    base = 10
    # Exponents from -2 to 2 (inclusive)
    exponents = np.arange(-2, 3, dtype=np.float64)

    # Randomly select an index from the exponent range
    random_index = np.random.randint(0, len(exponents))
    c = base ** exponents[random_index]
    random_params["msm"] = {"c": c}
    
    return random_params


def get_candidate_splitter(X, paramterized_distances):
    """Generate candidate splitter.
    
    Takes a time series dataset and a set of parameterized 
    distance measures to create a candidate splitter, which 
    contains a parameterized distance measure and a set of exemplars.
    
    Parameters
    ----------
    X : np.ndarray shape (n_cases, n_timepoints)
        The training input samples.
    parameterized_distances : dictionary
        Contains the distances and their parameters.

    Returns
    -------
    splitter : list of two dictionaries
        A distance and its parameter values and a set of exemplars.
    """
    