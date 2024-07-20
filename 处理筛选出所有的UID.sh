#!/bin/bash

input_file="1.txt"
output_file="output.txt"

# 从输入文件中提取所有的uid值，并保存到输出文件
grep -o '"uid":[0-9]*' "$input_file" | awk -F: '{print $2}' > "$output_file"

echo "所有uid值已保存到 $output_file"
