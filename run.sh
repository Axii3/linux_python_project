#!/bin/bash
cd Unc_Project
source .venv/bin/activate
python3 main.py 2>log.txt
output=$(cat log.txt)

if echo "$output" | grep -q "ModuleNotFoundError"; then
	echo "modules not found"
	echo "installing..."
	./install.sh
	source .venv/bin/activate
	python3 main.py >log.txt 2>&1
	exit;
fi
