search_word(){
file=$1
word=$2

if grep -qi "$word" "$file"
then
	echo "'$word' found in $file"
else
	echo "'$word' nhi mila bhai $file me"
fi
}

search_word searchfile.txt hello

count_word(){
file=$1
word=$2

count=$(grep -o "$word" "$file" | wc -l)

echo "Occurance of '$word': $count"
}

count_word searchfile.txt linux


#Print line numbers
show_line(){
file=$1
word=$2

grep -n "$word" "$file"
}

show_line searchfile.txt linux
