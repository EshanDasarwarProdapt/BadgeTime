let marks = [85,42,76,91,38,67,55,29,80,49];

let passed_students = 0
let failed_students = 0

for (let i = 0; i < marks.length; i++) {
    if (marks[i] >= 50) {
        console.log("Student " + (i + 1) + ": " + marks[i] + " - Pass");
        passed_students++;
    } else {
        console.log("Student " + (i + 1) + ": " + marks[i] + " - Fail");
        failed_students++;
    }
}

console.log("Number of students who passed: " + passed_students);
console.log("Number of students who failed: " + failed_students);
console.log("Total number of students: " + marks.length);

console.log("Highest Marks - " + Math.max(...marks));
console.log("Lowest Marks - " + Math.min(...marks));