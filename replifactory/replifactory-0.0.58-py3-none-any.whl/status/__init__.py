import datetime
import os
from replifactory.util import read_file_tail


class Status:
    def __init__(self, experiment):
        self.experiment = experiment

    def print_exp_status(self, increase_verbosity=False):

        self.experiment.worker.status()
        if self.experiment.device is not None:
            for v in range(1, 8):
                if self.experiment.device.cultures[v] is not None:
                    self.experiment.device.cultures[v].show_parameters(increase_verbosity=increase_verbosity)
        else:
            print("Device not connected.")

    def errors(self):
        return error_status(self.experiment.directory)

    def last_errors(self, max_count=5, max_age_hrs=24):
        return last_errors(self.experiment.directory, max_count=max_count, max_age_hrs=max_age_hrs)


def parse_error_file(path, max_count=5, max_age_hrs=24):
    lines = read_file_tail(path, max_count * 500)
    error_list = {}
    for i in range(len(lines)):
        t = lines[-i].decode()
        if "ERROR" in t:
            error_time = t[:19]
            error_time = datetime.datetime.strptime(error_time,
                                                    '%Y-%m-%d %H:%M:%S')  # e.g. "2022-09-30 20:08:31.351"
            delta = datetime.datetime.now() - error_time
            hrs_since_error = round(delta.total_seconds() / 3600, 2)
            max_count -= 1

            if max_count < 0 or hrs_since_error > max_age_hrs:
                break
            error_list[hrs_since_error] = t[:-1]

    return error_list


def last_errors(directory, max_count=5, max_age_hrs=24):
    main_errs = parse_error_file(os.path.join(directory, "main_run.log"), max_count=max_count,
                                 max_age_hrs=max_age_hrs)
    od_errs = parse_error_file(os.path.join(directory, "od_thread.log"), max_count=max_count,
                               max_age_hrs=max_age_hrs)
    dil_errs = parse_error_file(os.path.join(directory, "dilution_thread.log"), max_count=max_count,
                                max_age_hrs=max_age_hrs)

    return {"main run": main_errs, "OD thread": od_errs, "dilution thread": dil_errs}


def error_status(directory):
    d24 = last_errors(directory, max_count=24 * 60 * 2, max_age_hrs=24)
    m, o, d = [len(e.keys()) for e in d24.values()]
    err_hrs = [h for e in d24.values() for h in e.keys()]
    t = "Errors last 24h: (%d,%d,%d) (main, OD, dilution)." % (m, o, d)
    if len(err_hrs) > 0:
        last_err_h = min(err_hrs)
        t += " Most recent: %.2f hours ago" % last_err_h
    return t
