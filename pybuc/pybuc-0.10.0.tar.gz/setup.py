# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pybuc', 'pybuc.statespace', 'pybuc.utils', 'pybuc.vectorized']

package_data = \
{'': ['*']}

install_requires = \
['matplotlib>=3.5.3,<4.0.0',
 'numba>=0.56.2,<0.57.0',
 'numpy>=1.23.2,<2.0.0',
 'pandas>=1.4.4,<2.0.0']

setup_kwargs = {
    'name': 'pybuc',
    'version': '0.10.0',
    'description': 'Fast estimation of Bayesian structural time series models via Gibbs sampling.',
    'long_description': '# pybuc\n`pybuc` ((Py)thon (B)ayesian (U)nobserved (C)omponents) is a feature-limited version of R\'s Bayesian structural time \nseries package, `bsts`, written by Steven L. Scott. The source paper can be found \n[here](https://people.ischool.berkeley.edu/~hal/Papers/2013/pred-present-with-bsts.pdf) or in the *papers* \ndirectory of this repository. While there are plans to expand the feature set of `pybuc`, currently there is no roadmap \nfor the release of new features. The syntax for using `pybuc` closely follows `statsmodels`\' `UnobservedComponents` \nmodule.\n\nThe current version of `pybuc` includes the following options for modeling and \nforecasting a structural time series: \n\n- Stochastic or non-stochastic level\n- Stochastic or non-stochastic trend\n- Damped trend <sup/>*</sup>\n- Multiple stochastic or non-stochastic periodic-lag seasonality\n- Multiple damped periodic-lag seasonality\n- Multiple stochastic or non-stochastic "dummy" seasonality\n- Multiple stochastic or non-stochastic trigonometric seasonality\n- Regression with static coefficients<sup/>**</sup>\n\n<sup/>*</sup> `pybuc` dampens trend differently than `bsts`. The former assumes an AR(1) process **without** \ndrift for the trend state equation. The latter assumes an AR(1) **with** drift. In practice this means that the trend, \non average, will be zero with `pybuc`, whereas `bsts` allows for the mean trend to be non-zero. The reason for \nchoosing an autoregressive process without drift is to be conservative with long horizon forecasts.\n\n<sup/>**</sup> `pybuc` estimates regression coefficients differently than `bsts`. The former uses a standard Gaussian \nprior. The latter uses a Bernoulli-Gaussian mixture commonly known as the spike-and-slab prior. The main \nbenefit of using a spike-and-slab prior is its promotion of coefficient-sparse solutions, i.e., variable selection, when \nthe number of predictors in the regression component exceeds the number of observed data points.\n\nFast computation is achieved using [Numba](https://numba.pydata.org/), a high performance just-in-time (JIT) compiler \nfor Python.\n\n# Installation\n```\npip install pybuc\n```\nSee `pyproject.toml` and `poetry.lock` for dependency details. This module depends on NumPy, Numba, Pandas, and \nMatplotlib. Python 3.9 and above is supported.\n\n# Motivation\n\nThe Seasonal Autoregressive Integrated Moving Average (SARIMA) model is perhaps the most widely used class of \nstatistical time series models. By design, these models can only operate on covariance-stationary time series. \nConsequently, if a time series exhibits non-stationarity (e.g., trend and/or seasonality), then the data first have to \nbe stationarized. Transforming a non-stationary series to a stationary one requires taking local and/or seasonal \ntime-differences of the data. Whether to difference the data and to what extent is a question that is answered using \nstatistical methods. \n\nOnce a stationary series is in hand, a SARIMA specification must be identified. Identifying the "right" SARIMA \nspecification can be achieved algorithmically (e.g., see the Python package `pmdarima`) or through examination of a \nseries\' patterns. The latter involves statistical and visual inspection of a series\' autocorrelation (ACF) and partial \nautocorrelation (PACF) functions. Ultimately, the necessary condition for stationarity engenders a prerequisite for \nrigorous statistical tests. It also implies that the underlying trend and seasonality, if they exist, are eliminated in \nthe process of generating a stationary series. The underlying time components that characterize a series are, therefore, \nnot of empirical interest.\n\nAnother less commonly used class of model is structural time series (STS), also known as unobserved components (UC). \nWhereas SARIMA models abstract away from an explicit model for trend and seasonality, STS/UC models do not. Thus, it is \nnot possible to visualize the underlying components that characterize a time series using a SARIMA model, but one can do \nso with a STS/UC model.\n\nSTS/UC models also have the flexibility to accommodate multiple stochastic seasonalities. SARIMA models, in contrast, \ncan accommodate multiple seasonalities, but only one seasonality/periodicity can be treated as stochastic. For example, \ndaily data may have day-of-week and week-of-year seasonality. Under a SARIMA model, only one of these seasonalities can \nbe modeled as stochastic. The other seasonality will have to be modeled as deterministic, which amounts to creating and \nusing a set of predictors that capture said seasonality. STS/UC models, on the other hand, can accommodate both \nseasonalities as stochastic by treating each as distinct, unobserved state variables.\n\nWith the above in mind, what follows is a comparison between `statsmodels`\' `SARIMAX\'` module, `statsmodels`\' \n`UnobservedComponents` module, and `pybuc`. The distinction between `statsmodels.UnobservedComponents` and `pybuc` is \nthe former is a maximum likelihood estimator (MLE) while the latter is a Bayesian estimator. The following code \ndemonstrates the application of these methods on a data set that exhibits trend and multiplicative seasonality.\nThe STS/UC specification for `statsmodels.UnobservedComponents` and `pybuc` includes stochastic level, stochastic trend \n(trend), and stochastic trigonometric seasonality with periodicity 12 and 6 harmonics.\n\n# Usage\n\n## Example: univariate time series with level, trend, and multiplicative seasonality\n\nA canonical data set that exhibits trend and seasonality is the airline passenger data used in\nBox, G.E.P.; Jenkins, G.M.; and Reinsel, G.C. Time Series Analysis, Forecasting and Control. Series G, 1976. See plot \nbelow.\n\n![plot](./examples/images/airline_passengers.png)\n\nThis data set gave rise to what is known as the "airline model", which is a SARIMA model with first-order local and \nseasonal differencing and first-order local and seasonal moving average representations. \nMore compactly, SARIMA(0, 1, 1)(0, 1, 1) without drift.\n\nTo demonstrate the performance of the "airline model" on the airline passenger data, the data will be split into a \ntraining and test set. The former will include all observations up until the last twelve months of data, and the latter \nwill include the last twelve months of data. See code below for model assessment.\n\n### Import libraries and prepare data\n\n```\nfrom pybuc import buc\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom statsmodels.tsa.statespace.sarimax import SARIMAX\nfrom statsmodels.tsa.statespace.structural import UnobservedComponents\n\n\n# Convenience function for computing root mean squared error\ndef rmse(actual, prediction):\n    act, pred = actual.flatten(), prediction.flatten()\n    return np.sqrt(np.mean((act - pred) ** 2))\n\n\n# Import airline passenger data\nurl = "https://raw.githubusercontent.com/devindg/pybuc/master/examples/data/airline-passengers.csv"\nair = pd.read_csv(url, header=0, index_col=0)\nair = air.astype(float)\nair.index = pd.to_datetime(air.index)\nhold_out_size = 12\n\n# Create train and test sets\ny_train = air.iloc[:-hold_out_size]\ny_test = air.iloc[-hold_out_size:]\n```\n\n### SARIMA\n\n```\n\'\'\' Fit the airline data using SARIMA(0,1,1)(0,1,1) \'\'\'\nsarima = SARIMAX(y_train, order=(0, 1, 1),\n                 seasonal_order=(0, 1, 1, 12),\n                 trend=[0])\nsarima_res = sarima.fit(disp=False)\nprint(sarima_res.summary())\n\n# Plot in-sample fit against actuals\nplt.plot(y_train)\nplt.plot(sarima_res.fittedvalues)\nplt.title(\'SARIMA: In-sample\')\nplt.xticks(rotation=45, ha="right")\nplt.show()\n\n# Get and plot forecast\nsarima_forecast = sarima_res.get_forecast(hold_out_size).summary_frame(alpha=0.05)\nplt.plot(y_test)\nplt.plot(sarima_forecast[\'mean\'])\nplt.fill_between(sarima_forecast.index,\n                 sarima_forecast[\'mean_ci_lower\'],\n                 sarima_forecast[\'mean_ci_upper\'], alpha=0.2)\nplt.title(\'SARIMA: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"SARIMA RMSE: {rmse(y_test.to_numpy(), sarima_forecast[\'mean\'].to_numpy())}")\n```\nThe SARIMA(0, 1, 1)(0, 1, 1) forecast plot and root mean squared error (RMSE) are shown below. \n\n![plot](./examples/images/airline_passengers_sarima_forecast.png)\n\n```\nSARIMA RMSE: 21.09028021383853\n```\n\n### MLE Unobserved Components\n\n```\n\'\'\' Fit the airline data using MLE unobserved components \'\'\'\nmle_uc = UnobservedComponents(y_train, exog=None, irregular=True,\n                              level=True, stochastic_level=True,\n                              trend=True, stochastic_trend=True,\n                              freq_seasonal=[{\'period\': 12, \'harmonics\': 6}],\n                              stochastic_freq_seasonal=[True])\n\n# Fit the model via maximum likelihood\nmle_uc_res = mle_uc.fit(disp=False)\nprint(mle_uc_res.summary())\n\n# Plot in-sample fit against actuals\nplt.plot(y_train)\nplt.plot(mle_uc_res.fittedvalues)\nplt.title(\'MLE UC: In-sample\')\nplt.show()\n\n# Plot time series components\nmle_uc_res.plot_components(legend_loc=\'lower right\', figsize=(15, 9), which=\'smoothed\')\nplt.show()\n\n# Get and plot forecast\nmle_uc_forecast = mle_uc_res.get_forecast(hold_out_size).summary_frame(alpha=0.05)\nplt.plot(y_test)\nplt.plot(mle_uc_forecast[\'mean\'])\nplt.fill_between(mle_uc_forecast.index,\n                 mle_uc_forecast[\'mean_ci_lower\'],\n                 mle_uc_forecast[\'mean_ci_upper\'], alpha=0.2)\nplt.title(\'MLE UC: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"MLE UC RMSE: {rmse(y_test.to_numpy(), mle_uc_forecast[\'mean\'].to_numpy())}")\n```\n\nThe MLE Unobserved Components forecast plot, components plot, and RMSE are shown below.\n\n![plot](./examples/images/airline_passengers_mle_uc_forecast.png)\n\n![plot](./examples/images/airline_passengers_mle_uc_components.png)\n\n```\nMLE UC RMSE: 17.961873327622694\n```\n\nAs noted above, a distinguishing feature of STS/UC models is their explicit modeling of trend and seasonality. This is \nillustrated with the components plot.\n\nFinally, the Bayesian analog of the MLE STS/UC model is demonstrated. Default parameter values are used for the priors \ncorresponding to the variance parameters in the model. If no explicit prior is given, by default each variance\'s prior \nis assumed to be inverse-Gamma with shape and scale values equal to 1e-6. This approximates what is known as Jeffreys \nprior, a vague/non-informative prior.\n\n**Note that because computation is built on Numba, a JIT compiler, the first run of the code could take a while. \nSubsequent runs (assuming the Python kernel isn\'t restarted) should execute considerably faster.**\n\n### Bayesian Unobserved Components\n```\n\'\'\' Fit the airline data using Bayesian unobserved components \'\'\'\nbayes_uc = buc.BayesianUnobservedComponents(response=y_train,\n                                            level=True, stochastic_level=True,\n                                            trend=True, stochastic_trend=True, damped_trend=False,\n                                            trig_seasonal=((12, 0),), stochastic_trig_seasonal=(True,),\n                                            seed=123)\n\npost = bayes_uc.sample(5000)\nmcmc_burn = 100\n\n# Print summary of estimated parameters\nfor key, value in bayes_uc.summary(burn=mcmc_burn).items():\n    print(key, \' : \', value)\n\n# Plot in-sample fit against actuals\nyhat = np.mean(post.filtered_prediction[mcmc_burn:], axis=0)\nplt.plot(y_train)\nplt.plot(y_train.index, yhat)\nplt.title(\'Bayesian-UC: In-sample\')\nplt.show()\n\n# Plot time series components\nbayes_uc.plot_components(burn=mcmc_burn, smoothed=True)\nplt.show()\n\n# Get and plot forecast\nforecast = bayes_uc.forecast(hold_out_size, mcmc_burn)\nforecast_mean = np.mean(forecast, axis=0)\nforecast_l95 = np.quantile(forecast, 0.025, axis=0).flatten()\nforecast_u95 = np.quantile(forecast, 0.975, axis=0).flatten()\n\nplt.plot(y_test)\nplt.plot(bayes_uc.future_time_index, forecast_mean)\nplt.fill_between(bayes_uc.future_time_index, forecast_l95, forecast_u95, alpha=0.2)\nplt.title(\'Bayesian UC: Forecast\')\nplt.legend([\'Actual\', \'Mean\', \'95% Prediction Interval\'])\nplt.show()\n\n# Print RMSE\nprint(f"BAYES-UC RMSE: {rmse(y_test.to_numpy(), forecast_mean)}")\n```\n\nThe Bayesian Unobserved Components forecast plot, components plot, and RMSE are shown below.\n\n![plot](./examples/images/airline_passengers_bayes_uc_forecast.png)\n\n![plot](./examples/images/airline_passengers_bayes_uc_components.png)\n\n```\nBAYES-UC RMSE: 17.002265220323128\n```\n\n# Model\n\nA structural time series model with level, trend, seasonal, and regression components takes the form: \n\n$$\ny_t = \\mu_t + \\gamma_t + \\mathbf x_t^\\prime \\boldsymbol{\\beta} + \\epsilon_t\n$$ \n\nwhere $\\mu_t$ specifies an unobserved dynamic level component, $\\gamma_t$ an unobserved dynamic seasonal component, \n$\\mathbf x_t^\\prime \\boldsymbol{\\beta}$ a partially unobserved regression component (the regressors $\\mathbf x_t$ are \nobserved, but the coefficients $\\boldsymbol{\\beta}$ are not), and $\\epsilon_t \\sim N(0, \\sigma_{\\epsilon}^2)$ an \nunobserved irregular component. The equation describing the outcome $y_t$ is commonly referred to as the observation \nequation, and the transition equations governing the evolution of the unobserved states are known as the state \nequations.\n\n## Level and trend\n\nThe unobserved level evolves according to the following general transition equations:\n\n$$\n\\begin{align}\n    \\mu_{t+1} &= \\mu_t + \\delta_t + \\eta_{\\mu, t} \\\\ \n    \\delta_{t+1} &= \\phi \\delta_t + \\eta_{\\delta, t} \n\\end{align}\n$$ \n\nwhere $\\eta_{\\mu, t} \\sim N(0, \\sigma_{\\eta_\\mu}^2)$ and $\\eta_{\\delta, t} \\sim N(0, \\sigma_{\\eta_\\delta}^2)$ for all \n$t$. The state equation for $\\delta_t$ represents the local trend at time $t$. \n\nThe parameter $\\phi$ represents an autoregressive coefficient. In general, $\\phi$ is expected to be in the interval \n$(-1, 1)$, which implies a stationary process for trend. In practice, however, it is possible for $\\phi$ to be \noutside the unit circle, which implies an explosive process. While it is mathematically possible for an explosive \nprocess to be stationary, the implication of such a result implies that the future predicts the past, which is not a \nrealistic assumption. \n\nIf an autoregressive trend is specified, no hard constraints (by default) are placed on the bounds of $\\phi$. Instead, \nthe default prior for $\\phi$ is $N(0, 0.25)$. Thus, -1 and 1 are within two standard deviations of the mean. It is \ntherefore possible for the Gibbs sampler to sample values outside the unit circle. If the posterior mean of $\\phi$ is \noutside the unit circle (or very close to the bounds), then an autoregressive trend is not a good assumption. If only \na "few" of the posterior samples have $\\phi$ outside the unit circle, this shouldn\'t be problematic for forecasting. \n$\\phi$ is set to 1 if a damped trend is not specified.\n\nFinally, note that if $\\sigma_{\\eta_\\mu}^2 = \\sigma_{\\eta_\\delta}^2 = 0$ and $\\phi = 1$, then the level component in \nthe observation equation, $\\mu_t$, collapses to a deterministic intercept and linear time trend.\n\n## Seasonality\n\n### Periodic-lag form\nThe seasonal component, $\\gamma_t$, can be modeled in three ways. One way is based on periodic lags. Formally, the \nseasonal effect on $y$ is modeled as\n\n$$\n\\gamma_t = \\rho \\gamma_{t-S} + \\eta_{\\gamma, t},\n$$\n\nwhere $S$ is the number of periods in a seasonal cycle, $\\rho$ is an autoregressive parameter expected to lie in the \nunit circle (-1, 1), and $\\eta_{\\gamma, t} \\sim N(0, \\sigma_{\\eta_\\gamma}^2)$ for all $t$. If damping is not specified \nfor a given periodic lag, $\\rho = 1$ and seasonality is treated as a random walk process.\n\nThis specification for seasonality is arguably the most parsimonious representation as it requires the fewest/weakest \nassumptions.\n\n### Dummy form\nAnother way is known as the "dummy" variable approach. Formally, the seasonal effect on the outcome $y$ is modeled as \n\n$$\n\\sum_{j=0}^{S-1} \\gamma_{t-j} = \\eta_{\\gamma, t} \\iff \\gamma_t = -\\sum_{j=1}^{S-1} \\gamma_{t-j} + \\eta_{\\gamma, t},\n$$ \n\nwhere $j$ indexes the number of periods in a seasonal cycle, and $\\eta_{\\gamma, t} \\sim N(0, \\sigma_{\\eta_\\gamma}^2)$ \nfor all $t$. Intuitively, if a time series exhibits periodicity, then the sum of the periodic effects over a cycle \nshould, on average, be zero.\n\n### Trigonometric form\nThe final way to model seasonality is through a trigonometric representation, which exploits the periodicity of sine and \ncosine functions. Specifically, seasonality is modeled as\n\n$$\n\\gamma_t = \\sum_{j=1}^h \\gamma_{j, t}\n$$\n\nwhere $j$ indexes the number of harmonics to represent seasonality of periodicity $S$ and \n$1 \\leq h \\leq \\lfloor S/2 \\rfloor$ is the highest desired number of harmonics. The state transition equations for each \nharmonic, $\\gamma_{j, t}$, are represented by a real and imaginary part, specifically\n\n$$\n\\begin{align}\n    \\gamma_{j, t+1} &= \\cos(\\lambda_j) \\gamma_{j, t} + \\sin(\\lambda_j) \\gamma_{j, t}^* + \\eta_{\\gamma_j, t} \\\\\n    \\gamma_{j, t+1}^* &= -\\sin(\\lambda_j) \\gamma_{j, t} + \\cos(\\lambda_j) \\gamma_{j, t}^* + \\eta_{\\gamma_j^* , t}\n\\end{align}\n$$\n\nwhere frequency $\\lambda_j = 2j\\pi / S$. It is assumed that $\\eta_{\\gamma_j, t}$ and $\\eta_{\\gamma_j^ * , t}$ are \ndistributed $N(0, \\sigma^2_{\\eta_\\gamma})$ for all $j, t$.\n\n## Regression\nThere are two ways to configure the model matrices to account for a regression component with static coefficients. \nThe canonical way (Method 1) is to append $\\mathbf x_t^\\prime$ to $\\mathbf Z_t$ and $\\boldsymbol{\\beta}_t$ to the \nstate vector, $\\boldsymbol{\\alpha}_t$ (see state space representation below), with the constraints \n$\\boldsymbol{\\beta}_0 = \\boldsymbol{\\beta}$ and $\\boldsymbol{\\beta}_t = \\boldsymbol{\\beta} _{t-1}$ for all $t$. \nAnother, less common way (Method 2) is to append $\\mathbf x_t^\\prime \\boldsymbol{\\beta}$ to $\\mathbf Z_t$ and 1 to the \nstate vector. \n\nWhile both methods can be accommodated by the Kalman filter, Method 1 is a direct extension of the Kalman filter as it \nmaintains the observability of $\\mathbf Z_t$ and treats the regression coefficients as unobserved states. Method 2 does \nnot fit naturally into the conventional framework of the Kalman filter, but it offers the significant advantage of only \nincreasing the size of the state vector by one. In contrast, Method 1 increases the size of the state vector by the size \nof $\\boldsymbol{\\beta}$. This is significant because computational complexity is quadratic in the size of the state \nvector but linear in the size of the observation vector.\n\nThe unobservability of $\\mathbf Z_t$ under Method 2 can be handled with maximum likelihood or Bayesian estimation by \nworking with the adjusted series \n\n$$\ny_t^* \\equiv y_t - \\tau_t = \\mathbf x_ t^\\prime \\boldsymbol{\\beta} + \\epsilon_t\n$$\n\nwhere $\\tau_t$ represents the time series component of the structural time series model. For example, assuming a level \nand seasonal component are specified, this means an initial estimate of the time series component \n$\\tau_t = \\mu_t + \\gamma_t$ and $\\boldsymbol{\\beta}$ has to be acquired first. Then $\\boldsymbol{\\beta}$ can be \nestimated conditional on \n$\\mathbf y^ * \\equiv \\left(\\begin{array}{cc} y_1^ * & y_2^ * & \\cdots & y_n^ * \\end{array}\\right)^\\prime$.\n\n`pybuc` uses Method 2 for estimating static coefficients.\n\n## State space representation (example)\nThe unobserved components model can be rewritten in state space form. For example, suppose level, trend, seasonal, \nregression, and irregular components are specified, and the seasonal component takes a trigonometric form with \nperiodicity $S=4$ and $h=2$ harmonics. Let $\\mathbf Z_t \\in \\mathbb{R}^{1 \\times m}$, \n$\\mathbf T \\in \\mathbb{R}^{m \\times m}$, $\\mathbf R \\in \\mathbb{R}^{m \\times q}$, and \n$\\boldsymbol{\\alpha}_ t \\in \\mathbb{R}^{m \\times 1}$ denote the observation matrix, state transition matrix, \nstate error transformation matrix, and unobserved state vector, respectively, where $m$ is the number of state equations \nand $q$ is the number of state parameters to be estimated (i.e., the number of stochastic state equations, \nwhich is defined by the number of positive state variance parameters). \n\nThere are $m = 1 + 1 + h * 2 + 1 = 7$ state equations and $q = 1 + 1 + h * 2 = 6$ stochastic state equations. There are \n6 stochastic state equations because the state value for the regression component is not stochastic; it is 1 for all $t$ \nby construction. The observation, state transition, and state error transformation matrices may be written as\n\n$$\n\\begin{align}\n    \\mathbf Z_t &= \\left(\\begin{array}{cc} \n                        1 & 0 & 1 & 0 & 1 & 0 & \\mathbf x_t^{\\prime} \\boldsymbol{\\beta}\n                        \\end{array}\\right) \\\\\n    \\mathbf T &= \\left(\\begin{array}{cc} \n                        1 & 1 & 0 & 0 & 0 & 0 & 0 \\\\\n                        0 & 1 & 0 & 0 & 0 & 0 & 0 \\\\\n                        0 & 0 & \\cos(2\\pi / 4) & \\sin(2\\pi / 4) & 0 & 0 & 0 \\\\\n                        0 & 0 & -\\sin(2\\pi / 4) & \\cos(2\\pi / 4) & 0 & 0 & 0 \\\\\n                        0 & 0 & 0 & 0 & \\cos(4\\pi / 4) & \\sin(4\\pi / 4) & 0 \\\\\n                        0 & 0 & 0 & 0 & -\\sin(4\\pi / 4) & \\cos(4\\pi / 4) & 0 \\\\\n                        0 & 0 & 0 & 0 & 0 & 0 & 1\n                        \\end{array}\\right) \\\\\n    \\mathbf R &= \\left(\\begin{array}{cc} \n                    1 & 0 & 0 & 0 & 0 & 0 \\\\\n                    0 & 1 & 0 & 0 & 0 & 0 \\\\\n                    0 & 0 & 1 & 0 & 0 & 0 \\\\\n                    0 & 0 & 0 & 1 & 0 & 0 \\\\\n                    0 & 0 & 0 & 0 & 1 & 0 \\\\\n                    0 & 0 & 0 & 0 & 0 & 1 \\\\\n                    0 & 0 & 0 & 0 & 0 & 0\n                    \\end{array}\\right)\n\\end{align}\n$$\n\nGiven the definitions of $\\mathbf Z_t$, $\\mathbf T$, and $\\mathbf R$, the state space representation of the unobserved \ncomponents model above can compactly be expressed as\n\n$$\n\\begin{align}\n    y_t &= \\mathbf Z_t \\boldsymbol{\\alpha}_ t + \\epsilon_t \\\\\n    \\boldsymbol{\\alpha}_ {t+1} &= \\mathbf T \\boldsymbol{\\alpha}_ t + \\mathbf R \\boldsymbol{\\eta}_ t, \\hspace{5pt} \n    t=1,2,...,n\n\\end{align}\n$$\n\nwhere\n\n$$\n\\begin{align}\n    \\boldsymbol{\\alpha}_ t &= \\left(\\begin{array}{cc} \n                            \\mu_t & \\delta_t & \\gamma_{1, t} & \\gamma_{1, t}^* & \\gamma_{2, t} & \\gamma_{2, t}^* & 1\n                            \\end{array}\\right)^\\prime \\\\\n    \\boldsymbol{\\eta}_ t &= \\left(\\begin{array}{cc} \n                            \\eta_{\\mu, t} & \\eta_{\\delta, t} & \\eta_{\\gamma_ 1, t} & \\eta_{\\gamma_ 1^\\*, t} & \n                            \\eta_{\\gamma_ 2, t} & \\eta_{\\gamma_ 2^\\*, t}\n                            \\end{array}\\right)^\\prime\n\\end{align}\n$$\n\nand \n\n$$\n\\mathrm{Cov}(\\boldsymbol{\\eta}_ t) = \\mathrm{Cov}(\\boldsymbol{\\eta}_ {t-1}) = \\boldsymbol{\\Sigma}_ \\eta = \n\\mathrm{diag}(\\sigma^2_{\\eta_\\mu}, \\sigma^2_{\\eta_\\delta}, \\sigma^2_{\\eta_{\\gamma_ 1}}, \\sigma^2_{\\eta_{\\gamma_ 1^\\*}}, \n\\sigma^2_{\\eta_{\\gamma_ 2}}, \\sigma^2_{\\eta_{\\gamma_ 2^\\*}}) \\in \\mathbb{R}^{6 \\times 6} \\hspace{5pt} \\textrm{for all } \nt=1,2,...,n\n$$\n\n# Estimation\n`pybuc` mirrors R\'s `bsts` with respect to estimation method. The observation vector, state vector, and regression \ncoefficients are assumed to be conditionally normal random variables, and the error variances are assumed to be \nconditionally independent inverse-Gamma random variables. These model assumptions imply conditional conjugacy of the \nmodel\'s parameters. Consequently, a Gibbs sampler is used to sample from each parameter\'s posterior distribution.\n\nTo achieve fast sampling, `pybuc` follows `bsts`\'s adoption of the Durbin and Koopman (2002) simulation smoother. For \nany parameter $\\theta$, let $\\theta(s)$ denote the $s$-th sample of parameter $\\theta$. Each sample $s$ is drawn by \nrepeating the following three steps:\n\n1. Draw $\\boldsymbol{\\alpha}(s)$ from \n   $p(\\boldsymbol{\\alpha} | \\mathbf y, \\boldsymbol{\\sigma}^2_\\eta(s-1), \\boldsymbol{\\beta}(s-1), \\sigma^2_\\epsilon(s-1))$ \n   using the Durbin and Koopman simulation state smoother, where \n   $\\boldsymbol{\\alpha}(s) = (\\boldsymbol{\\alpha}_ 1(s), \\boldsymbol{\\alpha}_ 2(s), \\cdots, \\boldsymbol{\\alpha}_ n(s))^\\prime$ \n   and $\\boldsymbol{\\sigma}^2_\\eta(s-1) = \\mathrm{diag}(\\boldsymbol{\\Sigma}_\\eta(s-1))$. Note that `pybuc` implements a \n   correction (based on a potential misunderstanding) for drawing $\\boldsymbol{\\alpha}(s)$ per "A note on implementing \n   the Durbin and Koopman simulation smoother" (Marek Jarocinski, 2015).\n2. Draw $\\boldsymbol{\\sigma}^2(s) = (\\sigma^2_ \\epsilon(s), \\boldsymbol{\\sigma}^2_ \\eta(s))^\\prime$ from \n   $p(\\boldsymbol{\\sigma}^2 | \\mathbf y, \\boldsymbol{\\alpha}(s), \\boldsymbol{\\beta}(s-1))$ using Durbin and Koopman\'s \n   simulation disturbance smoother.\n3. Draw $\\boldsymbol{\\beta}(s)$ from \n   $p(\\boldsymbol{\\beta} | \\mathbf y^ *, \\boldsymbol{\\alpha}(s), \\sigma^2_\\epsilon(s))$, where $\\mathbf y^ *$ is defined \n   above.\n\nBy assumption, the elements in $\\boldsymbol{\\sigma}^2(s)$ are conditionally independent inverse-Gamma distributed random \nvariables. Thus, Step 2 amounts to sampling each element in $\\boldsymbol{\\sigma}^2(s)$ independently from their \nposterior inverse-Gamma distributions.\n',
    'author': 'Devin D. Garcia',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.11',
}


setup(**setup_kwargs)
