# coding: utf-8

import numpy as np

f = np.load("result/dp.npz")
Q_dp = f["Q"]
ER = f["ER"]
P = f["P"]
mean_value_dp = f["mean_value"]

# copied from the DP notebook
def evaluate_policy(policy, ER, P, gamma, V0=None, tol=1e-3):

    v = np.zeros((22*11)) if V0 is None else V0
    row_idx = np.arange(len(v))
    converged = False
    for t in range(100):
        new_v = ER[row_idx, policy] + gamma * np.matmul(P[row_idx, policy], v)
        dev = np.max(np.abs(new_v - v))
        v = new_v
        if dev < tol:
            converged = True
            break
    if not converged:
        print("WARN: policy evaluation did not converge (final deviation = %.5f)" % dev)
    return v

def mean_policy_value(policy, gamma, tol=1e-3):
    # add terminal states
    policy_ = np.zeros((22, 11), dtype=int)
    policy_[1:, 1:] = policy
    policy_ = policy_.flatten()
    v = evaluate_policy(policy_, ER, P, gamma=gamma, tol=tol)
    v = v.reshape((22, 11))
    return np.mean(v[1:11, 1:11])