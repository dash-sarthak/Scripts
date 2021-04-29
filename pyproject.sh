name=$1

mkdir $name
cd $name
conda create --name $name python=3.7 pylint
conda activate $name
pip install pynvim
touch main.py
touch structure.md
