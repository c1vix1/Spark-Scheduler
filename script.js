var totalEvents = 10;

const table = document.getElementById("schedulerTable");
const runButton = document.getElementById("runButton");

runButton.addEventListener("click", addRows);
    

function addRows(e) {
    console.log(e.key)
    console.log("adding Rows")
    console.log(totalEvents)
    for (let i = 0; i < totalEvents; i++) {
        let row = table.insertRow(-1);
        let cell0 = row.insertCell(0);
        let ce1l1 = row.insertCell(1);
        cell0.textContent = "John Doe";
        cell1.textContent = "Developer";
    }
}