from sklearn import linear_model
from spdlogger import SPDLogger

logger = SPDLogger(config='/Users/pcsh0974/Documents/SPDLogger/examples/conf.toml') 


x = 9
y = 1

parameters = {
    "dense_units": 125,
    "activation": "relu",
    "dropout": 0.22,
    "learning_rate": 0.10,
    "batch_size": 64,
    "n_epochs": 20,
}

try:
    x/y
    logger.debug("this is debug")
    logger.info(f"info!! {x}/{y} successful with result: {x/y}.")
    logger.warning("warning!! x and y are set manually!")
    logger.critical("this is critical!")
    reg = linear_model.LinearRegression()
    model = reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    logger.params(key="model/parameters", value=parameters)
    logger.metrics('accuracy', 0.9)
    for epoch in range(parameters["n_epochs"]):
        loss = 0.5 ** epoch
        acc = 0.9 ** epoch
        logger.metrics("train/epoch/loss",loss)
        logger.metrics("train/epoch/accuracy",acc)
except Exception as err:
    logger.error(err)
    logger.fatal("this is fatal!")

logger.model("linear_model", model, "sklearn")
logger.file("logfile", "log.log")
logger.register_model("linear_model", model, "Staging")

    


