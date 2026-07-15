info_count=0
error_count=0
warning_count=0

#Function to analyze log file
analyze_log(){
line=$1
if echo "$line" | grep -q "INFO"
then
((info_count++))
elif echo "$line" | grep -q "WARNING"
then
((warning_count++))
else
((error_count++))
fi
}

#Func to deternime the system status
check_status(){
status=""
if [[ $error_count -gt 10 ]]
then
	status="Critical"
elif [[ $error_count -gt 0 ]]
then
	status="Warning"
else
	status="Healthy"
fi
}

echo "Enter the log file name: "
read logfile
if [[ ! -f "$logfile" ]]
then
	echo "File nhi hai bhai"
	exit
fi

while read line
do
analyze_log "$line"
done < $logfile


#determine status
check_status
{
echo "System Log Analyzer Report"
echo "=========================="
echo "INFO count: $info_count"
echo "WARNING count: $warning_count"
echo "ERROR count: $error_count"
echo
echo "Ststem status: $status"
} > report.txt

echo "Report Generated: report.txt"
