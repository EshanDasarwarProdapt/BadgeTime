FILE="books.txt"

###########################################
# View All Books
###########################################
display_books() {

    echo "=========== Book Records ==========="

    cat "$FILE"
}

###########################################
# Search for a Book
###########################################
search_book() {

    echo "Enter Book Name:"
    read name

    if grep -i "$name" "$FILE"
    then
        echo "Book Found"
    else
        echo "Book Not Found"
    fi
}

###########################################
# Count Books Out Of Stock
###########################################
count_outofstock() {

    count=$(grep -c "OutOfStock" "$FILE")

    echo "Out Of Stock Books : $count"
}

###########################################
# Update Stock Status
###########################################
update_stock() {

    echo "Enter Book ID:"
    read id

    sed -i "/^$id,/ s/OutOfStock/Available/" "$FILE"

    echo "Stock Updated Successfully"
}

###########################################
# Calculate Total Inventory Value
###########################################
calculate_inventory() {

    total=$(awk -F',' '
    {
        sum += $5
    }
    END{
        print sum
    }' "$FILE")

    echo "Total Inventory Value : Rs.$total"
}

###########################################
# Display Books By Category
###########################################
category_books() {

	echo "Enter Category:"
    	read category

	result=$(grep -i ",$category," "$FILE")
	if [[ -n "$result" ]]; then
		echo "Books in category: $category"
		echo "$result"
	else
		echo "Nhi hai book"
	fi
}

###########################################
# Find the Costliest Book
###########################################
costliest_book() {

    awk -F',' '

    BEGIN{
        max = 0
    }

    {
        if($5 > max)
        {
            max = $5
            book = $2
        }
    }

    END{
        print "Costliest Book :", book
        print "Price : Rs." max
    }

    ' "$FILE"
}

###########################################
# Menu
###########################################

while true
do
    echo
    echo "====================================="
    echo "      Library Management System"
    echo "====================================="
    echo "1. View All Books"
    echo "2. Search for a Book"
    echo "3. Count Books Out Of Stock"
    echo "4. Update Stock Status"
    echo "5. Calculate Total Inventory Value"
    echo "6. Display Books By Category"
    echo "7. Find the Costliest Book"
    echo "8. Exit"

    echo "Enter Choice:"
    read choice

    case $choice in

        1)
            display_books
            ;;

        2)
            search_book
            ;;

        3)
            count_outofstock
            ;;

        4)
            update_stock
            ;;

        5)
            calculate_inventory
            ;;

        6)
            category_books
            ;;

        7)
            costliest_book
            ;;

        8)
            echo "Thank You"
            break
            ;;

        *)
            echo "Invalid Choice"
            ;;
    esac

done
