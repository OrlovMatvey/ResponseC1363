function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split('; ');
        for (let i = 0; i < cookies.length+1; i++) {
            const cookie = (cookies[i]);
            if (cookie.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken')
console.log(csrftoken)

function GetSolution(){
    if (isNaN(document.getElementById('iter'))!='True' &
        isNaN(document.getElementById('count'))!='True' &
        isNaN(document.getElementById('special'))!='True' &
        isNaN(document.getElementById('nodes').length)!='True'
    ){
        fetch('http://127.0.0.1:8000/taskC/task', {
            method: 'POST',
            credentials: "include",
            headers: {'X-CSRFToken': csrftoken},
            body: JSON.stringify({
                't': document.getElementById('iter').value,
                'n': document.getElementById('count').value, 
                'x': document.getElementById('special').value, 
                'uv': document.getElementById('nodes').value,
                "csrftoken": csrftoken
            })
        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log(data)
            document.getElementById('answer').textContent=Object.values(JSON.parse(JSON.stringify(data)))
        })
}
    else{
        alert('Некорректные входные данные!')
    }
}