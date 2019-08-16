#!/bin/bash

function create() {
    cd
    python3 create.py $1
    cd /Users/glennbarosen/Dev/$1 # Change "/Users/YourName/Dev/" to your path
    echo "# $1" >> README.md
    git init
    git add README.md
    git commit -m "🚀Initialized with AutoInit"
    git remote add origin https://github.com/YourUsername/$1.git # Insert username
    git push -u origin master