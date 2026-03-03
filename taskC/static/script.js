function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split("; ");
        for (let i = 0; i < cookies.length+1; i++) {
            const cookie = (cookies[i]);
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie("csrftoken")
console.log(csrftoken)

function GetSolution(){
    if ((document.getElementById("iter")).value !== "" &
        (document.getElementById("count")).value !== "" &
        (document.getElementById("special")).value !== "" &
        (document.getElementById("nodes")).value !== ""
    ){
        fetch("http://127.0.0.1:8000/taskC/task", {
            method: "POST",
            credentials: "include",
            headers: {"X-CSRFToken": csrftoken},
            body: JSON.stringify({
                "t": document.getElementById("iter").value,
                "n": document.getElementById("count").value, 
                "x": document.getElementById("special").value, 
                "uv": document.getElementById("nodes").value,
                "csrftoken": csrftoken
            })
        })
        .then((response) => {
            if (response.ok){
                return response.json()
            }
            else{
                document.getElementById("answer").textContent="Упс, похоже что-то не так с входными данными"
            }
        })
        .then((data) => {
            document.getElementById("answer").style.display="block"
            document.getElementById("answer").textContent=Object.values(JSON.parse(JSON.stringify(data)))
        })
}
    else{
        alert("Заполните все поля!")
    }
}