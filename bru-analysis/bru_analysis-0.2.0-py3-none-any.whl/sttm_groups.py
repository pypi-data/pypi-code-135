import os
import traceback
import pandas as pd
from sys import exc_info
from copy import deepcopy
from bertopic import BERTopic
from common.nlp_utils import CleanText
from sentence_transformers import SentenceTransformer

ERR_SYS = 'SYSTEM ERROR FROM: sttm_groups '

COLS_EMPTY_DF = ['processed_text', 'page_id__', '_id', 'name__',
                 'date__', 'polarity__', 'group', 'sttm_group',
                 'len_text']


def remove_from_text(text, toremove):
    '''
    remove text from list text

    Parameters
    ----------
    text : TYPE str
        DESCRIPTION. target text
    toremove : TYPE list
        DESCRIPTION. text to remove

    Returns
    -------
    text_copy : TYPE str
        DESCRIPTION. clena text

    '''
    text_copy = deepcopy(text)
    for word in text:
        if word in toremove:
            text_copy.remove(word)
    return text_copy


class SttmGroups():
    '''
    this class calculate Short Text Topic Modeling algorithm and group data
    '''

    def __init__(self, dataframe, s_net, comments=True):
        '''
        init parameters for calculate

        Parameters
        ----------
        dataframe : TYPE dataframe
            DESCRIPTION. Dataframe with texts of Facebook, Instagram or Twitter.
        s_net : TYPE string
            DESCRIPTION. social net to calculate 'fb': facebook, 'ig': instagram
                        'tw': twitter
        comments : TYPE bool, default True
            DESCRIPTION. Dataframe with comments of Facebook, Instagram or Twitter.

        Returns
        -------
        None.

        '''
        method_name = '__init__'

        if s_net == 'fb':
            col_name = 'message'
        elif s_net == 'ig':
            if comments:
                col_name = 'text'
            else:
                col_name = 'caption'
        elif s_net == 'tw':
            col_name = 'text'
        else:
            print(f'{s_net} social network not valid')

        try:
            dataframe['clean_text'] = dataframe[col_name].apply(lambda x: CleanText(x).process_text())

            # Link to see more models https://www.sbert.net/docs/pretrained_models.html
            self.sentence_model = SentenceTransformer("distiluse-base-multilingual-cased-v2")
            self.df_com_full = dataframe.fillna('')

        except Exception as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'Method: {method_name} ')
            print(''.center(60, '='))
            traceback.print_exc()
            self.df_com_full = pd.DataFrame(columns=['processed_text', 'page_id__', '_id',
                                                     'name__', 'date__', 'polarity__'])

    def get_sttm_groups(self, list_remove=None, min_texts=100):
        '''
        the get_sttm_groups method checks if there is a sufficient number

        Parameters
        ----------
        list_remove : TYPE, list
            DESCRIPTION. Terms to be removed
        min_texts : TYPE, optional int
            DESCRIPTION. The default is 100. min text to analyse.

        Returns
        -------
        TYPE dataframe
            DESCRIPTION. dataframe with column sttm_groups
        '''

        method_name = "get_sttm_groups"
        try:
            if len(self.df_com_full) >= min_texts:
                if len(self.df_com_full) >= 100 and len(self.df_com_full)<500:
                    min_topic = 20
                elif len(self.df_com_full) >= 500 and len(self.df_com_full)<1000:
                    min_topic = 50
                elif len(self.df_com_full) >= 1000:
                    min_topic = 100

                if list_remove:
                    self.df_com_full['clean_text'] = self.df_com_full\
                        ['clean_text'].apply(lambda x: str(x).split(" "))
                    self.df_com_full['clean_text'] = self.df_com_full\
                        ['clean_text'].apply(lambda x: remove_from_text(x, list_remove))
                    self.df_com_full['clean_text'] = self.df_com_full\
                        ['clean_text'].apply(lambda msg: str(msg))

                topic_model = BERTopic(language='spanish',
                                       min_topic_size=min_topic,
                                       nr_topics="auto")

                docs = self.df_com_full['clean_text'].tolist()
                embeddings = self.sentence_model.encode(docs, show_progress_bar=True)

                topics, probs = topic_model.fit_transform(docs, embeddings)
                labels = [topic_model.topic_labels_[i] for i in topics]

                self.df_com_full['sttm_group'] = labels

            else:
                print("warning: in",
                      f'Class: {self.__str__()}\nMethod: {method_name}',
                      "\n Not enough texts in DataFrame for STTM grouping.",
                      "Returning value 1 for group column for sttm_group.")
                self.df_com_full['sttm_group'] = 'No_STTM'

        except Exception as e_1:
            print(''.center(60, '='))
            print(e_1)
            print(''.center(60, '='))
            error_1 = exc_info()[0]
            print(ERR_SYS + str(error_1))
            print(f'Method: {method_name} ')
            print(''.center(60, '='))
            traceback.print_exc()
            self.df_com_full = pd.DataFrame(columns=COLS_EMPTY_DF)

        return self.df_com_full
