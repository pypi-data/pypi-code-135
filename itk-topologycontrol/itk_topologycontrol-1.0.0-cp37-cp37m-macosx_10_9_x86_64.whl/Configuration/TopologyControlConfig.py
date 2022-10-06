depends = ('ITKPyBase', 'ITKDistanceMap', 'ITKCommon', 'ITKCommon', 'ITKBinaryMathematicalMorphology', )
templates = (
  ('FixTopologyCarveOutside', 'itk::FixTopologyCarveOutside', 'itkFixTopologyCarveOutsideISS3', True, 'itk::Image< signed short,3 >,itk::Image< signed short,3 >,itk::Image< unsigned char,3 >'),
  ('FixTopologyCarveOutside', 'itk::FixTopologyCarveOutside', 'itkFixTopologyCarveOutsideIUC3', True, 'itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >,itk::Image< unsigned char,3 >'),
  ('FixTopologyCarveOutside', 'itk::FixTopologyCarveOutside', 'itkFixTopologyCarveOutsideIUS3', True, 'itk::Image< unsigned short,3 >,itk::Image< unsigned short,3 >,itk::Image< unsigned char,3 >'),
)
