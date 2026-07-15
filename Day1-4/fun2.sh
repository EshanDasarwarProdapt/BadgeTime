add_num(){
	sum=$(($1+$2))
	echo "Sum is: $sum"
}

echo "Num1: "
read num1
echo "Num2: "
read num2
add_num $num1 $num2
