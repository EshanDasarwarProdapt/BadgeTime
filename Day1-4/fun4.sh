reverse(){
str=$1
rev_str=""
#echo "$str" | rev nhi chalega kyuki rev nhi hai
for (( i=${#str}-1; i>=0; i--))
do
	rev_str="$rev_str${str:$i:1}"
done
echo "$rev_str"
}

reverse anything
