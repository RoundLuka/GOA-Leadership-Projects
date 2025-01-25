const dataBase = document.getElementById("dataBase");

const addGroupBtn = document.getElementById("addGroup");
const addStudent = document.getElementById("addStudent");

const groupName = document.getElementById("groupName");



addGroupBtn.addEventListener("click", (e) => {
    e.preventDefault;

    
    const groupNum = groupName.value; 
    const groupDiv = document.createElement("div");

    const groupHeader = document.createElement("h2");
    groupHeader.textContent = "Group" + groupNum

    groupDiv.className = "group";
    groupDiv.id = groupNum;

    groupDiv.append(groupHeader);
    dataBase.appendChild(groupDiv);
});

addStudent.addEventListener("click", (e) => {
    e.preventDefault;

    
});

// couldn't finish as wasted time trying to figure out import/export
// had to add many more
