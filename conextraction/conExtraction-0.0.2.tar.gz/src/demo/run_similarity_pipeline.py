from myInitialize import SetupLogging
import argparse
from text_utils import ReadNumbersFromFile
from text_line_extract import TextLinesExtractor
from text_similarity_calculate import HpiTrainingDataGenerator
from text_label_base_on_scores import HpiTrainingCaseFormatter

def filter_file(
    intput_file: str,
    output_file: str,
    sample_line_no_file: str,
    sample_all_lines: bool):
    print(f"Sample line from {intput_file} and save to {output_file}")
    print("keeping all lines" if sample_all_lines else f"filtering lines in {sample_line_no_file}")
    if sample_all_lines:
        extractor = TextLinesExtractor(None, sample_all_lines)
    else:
        lineNums = ReadNumbersFromFile(sample_line_no_file)
        extractor = TextLinesExtractor(lineNums)
    extractor.Extract(intput_file, output_file)

if __name__ == "__main__":
    """
    The pipeline to get the similarity score.
    Step 1. re-format and filter the conversation and summary file.
    Step 2. calculate the similarity score base on it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--src_file', type=str, required=True)
    parser.add_argument('--tgt_file', type=str, required=True)
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--sample_line_no_file', type=str)
    group.add_argument('--sample_all_lines', action='store_true')
    
    parser.add_argument('--sample_src_file', type=str)
    parser.add_argument('--sample_tgt_file', type=str)
    parser.add_argument('--similarity_file', type=str)
    
    args = parser.parse_args()
    
    # source conversation
    src_file = args.src_file
    # source summary file
    tgt_file = args.tgt_file
    # the filter file
    sample_line_no_file = args.sample_line_no_file
    # whether to do the filtering
    sample_all_lines = args.sample_all_lines
    
    # sample conversation output
    sample_src_file = args.sample_src_file if args.sample_src_file is not None else "./test_sample.src"
    # sample summary output
    sample_tgt_file = args.sample_tgt_file if args.sample_tgt_file is not None else "./test_sample.tgt"
    # final output similarity scores
    similarity_file = args.similarity_file if args.similarity_file is not None else "./test_similarity_scores"
    
    
    # sample conversation:
    filter_file(src_file, sample_src_file, sample_line_no_file, sample_all_lines)
    
    # sample summarization:
    filter_file(tgt_file, sample_tgt_file, sample_line_no_file, sample_all_lines)
    
    print(f"Start calculating similarity scores.")
    # calculate similarity:
    caseGen = HpiTrainingDataGenerator()
    caseGen.GenerateCases(sample_src_file, sample_tgt_file, similarity_file)