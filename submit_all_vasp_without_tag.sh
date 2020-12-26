#!/bin/tcsh
echo "Begin"
set foldername=$PWD
cd $foldername
foreach filename (`ls -d */`)
set INPUT=`basename $filename /`
cd $foldername/$INPUT
if ( -e "submit_tag" )  then
echo "Find a tag in" $INPUT ", SKIP THAT..."
else
echo "No tag in" $INPUT ", SUBMIT JOB!"
cp $foldername/vasp.sh $foldername/$INPUT/
qsub -N $INPUT vasp.sh
echo "submit time at" > submit_tag
date >> submit_tag
echo "SUBMIT_TAG MADE in " $INPUT
endif
cd $foldername
end
echo "Finished"


