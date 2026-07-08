check_odd_even(){
	if [[ $(($1 % 2)) -eq 0 ]]; then
		echo "$1 is even"
	else
		echo "$1 is odd"
	fi
}

echo "Enter: "
read numm
check_odd_even $numm
