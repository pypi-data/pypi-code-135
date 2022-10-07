from sklearn.manifold import TSNE
from dtreeviz.trees import *
from . import utils
import pandas as pd
import seaborn as sns

from kolibri.logger import get_logger

logger=get_logger(__name__)
class AdvancedCalssificationPlots():
    def __init__(self, X, y, labels_dict, classifier=None, max_depth=4, targe_namet=None, features_names=None):

        if classifier is None:
            self.classifier = tree.DecisionTreeClassifier(max_depth=max_depth)
        else:
            self.classifier=classifier
        self.targe_namet=targe_namet
        self.X=X
        self.y=y
        self.labels_names=labels_dict
        self.n_classes=len(self.labels_names)
        self.features_names=features_names
    def plot_tree(self, X=None, y=None):

        if X is None or y is None:
            X=self.X
            y=self.y
        self.classifier.fit(X, y)
        return dtreeviz(self.classifier, X, y,
                        target_name='variety',
                        feature_names=self.features_names,
                        class_names=self.labels_names)



    def tsne(self, X=None, y=None):

        if X is None or y is None:
            X=self.X.toarray()
            y=self.y


#        from sklearn.manifold import TSNE
        plt.clf()
        logger.info("Fitting TSNE()")
        X_embedded = TSNE(n_components=2,
                              perplexity=30,
#                              initialization="pca",
                              metric="cosine"
                              ).fit_transform(X)

        X = pd.DataFrame(X_embedded)

        logger.info("Rendering Visual")
#        import plotly.express as px

        df = X
        df['target']=y
        df['target'] =df['target'].astype(str)


        sns.scatterplot(0, 1, data=df, hue='target')
        plt.gca().update(dict(title="TSNE Projection of {} Documents".format(len(y))))


        logger.info("Visual Rendered Successfully")

        return plt

    def umap(self, X=None, y=None):

        import umap
        if X is None or y is None:
            X=self.X.toarray()
            y=self.y

        reducer = umap.UMAP(n_components=2, n_jobs=1)
        logger.info("Fitting UMAP()")
        embedding = reducer.fit_transform(X)
        X = pd.DataFrame(embedding)


        df = X
        df['target']=[str(i) for i in y]
        df.columns=['CP1', 'CP2', 'target']




        sns.scatterplot('CP1', 'CP2', data=df, hue='target')
        plt.gca().update(dict(title="UMAP Projection of {} Documents".format(len(y))))


        logger.info("Visual Rendered Successfully")
        return plt


    def calibration_(self):
        from sklearn.calibration import calibration_curve

        plt.figure(figsize=(7, 6), dpi=300)
        ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)

        ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
        logger.info("Scoring test/hold-out set")
        prob_pos = self.classifier.predict_proba(self.X)[:, 1]
        prob_pos = (prob_pos - prob_pos.min()) / (
                prob_pos.max() - prob_pos.min()
        )
        (
            fraction_of_positives,
            mean_predicted_value,
        ) = calibration_curve(self.y, prob_pos, n_bins=10)
        ax1.plot(
            mean_predicted_value,
            fraction_of_positives,
            "s-",
            label=f"{str(self.classifier)}",
        )

        ax1.set_ylabel("Fraction of positives")
        ax1.set_ylim([0, 1])
        ax1.set_xlim([0, 1])
        ax1.legend(loc="lower right")
        ax1.set_title("Calibration plots (reliability curve)")
        ax1.set_facecolor("white")
        ax1.grid(b=True, color="grey", linewidth=0.5, linestyle="-")
        plt.tight_layout()

        return plt


    def calibration(self):

        from sklearn.preprocessing import label_binarize
        from sklearn.calibration import calibration_curve

        plt.figure(figsize=(7, 6), dpi=300)
        ax1 = plt.subplot2grid((3, 1), (0, 0), rowspan=2)

        ax1.plot([0, 1], [0, 1], "k:", label="Perfectly calibrated")
        logger.info("Scoring test/hold-out set")
        y = label_binarize(self.y, classes=list(self.labels_names.keys()))
        for i in range(self.n_classes):
            prob_pos = self.classifier.predict_proba(self.X)[:, i]
            prob_pos = (prob_pos - prob_pos.min()) / (
                    prob_pos.max() - prob_pos.min()
            )
            (
                fraction_of_positives,
                mean_predicted_value,
             ) = calibration_curve(y[:,i], prob_pos, n_bins=20)
            plt.plot(
                mean_predicted_value,
                fraction_of_positives,
                "s-",
                label=f"{self.labels_names[i]}",
            )

        ax1.set_ylabel("Fraction of positives")
        ax1.set_ylim([0, 1])
        ax1.set_xlim([0, 1])
        ax1.legend(loc="lower right")
        ax1.set_title("Calibration plots (reliability curve)")
        ax1.set_facecolor("white")
        ax1.grid(b=True, color="grey", linewidth=0.5, linestyle="-")
        plt.tight_layout()

        return plt