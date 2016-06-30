FixedPointInverseDisplacementField
========================

.. image:: https://circleci.com/gh/KitwareMedical/ITKFixedPointInverseDisplacementField.svg?style=svg
    :target: https://circleci.com/gh/KitwareMedical/ITKFixedPointInverseDisplacementField

FixedPointInverseDisplacementField takes a Displacement field as input and
computes the Displacement field that is its inverse. If the input Displacement
field was mapping coordinates from a space A into a space B, the output of
this filter will map coordinates from the space B into the space A.

The fixed point algorithm is described in the paper::

  Mingli Chen, Weiguo Lu, Quan Chen, Knneth J. Ruchala and Gusavo H. Olivera "A simple fixed-point approach to invert a Displacement field",
    Medical Physics, vol. 35, issue 1, p. 81,

The FixedPointInverseDisplacementFieldImageFilter has been implemented and described in the Insight Journal article::

  Luethi M. "Inverting Displacement fields using a fixed point iteration scheme."
    http://hdl.handle.net/10380/3222
    http://www.insight-journal.org/browse/publication/768
    October 2010. 

Since ITK 4.10.0, this module is available in the ITK source tree as a Remote
module.  To enable it, set::

  Module_FixedPointInverseDisplacementField:BOOL=ON

in ITK's CMake build configuration.
