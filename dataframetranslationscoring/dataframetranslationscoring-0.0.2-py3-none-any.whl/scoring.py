from .utils import *


def translation_quantitative_scoring(original_dataframe, translated_dataframe):
    """
    This function takes two dataframes as input and prints out the translation quality scores.
    The score is calculated by comparing the original text to the translated text.
    The score is a float between 0 and 100.

    Args:
        original_dataframe (dataframe): The original dataframe.
        translated_dataframe (dataframe): The translated dataframe.

    Returns:
        dataframe: The dataframe with the translation quality scores.
    """

    total_characters_to_translate = 0
    for column in original_dataframe.columns:
        original_dataframe = original_dataframe.astype({column: str})
        translated_dataframe = translated_dataframe.astype({column: str})
        list_score_words = []
        list_score_characters = []
        list_score_completeness = []
        completeness_score = 0
        scores_words = 0
        scores_character = 0
        for row in range(len(original_dataframe)):
            if (translated_dataframe[column][row] in ["", np.nan, "nan"]) & (
                original_dataframe[column][row] == translated_dataframe[column][row]
            ):
                pass
            elif (translated_dataframe[column][row] in ["", np.nan, "nan"]) & (
                original_dataframe[column][row] != translated_dataframe[column][row]
            ):
                completeness_score += 1
            else:
                scores = translation_quality_scores(
                    original_dataframe[column][row], translated_dataframe[column][row]
                )
                scores_character += scores[0]
                scores_words += scores[1]
                total_characters_to_translate += scores[2]
        list_score_completeness.append(
            1 - completeness_score / (len(translated_dataframe))
        )
        list_score_words.append(scores_words / (len(translated_dataframe)))
        list_score_characters.append(scores_character / (len(translated_dataframe)))
    print(
        "Overall percentage of characters translated vs available: ",
        "{:.2f}".format(sum(list_score_words) / len(list_score_words) * 100),
        "%",
    )
    print(
        "Overall percentage of words translated vs available: ",
        "{:.2f}".format(sum(list_score_characters) / len(list_score_characters) * 100),
        "%",
    )
    print(
        "Overall average percentage of non-missing translations: ",
        "{:.2f}".format(
            sum(list_score_completeness) / len(list_score_completeness) * 100
        ),
        "%",
    )
    print(
        "Total number of characters to be translated: ",
        "{:.2f}".format(total_characters_to_translate),
    )
