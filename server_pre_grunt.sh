#!/bin/bash

echo "==========================================================================" 
echo "--- start"
echo "==========================================================================" 

cd themes/tranquilpeak

current=$(pwd)

echo "grunt build will execute at " [${current}]

grunt build

echo "==========================================================================" 
echo "--- build finish" 
echo "==========================================================================" 

cd ../

current=$(pwd)
echo "hexo server execute at " [${current}]

hexo s
