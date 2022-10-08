import tensorflow as tf
import tensorflow_probability as tfp
tfd = tfp.distributions
import numpy as np

# Heteroscedastic Normal distribution loss
def normal_heteroscedastic(y_true, y_pred):
    if len(y_pred.shape) == 2:
        mu_pred = y_pred[:,0]
        sigma_pred = tf.math.exp(y_pred[:, 1])
    elif len(y_pred.shape) == 1:
        mu_pred = y_pred[0]
        sigma_pred = tf.math.exp(y_pred[1])

    dist = tfd.Normal(loc=mu_pred, scale=sigma_pred)
    loss = dist.log_prob(y_true)
    return - tf.reduce_mean(loss)

# Gamma loss
def gamma_loss(y_true, y_pred):
    if len(y_pred.shape) == 2:
        alpha_pred = tf.math.exp(y_pred[:,0])
        beta_pred = tf.math.exp(y_pred[:, 1])
    elif len(y_pred.shape) == 1:
        alpha_pred = tf.math.exp(y_pred[0])
        beta_pred = tf.math.exp(y_pred[1])

    dist = tfd.Gamma(concentration=alpha_pred, rate=beta_pred)
    loss = dist.log_prob(y_true)
    return - tf.reduce_mean(loss)

# Poisson loss
def poisson_loss(y_true, y_pred):
    mu_pred = tf.math.exp(y_pred)
    dist = tfd.Poisson(rate=mu_pred)
    loss = dist.log_prob(y_true)
    return - tf.reduce_mean(loss)

#  Negative Binomial loss
def negbin_loss(y_true, y_pred):
    # Batches
    if len(y_pred.shape) == 2:
        log_r = y_pred[:,0]
        logit_p = y_pred[:,1]

        r = tf.math.exp(log_r)
        p = tf.math.sigmoid(logit_p)
        dist = tfd.NegativeBinomial(r, p)
        loss = dist.log_prob(y_true)
        return - tf.reduce_mean(loss)

    # Single observations
    elif len(y_pred.shape) == 1:
        log_r = y_pred[0]
        logit_p = y_pred[1]

        r = tf.math.exp(log_r)
        p = tf.math.sigmoid(logit_p)
        dist = tfd.NegativeBinomial(r, p)
        loss = dist.log_prob(y_true)
        return - tf.reduce_mean(loss)

#  Negative Binomial loss
def beta_loss(y_true, y_pred):
    # Batches
    if len(y_pred.shape) == 2:
        log_alpha = y_pred[:,0]
        log_beta = y_pred[:,1]

        alpha = tf.math.exp(log_alpha)
        beta = tf.math.exp(log_beta)
        dist = tfd.Beta(alpha, beta)
        loss = dist.log_prob(y_true)
        return - tf.reduce_mean(loss)

    # Single observations
    elif len(y_pred.shape) == 1:
        log_alpha = y_pred[0]
        log_beta = y_pred[1]

        alpha = tf.math.exp(log_alpha)
        beta = tf.math.exp(log_beta)
        dist = tfd.Beta(alpha, beta)
        loss = dist.log_prob(y_true)
        return - tf.reduce_mean(loss)
