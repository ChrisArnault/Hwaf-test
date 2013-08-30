#! /bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

rm -rf test
mkdir test
cd test

base="$PWD/test"
uses=""
puses=""

set -x

for project in `python $DIR/generator.py projects=1 packages=8 | egrep 'do ' | sed 's/do //'`
do
  echo "running in project $project using $uses"
  hwaf init $project
  cd $project
    hwaf setup $puses 
    hwaf configure
    hwaf
    hwaf show pkg-tree
  cd ..
  uses="${uses}${base}/$project/install-area"
  puses="-p=$uses"
  uses="${uses}:"
done

exit

for n in `find . -name 'hscript.yml'`
do
  m=`dirname $n`
  p=`basename $m`
  echo "----------------  testing $p  -----------------------------"
  hwaf run test$p
done


cd ${here}


