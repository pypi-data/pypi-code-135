from aidev.blocks.sampling import Random, Latin
from aidev.blocks.surrogates import (
    Polynomial,
    Kriging,
    NeuralNetwork,
    Spline,
    SupportVector,
)
from aidev.blocks.optimization import NelderMeadSearch, NSGA_III, GeneticAlgorithm, PSO
from aidev.utilities.types import FeatureDefinition
from aidev.blocks.data import Data
from aidev.blocks.postprocessing import Decision
from pandas import DataFrame

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from typing import Union
from os.path import join
from numpy import ndarray


class AiDev:
    def __init__(self, features: FeatureDefinition, objective: callable, path: str):
        self.features = features
        self.objective = objective
        self.path = path

        self.data = None
        self.datahandler = Data(
            features=self.features,
            objective=self.objective,
            db_name=join(self.path, "db.csv"),
        )

        self.n_samples = 50
        self.sampling_strategy = "latin"
        self.surrogate_strategy = "polynomial"
        self.optimization_strategy = "global"
        self.global_optimizer = "PSO"
        self.popsize = 15
        self.degree_fit = 1
        self.interaction_only = False
        self.fit_intercept = True
        self.kernel = None
        self.n_nodes = (16, 8)
        self.activation = "relu"
        self.n_epochs = 1000
        self.n_knots = 2

    def run(
        self,
        global_iter: int = 5,
        data: Union[DataFrame, None] = None,
        sampling: bool = True,
        optimization: bool = True,
        # mail_at_completion=False
    ) -> DataFrame:
        if data:
            self.data = data.dropna().drop_duplicates()[
                self.features.pnames + self.features.tnames
            ]

        if sampling:
            doe = self._sampling()
            if self.data:
                self.data = self.datahandler.add(data=self.data, samples=doe)
            else:
                self.data = self.datahandler.generate(samples=doe)
            self.data.to_csv(join(self.path, "db.csv"), index=False, mode="w")

        if optimization:
            for _ in range(global_iter):
                surrogates, performance, target_values = self._surrogate()
                results = self._optimization(surrogates)["x"]
                self.data = self.datahandler.add(data=self.data, samples=results)

            self.data = self._decision(
                target_values
            )  # todo would be nice to perform decisions also after the sampling
            self.data.to_csv(join(self.path, "db.csv"), index=False, mode="w")

        return self.data

    def _sampling(self) -> ndarray:
        if self.sampling_strategy == "latin":
            doe = Random(self.features)(n_samples=self.n_samples)
        else:
            doe = Latin(self.features)(n_samples=self.n_samples)
        return doe

    def _surrogate(self) -> tuple:
        x = self.data[self.features.pnames].values
        y = self.data[
            [
                tname
                for tname, isobjective in zip(
                    self.features.tnames, self.features.areobjs
                )
                if isobjective
            ]
        ].values

        if self.surrogate_strategy == "kriging":
            smodel, performance = Kriging(kernel=None)(x, y)
        elif self.surrogate_strategy == "supportvector":
            smodel, performance = SupportVector(
                kernel=self.kernel,
                degree_fit=self.degree_fit,
            )(x, y)
        elif self.surrogate_strategy == "neuralnetwork":
            smodel, performance = NeuralNetwork(
                n_nodes=self.n_nodes,
                activation=self.activation,
                n_epochs=self.n_epochs,
            )(x, y)
        elif self.surrogate_strategy == "spline":
            smodel, performance = Spline(
                n_knots=self.n_knots,
                degree_fit=self.degree_fit,
                fit_intercept=self.fit_intercept,
            )(x, y)
        else:
            smodel, performance = Polynomial(
                degree_fit=self.degree_fit,
                interaction_only=self.interaction_only,
                fit_intercept=self.fit_intercept,
            )(x, y)

        surrogates = []

        for i in range(len(self.features.tnames)):
            surrogates.append(
                lambda p, i=i: smodel.predict([p])[0][i]
            )  # todo this is not the same as in types

        return surrogates, performance, y

    def _optimization(self, surrogates: list):
        if len(self.features.targets) == 1:
            if self.optimization_strategy == "local":
                results = NelderMeadSearch(
                    surrogates,
                    self.features,
                    popsize=self.popsize,
                )()
            else:
                if self.global_optimizer == "GA":
                    results = GeneticAlgorithm(
                        surrogates,
                        self.features,
                        popsize=self.popsize,
                    )()
                else:
                    results = PSO(
                        surrogates,
                        self.features,
                        popsize=self.popsize,
                    )()
        else:
            results = NSGA_III(surrogates, self.features, popsize=self.popsize)()
        return results

    def _decision(self, target_values: ndarray, return_choices: int = 10):
        data = Decision(target_values, self.features.weights).decide(
            self.data, return_choices=return_choices
        )
        return data

    # @staticmethod
    # def _mail(content: str):
    #     with open("../../settings.json") as settings_file:
    #         settings = load(settings_file)
    #     message = MIMEMultipart()
    #     sender_address = settings["sender_address"]
    #     sender_psw = settings["sender_psw"]
    #     receiver_address = settings["receiver_address"]
    #
    #     message["From"] = sender_address
    #     message["To"] = receiver_address
    #     message["Subject"] = "Notification of AiDev process end."
    #     message.attach(MIMEText(content, "plain"))
    #
    #     session = smtplib.SMTP("smtp.gmail.com", 587)
    #     session.starttls()
    #     session.login(sender_address, sender_psw)
    #     text = message.as_string()
    #     session.sendmail(sender_address, receiver_address, text)
    #     session.quit()
