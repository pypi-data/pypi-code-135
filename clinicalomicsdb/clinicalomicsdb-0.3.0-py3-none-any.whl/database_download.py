""" ClinicalOmicsDB: Bridging the gap between next-generation clinical omics data and machine learning
Reference: Chang In Moon, Byron Jia, Bing Zhang
Paper link: TBD
Last updated Date: October 6th 2022
Code author: Chang In Moon (moonchangin@gmail.com)
-----------------------------
database_download.py
- Basic functions that will use box api to obtain dataset

(1) get_dataset_link: provide available data in a data frame
(2) download: returns dataset for analysis
(3) get_patient_dataset_link: provide available clinical in a data frame [under development]
(4) download_patient_data: returns dataset for subsetting data frame [under development]

"""
import io
import pandas as pd
from file_download import download_text as _download_text
from exceptions import BaseError, BaseWarning, InvalidParameterError, NoInternetError, OldPackageVersionWarning

def get_dataset_link():
    dataset_link_url = "https://bcm.box.com/shared/static/1rs6wid9em7tewjpqchnar4wlr75l3ml.csv"
    try:
        dataset_link_text = _download_text(dataset_link_url)
    except NoInternetError:
        raise NoInternetError("Insufficient internet to download available dataset info. Check your internet connection.") from None
    return pd.read_csv(io.StringIO(dataset_link_text), header=0)

def get_ssl_dataset_link():
    dataset_link_url = "https://bcm.box.com/shared/static/6h0jdwq1lsfm13qmrfbv8yac8hje8zzb.csv"
    try:
        dataset_link_text = _download_text(dataset_link_url)
    except NoInternetError:
        raise NoInternetError("Insufficient internet to download available dataset info. Check your internet connection.") from None
    return pd.read_csv(io.StringIO(dataset_link_text), header=0)

def download(url):
    try:
        dataset_text = _download_text(url)
    except NoInternetError:
        raise NoInternetError("Insufficient internet to download available dataset info. Check your internet connection.") from None
    return pd.read_csv(io.StringIO(dataset_text), header=0)

def get_patient_dataset_link():
    dataset_link_url = "https://bcm.box.com/shared/static/yt0ldc2nptxn96ovnna3hjxtlntzfvig.csv"
    try:
        dataset_link_text = _download_text(dataset_link_url)
    except NoInternetError:
        raise NoInternetError("Insufficient internet to download available dataset info. Check your internet connection.") from None
    return pd.read_csv(io.StringIO(dataset_link_text), header=0)


def download_patient_data(input):
    input = input.upper()
    data_link = get_patient_dataset_link()
    target = data_link.loc[data_link['Series'] == input]
    url = target.iloc[0,1]
    try:
        dataset_text = _download_text(url)
    except NoInternetError:
        raise NoInternetError("Insufficient internet to download available dataset info. Check your internet connection.") from None
    return pd.read_csv(io.StringIO(dataset_text), header=0)