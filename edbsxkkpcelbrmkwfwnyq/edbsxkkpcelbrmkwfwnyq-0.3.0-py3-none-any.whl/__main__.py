import testing
import os

# Get the name of the assessment which is being tested
assessment_name = testing._cwd_Dir.dirs[-1] 

# Load the assessment module from testing/assessments/<name>.py
module = testing.utils.load_assessment( assessment_name )

# Run all the tests in the module
testing.utils.run_test( module )


