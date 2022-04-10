#!/bin/bash

touch go/$1.go
touch go/$1_test.go

touch python/algos/$1.py

touch rust/src/algos/$1.rs
touch rust/tests/test_$1.rs
