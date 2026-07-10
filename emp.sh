report_file="payroll_report.txt"

# Clear old report
> "$report_file"

echo "Employee Payroll Report" >> "$report_file"
echo "=======================" >> "$report_file"
echo "ID   Name   Salary   Tax   Bonus   Net Salary" >> "$report_file"

calculate_payroll() {
    emp_id=$1
    name=$2
    salary=$3

    echo "emp_id='$emp_id' name='$name' salary='$salary'"
    # Calculate Tax
    if [[ $salary -le 30000 ]]
    then
        tax=$((salary * 5 / 100))
    elif [[ $salary -le 60000 ]]
    then
        tax=$((salary * 10 / 100))
    else
        tax=$((salary * 15 / 100))
    fi

    # Calculate Bonus
    if [[ $salary -le 50000 ]]
    then
        bonus=2000
    else
        bonus=5000
    fi

    # Calculate Net Salary
    net_salary=$((salary - tax + bonus))

    # Write to report
    echo "$emp_id  $name  $salary  $tax  $bonus  $net_salary" >> "$report_file"
}

echo "Enter employee file name:"
read file

if [[ ! -f "$file" ]]
then
    echo "File not found!"
    exit 1
fi

while read -r emp_id name salary
do
    calculate_payroll "$emp_id" "$name" "$salary"
done < "$file"

echo
echo "Payroll report generated successfully: $report_file"

