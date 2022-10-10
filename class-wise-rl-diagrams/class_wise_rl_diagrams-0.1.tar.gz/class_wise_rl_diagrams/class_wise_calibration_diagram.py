import logging
import math
import pathlib

import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import json
import base64

logger = logging.getLogger('__class_wise_calibration_diagram__')






def compute_calibration(confidences, true_labels, pred_labels, delta):
    """Collects predictions into bins used to draw a reliability diagram.

    Arguments:
        true_labels: the true labels for the test examples
        pred_labels: the predicted labels for the test examples
        confidences: the predicted confidences for the test examples
        num_bins: number of bins

    The true_labels, pred_labels, confidences arguments must be NumPy arrays;
    pred_labels and true_labels may contain numeric or string labels.

    For a multi-class model, the predicted label and confidence should be those
    of the highest scoring class.

    Returns a dictionary containing the following NumPy arrays:
        accuracies: the average accuracy for each bin
        confidences: the average confidence for each bin
        counts: the number of examples in each bin
        bins: the confidence thresholds for each bin
        avg_accuracy: the accuracy over the entire test set
        avg_confidence: the average confidence over the entire test set
        expected_calibration_error: a weighted average of all calibration gaps
        max_calibration_error: the largest calibration gap across all bins
    """

    num_bins = int(1 / delta) + 1
    bins = np.linspace(0.0, 1.0, num_bins)
    indices = np.digitize(confidences, bins, right=True)

    bin_accuracies = np.zeros(num_bins, dtype=np.float)
    bin_confidences = np.zeros(num_bins, dtype=np.float)
    bin_counts = np.zeros(num_bins, dtype=np.int)

    for b in range(num_bins):
        selected = np.where(indices == b + 1)[0]
        if len(selected) > 0:
            bin_accuracies[b] = np.mean(true_labels[selected] == pred_labels[selected])
            bin_confidences[b] = np.mean(confidences[selected])
            bin_counts[b] = len(selected)

    avg_acc = np.sum(bin_accuracies * bin_counts) / np.sum(bin_counts)
    avg_conf = np.sum(bin_confidences * bin_counts) / np.sum(bin_counts)

    gaps = np.abs(bin_accuracies - bin_confidences)
    ece = np.sum(gaps * bin_counts) / np.sum(bin_counts)
    mce = np.max(gaps)

    return {"accuracies": bin_accuracies,
            "confidences": bin_confidences,
            "counts": bin_counts,
            "bins": bins,
            "avg_accuracy": avg_acc,
            "avg_confidence": avg_conf,
            "expected_calibration_error": ece,
            "max_calibration_error": mce}


def positive_and_negative(scores, labels, class_id):
    size_dataset = labels.shape[0]
    pos_neg_scores = np.empty(size_dataset, dtype=np.float32)
    ipos, ineg = 0, size_dataset
    for i in range(size_dataset):
        if class_id == labels[i]:
            pos_neg_scores[ipos] = scores[i][class_id]
            ipos += 1
        else:
            ineg -= 1
            pos_neg_scores[ineg] = scores[i][class_id]
    return pos_neg_scores[:ipos], pos_neg_scores[ipos:]


def initialize_subplots(classes, w=30, h=20):
    fig = plt.figure(figsize=(w, h), clear=True)
    plt.subplots_adjust(left=0.125, right=0.9, bottom=0.08, top=0.92, wspace=0.2, hspace=0.7)
    nb_class = len(classes)
    return fig, nb_class


def get_r_delta_r_class_id(scores, labels, class_id, intervals):
    posterior_probability_x = scores[:, class_id]

    r = np.empty(len(intervals), dtype=np.float32)
    delta_r = np.empty(len(intervals), dtype=np.float32)
    n_Is = []
    for k, I in enumerate(intervals):
        n_pos_I, n_neg_I = 0, 0
        size_dataset = labels.shape[0]
        for i in range(size_dataset):
            if I[0] <= posterior_probability_x[i] <= I[1]:
                if labels[i] == class_id:
                    n_pos_I += 1
                else:
                    n_neg_I += 1
        n_Is.append((n_pos_I, n_neg_I))
        r[k] = n_pos_I / (n_pos_I + n_neg_I + 1)  # We add 1 to avoid division by zero
        delta_r[k] = math.sqrt(r[k] * (1 - r[k]) / (n_pos_I + n_neg_I + 1))  # We add 1 to avoid division by zero
    return r, delta_r, n_Is


def plot_class_wise_calibration_diagram(class_id, scores, labels, classes, delta_p=0.05):
    fig = plt.figure(figsize=(7, 7))
    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)

    num = int(1 / delta_p) + 1
    probabilities = np.linspace(0, 1, num)
    intervals = np.array([(i, i + delta_p) for i in probabilities])

    # r and delta_r estimations for all intervals
    r, delta_r, n_Is = get_r_delta_r_class_id(scores, labels, class_id, intervals)

    # plots
    color = "black"
    ax1.set_ylabel('accuracy', color=color)
    ax1.set_xlabel('confidences', color=color)
    ax1.grid(zorder=0)
    accurac_bar_plot = ax1.bar(probabilities, r, width=0.05, edgecolor='b', label='accuracy')


    gap_plt = ax1.bar(probabilities, np.abs(r - probabilities),
                     bottom=np.minimum(r, probabilities), width=.05,
                     edgecolor='black', color='r', linewidth=1, hatch='\\',label="Gap")


    ax1.plot(probabilities, probabilities, 'k--')
    # ax1.fill_between(probabilities[1:-1], r + delta_r, r - delta_r, facecolor='blue', alpha=0.3)
    ax1.set_title(classes[class_id])
    ax1.legend(handles=[accurac_bar_plot, gap_plt])
    # ax1.text(0.98,1, 'ECE= '+ str(round(calibration_metrics["expected_calibration_error"] * 100, 2)), color="black",
    #         ha="right", va="bottom", transform=ax1.transAxes)


    color = "tab:red"
    ax2.set_ylim(0, 1000)
    ax2.set_ylabel('#pos_I + #neg_I', color='red')  # we already handled the x-label with ax1

    t = [sum(n_Is[i]) for i in range(len(n_Is))]
    acc_plt = ax2.axvline(x=np.average(r), ls="solid", lw=3,
                         c="black", label="Accuracy")
    conf_plt = ax2.axvline(x=np.average(probabilities), ls="dotted", lw=3,
                          c="#444", label="Avg. confidence")
    ax2.legend(handles=[acc_plt, conf_plt])

    ax2.bar(probabilities, t, color='red', width=0.05, alpha=0.6)
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_title(classes[class_id])
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    tempfile = BytesIO()
    plt.savefig(tempfile, format='png')
    encoded = base64.b64encode(tempfile.getvalue()).decode('utf-8')
    return encoded


def get_calibration_metrics(results):
    true_labels = []
    predicted_labels = []
    confidences = []

    for (true_index, predicted_index, probabilities) in results:
        true_labels.append(true_index)
        predicted_labels.append(predicted_index)
        confidences.append(probabilities.tolist())

    calibration_metrics = compute_calibration(np.asarray(confidences), np.asarray(true_labels),
                                              np.asarray(predicted_labels), 0.05)
    return calibration_metrics, np.asarray(confidences), np.asarray(true_labels)

def static_calibration_error(y_true, y_pred, num_bins=20):
  classes = y_pred.shape[-1]

  o = 0
  for cur_class in range(classes):
      correct = (cur_class == y_true).astype(np.float32)
      prob_y = y_pred[..., cur_class]

      b = np.linspace(start=0, stop=1.0, num=num_bins)
      bins = np.digitize(prob_y, bins=b, right=True)

      for b in range(num_bins):
        mask = bins == b
        if np.any(mask):
            o += np.abs(np.sum(correct[mask] - prob_y[mask]))

  return o / (y_pred.shape[0] * classes)

def generate_calibration_html_report(results, class_keys_by_index, output_name, model_name, plot_dir):
    calibration_metrics, confidences, true_labels = get_calibration_metrics(results)
    static_calib_error = static_calibration_error(true_labels, confidences)
    print(static_calib_error)
    calibration_filename = pathlib.Path(plot_dir,
                                        f"{model_name}_{output_name}_multi_class_wise_reliability_diagram_report.html")
    hfile = calibration_filename.open(mode='w')
    hfile.write(f"""<!DOCTYPE html>
       <html>
       <head>
       <title>Clustering Image Report</title>
       </head>
       <body>
       """)
    hfile.write(f'<h1>Calibration report for : {model_name}_{output_name} on '
                f'</h1>\n')
    hfile.write(f'<h3> Static Calibration Error: {static_calib_error}'
                f'</h3>\n')
    for i in range(0, len(class_keys_by_index)):
        calibration_plot_html = '<img src=\'data:image' \
                                '/png;base64,{}\'>'.format(
            plot_class_wise_calibration_diagram(i, confidences, true_labels, class_keys_by_index))
        hfile.write(calibration_plot_html)
    hfile.write(f'<h3> Calibration Metrics </h3>')
    hfile.write(str(calibration_metrics))
    hfile.write('</body>\n</html>\n')
    hfile.close()
