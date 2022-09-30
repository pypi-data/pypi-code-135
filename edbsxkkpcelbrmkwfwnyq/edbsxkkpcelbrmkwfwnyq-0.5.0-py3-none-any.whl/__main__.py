import testing
import os

# Get the name of the assessment which is being tested
cwd = testing._cwd_Dir.dirs[-1] 
assessment_name = cwd.split( '-' )[0]


# Load the assessment module from testing/assessments/<name>.py
module = testing.utils.load_assessment( assessment_name )

# Run all the tests in the module
testing.utils.run_test( module )


