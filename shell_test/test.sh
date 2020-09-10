#!/bin/bash
#
# jun.hu@20200910

python3 shell_test.py 10 2 || code=$?
echo "befor exit"
if $code 2>&1 >/dev/null; then echo "success"; else exit 1; fi
echo "after exit"

python3 shell_test.py 10 20 || code_exit=$?
if $code_exit 2>&1 >/dev/null; then echo "success"; else exit 1 ; fi
echo "after exit"
